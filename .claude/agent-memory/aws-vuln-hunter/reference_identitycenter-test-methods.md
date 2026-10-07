---
name: identitycenter-test-methods
description: Reusable facts/techniques for live-testing IAM Identity Center / Identity Store (singlesignon, identitystore, sso-admin) in the two sandbox accounts
metadata:
  type: reference
---

IAM Identity Center hunt facts (observed 2026-10-06, run 20261006-idc). See [[agentcore-env]] for accounts/tooling.

**Org topology (critical scope fact):** Both sandbox accounts (183174222929, 289531347876) are MEMBER accounts of an org whose IdC ORG instance (ssoins-7223cfab9178db6f, store d-9067d20885) is owned by OUT-OF-SCOPE account 532876697804. ListInstances surfaces it to members but it must NOT be mutated/Described. organizations:DescribeOrganization is denied to members.

**Synthetic substrate = account instance:** `sso-admin:CreateInstance(Name,Tags)` creates a self-owned ACCOUNT-level IdC instance + dedicated identity store (free, instant) in-scope. `DescribeInstance` gives IdentityStoreId. `DeleteInstance` cascades the store. This is the clean way to get a mutable identity store you own. Account instances do NOT support permission sets / account assignments / catalog applications ("This operation is not supported for account instances") — so L10-style CreateAccountAssignment and most PutApplicationGrant/L6 tests are blocked:precondition unless you have an in-scope ORG instance (we don't).

**UpdateIdentityStore NetworkConfiguration (L1/L7/L8):**
- NetworkConfiguration = {VpceAccessRequired:bool, ApiRestrictSourceVpcs[], ApiAllowSourceIps[], ScimRestrictSourceVpcs[], ScimAllowSourceIps[]}. FULL-REPLACE: omitted fields are cleared (footgun, confirmed).
- Rule: when VpceAccessRequired=false, ALL source lists must be empty (ValidationException otherwise) = fully-open state. Restrictions only expressible with VpceAccessRequired=true.
- Self-lockout GUARD: a posture that would deny the caller's own source IP is rejected ("would deny the calling principal access... Add the caller's source IP to ApiAllowSourceIps"). You literally cannot brick yourself. Posture evaluated vs caller source IP at write time. Get your egress IP from CloudTrail LookupEvents GetCallerIdentity sourceIPAddress (in-AWS, no external host).
- ApiRestrictSourceVpcs regex: vpc-[0-9a-f]{8}(([0-9a-f]){9})? (8 or 17 hex). ApiAllowSourceIps/ScimAllowSourceIps accept 0.0.0.0/0.

**L1 finding (CONFIRMED, Medium, AWS-owned granularity gap):** identitystore:UpdateIdentityStore has resource Identitystore* and ZERO condition keys (not even PrimaryRegion; siblings UpdateUser/UpdateGroup carry PrimaryRegion+ExternalIdIssuers). No way to permit UpdateIdentityStore while denying a network-perimeter-weakening change -> scoped role with only that action flips VpceAccessRequired true->false / adds 0.0.0.0/0. Intra-account defense-in-depth removal, not cross-tenant, not data exposure. Classification: least-privilege-trap / Client-VPN-M2 shape. Remediation = AWS add a NetworkConfiguration-scoping condition key or split the action.

**Trusted token issuer (L2/L4/L5, config-plane only):** sso-admin:CreateTrustedTokenIssuer(InstanceArn,Name,TrustedTokenIssuerType='OIDC_JWT',TrustedTokenIssuerConfiguration={OidcJwtConfiguration:{IssuerUrl,ClaimAttributePath,IdentityStoreAttributePath,JwksRetrievalOption='OPEN_ID_DISCOVERY'}}). Accepts ARBITRARY IssuerUrl incl http:// AND http://169.254.169.254 (no TLS/SSRF validation at create). Mapping is arbitrary JMESPath and MUTABLE via UpdateTrustedTokenIssuer. Condition keys on CreateTrustedTokenIssuer = tags + sso:PrimaryRegion only (no issuer/audience/scheme key). NO synchronous discovery fetch at create (accepts unreachable hosts instantly).

**HARD-STOP ZONE:** the OIDC discovery/JWKS fetch and sso-oauth:CreateTokenWithIAM token exchange = AWS service plane. The fetch happens at exchange time, NOT at TTI create. Never induce it; L3 SSRF and L5/L6 impersonation/audience impact are therefore blocked:scope (service-plane), config-plane facts are the documentable result.

**Tenant isolation (L9, clean):** cross-account DescribeIdentityStore(real foreign store)->AccessDeniedException vs (fabricated id)->ResourceNotFoundException = existence-oracle delta only (40-bit id space, no data) = not of interest. ListIdentityStores returns only the CALLER's own stores (not org/member instance). No cross-account read/mutate.
