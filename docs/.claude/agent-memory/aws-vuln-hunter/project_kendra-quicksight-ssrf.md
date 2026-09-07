---
name: kendra-quicksight-ssrf-env
description: Environment facts for A3/A4 SSRF hunt — Kendra closed to new customers; QuickSight JDBC probe fleet behavior, egress IPs, deny-set gap, and subscription teardown recipe
metadata:
  type: project
---

Findings from the 2026-09-07 SSRF pattern hunt bundle A3 (Kendra) + A4 (QuickSight), accounts A `183174222929` / B `289531347876`, us-east-1. Full report: `/work/findings/18-kendra-quicksight-ssrf-jdbc-egress-denylist-gap.md`.

- **Amazon Kendra is closed to new customers** (Maintenance Mode 2026-06-30, closed 2026-07-30). `kendra:CreateIndex` → `NotAuthorizedException` in BOTH in-scope accounts. Any Kendra web-crawler / connector SSRF surface is untestable here — don't re-attempt without an allowlisted account.
- **QuickSight data-source APIs require a subscribed account** ("Directory information for account … is not found" otherwise). Subscribe via `create_account_subscription` Edition=ENTERPRISE AuthenticationMethod=IAM_AND_QUICKSIGHT (free-trial tier, provisions in ~30s). **Teardown recipe:** `update-account-settings --no-termination-protection-enabled` THEN `delete-account-subscription` (reaches `UNSUBSCRIBED` in ~2 min).
- **QuickSight JDBC connector (`CreateDataSource`/`UpdateDataSource`, MySqlParameters Host+Port) is a confirmed blind SSRF / server-side TCP-connect engine** from AWS-owned egress `52.20.0.0/14` (observed 52.23.63.231/232/233). Connects to arbitrary ports. `ErrorInfo.Message` reflects the resolved IP (DNS oracle). Egress guard = resolve-and-check (blocks IMDS/RFC1918/loopback/decimal/IPv6-ULA, IMDS holds under DNS-rebind) BUT **deny-set is incomplete: allows link-local 169.254.0.0/16 except .169.254 (incl. 169.254.170.2 ECS creds) and CGNAT 100.64.0.0/10**. Blind (MySQL wire proto) → no body/credential read → Low-Med product-hardening. WEB_CRAWLER LoginPageUrl is NOT fetched at create (only at ingestion).

**Why:** These are expensive/slow preconditions and a non-obvious teardown; re-deriving them wastes budget.
**How to apply:** Skip Kendra entirely in these accounts. For any future QuickSight fetcher hunt, reuse the subscription recipe and the JDBC-probe primitive; a *readable* connector over the same egress layer would escalate the deny-set gap.
