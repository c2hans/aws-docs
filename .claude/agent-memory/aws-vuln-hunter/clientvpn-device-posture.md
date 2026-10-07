---
name: clientvpn-device-posture
description: AWS Client VPN device-posture attack surface — control-plane API, validation behavior observed live, and what is untestable headless
metadata:
  type: project
---

Target of the 2026-10-06 run: AWS Client VPN **device posture** (`DevicePostureOptions` on Create/ModifyClientVpnEndpoint) + Cedar auth policy (`*ClientVpnEndpointAuthorizationPolicy`). Feature IS live in botocore 1.43 and account 183174222929.

**Why:** doc-derived plan (`/work/vpn-attack-research-plan.md`) hypothesized token forgery/cross-tenant reuse/Cedar injection/PublicSigningKeyUrl SSRF.

**How to apply — what is testable vs blocked:**
- **Control plane fully testable.** Shapes: `DevicePostureOptions{Enabled, TrustProviders:[{TrustProviderType(crowdstrike|jamf|jumpcloud), TenantId, PublicSigningKeyUrl}]}`. Endpoints create in `pending-associate` with no VPC association → **no hourly cost, no ENI/SG/log residue** if ConnectionLogOptions.Enabled=false and never associated. Per-region limit 5 endpoints.
- **Data plane is NOT testable headless** (the whole FF/U/BB token story): needs AWS VPN client v6.2.0+ and a device-trust agent minting signed posture tokens + an established OpenVPN tunnel. Token forgery, cross-tenant token reuse, Cedar context injection, stale-token grace → all **blocked: precondition**.

**Observed control-plane validation (183174222929, us-east-1):**
- crowdstrike/jumpcloud: `PublicSigningKeyUrl` REQUIRED (`MissingParameter`); jamf: not required (creates fine).
- URL must be **https** (http/file → generic `InternalError` 500 — minor robustness bug, 400 expected).
- SSRF guard: rejects localhost + IP literals in decimal/hex/octal/dotted & IPv6 (`InvalidParameterValue: must reference a public hostname, not localhost or an IP address`). **But accepts any DNS hostname without resolving it** (`metadata.google.internal`, `internal.vpc.local` accepted) → latent SSRF-filter bypass IF the deferred data-plane JWK fetch is fleet-side (undocumented — HARD STOP line, not developed). No fetch occurs at create/modify time (collaborator got 0 hits).
- URL is **mutable post-create** via Modify (same validation) → TOCTOU on key source.
- Cedar policy parsed (`permit-all` ok, malformed rejected, **empty string accepted** — possible fail-open footgun).
- **IAM finding (confirmed, scoped-principal):** `DevicePostureOptions` is gated only by generic `ec2:ModifyClientVpnEndpoint` — a principal with just that action can repoint `PublicSigningKeyUrl` to an attacker host AND disable posture entirely, but is correctly blocked from the Cedar policy (`ec2:ModifyClientVpnEndpointAuthorizationPolicy`, separate action → UnauthorizedOperation). No granular action protects the device-trust config.

No HARD STOP hit: no link-local reached, no AWS fleet identity/issuer observed.
