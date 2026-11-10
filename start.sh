#!/usr/bin/env bash
set -Eeuo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
BUILT_DIR="$PROJECT_DIR/web"
PORT="${PORT:-3000}"
: "${OPENCODE_WEB_DIR:?OPENCODE_WEB_DIR must point to worker metadata outside the project}"

run() {
  /usr/bin/time -p "$@"
}

cd "$PROJECT_DIR"
run test -f "$BUILT_DIR/index.html"
run mkdir -p "$OPENCODE_WEB_DIR"
run node -e 'const fs=require("node:fs"); const p=process.argv[1]; const d=process.argv[2]; fs.writeFileSync(p, JSON.stringify({project:d, directory:process.argv[3]}, null, 2)+"\n")' "$OPENCODE_WEB_DIR/deployment-output.json" "$PROJECT_DIR" "$BUILT_DIR"

# Serve the checked-in static build in the foreground. Node is part of the worker runtime.
run env PORT="$PORT" PROJECT_STATIC_DIR="$BUILT_DIR" node -e '
const http = require("node:http");
const fs = require("node:fs");
const path = require("node:path");
const root = path.resolve(process.env.PROJECT_STATIC_DIR);
const types = {".html":"text/html; charset=utf-8", ".css":"text/css; charset=utf-8", ".js":"text/javascript; charset=utf-8", ".json":"application/json; charset=utf-8", ".svg":"image/svg+xml"};
http.createServer((req, res) => {
  let pathname;
  try { pathname = decodeURIComponent(new URL(req.url, "http://localhost").pathname); }
  catch { res.writeHead(400); return res.end("Bad request"); }
  let target = path.resolve(root, "." + pathname);
  if (target !== root && !target.startsWith(root + path.sep)) { res.writeHead(403); return res.end("Forbidden"); }
  try {
    if (fs.statSync(target).isDirectory()) target = path.join(target, "index.html");
    const body = fs.readFileSync(target);
    res.writeHead(200, {"Content-Type": types[path.extname(target)] || "application/octet-stream", "Cache-Control":"no-cache"});
    res.end(body);
  } catch { res.writeHead(404, {"Content-Type":"text/plain; charset=utf-8"}); res.end("Not found"); }
}).listen(Number(process.env.PORT), "0.0.0.0", () => console.log(`Serving ${root} on port ${process.env.PORT}`));
'
