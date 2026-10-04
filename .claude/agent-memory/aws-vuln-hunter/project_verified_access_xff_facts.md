---
name: verified-access-xff-facts
description: AWS Verified Access XFF/Cedar doc-defect facts + live-leg cost blockers (HUNT-E, run 2026-09-16-1)
metadata:
  type: project
---

HUNT-E (RESEARCH-PLAN-E, lens CC-7): AWS Verified Access `x_forwarded_for` as a first-class Cedar authz input.

**Confirmed doc defect (F26-class, Medium, AWS-owned).** `verified-access/latest/ug/trust-data-default-context.md` `context.http_request` schema lists `x_forwarded_for` (L46-50, "The value of the X-Forwarded-For request header" — raw client header) side-by-side with connection-derived `client_ip` (L61-65), identically framed, NO spoofability caveat. Preamble L8 invites keying policy on it. `auth-policies-policy-eval.md` L10: VA "validates the syntax ... but does not validate the data you put in the conditional clause."

**Observed product corroboration:** VA control-plane accepts XFF-keyed Cedar policies (`==`, `like "*ip*"`, even XFF==non-IP-string) with NO warning/error. Cheap (~4s, ~$0) reversible probe: create OIDC trust provider (dummy canary config accepted at create time), create instance, attach, create/modify group policy. Teardown reverse order: group -> detach -> instance -> trust provider; verify via describe-verified-access-{instances,trust-providers,groups} == [].

**Why live authz-bypass is deprioritized-by-cost (plan-authorized fallback):** (1) VA default-denies + user trust provider forces INTERACTIVE sign-in (getting-started L156/L177) — headless curl with forged XFF never reaches an access-granting Cedar eval without completing OIDC/IdC browser login. (2) No lightweight trust provider: IAM Identity Center needs an AWS Organizations instance (standalone won't work, user-trust.md L21) and isn't cleanly reversible; OIDC needs a full live IdP. (3) Endpoint needs internal ALB + ACM cert + public DNS CNAME + hourly VA billing. Minimal live chain = canary OIDC IdP + scripted headless auth + ALB + cert + DNS + endpoint = disproportionate.

Routing: aws-security (AWS-owned docs). Results: /work/findings/HUNT-E-verified-access-xff-results.md. See [[aws-env-setup]].
