---
name: ra-enforced-boundaries
description: Confirmed Roles Anywhere service-side controls (what holds) and the real residual gaps, from live testing 2026-09-30
metadata:
  type: project
---

Live-tested IAM Roles Anywhere (accounts 183174222929 / 289531347876, us-east-1) against the doc-derived attack plan. Results that hold and that future RA runs should treat as settled:

**Enforced service-side (don't re-litigate as bugs):**
- `trustAnchorArn` in CreateSession IS cryptographically bound to the signing CA — a cert must chain to the CA of the *specific* trustAnchorArn named (attacker cert + victim TA → 403 "Untrusted signing certificate"). `aws:SourceArn` cannot be spoofed; it reflects the real TA and STS enforces the role-trust condition. The documented confused-deputy mitigation is real.
- Cross-account vend blocked at two layers: CreateProfile ("Cross-account pass role is not allowed") and CreateSession (400 "different account ID").
- Disable (TA/profile) and CRL revocation take effect immediately — no usable TOCTOU window (strongly consistent, <1.5s).
- CreateProfile enforces `iam:PassRole` on every role in roleArns (plan wrongly assumed no PassRole needed).
- Attribute mappings confined to `aws:PrincipalTag/x509{Subject,Issuer,SAN}` (certificateField is an enum; specifier validated). Cannot populate a foreign ABAC key or set arbitrary sts:SourceIdentity. Signature verification enforced; unsigned rejected; ListSubjects is account-scoped.

**Real residual findings:**
- CRL is per-trust-anchor, NOT per-CA: same CA registered as two trust anchors → CRL on one does not block the cert via the other (Medium; revocation-completeness footgun).
- x509Subject/Issuer/SAN trust-policy conditions are attacker-chosen strings — worthless without aws:SourceArn (customer footgun, matches AWS's own "strongly recommended aws:SourceArn").
- `rolesanywhere:CreateTrustAnchor`+`CreateProfile`+`iam:PassRole(role)` = AssumeRole-equivalent for any RA-trusting role (standard PassRole→compute escalation, RA as the consuming service).
- No DeleteSubject API — Subject audit records are non-deletable and persist after all TAs/profiles are removed (teardown leaves them orphaned; synthetic-CN only, inert).
