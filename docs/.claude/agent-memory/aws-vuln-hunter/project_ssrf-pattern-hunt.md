---
name: ssrf-pattern-hunt
description: Cross-service AWS "managed URL fetcher" SSRF sweep — in-scope accounts, OOB infra, and confirmed P3 OIDC-fetcher results
metadata:
  type: project
---

Ongoing SSRF pattern hunt across AWS managed server-side URL fetchers. Plan: `/work/ssrf-pattern-hunt-plan.md`; findings in `/work/findings/`.

**Accounts (tester-owned, in scope):** A `183174222929` (default profile), B `289531347876` (awsbb2 profile). Both `user/research-admin`. us-east-1. `source /work/env.sh`.

**Confirmed P3 (OIDC/JWKS discovery-fetch) results, 2026-09-07** (`19-avp-idc-appsync-oidc-ssrf-*.md`):
- **Verified Permissions** `CreateIdentitySource` `issuer`: create-time server-side fetch from AWS egress (e.g. 34.226.80.60/35.168.6.23), blind, rich differential ValidationException oracle. Redirects NOT followed. `jwks_uri` = 2nd sink (arbitrary https path, `http://` rejected). NO internal-IP egress guard (attempts TCP to 127.0.0.1/169.254/10.x) but https-only+no-redirect+IMDS-is-http = no internal reach. Fires under scoped principal.
- **AppSync** `openIDConnectConfig.issuer`: request-time fetch, anonymously triggerable via GraphQL `Authorization: Bearer <jwt>`. FOLLOWS redirects (arbitrary host/path) and ACCEPTS `http://` jwks_uri (proven to public OOB). Egress 3.213.7.93/98.84.71.162 UA Java/17.0.20.1. More capable than AVP; internal attempts stayed blind ("failed to load").
- **IAM Identity Center TTI**: blocked:scope — only SSO instance owned by out-of-scope acct `532876697804`.

**Why:** map which AWS fetchers reach internal/service-plane vs are contained; product-hardening disclosure to AWS.
**How to apply:** when handed another bundle, reuse the OOB pattern below and check whether the fetcher follows redirects / accepts http / has an internal-IP guard — those three axes are what separated AVP from AppSync.
