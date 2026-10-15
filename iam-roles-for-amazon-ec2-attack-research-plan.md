# IAM Roles for Amazon EC2 — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html` (+ `.md` twin) and its linked children — `instance-metadata-security-credentials.html`, `permission-to-pass-iam-roles.html`, `attach-iam-role.html`, plus the "Instance identity roles" section on the parent page and its six consuming-service pages (SSM DHMC, EC2 Instance Connect, GuardDuty Runtime Monitoring, Lambda Managed Instances, Bedrock AgentCore, STS GetCallerIdentity). Authoritative condition-key data from the IAM Service Authorization Reference `list_ec2.md` (10,206 lines), `list_iam.md`, `list_sts.md`, `list_ssm.md`, pulled live 2026-10-15 by `curl`+`grep` (WebFetch of these truncates before the tables). Status: **documentation-derived hypotheses only; nothing tested against a live account.**

> **Offline mirror note:** `/work/aws-docs` (122 files) does NOT contain this page or its children — only API_* stubs and sibling plans. All page content read from the online `.md` twins on 2026-10-15. No offline==online drift comparison possible for the content pages; condition-key tables cross-checked against the live Service Authorization Reference.

> **Relationship to existing sibling plans (COMPLEMENT, do not restate):** this plan OWNS the **instance-profile attach/replace/detach + `iam:PassRole` credential-vending privesc chain**, the **IMDS role-credential retrieval surface** (incl. IMDSv2 enforcement condition keys), and **EC2 instance identity roles** (new, thinly-documented feature). It defers:
> - EC2 **AWS-managed policy** audit (EC2FastLaunchFullAccess PassRole+RunInstances privesc headliner, EC2InstanceConnect SendSSHPublicKey) → `security-iam-awsmanpol-attack-research-plan.md`.
> - EC2 **condition-key evaluation semantics** canon (AssociateSecurityGroupVpc, `ec2:Attribute` case-sensitivity, ResourceID resolve-to-* Deny-inert pairs, `ec2:SourceInstanceARN`) → `iam-policies-for-amazon-ec2-attack-research-plan.md`.
> - EC2 **console sample policies** (t2.micro/subnet sample, AuthorizeSecurityGroupIngress Resource:* ) → `iam-policies-ec2-console-attack-research-plan.md`.
> - The `ExamplePolicies_EC2.html` "Work with IAM roles" sample block itself → `ExamplePolicies_EC2-attack-research-plan.md` (cross-ref; this plan audits only the sample printed on the three target children).
> - The `ec2-security.html` hub framing → `ec2-security-iam` / hub note.

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- Preferred read-only oracle for every IAM-scoping lead here is **`iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy`** (a condition key either applies to an action or it does not — no resource creation needed). Escalate to a live scoped call only with synthetic canary data under a role holding *exactly* the artifact.
- **`DryRunOperation` is caller-IAM only, NOT an ownership oracle** — it is evaluated before resource resolution.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane (e.g. the fleet identity behind an instance identity role integration), stop, preserve evidence, flag for AWS-Security disclosure.

---

## 1. Pentest Objectives (boundary-breach goals, concrete outcomes)
1. **Privilege escalation via role attach:** holding only `ec2:AssociateIamInstanceProfile`/`ec2:ReplaceIamInstanceProfileAssociation` + `iam:PassRole` (and control of an instance), attach a *more-privileged* role to an instance and harvest its credentials from IMDS — gaining permissions the caller never held directly. **Breach oracle:** an API action performed with a role the caller could not have assumed, sourced from IMDS creds on an instance the caller attached the role to.
2. **IMDSv2-enforcement guarantee breakage:** prove that a documented "require IMDSv2 / require tokens" mandate is *not* expressible against a given launch/attach path (an inert or wrong-named condition key), so instances still vend role credentials over IMDSv1 reachable by SSRF. **Breach oracle:** a policy keyed on the IMDS-version/role-delivery control is accepted but authorizes a weaker configuration (SimulateCustomPolicy shows the key never binds the action).
3. **Instance-identity-role abuse:** reach the always-present instance identity credentials at IMDS `/identity-credentials/ec2/security-credentials/ec2-instance` and use them against a consuming service (SSM DHMC, EC2 Instance Connect) to act as, or on behalf of, an instance that is not the caller's — or to obtain a role the consuming service passes to the instance. **Breach oracle:** a consuming service treats the identity-role credential as authority to register/mutate/receive-a-role for an instance the credential's holder does not own.
4. **Cross-tenant / cross-account reach** on any of the above = Critical and the primary target; intra-account cross-team wildcard footguns = lower, but AWS-authored uneditable artifacts stay in scope (Tier-2).
5. **Read-oracle recon:** enumerate instance→instance-profile(role) mappings account-wide via an unscopable Describe to select privesc targets.

---

## 2. Components, Assets, and Design

**Mechanism (not marketing):** EC2 delegates AWS API permissions to code on an instance by attaching an **IAM role** to the instance, wrapped in an **instance profile** (1:1 container; a role may live in many profiles, a profile holds exactly one role). The instance's applications retrieve **temporary role credentials** from the **Instance Metadata Service (IMDS)** at `http://169.254.169.254/latest/meta-data/iam/security-credentials/<role-name>`. Separately, every instance also has an auto-created **instance identity role** whose credentials sit at IMDS `/identity-credentials/ec2/security-credentials/ec2-instance` — present regardless of feature enablement, with **no trust policy and not subject to any identity or resource policy**.

**Customer-facing interface / APIs:**
- Control plane (SigV4 IAM): `RunInstances` (launch with `IamInstanceProfile`), `AssociateIamInstanceProfile`, `ReplaceIamInstanceProfileAssociation`, `DisassociateIamInstanceProfile`, `DescribeIamInstanceProfileAssociations`, `ModifyInstanceMetadataOptions`; IAM `PassRole`; `iam:CreateInstanceProfile`/`AddRoleToInstanceProfile` (profile construction).
- Data plane (link-local, no SigV4): IMDS HTTP on `169.254.169.254` — IMDSv1 (open GET) vs IMDSv2 (`PUT /latest/api/token` → session token, hop-limit-bounded).
- Consuming services of the instance identity role: SSM DHMC (`RegisterManagedInstance` + passes `AWSSystemsManagerDefaultEC2InstanceManagementRole`), EC2 Instance Connect (host-key update), GuardDuty Runtime Monitoring, Lambda Managed Instances, Bedrock AgentCore Runtime Instances, STS `GetCallerIdentity`.

**Identity / credential model:**
- Role creds: temporary STS creds surfaced through IMDS; **not subject to the role's max-session-duration** (doc note) — long-lived refresh on the box.
- Instance identity role ARN: `arn:aws:iam::<account>:assumed-role/aws:ec2-instance/<instance-id>` — **fully predictable** from account-id + instance-id.

**Resource identifiers / entropy:** instance IDs `i-<17 hex>` (not fabricable blind cross-account, but the identity-role ARN is derivable once an instance-id is known); instance-profile ARNs are name-based (`instance-profile/<name>`); association IDs `iip-assoc-<hex>`.

**Where untrusted data meets privilege:** (a) a caller-chosen *instance-profile/role ARN* fed to attach/launch (PassRole seam); (b) IMDS as an SSRF sink that converts any server-side-fetch bug on the box into credential theft; (c) the instance identity credential as an assertion a downstream service trusts.

```
   caller (IAM principal)
      │  RunInstances(IamInstanceProfile) / Associate / Replace  + iam:PassRole(role)
      ▼
   ┌─────────────── EC2 instance ───────────────┐
   │  app code ──GET──▶ IMDS 169.254.169.254     │
   │                     ├─ /iam/security-credentials/<role>  (role creds, no max-session cap)
   │                     └─ /identity-credentials/ec2/security-credentials/ec2-instance
   │                            (instance identity creds — always present, no trust policy)
   └──────────────────────────────────┬──────────┘
         identity creds used by ──────▶ SSM DHMC / EC2 Instance Connect / GuardDuty /
                                        Lambda Managed Inst / AgentCore / STS GetCallerIdentity
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Low-priv IAM principal | High-priv IAM role's effective permissions | `Associate`/`Replace`IamInstanceProfile + `iam:PassRole` → IMDS cred harvest | Caller performs an action only the attached role could; creds trace to IMDS of the attached instance |
| Caller's identity policy (intends IMDSv2-only) | Instance's actual IMDS config | `ec2:MetadataHttpTokens` / `ec2:RoleDelivery` condition keys at launch/attach/modify | A Deny/Allow keyed on the IMDS control is accepted but never binds the action (SimulateCustomPolicy) → IMDSv1 still vends creds |
| Any process/SSRF on the instance | Role credentials | IMDS GET on `169.254.169.254` | Credential retrieval from a request that should not reach IMDS (hop-limit / v1 open) |
| Holder of instance X's identity creds | SSM / EC2 Instance Connect acting for instance X (or another) | Consuming service trusts the identity-role credential | A consuming service registers/mutates/passes-a-role for an instance the credential-holder does not own |
| Instance identity role (no trust/identity/resource policy) | AWS consuming-service plane | Service-side decision to trust the credential | Any identity/credential/ARN belonging to AWS's own fleet surfaces — **HARD STOP** |
| Any principal with `ec2:DescribeIamInstanceProfileAssociations` | Account-wide instance→role mapping | Unscopable List action (only `ec2:Region`) | Enumerating role ARNs attached to instances the caller cannot otherwise read |
| `DisassociateIamInstanceProfile` holder | A running app instance's AWS access | Detach the profile | App on a foreign-but-reachable instance loses role creds (availability) |

---

## 4. API / Interface Inventory

| Name | Mutating | Ext-facing | Resource type (list_ec2) | Condition keys of interest | Notes |
|---|---|---|---|---|---|
| `RunInstances` | yes | yes | `instance*` (+many) | `ec2:InstanceProfile`, `ec2:MetadataHttpTokens`, `ec2:MetadataHttpEndpoint`, `ec2:MetadataHttpPutResponseHopLimit`, `ec2:InstanceMetadataTags` — **NOT** `ec2:NewInstanceProfile`, **NOT** `ec2:RoleDelivery` | Launch-time attach uses `ec2:InstanceProfile` key |
| `AssociateIamInstanceProfile` | yes | yes | `instance*` | `ec2:InstanceProfile` **and** `ec2:NewInstanceProfile`, + instance tag/metadata keys | Attach to running/stopped instance; needs `iam:PassRole` |
| `ReplaceIamInstanceProfileAssociation` | yes | yes | `instance*` | same as Associate (incl. `ec2:NewInstanceProfile`) | **Swap role on a running instance** by association-id |
| `DisassociateIamInstanceProfile` | yes | yes | `instance*` | `ec2:InstanceProfile` (no `NewInstanceProfile`) | Detach = availability/DoS primitive |
| `DescribeIamInstanceProfileAssociations` | no | yes | **(blank)** | **only `ec2:Region`** | **Unscopable account-wide read oracle** (instance→role map) |
| `ModifyInstanceMetadataOptions` | yes | yes | `instance*` | `ec2:MetadataHttpTokens`/`-Endpoint`/`-PutResponseHopLimit`/`InstanceMetadataTags` (list_ec2:8873 — all 4, parity with RunInstances); **no key for `HttpProtocolIpv6`** | Weakens IMDS **live, no reboot**; blocked only by account `HttpTokensEnforced` |
| `ssm:RegisterManagedInstance` | yes | yes | **(blank)** | `aws:RequestTag`, `aws:TagKeys`, `ssm:NodeAccountId`, `ssm:NodeOrgId` — **NO `SourceInstanceARN`** (unlike all other SSM mgmt actions) | DHMC registration; identity-role confused-deputy (§5C) |
| `ec2:RoleDelivery` (key, not action) | — | — | — | global credential-context key; used `Action:"*"` Deny `NumericLessThan 2.0` | Enforces IMDSv2-sourced-creds-only account-wide (ExamplePolicies_EC2) |
| `iam:PassRole` | yes | yes | `role*` | `iam:PassedToService` (ec2.amazonaws.com), `iam:AssociatedResourceArn`, `aws:ResourceTag`, `iam:ResourceTag` | The real gate on *which role* gets attached |
| `sts:GetCallerIdentity` | no | yes | — | none (list_sts:125) | Permission-free, deny-silent identity oracle with instance-identity creds |

Key fields to probe: `IamInstanceProfile.{Arn,Name}` (two naming for one resource — Lens A), association-id vs instance-id (Replace/Disassociate), `MetadataOptions.{HttpTokens,HttpEndpoint,HttpPutResponseHopLimit,InstanceMetadataTags}`.

---

## 5. Recommended Areas of Focus
*(One block per firing lens; priority order. §5A–§5C enriched by three parallel documentation deep-dives folded in below.)*

### §5A — PassRole + instance-profile attach privilege escalation (Lens B / E / C / R / S / X) — HIGHEST PRIORITY
**Background.** Attaching an instance profile vends the wrapped role's credentials to anything on the instance via IMDS, with creds that **bypass the role's `MaxSessionDuration`** (EC2 auto-refreshes them for the life of the association — "not subject to maximum session durations configured in the role"). Authorization is split across **two services**: `ec2:Associate/Replace/RunInstances` (scoped by `ec2:NewInstanceProfile`/`ec2:InstanceProfile` + instance tag/ID keys) **and** `iam:PassRole` on the role (scoped by `iam:AssociatedResourceArn` + `iam:PassedToService`). A gap in *either* half opens privesc.

**Security Concern.** Confirmed from `list_ec2.md`/`list_iam.md` + the three EC2 UserGuide pages (2026-10-15):
- **PassRole IS enforced on all four paths** — `iam:PassedToService=ec2.amazonaws.com` is wired to `AssociateIamInstanceProfile` (list_ec2:160-161), `ReplaceIamInstanceProfileAssociation` (4298-4299) **and** `RunInstances` (4457-4458). `permission-to-pass-iam-roles.md` lists all four actions as required together. So there is **no "Replace skips the PassRole check" bypass** (this *refutes* an earlier hypothesis) — the privesc instead rides on PassRole being granted *too broadly*.
- Attach *can* be scoped **two independent ways**: by **which instance** (`ec2:ResourceTag`/`ec2:InstanceID`, since `Resource` must be an `instance*` ARN) and by **which profile is attached** (`ec2:NewInstanceProfile` on Associate/Replace, def 10134; `ec2:InstanceProfile` on RunInstances/Disassociate, def 10113). This **refutes** the common belief that only `iam:PassRole` can scope the role side — EC2 itself exposes an ARN-typed key for the profile on the EC2 action. The catch: *no EC2 UserGuide page teaches either key.*
- **Lens-X wrong-key-name fail-open:** `RunInstances` scopes the attached profile via `ec2:InstanceProfile` only (**NO `ec2:NewInstanceProfile`**); Associate/Replace use `ec2:NewInstanceProfile`. An admin who writes `Deny unless ec2:InstanceProfile = <approved>` covers `RunInstances` but is **inert on Associate/Replace** (and vice-versa). A condition template ported from an Associate statement onto a `RunInstances` statement silently loses the pin. Two key names for one conceptual control across one family = silent coverage gap.
- **No `iam-instance-profile-association` resource type exists.** Confirmed by exhaustive grep of the resource-ARN table — authorization for Replace/Disassociate anchors entirely to the **`instance` ARN**, never the `iip-assoc-...` AssociationId the CLI makes look authoritative. A policy author who writes `Resource: arn:...:iam-instance-profile-association/iip-assoc-*` finds no such ARN format → the pin they think they wrote does not exist (doc-vs-reference gap).
- `iam:PassRole` (list_iam:2387) requires `role*` and supports `iam:AssociatedResourceArn` (2434: "the resource the role will be used on behalf of" — the instance ARN) + `iam:PassedToService`. **`iam:AssociatedResourceArn` is mentioned on NONE of the three EC2 UserGuide pages** — the only scoping technique AWS teaches is role-ARN-*prefix* matching on `Resource`, which bounds the role axis but not the consuming-instance axis.

**High-level Test Scenarios (falsifiable):**
1. **Claim (Lens E, headline):** `ec2:ReplaceIamInstanceProfileAssociation` (on `instance/*`, no `ec2:NewInstanceProfile` cond) + `iam:PassRole` on a high-priv ec2-trusting role + reach to a running instance ⇒ attacker swaps the role **in place, no stop/start/reboot** (`attach-iam-role.md`: "the instance must be running… API actions… are not interrupted") and harvests creds from IMDS. → **Oracle:** `iam:SimulateCustomPolicy` for `{ReplaceIamInstanceProfileAssociation on target instance, PassRole on target role with PassedToService=ec2}` → both-allow confirms the chain is policy-live. IMDS reachability needs a live hunter. → **Sev: Critical** (role is cross-service-powerful), High intra-team.
2. **Claim (Lens X):** a Deny `ec2:AssociateIamInstanceProfile if ec2:InstanceProfile != approved` fails — Associate reads `ec2:NewInstanceProfile`, so the Deny never binds and the unapproved profile attaches. → **Oracle:** SimulateCustomPolicy shows the Deny inert (key mismatch) while the Allow passes; also simulate `ArnLike ec2:NewInstanceProfile` on a `RunInstances` statement → ignored for that action. → **Sev: Medium–High** (control bypass by key-name confusion; produces false confidence in a written-but-inert condition).
3. **Claim (Lens B):** `iam:AssociatedResourceArn` *could* pin PassRole to a single instance ARN but is undocumented for this flow, so real-world policies under-scope. → **Oracle:** SimulateCustomPolicy for `iam:PassRole` with a `contextEntry` setting `iam:AssociatedResourceArn` to a specific instance ARN, comparing allow/deny with/without a matching `Condition` under `PassedToService=ec2` → confirms the key is live and the pin works. → **Sev: Medium–High** (systemic under-scoping; it's the official example that omits it).
4. **Claim (Lens R/S, headline artifact defect):** the single AWS sample policy in `permission-to-pass-iam-roles.md` is over-broad on both axes. Statement 1 grants `RunInstances/Associate/Disassociate/Replace` on **`Resource:"*"` with no Condition** → attach/replace a role on *every* instance in the account/region. Statement 2 grants `iam:PassRole` on a **role-name prefix wildcard** `role/DevTeam*` → classic **role-squatting escalation**: anyone who can `iam:CreateRole` named `DevTeam*` with an `ec2.amazonaws.com` trust policy and `AdministratorAccess` can then be passed+attached via Statement 1. The console note adds `iam:ListInstanceProfiles` (account-wide List, no scoping) — compounds recon breadth. → **Oracle:** SimulateCustomPolicy under the verbatim sample across several unrelated instance ARNs → `allowed` for all. → **Sev: High** (AWS-authored copy-verbatim artifact; defect propagates to every copier).
5. **Claim (Lens C):** the usual containment control "cap blast radius with a short `MaxSessionDuration`" is a **no-op** here — IMDS creds ignore it; the only real mitigations are detach/replace-fast + rotate. → **Oracle:** doc note (iam-roles-for-amazon-ec2.md). → **Sev: raises severity of scenario 1 (persistence).**

Doc evidence: list_ec2.md:160, 4298, 4455, 4756, 7921, 9407, 9596, 10113, 10134; list_iam.md:2387, 2434, 2442; permission-to-pass-iam-roles.md (sample policy + required-actions sentence); attach-iam-role.md ("instance must be running… not interrupted"). Severity-if-true: **Critical** (scenario 1), **High** (sample artifact).

### §5B — IMDS role-credential retrieval & IMDSv2 enforcement (Lens G / C / S / U / X / M / O)
**Background.** IMDS is the credential-delivery channel and the canonical SSRF sink (AWS's own Warning on `instance-metadata-security-credentials.md` names HTTP proxies, HTML/CSS validators, and XML processors as credential-exposure vectors). Creds are JSON (`AccessKeyId`/`SecretAccessKey`/`Token`/`Expiration`), rotated with a ≥5-min overlap, no fixed TTL published. "Require IMDSv2" is the documented hardening; the question is whether it is *expressible* as IAM across every path.

**Security Concern (confirmed from list_ec2.md + ExamplePolicies_EC2.md + the IMDS config pages):**
- The per-action enforceable IMDS keys are `ec2:MetadataHttpTokens` (optional|required, def 10131), `ec2:MetadataHttpEndpoint` (10129), `ec2:MetadataHttpPutResponseHopLimit` (10130), `ec2:InstanceMetadataTags` (10111) — **all four present on both `RunInstances` (line 9599) and `ModifyInstanceMetadataOptions` (line 8873)** → launch-vs-modify parity holds for these four.
- **CORRECTED headline on `ec2:RoleDelivery` (an earlier draft wrongly called it "defined-but-unwired/inert" — that is REFUTED).** `ec2:RoleDelivery` (def 10164, Numeric, "version of the IMDS for retrieving IAM role credentials") is **real and functions correctly** — it is a **global credential-*context* key**, not a per-action attach key. `ExamplePolicies_EC2.md` §"Require role credentials to be retrieved from IMDSv2" shows its sole intended use: `Effect:Deny, Action:"*", Resource:"*", Condition:{NumericLessThan:{ec2:RoleDelivery:"2.0"}}` — a policy evaluated on **every subsequent API call signed with EC2 role credentials**, denying the call if those creds were originally retrieved over IMDSv1. That is exactly *why* it never appears on any action's per-action condition column in `list_ec2.md` (those columns list resource-scoped keys for one action; RoleDelivery is checked against the caller's *request context* with `Action:"*"`). **The real trap is the opposite of "inert":** an auditor reading only the per-action tables concludes RoleDelivery "isn't wired to anything" and misses that it is the one key that actually enforces IMDSv2-*only credential use* account-wide. Still worth a lead: confirm the key is live via SimulateCustomPolicy and that it is *credential-context*, not request-param — i.e. it cannot pin a *launch* to IMDSv2 (only `ec2:MetadataHttpTokens=required` does that), only *downstream use* of v1-sourced creds.
- **Real governance gap — `ec2:MetadataHttpProtocolIpv6` does NOT exist.** `HttpProtocolIpv6` is a settable `MetadataOptions` field (RunInstances/ModifyInstanceMetadataOptions) but there is **no IAM condition key** for it (0 hits in list_ec2.md). An SCP/IAM Deny therefore **cannot restrict or require** the IMDS IPv6 endpoint (`[fd00:ec2::254]`) — the control knob exists, the governance primitive does not (Lens S/U).
- **Doc self-contradiction (Lens S/U).** `ExamplePolicies_EC2.md` §"Deny opt-out of IMDSv2" uses `ec2:Attribute/HttpTokens` to Deny `ModifyInstanceMetadataOptions`, while `list_ec2.md:8873` lists `ec2:MetadataHttpTokens` for that action — and a nearby section states "there are currently no fine-grained access controls (conditions) for the ModifyInstanceMetadataOptions API," contradicting its own worked example. A lead can legitimately ask *which key actually governs the Deny*, since AWS's docs disagree with themselves.

**High-level Test Scenarios:**
1. **Claim (Lens G, headline):** IMDSv1 is **allowed by default** (precedence table: no launch param + no account default + no AMI `ImdsSupport` → "V1 or V2"), hop-limit default is 1, and account-wide enforcement (`ModifyInstanceMetadataDefaults --http-tokens-enforced enabled`) is a **separate per-Region opt-in** — so any single launch path that omits `MetadataOptions` yields an SSRF-exploitable box vending role creds over open GET. → **Oracle:** doc default + SimulateCustomPolicy showing only `ec2:MetadataHttpTokens=required` (not RoleDelivery) can Deny the weak *launch*. → **Sev: High** (SSRF→credential-theft precondition).
2. **Claim (Lens X):** `ModifyInstanceMetadataOptions` **weakens IMDS live, no stop/start/reboot** — "restore IMDSv1" sets `HttpTokens=optional`, and hop-limit can be raised to 2–3 on a running instance (containers need 2, which weakens the SSRF boundary by design). The only blockers are account-level `HttpTokensEnforced=enabled` (returns `UnsupportedOperation`) or an IAM Deny — the latter being the self-contradicted control above. → **Oracle:** SimulateCustomPolicy a `Deny HttpTokens=optional` on both RunInstances and Modify; confirm a hardened launch is reversible post-launch if Modify is unscoped. → **Sev: Medium–High.**
3. **Claim (Lens G, adjacent — ASG/launch-template gap, AWS-documented):** `configuring-IMDS-new-instances.md` states IMDSv1 restrictions on `RunInstances` "are only checked when an Auto Scaling group that is using a launch template is created or updated… For an ASG configured to use the Latest or Default launch template, the permissions are not checked when a new version of the launch template is created." → an IMDS-hardening Deny on `RunInstances` is bypassable via the ASG/LT path. → **Oracle:** doc; cross-ref the Fleet/Spot-Fleet siblings where `MetadataHttpTokens` is absent entirely. → **Sev: Medium–High (enforcement-coverage gap).**
4. **Claim (Lens O):** IMDS credential *retrievals* appear to produce **no CloudTrail record** (data-plane, link-local — not an AWS API call); only the control-plane attach/modify/`ModifyInstanceMetadataDefaults` are logged. The config-change-is-audited / credential-theft-is-not asymmetry makes SSRF cred theft audit-silent. **Doc gap — the IMDS pages don't state this either way;** cite GuardDuty finding types (`UnauthorizedAccess:EC2/MetadataDNSRebind`, `InstanceCredentialExfiltration`) or the Security Blog, not the UserGuide, when resting a lead on it. → **Sev: Informational (enabler).**
5. **Claim (Lens M):** `ec2:InstanceMetadataTags=enabled` (off by default) exposes all instance tag key/values at IMDS `tags/instance/<key>` — any SSRF/on-box reader harvests tag content (teams encode owner/env/tenant/cost data, sometimes secrets) through the *same* primitive that leaks creds, widening blast radius with no extra privilege. Tag updates propagate live, no reboot. (Inference-from-mechanism, not an explicit AWS warning.) → **Sev: Medium if tags carry sensitive data.**

Doc evidence: list_ec2.md:8873/9599/10111/10129/10130/10131/10164; ExamplePolicies_EC2.md (RequireAllEc2RolesToUseV2 / Deny-opt-out-of-IMDSv2); configuring-instance-metadata-options.md (precedence/default); configuring-IMDS-new-instances.md (ASG/LT gap); configuring-IMDS-existing-instances.md (live weakening + `MetadataNoToken` metric). Severity-if-true: **High** (SSRF path).

### §5C — EC2 Instance Identity Roles (Lens A / B / C / EE / M / U / O) — NEW SURFACE
**Background.** Every instance has an auto-created **instance identity role**; its credentials live at IMDS `/identity-credentials/ec2/security-credentials/ec2-instance`, are **present regardless of whether any consuming feature is enabled**, and the role has **no trust policy and is not subject to any identity or resource policy**. The ARN `arn:aws:iam::<acct>:assumed-role/aws:ec2-instance/<instance-id>` is **fully predictable**. Six services choose to trust it.

**Security Concern.** Because nothing *scopes* the identity role by policy (fact #3), **each consuming service is the sole authorization boundary for its own integration** — and IAM tooling (`iam:SimulateCustomPolicy`, Access Analyzer, policy export) will *under-report* the role's effective power because the real trust logic lives server-side in SSM/GuardDuty/Lambda/Bedrock/EC2, not in an attachable policy. The ARN `arn:aws:iam::<acct>:assumed-role/aws:ec2-instance/<instance-id>` is fully derivable from account-id + instance-id. Six services opt to trust it; binding-to-the-right-instance is the whole game.

- **SSM DHMC (Lens B — the single most actionable lead).** DHMC uses the identity role to **register** the instance (`ssm:RegisterManagedInstance`) and then **passes the account-wide `AWSSystemsManagerDefaultEC2InstanceManagementRole`** to it (one role per account+Region, not per-instance). **`RegisterManagedInstance` is the ONLY SSM management action with no resource type and NO `ec2:SourceInstanceARN`/`ssm:SourceInstanceARN` condition key** (list_ssm:1672-1676; its only keys are `aws:RequestTag`, `aws:TagKeys`, `ssm:NodeAccountId`, `ssm:NodeOrgId`). Every *post*-registration action checked — `UpdateInstanceInformation` (1835), `UpdateInstanceAssociationStatus` (1941), `PutComplianceItems` (1640) — **does** carry `SourceInstanceARN`. The `ssm:SourceInstanceARN` glossary entry even states it is "not present when the request comes from the managed instance authenticated with an IAM role associated with EC2 instance profile." So registration bootstraps purely from the SigV4 signature of the identity credential, with no documented resource-level pin to a specific target instance.
- **EC2 Instance Connect (Lens A) — DOC GAP.** The "host-key update using the instance identity role" named on the parent page is **documented in exactly one sentence**; there is no dedicated page, no API, and **zero `HostKey`/`host-key` matches in list_ec2.md**. Scope (per-instance vs broader), direction, and anti-replay controls are all unknown from docs. (Note: `connect-linux-inst-eic.md` describes the older `SendSSHPublicKey` push, a *different* mechanism.) Mark "doc-gap — confirm surface first."
- **GuardDuty Runtime Monitoring / Lambda Managed Instances / Bedrock AgentCore (Lens C) — DOC GAPS.** Each is asserted once on the parent page ("send telemetry", "lifecycle hooks/telemetry/artifact distribution", "setting up during launch") and each service's own security page is **silent on the identity role**. No documentation on whether telemetry/lifecycle calls are pinned to the presenting instance. Mark "doc-gap."
- **STS GetCallerIdentity:** no permissions, no resource, no condition keys (list_sts:125) — a permission-free, deny-silent **verification oracle**: present instance X's identity creds, read back the ARN, confirm the exfil worked before probing elsewhere.

**High-level Test Scenarios:**
1. **Claim (Lens B, HEADLINE):** a process with IMDS read access to **only** instance X's identity creds (SSRF, high/absent hop-limit, on-box exec) can drive `ssm:RegisterManagedInstance` as X in a DHMC-enabled account and thereby obtain the account-wide `AWSSystemsManagerDefaultEC2InstanceManagementRole` scoped to X — with no per-instance pin at registration. → **Oracle (live-only, hand to vuln-hunter):** from identity-creds-only, attempt RegisterManagedInstance, then test whether UpdateInstanceInformation / Session Manager work under the DHMC role; **and** whether presenting X's creds while claiming a *different* already-registered managed-instance ID is rejected. SimulateCustomPolicy is a dead-end (no policy on the principal + server-side trust). → **Sev: High** (read-one-IMDS ⇒ SSM-management role for that instance; blast radius = whatever `AmazonSSMManagedEC2InstanceDefaultPolicy` grants — commonly Session Manager/RunCommand = command exec).
2. **Claim (Lens B, cross-account):** `ssm:NodeAccountId` / `ssm:NodeOrgId` on `RegisterManagedInstance` imply account/org identity is a **request attribute**, not something validated against the real instance — worth testing cross-account registration under Organizations-centralized SSM. → **Oracle:** live. → **Sev: High–Critical if cross-account.**
3. **Claim (Lens A/EE):** the predictable ARN + permission-free `GetCallerIdentity` gives a zero-cost existence/identity oracle; once SSRF reaches *some* instance's IMDS, "which identity did I get" is answered without burning any IAM permission or raising a deny signal. → **Sev: Low standalone, force-multiplier.**
4. **Claim (Lens U/O):** "no identity or resource policy" means an account admin **cannot centrally restrict or audit** what the identity role can do — compliance tooling cannot answer "what can this role do" the way it can for a normal role (it under-reports). → **Oracle:** doc; a confirmatory live SimulateCustomPolicy against the ARN likely returns implicit-deny-for-all and thus *under*-reports the real server-side-reachable actions (document as a negative result). → **Sev: Informational–Medium (assurance gap).**
5. **HARD STOP watch:** if any identity-role integration surfaces an AWS-fleet credential/ARN behind these flows, stop and flag for disclosure.

Doc evidence: iam-roles-for-amazon-ec2.md "Instance identity roles" (lines 57-85); list_ssm.md:1672-1676 / 1835 / 1941 / 1640 + `ssm:SourceInstanceARN` glossary; list_sts.md:125; fleet-manager-default-host-management-configuration.md (DHMC role is account+Region-wide; note the task-suggested `managed-instances-default-host-management.md` **404s**). Severity-if-true: **High–Critical** (DHMC confused deputy), Informational (assurance).

### §5D — Instance→role recon oracle & detach DoS (Lens A / L)
**Background/Concern.** `DescribeIamInstanceProfileAssociations` has a **blank resource type and only `ec2:Region`** (list_ec2:6870) → **unscopable account-wide**: any principal with the List grant enumerates every instance's attached instance-profile (role) ARN, selecting privesc targets for §5A even when it cannot read the instances otherwise. `DisassociateIamInstanceProfile` (7921, `instance*` + `ec2:InstanceProfile`) is a detach/availability primitive against a reachable app instance.
**Scenarios:** (1) **Claim:** the List action cannot be tag/ARN-scoped → account-wide role-map disclosure. **Oracle:** SimulateCustomPolicy shows no resource/tag condition binds it. **Sev: Medium.** (2) **Claim:** detach strips a running app's AWS access with only `ec2:DisassociateIamInstanceProfile`. **Sev: Medium (single-tenant availability; higher if it blocks a security agent's telemetry).**

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Attach high-priv role → IMDS cred harvest | Associate/Replace + PassRole | Split authz (`ec2:NewInstanceProfile` + `iam:AssociatedResourceArn`); test both halves present |
| Key-name confusion `InstanceProfile` vs `NewInstanceProfile` | RunInstances vs Associate/Replace | "Resource-level permissions" doc; prove inert Deny |
| `ec2:RoleDelivery` misread as unwired (it's a credential-context key, works with `Action:*`); IPv6 endpoint ungovernable (`ec2:MetadataHttpProtocolIpv6` doesn't exist) | IMDS cred delivery | ExamplePolicies_EC2 RequireAllEc2RolesToUseV2; prove IPv6 key absent |
| Post-launch IMDS weakening (live, no reboot) + ASG/launch-template RunInstances-Deny bypass | ModifyInstanceMetadataOptions / ASG | launch-vs-modify parity (4 keys symmetric); ASG LT enforcement gap |
| Instance identity cred reused cross-instance → DHMC management role | SSM DHMC `RegisterManagedInstance` (no SourceInstanceARN) | prove registration not pinned to presenting instance |
| Account-wide role-map disclosure | DescribeIamInstanceProfileAssociations | resource-level perms (prove absent) |

---

## 7. Out-of-Scope / Risk Categories to NOT chase
- IMDS exploitation *on a host the tester already fully controls* with no cross-boundary gain (single-tenant self-reach).
- The role's *downstream* permissions themselves (that's the customer's least-privilege authoring, unless the role is AWS-authored/managed → route to `security-iam-awsmanpol`).
- Shared SSM/GuardDuty/Lambda service infrastructure beyond the documented identity-role trust decision (shared-responsibility line).
- Customer-authored IAM policy footguns (in scope ONLY when the artifact is AWS-published/managed/copy-verbatim).
- EC2 AWS-managed-policy privesc headliners (EC2FastLaunchFullAccess, EC2InstanceConnect) → owned by `security-iam-awsmanpol` plan.
- Condition-key *evaluation-semantics* canon (ResourceID Deny-inert, `ec2:Attribute` case) → owned by `iam-policies-for-amazon-ec2` plan.
- **HARD STOP:** anything reaching AWS's own service-plane identity behind an instance-identity-role integration.

---

## 8. Null hypotheses / doc gaps (lenses checked, pages named)
- **Lens F (translation/injection):** N/A — read all three children + parent; no customer-input→query/parser transform on this surface (IMDS is a static read; attach takes ARNs/ids).
- **Lens H (KMS):** N/A on these pages — no encryption-context/CMK field; role-credential encryption is STS-internal.
- **Lens J (OAuth):** N/A — no 3P linking here.
- **Lens K (prompt injection):** N/A on this page; AgentCore Runtime Instances (identity-role consumer) is adjacent — flagged for its own plan, not here.
- **Lens Q (upload):** N/A — no blob upload on this surface.
- **Lens W (attestation):** N/A — no PCR/enclave gate on role attach.
- **Lens Y (transport):** IMDS is link-local HTTP by design (not an authenticated SigV4 endpoint); IMDSv2 token is the mitigation — covered under §5B, not a TLS gap.
- **RESOLVED during this analysis (no longer open):** (a) default `HttpTokens` = **IMDSv1 allowed** when nothing is set (precedence table); (b) `iam:PassRole` **IS enforced at Associate/Replace AND RunInstances** (`PassedToService=ec2` wired to all three) — there is no "Replace skips PassRole" bypass; (c) `ec2:RoleDelivery` is **real and correctly functioning** as a global credential-context key (`Action:"*"` Deny), NOT an inert/unwired key — the earlier "defined-but-unwired trap" framing is **refuted**; (d) no `iam-instance-profile-association` IAM resource type exists (authz anchors to the `instance` ARN).
- **Doc gaps still needing live confirmation first (mark "doc-gap — confirm surface first"):** (1) **SSM DHMC `RegisterManagedInstance` instance-pinning** — does the control plane bind the call to the SigV4-embedded instance ARN beyond "signature validates," and can one instance's identity creds register as / obtain the DHMC role for a *different* instance or cross-account via `ssm:NodeAccountId`/`NodeOrgId`? (highest research value); (2) **EC2 Instance Connect host-key-update** mechanism — one sentence, no API, no `HostKey` action in list_ec2.md; (3) **GuardDuty / Lambda Managed Instances / Bedrock AgentCore** identity-role instance-pinning — each asserted once, each service's own security page silent; (4) whether IMDS credential *retrievals* are CloudTrail-logged (UserGuide silent — rest on GuardDuty finding types, not these pages); (5) whether `iam:SimulateCustomPolicy` against the policy-less identity-role ARN returns anything (likely a dead-end oracle — document as negative result).

---
*Plan built with the `security-questionbuilder` skill, 2026-10-15. Authoritative condition keys from live `list_ec2.md`/`list_iam.md`/`list_sts.md`/`list_ssm.md`. Three parallel documentation deep-dives (attach/PassRole, IMDS, instance-identity) folded into §5A–§5C.*
