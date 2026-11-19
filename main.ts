// Sakura meme entry for make.fun's gta6-meme-x-01 bounty (Node 22, stdlib only).
//
// The entry itself is the X post: an AI-made GTA 6 meme (meme.png in this repo)
// posted from a public X account with make.fun and the entrant's play code in
// its text. This program is the small piece the grader runs: it hands the
// post's address over by copying POST.json from the repository root into the
// grader's output directory, so the house can read the post from X and build
// the dossier the judge sees (first picture, then post text).
//
// Run it locally the way the grader does:
//   mkdir -p out && MAKEFUN_BOT_DIR=. MAKEFUN_OUTPUT_DIR=out node main.ts
// On success it prints nothing and out/POST.json is byte-for-byte POST.json.

import { mkdirSync, readFileSync, writeFileSync } from "node:fs";
import { join } from "node:path";

const BOT_DIR = process.env.MAKEFUN_BOT_DIR ?? "/bot";
const OUTPUT_DIR = process.env.MAKEFUN_OUTPUT_DIR ?? "/output";

// The post's address, as written in POST.json at the repository root.
// It is JSON of the form {"url": "https://x.com/<handle>/status/<id>"}.
const postPath = join(BOT_DIR, "POST.json");
const postText = readFileSync(postPath, "utf8");
const post = JSON.parse(postText) as { url?: unknown };
if (typeof post.url !== "string" || post.url.length === 0) {
  console.error("POST.json must be an object with a non-empty url string");
  process.exit(1);
}

mkdirSync(OUTPUT_DIR, { recursive: true });
writeFileSync(join(OUTPUT_DIR, "POST.json"), postText, "utf8");
