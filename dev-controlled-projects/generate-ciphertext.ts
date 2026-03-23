/**
 * generate-ciphertext.ts
 * Generates the 684-char Entity Secret Ciphertext for manual registration
 * at console.circle.com → Configurator → Entity Secret Ciphertext
 *
 * Usage:
 *   node --env-file=.env --import=tsx generate-ciphertext.ts
 */
import crypto from "node:crypto";
import fs from "node:fs";
import https from "node:https";
import path from "node:path";
import { fileURLToPath } from "node:url";

const __dirname = path.dirname(fileURLToPath(import.meta.url));
const envPath = path.join(__dirname, ".env");

async function main() {
  const apiKey = process.env.CIRCLE_API_KEY;
  if (!apiKey) throw new Error("CIRCLE_API_KEY missing from .env");

  // Reuse or generate entity secret
  let entitySecret = process.env.CIRCLE_ENTITY_SECRET;
  if (!entitySecret) {
    entitySecret = crypto.randomBytes(32).toString("hex");
    fs.appendFileSync(envPath, `\nCIRCLE_ENTITY_SECRET=${entitySecret}\n`, "utf-8");
    console.log("Generated new entity secret and saved to .env");
  } else {
    console.log("Using existing CIRCLE_ENTITY_SECRET from .env");
  }
  console.log("Entity Secret:", entitySecret);

  // Fetch Circle's public key
  console.log("\nFetching Circle public key...");

  const publicKey = await new Promise<string>((resolve, reject) => {
    const req = https.request(
      {
        hostname: "api.circle.com",
        path: "/v1/w3s/config/entity/publicKey",
        method: "GET",
        headers: { Authorization: `Bearer ${apiKey}` },
      },
      (res) => {
        let body = "";
        res.on("data", (chunk) => (body += chunk));
        res.on("end", () => {
          if (res.statusCode !== 200) {
            return reject(new Error(`Circle API error (${res.statusCode}): ${body}`));
          }
          try {
            const parsed = JSON.parse(body);
            resolve(parsed.data.publicKey);
          } catch {
            reject(new Error("Failed to parse Circle API response: " + body));
          }
        });
      },
    );
    req.on("error", reject);
    req.end();
  });
  console.log("Got Circle public key.");

  // RSA-OAEP encrypt the entity secret with Circle's public key
  const secretBuffer = Buffer.from(entitySecret, "hex");
  const ciphertext = crypto.publicEncrypt(
    {
      key: publicKey,
      padding: crypto.constants.RSA_PKCS1_OAEP_PADDING,
      oaepHash: "sha256",
    },
    secretBuffer,
  );
  const ciphertextB64 = ciphertext.toString("base64");

  console.log(`\nEntity Secret Ciphertext (${ciphertextB64.length} chars):`);
  console.log("─".repeat(80));
  console.log(ciphertextB64);
  console.log("─".repeat(80));

  // Save ciphertext to file for easy copy-paste
  const outPath = path.join(__dirname, "output", "entity-ciphertext.txt");
  fs.mkdirSync(path.join(__dirname, "output"), { recursive: true });
  fs.writeFileSync(outPath, ciphertextB64, "utf-8");

  console.log(`\nAlso saved to: output/entity-ciphertext.txt`);
  console.log("\nNext steps:");
  console.log("  1. Copy the ciphertext above");
  console.log("  2. Go to console.circle.com → Configurator → Entity Secret Ciphertext");
  console.log("  3. Paste and click Register");
  console.log("  4. Then run: node --env-file=.env --import=tsx create-wallet.ts");
}

main().catch((err) => {
  console.error("Error:", err.message || err);
  process.exit(1);
});
