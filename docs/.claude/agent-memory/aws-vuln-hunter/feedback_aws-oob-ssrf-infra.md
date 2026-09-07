---
name: aws-oob-ssrf-infra
description: Reliable OOB responder setup for AWS server-side-fetch SSRF testing in these accounts
metadata:
  type: feedback
---

For AWS managed-fetcher SSRF tests, use an **API-Gateway-HTTP-API-fronted Lambda** as the controllable responder, not a Lambda Function URL.

**Why:** public Lambda Function URLs (`--auth-type NONE`) return `403 Forbidden` in account 183174222929 — an SCP/guardrail requires IAM auth. API Gateway HTTP API (`create-api --target <lambda-arn>`, default route, auth NONE) works and gives an https endpoint with a valid cert (`*.execute-api.us-east-1.amazonaws.com`).

**How to apply:**
- Lambda logs `requestContext.http.path` + `sourceIp` + `user-agent` to CloudWatch = self-contained redirect-follow / arbitrary-path oracle (no shared server).
- interactsh public servers (oast.me/oast.pro) get contaminated by other concurrent runs' Route53 health-check probes flooding the shared log — use a FRESH interactsh payload per test and grep for your own unique marker paths; prefer the CloudWatch self-marker channel for anything precise.
- Serve a valid discovery doc whose `issuer` field must equal the configured issuer string, `jwks_uri` = a marker path, to prove the 2nd (jwks) sink and http-scheme handling.
- `zip` is not installed; zip with python `zipfile`.
