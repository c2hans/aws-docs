# Run 2026-10-04-m1 — null / refuted / blocked results (first-class)

Hunter execution of `_change-analysis/plans/2026-10-04-sincelastpush/_MASTER-hunter-dispatch.md`.
Teardown verified clean (ledger empty); no pre-existing resource mutated.

| Lead | Verdict | Note |
|---|---|---|
| A1 Anthropic user-profile cross-tenant | **artifact-CONFIRMED / live HARD-STOP** | → `finding-001` + aws-security routing |
| A2 `AWSManagedAccountManagementAccess` v2 cross-acct privesc | artifact-allowed / **live BLOCKED** | Target `role/managed/AWSManagedAccountManagementAccessRole` is `NoSuchEntity` in A & B ⇒ chain inert |
| A3 Resource Explorer SLR v56 data-plane reads | **CONFIRMED (artifact), no boundary** | `cassandra:Select`/`sdb:GetAttributes`/`guardduty:GetFindings`/`kafka:ListScramSecrets` allowed on `*`, but SLR single-account. Scope-creep note for SLR owners (Low/info) |
| A4 Security Hub V2 condition-key parity gap | **CONFIRMED (artifact), Med/info** | `GetRemediationsV2`/`ListExposuresByRemediationV2` carry no condition keys (only own-acct `hubv2*` ARN) while `GetFindingsV2` supports OCSFSyntaxPath — org cannot author an IAM guardrail on the remediation reads |
| B1/B3 EUM brand-profile/registration cross-acct exfil & IDOR | **REFUTED** | A→B bare-id `404` (per-acct namespace), full-ARN `403` (authz-first; real & fake B-ARN both 403 = no existence oracle). Account ownership enforced throughout |
| B2 EUM Notify-OTP cross-acct validate | **BLOCKED** (needs phone/10DLC in B) | Validate is fail-safe: fabricated (code,destIdentity,referenceId)→`200 {"status":"INVALID"}`, no config param, no leak |
| B4 Security Hub V2 cross-acct exposure/remediation read | **REFUTED (control) / IDOR BLOCKED** | `ListFreeTrialStatusesV2`(B) non-DA→`ValidationException: Organization not found`; `ListExposuresByRemediationV2`(fab TargetUid)→`404`; `GetRemediationsV2`(filter owner=B)→`200 Items:[]`. Full IDOR needs DA designation+member enrollment via out-of-scope mgmt acct |
| B5/B6 Marketplace resale-auth ownership/role bypass | **BLOCKED** | Publishing a canary product in B needs full seller onboarding (legal/banking); `aws-marketplace:ListEntities` SCP-denied (`p-r2n826oj`) |
| B7 Marketplace `UpdateLegalTerms` Url SSRF | **BLOCKED** (no product to attach terms to) | Preserved as HARD-STOP-discipline lead for when a seller product exists |
| B8 Cognito cross-app-client step-up ACCESS_TOKEN credit | **REFUTED** | Built ESSENTIALS pool + 2 clients + TOTP user; USER_AUTH never credits a presented access token; A-client token on B-client USER_AUTH left AvailableChallenges unchanged, still forced SOFTWARE_TOKEN_MFA; same-client TARGET loa:1 forced full re-auth; garbage token silently ignored. MFA floor held in every variant |
| B9 securityagent cross-tenant trigger write | **BLOCKED** (needs 2 SCM-connected canary accts) | Not feasible with synthetic resources |

## Environment topology discovered (affects future planning)
- **A (183174222929) and B (289531347876) share AWS Org `o-pf2hyvtase`, management account `532876697804`
  (OUT OF SCOPE), SCP `p-r2n826oj`.** "Treat B as the second account" works for data-plane cross-account
  tests, but anything requiring org-admin designation (Security Hub DA, Marketplace `ListEntities`) routes
  through the out-of-scope mgmt account and is therefore BLOCKED, not refuted.
- **end-user-messaging** signing name is `end-user-messaging` (not `endusermessaging`/`sms-voice`); validate-OTP
  is fail-safe; brand-profile reads enforce account ownership authz-first with no 403/404 differential on full
  ARNs — a cleanly-defended surface. Note for future windows.

## Resources created & destroyed (all torn down, re-enumerated gone)
Cognito pool `us-east-1_tRK97kpnf` (+2 app clients, 1 TOTP user) in A; Security Hub V2 subscription in A
(disabled); 1 brand-profile + 1 registration in B.
