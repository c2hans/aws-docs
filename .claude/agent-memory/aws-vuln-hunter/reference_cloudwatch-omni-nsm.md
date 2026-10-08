---
name: cloudwatch-omni-nsm
description: CloudWatch Omni + Network Security Manager live-test facts — org-gated ForOrganization surface, clean domain/space isolation, NSM org-DescribeOrganization gate, deep-link redirect allowlist
metadata:
  type: reference
---

Live run 2026-10-07 against [[env-sessions]] (default=183174222929 attacker, awsbb2=289531347876 victim). Both services live in botocore 1.43.108: `cloudwatchomni` (api 2025-01-01, endpoint cloudwatch-omni.<region>.amazonaws.com) and `network-security-manager` (api 2025-10-30). All leads REFUTED / DOC-GAP; clean isolation. No service-plane (fleet-role) evidence ever surfaced.

**Org posture (both accounts):** `organizations:*` (DescribeOrganization/ListRoots/DescribeAccount) uniformly `AccessDeniedException "You don't have permissions to access this resource."` even for AdministratorAccess — i.e. SCP-blocked member accounts, neither is an org management/delegated-admin. This makes every `*ForOrganization` omni API and all of NSM unprovisionable from these creds (positive org-admin paths = DOC-GAP, not refuted).

**CloudWatch Omni resource model / cheap substrate:**
- `CreateDomain(name, identityProviders=['IAM'])` → works in BOTH accounts, no role needed. domainArn uses service `cloudwatch` (arn:aws:cloudwatch:...:domain/d-...). Global app endpoint `https://d-<id>.cloudwatch-omni.global.app.aws`.
- `CreateSpace(name, domainId, dataAccessRoleArn)` → works; does NOT validate the roleArn exists at create time (accepted a roleArn whose IAM role creation had failed). Space creator auto-gets a SPACE_ADMIN grant (CreateAccessGrant self → ConflictException "active SPACE_ADMIN grant already exists"). Also an auto grant `OmniDefaults-*`.
- `CreateDomainForOrganization` / `GetSpaceCredentialsForOrganization` / `*ForOrganization` / `SearchPrincipals`(IdC-gated) → all org-gated.
- Teardown: delete grants (DeleteAccessGrant takes only grantId) → DeleteSpace(spaceId) → DeleteIntegration(identifier={'integrationId':...}) → DeleteDomain(domainId). Grants auto-drop with space.

**LEAD-1 GetSpaceCredentialsForOrganization (P0) — REFUTED(surface)+DOC-GAP:** context{spaceId | domainId+targetAccountId}, credentialType enum = only `SPACE_OPERATION`. From [default], ALL inputs (victim/self/bogus targetAccountId, bogus/guessed spaceId, EVEN own space in own domain) → identical `AccessDeniedException` 403 "Access denied". Enforcement keys on the caller's org-management/delegated-admin role (service-side authz, bare "Access denied", NOT IAM — admin has the action), NOT on caller-supplied targetAccountId. No differential = no existence/ownership oracle. Non-admin bypass refuted; never reached the fleet-role vend path (no hard stop triggered).

**LEAD-2 CreateAccessGrant / CreateDomainAccessGrantForOrganization (P0) — REFUTED, clean isolation:**
- CreateAccessGrant resolves `domainId` in the CALLER's account namespace: attacker passing victim's domainId → `ResourceNotFoundException "Domain not found"` (victim domain invisible). Both domainId AND spaceId validated (mydom+victimspace → "Space not found"); no "first-id-only" bug.
- Cross-account reads/mutations on victim space uuid: GetSpace/UpdateSpace/DeleteSpace → `AccessDeniedException "Authorization failed"` (victim uuid == bogus uuid, no existence leak). GetDomain → `ResourceNotFoundException "Domain not found"` (victim == bogus).
- `CreateDomainAccessGrantForOrganization` (permission enum=ADMIN only) → `AccessDenied "Access denied"` for BOTH victim and own domain (org-gated).

**LEAD-3 NSM PutAdminAccount / scope widening (P1) — REFUTED(surface)+DOC-GAP:** `PutAdminAccount(accountId, priority, adminScope{scopeFilter{includeAll|includeOnly|excludeOnly{accounts,organizationalUnits}}, firewallTypeScope})`. Self-designate, other-account designate, and scope-includes-victim ALL → `AccessDeniedException "You are not authorized to perform organizations:DescribeOrganization, which is required for this operation"`. NSM delegates the mgmt-account check to the REAL Organizations API; caller-supplied accountId/scope never reaches scope logic (org gate fires first). Non-admin data plane: `CreateScope` with ANY accountFilter (includeAll or include.accountIds=[victim]) → `ValidationException "accountFilter is not supported for this account"` — a non-NSM-admin can't define cross-account scope at all. Firewall types enum: WAF, SHIELD_ADVANCED.

**LEAD-4 CreateIntegration confused-deputy/SSRF (P1) — REFUTED:** `roleArn` is iam:PassRole-enforced — cross-account victim roleArn → `AccessDeniedException "...not authorized to perform: iam:PassRole on resource: arn:aws:iam::289531347876:role/... because no resource-based policy allows"`. PassRole check happens BEFORE other validation. No customer-controllable server-side fetch URL: SLACK only accepts oauthCodeCredential and exchanges against Slack's own fixed endpoint (bogus code → InternalServerException from the failed real exchange; providerId does not override host); AWS_INTEGRATION/AWS_CONFIG_SLREC use PassRole-gated roleArn (AWS_CONFIG_SLREC creates clean, authType NONE); EXTERNAL_AGENT requires catalogId (validated before any fetch). integrationType enum: AWS_CONFIG_SLREC, SLACK, EXTERNAL_AGENT, AWS_INTEGRATION.

**LEAD-5 CreateOneTimeDeepLinkCode (P2) — REFUTED(session-theft)+informational:** `redirectUrl` validation is robust: rejects off-domain, host@attacker userinfo, `//attacker`, path `/auth/callback/../..`, non-/auth/callback paths, http (must be HTTPS), query/fragment, subdomain-prefix (host.attacker.com), bare suffix, wrong TLD (.app.com), suffix+extra (.app.aws.evil.com). deepLinkUrl = `/auth/code?code=<64char>&domainId=<id>&redirect=<urlencoded>`. INFORMATIONAL loose spot: the host check is a suffix-pattern allowlist for `<any-single-label>.cloudwatch-omni.global.app.aws/auth/callback` — accepts ANY label incl. nonexistent omni hosts and OTHER domains' hosts (not bound to the code's domainId). But every accepted host is within AWS's own `*.cloudwatch-omni.global.app.aws` zone, so NO attacker-origin redirect/token-theft is possible. Cross-domain code: minting a code for a victim domainId → ResourceNotFound (domainId caller-scoped).

**LEAD-6 enumeration oracles — REFUTED:** no victim-vs-bogus differential anywhere (GetSpace, GetDomain, SearchPrincipals all identical for real-victim vs syntactically-valid-bogus).

Scoped-principal note: no re-judgement needed — every boundary crossing FAILED under the over-privileged AdministratorAccess principal, so a scoped principal fares no better. No findings.
