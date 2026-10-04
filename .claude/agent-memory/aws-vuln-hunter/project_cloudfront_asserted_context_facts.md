---
name: cloudfront-asserted-context-facts
description: HUNT-D result — CloudFront CloudFront-* asserted-context header integrity is INTACT; all spoof hypotheses REFUTED (run 2026-09-16-1)
metadata:
  type: project
---

**CloudFront `CloudFront-*` viewer-header spoofing is REFUTED — do not re-run.** (RESEARCH-PLAN-D / HUNT-D, run 2026-09-16-1, results in `/work/findings/HUNT-D-cloudfront-asserted-context-results.md`.)

**What was observed live** (viewer → CloudFront `d3r83phw5jjfg7.cloudfront.net` → own echo origin, egress geo=DE):
- CloudFront **computes/overwrites** the entire `CloudFront-*` namespace before forwarding to origin. A viewer-supplied `CloudFront-Viewer-Country: ZZ` (or valid-but-wrong `US`, or `US,ZZ`, or duplicate headers) always arrives at origin as CloudFront's computed `DE`.
- Holds **even with the documented-correct origin-request policy** that provisions `CloudFront-Viewer-Country` (D-2 prize) — no append, no comma-join, no last-write-wins.
- `CloudFront-Forwarded-Proto` spoofed `https` over an HTTP viewer → origin sees `http` (computed). `CloudFront-Is-*-Viewer` computed from real UA. `X-Amz-Cf-Id` forged value overwritten with a real one (not duplicated).
- **No strip-control asymmetry:** `X-Real-IP`/`X-Forwarded-Proto` stripped AND `CloudFront-*` overwritten in the same request. The plan's premise (CF strips client headers but forwards its own namespace verbatim) is false.
- **D-6 (managed CloudFront SG prefix-list is cross-customer):** doc `restrict-access-to-load-balancer.html` is accurate — it leads with the secret-custom-header control and labels the prefix list "(Optional)" / "layer 3/4" / "traffic from CloudFront", never claims distribution-scoping. No doc defect.

**Nothing disclosure-grade.** Only a minor doc-clarity nit: the custom-origin behavior table says "CloudFront does not add the header before forwarding" for `CloudFront-*` and is silent that it *overwrites* a viewer copy — live behavior is safer than the silence implies.

**Env gotcha:** Lambda Function URL with `AuthType NONE` is **blocked by an org SCP** in account 183174222929 (403 despite public resource policy). Use API Gateway HTTP API as the public custom origin instead. Also: managed AllViewer* origin-request policies forward the viewer `Host` header, which API Gateway rejects (403) — use `AllViewerExceptHostHeader` or a custom policy that excludes `host`.

Related: [[trusted-upstream-federation-variant-analysis]] lens CC. Prior CC-1..CC-6 (ALB unsigned-header, API-GW authorizer-dropout) already refuted as customer footguns.
