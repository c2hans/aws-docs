---
name: aws-idp-metadata-fetchers
description: Behavior of AWS server-side IdP-metadata/OIDC-discovery fetchers (Cognito User Pools, WorkSpaces Web) as observed on 2026-09-07 — SSRF-relevant egress IPs, UAs, and guard characterization
metadata:
  type: reference
---

Server-side IdP-metadata / OIDC-discovery fetchers in **Cognito User Pools** and **WorkSpaces Web** share
the same two AWS-managed fetcher fleets (us-east-1, observed 2026-09-07):

- **SAML `MetadataURL`** fetch → User-Agent `Amazon/IdPConfig`. Follows HTTP redirects. **Semi-readable on
  Cognito**: `DescribeIdentityProvider` echoes `SSORedirectBindingURI`/`SLORedirectBindingURI`/
  `ActiveEncryptionCertificate` parsed from the fetched XML (readable oracle for SAML-shaped responses).
  WorkSpaces Web SAML is blind (stores only `MetadataURL`).
- **OIDC `oidc_issuer`** discovery fetch → User-Agent `Amazon/Cognito`. Blind (discovered endpoints not echoed).
- Egress IPs seen: 52.6.172.15, 3.217.36.237, 184.72.253.136 (all AMAZON/EC2 in ip-ranges.json, us-east-1).

**Egress guard is SOUND** (all internal-reach + XXE vectors refuted):
- Reserved-IP blocked (`Endpoints cannot be reserved IP addresses` / `... can not be private or local IPs`)
  on: direct URL, redirect hop (re-validated), DNS-resolved hostname (resolves & checks resolved IP),
  decimal-notation IPs (decoded), and on UpdateIdentityProvider (re-validated). Resolve-and-pin (no rebind window).
- OIDC path requires `https://` (rejects http pre-resolve).
- **SAML parser is XXE-safe**: external general entities AND external-DTD parameter entities are NOT resolved
  (no OOB fetch); DOCTYPE-with-entities → `Input XML is invalid`.

Net severity: Low AWS-egress confused-deputy / narrow readable SSRF; no internal/service-plane/cross-tenant
reach. Same family as agent-registry-fromurl-readable-ssrf but weaker primitive. Full write-up:
/work/findings/20-workspacesweb-cognito-idp-ssrf-bounded-egress-guard-sound.md
