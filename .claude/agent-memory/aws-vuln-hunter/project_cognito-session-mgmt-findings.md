---
name: cognito-session-mgmt-findings
description: Results of testing Cognito user-pool session-management APIs + GetDerivedToken exchange (run 2026-11-17-1) — surface held; what to skip, what needs a browser harness
metadata:
  type: project
---

Cognito user-pool **session management** (ListUserSessions/RevokeUserSession, Admin*, Get/Set UserPool[Client]SessionConfiguration) and adjacent **GetDerivedToken** (RFC 8693 token exchange) were hunted live in account A (run 2026-11-17-1, plan `/work/analysis-2026-11-17/qb/03-cognito-sessions.md`). **The surface is well-built — all hypothesized isolation gaps were REFUTED.** Don't re-run these unless the SDK/feature version changed.

**What held (don't retest):**
- Cross-user `RevokeUserSession`(A token, B's SessionId) -> `ResourceNotFoundException`. SessionId is resolved inside the token's own user namespace; no `Username` param != no ownership check. Same for `ListUserSessions` (pool/`iss`-scoped, not username-scoped — verified with a same-username second pool).
- SessionIds carry a checksum (last-char flip -> `InvalidParameterException`; checksum-valid random -> `ResourceNotFoundException`) so there's **no existence oracle** and they're not enumerable (~2^129).
- `AdminRevokeUserSession` Username<->SessionId binding holds (mismatch -> ResourceNotFound).
- Token pinning: ID token rejected (`NotAuthorizedException`); revoked/global-signed-out access tokens rejected; cross-pool scoped.
- Cross-account `UserPoolId` reach: `ResourceNotFoundException` (account/region-local; confirmed with a real awsbb2 pool).
- GetDerivedToken: scope-intersection enforced ("Requested scopes are not permitted for this subject token"), unregistered audience rejected ("Invalid resource requested"), subject revocation honored AND cascades to the derived token (survives nothing past GlobalSignOut).

**Only confirmed item:** GetDerivedToken does NOT evaluate `may_act` (AWS-documented) — a DELEGATION exchange stamps `act.sub` = whatever ActorToken you present, no subject consent checked. BOUNDED (caller must hold valid tokens for both subject and actor) -> intended-behavior/design-caveat, reportable only if a downstream service authorizes on `act`. Also: `GetDerivedToken` is a live op but ABSENT from `list_cognito-idp.md` IAM action table (doc-gap) and absent from botocore 1.44.3 (call it with raw SigV4/JSON, X-Amz-Target `AWSCognitoIdentityProviderService.GetDerivedToken`; ClientId-only path needs no SigV4).

**Could-not-test (need a managed-login/hosted-UI browser harness to create `sso...` sessions):** SSO-session cascade (RevokeAssociatedSessions NONE/LINKED), global-sign-out with tracking OFF, cross-client 90-day MaxValidityMinutes SSO reuse. API-only `InitiateAuth` makes only `tkn...` token sessions (no OriginSessionId parent).

**Environment gotcha:** pre-token-generation V2_0 `claimsToAddOverride` was **wholly inert** in a fresh ESSENTIALS *and* PLUS pool (even non-reserved claims never landed, trigger confirmed executing). Blocked the documented "`sid`-injection silently disables tracking" test (Area 5) — session tracking stayed fully operational and `sid` was always the real session id. Needs a known-good claim-customization config to close. Session tracking requires ESSENTIALS/PLUS tier (set `UserPoolTier` on create; changeable via UpdateUserPool). See [[aws-test-environment]].
