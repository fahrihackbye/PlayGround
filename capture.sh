#!/usr/bin/env bash
set -Eeuo pipefail

PROJECT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
: "${CAPTURE_URL:?Set CAPTURE_URL to the exact preview URL}"
: "${CAPTURE_DIR:?Set CAPTURE_DIR to an evidence directory outside the source project}"
RUNTIME_DIR="${RUNTIME_DIR:-/home/runner/work/_temp/omgithub-runtime}"
export CAPTURE_URL CAPTURE_DIR

run() { /usr/bin/time -p "$@"; }
run mkdir -p "$CAPTURE_DIR"
run node "$RUNTIME_DIR/scripts/default-capture.mjs"
