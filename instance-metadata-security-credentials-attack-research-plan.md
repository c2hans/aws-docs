# EC2 IMDS Credential Vending (`instance-metadata-security-credentials`) — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-metadata-security-credentials.html` (target) plus the IMDS sibling family in the same UserGuide — `ec2-instance-metadata.md`, `instancedata-data-retrieval.md`, `configuring-instance-metadata-options.md`, `configuring-instance-metadata-service.md`, `configuring-IMDS-new-instances.md`, `configuring-IMDS-existing-instances.md`, `instance-metadata-transition-to-version-2.md`, `instance-metadata-limiting-access.md`, `work-with-tags-in-IMDS.md`, `instance-identity-documents.md` — and the EC2 IAM reference `/work/aws-docs/docs/service-authorization/latest/reference/list_ec2.md`.
Status: **documentation-derived hypotheses only; nothing tested against a live account.**
Author pass date: 2026-10-15. Offline mirror cross-checked against online `.md` renders where possible.

---

## 0. How to use this document
- Each lead is written as: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost → Severity → Stop condition.** Work in priority order (Section 5 is ordered). Look left and right for adjacent bugs the lead did not anticipate.
- The safe first oracle for every IAM lead here is `iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy` (no resources touched). Escalate to a live scoped call only with canary data in an account you are authorized to test.
- **Scope reality for this page.** IMDS is an *in-instance* interface (link-local `169.254.169.254` / `[fd00:ec2::254]`). Nothing here is a cross-tenant or cross-account boundary **by itself** — the metadata service only ever answers for the instance it runs on, and the docs state plainly: *"Although you can only access instance metadata and user data from within the instance itself, the data is not protected by authentication or cryptographic methods"* (`ec2-instance-metadata.md`). The attack value is therefore in two places only: (1) **the IAM/governance layer that is supposed to let an org durably require IMDSv2 / a hop limit / tags-off and reject v1-delivered credentials** — does that layer actually enforce it, or fail open? and (2) **the SSRF-to-credential-theft path** that turns an app-level request-forgery bug on the instance into exfiltration of the instance role's temporary credentials. Both are governed by documentation this plan audits.
- **HARD STOP:** the moment any evidence shows an identity/credential/ARN/account belonging to **AWS's own service plane** (e.g. the Nitro hypervisor, the IMDS backend, a cross-account credential), stop, preserve evidence, and flag for AWS-Security disclosure. Do not probe the IMDS backend host itself.

---

## 1. Pentest Objectives (boundary-breach goals, concrete)
1. **Durably defeat an "IMDSv2 required" guarantee.** Starting from a principal that is *supposed* to be unable to weaken IMDS, re-enable IMDSv1 (`HttpTokens=optional`), raise the response hop limit above 1, re-enable the metadata endpoint, or enable instance tags in IMDS — on an instance or account where policy intended to forbid it. Breach oracle: `ModifyInstanceMetadataOptions` / `ModifyInstanceMetadataDefaults` succeeds and `describe-instances`/`get-instance-metadata-defaults` reflects the weakened value, under a principal the policy author believed was bounded.
2. **Make a stolen IMDSv1 credential useless — or prove you cannot.** Confirm whether `ec2:RoleDelivery` can be used (in the role's identity policy / a resource policy / an SCP) to deny any AWS action performed with credentials delivered over IMDSv1, and find the fail-open conditions (absent key) where that Deny silently does not fire.
3. **Exfiltrate instance-role credentials via an app-level SSRF.** From an application-layer request-forgery primitive on the instance, retrieve `iam/security-credentials/<role>` (AccessKeyId / SecretAccessKey / Token) and use it off-instance. Breach oracle: a valid STS credential JSON egresses to an attacker-chosen sink. Determine exactly which IMDSv2 defenses (PUT-to-token, custom header, hop-limit=1) the SSRF primitive can and cannot defeat.
4. **Reach IMDS from outside the instance's process set / from the VPC.** Confirm the documented network-reach expansion (a VPC appliance forwarding packets to `169.254.169.254` with source/dest check disabled) and the credential/tag disclosure it enables.
5. **Recon the account's IMDS posture with a low-privilege principal** via the unscopable `GetInstanceMetadataDefaults` / `DescribeInstances` MetadataOptions, as a precondition check that selects soft targets.

---

## 2. Components, Assets, and Design

**Customer-facing interface.** A link-local HTTP endpoint inside every instance: IPv4 `http://169.254.169.254/`, optional IPv6 `http://[fd00:ec2::254]/`. Two protocol modes:
- **IMDSv1** — unauthenticated request/response. `GET http://169.254.169.254/latest/meta-data/iam/security-credentials/<role>` returns the role's temporary credentials with no token.
- **IMDSv2** — session-oriented. Client first does `PUT /latest/api/token` with header `X-aws-ec2-metadata-token-ttl-seconds` (≤ 21600 = 6h), receives a token, then sends it in `X-aws-ec2-metadata-token` on each `GET`. The PUT method + required header are the SSRF defense (most SSRF primitives can only drive `GET`/cannot set arbitrary request headers).

**The asset this page is about.** `iam/security-credentials/<role-name>` → a JSON blob `{Code, LastUpdated, Type:"AWS-HMAC", AccessKeyId:"ASIA…", SecretAccessKey, Token, Expiration}`. These are the live STS credentials of the instance profile role. They rotate automatically; a new set is published ≥ 5 min before the old set expires. Anyone/anything that can read this item **is** the instance role until the credentials expire.

**Adjacent sensitive IMDS items** (reachable over the *same* path, so the same SSRF reads them):
- `iam/info` — InstanceProfileArn / InstanceProfileId / LastUpdated (role recon).
- `identity-credentials/ec2/security-credentials/ec2-instance` — the **instance identity role** credentials (no attached policies; only identify the instance to features like EC2 Instance Connect and SSM Default Host Management). Lower blast radius but still an AWS-signed identity.
- `tags/instance/<key>` — instance tag keys/values, **only if `InstanceMetadataTags=enabled`**. Tags frequently carry ABAC keys, environment names, owner emails, and sometimes secrets → info-disclosure + ABAC-key leakage.
- `instance-identity/document`, `/pkcs7`, `/signature` — the signed instance identity document (instance-id, account-id, region, private IP, …) usable to prove instance identity to third parties.
- `user-data` — launch-time user data; the docs explicitly warn **not** to store secrets here because "anyone … and potentially any software running on the instance, can view" it.

**Control-plane actions that shape IMDS** (EC2 API, SigV4 IAM — these are the governance surface):
- `RunInstances --metadata-options {HttpTokens, HttpPutResponseHopLimit, HttpEndpoint, InstanceMetadataTags}` — launch-time posture.
- `ModifyInstanceMetadataOptions` — change the posture on a running/stopped instance.
- `ModifyInstanceMetadataDefaults` / `GetInstanceMetadataDefaults` — **account-+Region-wide** IMDS defaults applied to future launches that don't override.
- `DescribeInstances` → `MetadataOptions` — read an instance's current posture.

**Processes / trust zones.**
- The IMDS backend is served by the **Nitro/host (AWS service plane)** — out of scope as a target; it is the shared-responsibility line.
- On-instance software (the customer's apps, SDKs, agents) is the *consumer*. The AWS SDK/CLI/Tools automatically fetch and use these credentials.
- The EC2 control plane (SigV4 API) is where posture is set and is the governance surface this plan mostly attacks.

```
          off-instance attacker                         AWS service plane (HARD STOP)
                 │                                        ┌───────────────────────────┐
   (SSRF payload)│                                        │  IMDS backend (Nitro/host) │
                 ▼                                        │  STS cred vending, signing │
   ┌───────────────────────────┐   link-local HTTP        └──────────────┬────────────┘
   │ vulnerable app on instance │ ───────────────────────▶ 169.254.169.254 │
   │ (proxy / validator / XML / │   GET or PUT+token      [fd00:ec2::254]  │
   │  SSRFable fetch)           │ ◀─────────────────────── iam/security-credentials/<role>
   └───────────────────────────┘    {AccessKeyId, Secret, Token}
                 │  exfil creds                          hop-limit (default 1) drops
                 ▼                                        packets >1 IP hop from the NIC
         attacker-controlled sink  ───▶  use creds off-instance = instance role compromised

   governance layer (SigV4 EC2 API):  RunInstances / ModifyInstanceMetadataOptions /
   ModifyInstanceMetadataDefaults  — set HttpTokens, HopLimit, Endpoint, Tags
   consumer-side gate:  ec2:RoleDelivery in role/resource/SCP policy — reject v1-delivered creds
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Vulnerable app on instance (attacker-driven) | Instance role STS credentials (`iam/security-credentials/<role>`) | SSRF → link-local HTTP GET (v1) or PUT-token+GET (v2) | A valid `ASIA…`/Secret/Token tuple egresses off-instance and authenticates an AWS call as the instance role |
| On-instance process that should be firewalled off | IMDS endpoint | OS-level reachability (no per-process authz in IMDS itself) | Any process (not just the allow-listed user) reads credentials; only OS firewall rules, not IMDS, can stop it |
| Host *outside* the instance, inside the VPC | Instance's IMDS | A VPC network appliance forwards packets to `169.254.169.254` with source/dest check disabled | A packet from another host reaches the instance's IMDS and returns metadata/credentials |
| Low-/mis-privileged IAM principal | IMDS posture of an instance it can `ModifyInstanceMetadataOptions` on | SigV4 EC2 API | IMDSv1 re-enabled / hop limit raised / tags enabled on an instance a policy intended to keep hardened |
| Principal with `ModifyInstanceMetadataDefaults` | **Account-+Region-wide** IMDS default | SigV4 EC2 API | Account default set to `HttpTokens=optional` (or high hop limit / endpoint on), silently weakening future launches, with **no value-based condition key able to deny it** |
| Credential holder using IMDSv1-delivered creds | Any AWS service the role can call | SigV4 request carries `ec2:RoleDelivery=1.0` | An action succeeds that an `ec2:RoleDelivery>=2` Deny was supposed to block (fail-open on absent key) |
| Any customer surface | **AWS IMDS backend / Nitro host** | — | **HARD STOP** — do not target the backend; any backend credential/identity is a service-plane breach to disclose |

---

## 4. API / Interface Inventory

| Name | Method | Mutating | Internet-callable | Authorized callers | Functionality | Notes |
|---|---|---|---|---|---|---|
| `GET /latest/meta-data/iam/security-credentials/<role>` | IMDS HTTP GET | No | No (link-local; reachable via SSRF or VPC-appliance forward) | Anything on the instance that can reach link-local | Returns instance-role STS creds | **Core asset.** v1 = plain GET; v2 = requires token |
| `PUT /latest/api/token` | IMDS HTTP PUT | No (issues token) | No | On-instance | Mint IMDSv2 session token (TTL ≤ 21600s) | The PUT+header is the SSRF defense |
| `GET /latest/meta-data/tags/instance[/<key>]` | IMDS HTTP GET | No | No | On-instance | Instance tags | Only if `InstanceMetadataTags=enabled` |
| `GET /latest/dynamic/instance-identity/{document,pkcs7,signature}` | IMDS HTTP GET | No | No | On-instance | Signed identity doc | Identity-proof material |
| `ec2:RunInstances` (`--metadata-options`) | SigV4 | Yes | Yes | IAM principals | Launch-time IMDS posture | **Value-scopable**: supports `ec2:MetadataHttpTokens`, `ec2:MetadataHttpPutResponseHopLimit`, `ec2:MetadataHttpEndpoint`, `ec2:InstanceMetadataTags` on the `instance*` resource row |
| `ec2:ModifyInstanceMetadataOptions` | SigV4 | Yes | Yes | IAM principals w/ action on `instance*` | Change posture post-launch | **Value-scopable** — same four keys + `aws:ResourceTag`/`ec2:ResourceTag` on `instance*`. (Summary table at list_ec2.md:3780 shows a blank cell; the authoritative resource-detail at list_ec2.md:8861 lists the keys — the blank is a formatting artifact, not an absence.) |
| `ec2:ModifyInstanceMetadataDefaults` | SigV4 | Yes | Yes | IAM principals | **Account+Region** IMDS default | **NOT value-scopable** — resource = none; condition keys = **only** `ec2:Attribute/${AttributeName}` + `ec2:Region` (list_ec2.md:8855). Cannot deny a weak VALUE, only gate which attribute name / region. |
| `ec2:GetInstanceMetadataDefaults` | SigV4 | No (List) | Yes | IAM principals | Read account IMDS default | **Unscopable** — resource = none; only `ec2:Region` (list_ec2.md:8324). Posture-recon oracle. |
| `ec2:DescribeInstances` (`MetadataOptions`) | SigV4 | No | Yes | IAM principals | Read per-instance posture | Account-wide, effectively unscopable read (consistent with the corpus's "Describe* = unscopable oracle" pattern) |
| **Condition key** `ec2:RoleDelivery` | — | — | — | Evaluated when the vended role creds call AWS | Numeric; "version of the IMDS used for retrieving IAM role credentials" (list_ec2.md:10147) | Consumer-side enforcement knob; **not** attached to any EC2 action row — it is populated in the *using* request's context |

Undocumented/knob notes: `HttpTokens` values are `required|optional`; `HttpEndpoint` `enabled|disabled`; `HttpProtocolIpv6` `enabled|disabled` — **note: no condition key `ec2:MetadataHttpProtocolIpv6` exists in list_ec2.md, so this toggle is value-ungovernable (Area 8a)**; `InstanceMetadataTags` `enabled|disabled`; `HttpPutResponseHopLimit` 1–64 (default 1). The condition-key names that gate `HttpTokens` **differ between AWS's two example policies** (`ec2:MetadataHttpTokens` for RunInstances vs `ec2:Attribute/HttpTokens`+`Null` for Modify) — Area 2. Confirm whether each key populates with the **request** casing and whether a **partial** `ModifyInstanceMetadataOptions` (one field only) leaves the other keys **absent** in the authz context (fail-open axis). Account-level `HttpTokensEnforced` is an IAM-independent backstop that rejects `--http-tokens optional` with `UnsupportedOperation` (Area 8c).

---

## 5. Recommended Areas of Focus
*(ordered: governance/IAM enforcement gaps first — they are the durable, AWS-owned, documentation-backed defects; SSRF path second; network-reach and recon last.)*

### Area 1 — Account-wide IMDS default is weakenable and the weak VALUE cannot be denied *(HEADLINE)*
**Background.** `ModifyInstanceMetadataDefaults` sets the account-+Region default IMDS posture applied to future launches that don't explicitly override. Its authorization reference entry (list_ec2.md:8855) shows **no resource type** and condition keys **only** `ec2:Attribute/${AttributeName}` and `ec2:Region`.
**Security Concern.** The four value keys that exist for per-instance posture (`ec2:MetadataHttpTokens`, `…HopLimit`, `…Endpoint`, `ec2:InstanceMetadataTags`) are **absent** on this action. So a Deny/SCP can forbid *touching* the defaults in a region, or (via `ec2:Attribute/${AttributeName}`) gate *which attribute name* is set — but it **cannot deny a weak value**. A principal with `ec2:ModifyInstanceMetadataDefaults` can set the account default to `HttpTokens=optional` (IMDSv1), raise the default hop limit, enable the endpoint, or enable instance tags — fleet-wide, silently, for all future non-overriding launches — and no value-based guardrail can stop it. This matches the corpus's recurring "binds attribute *name*, not *value* → fail-open" shape (`ec2:Attribute` on other actions).
**High-level Test Scenarios.**
- *Claim:* With only `ec2:ModifyInstanceMetadataDefaults` + `ec2:Region=us-east-1`, a principal can set the account IMDS default to `HttpTokens=optional`. → *Oracle:* `iam:SimulateCustomPolicy` for the action under an SCP/identity policy that attempts `StringEquals ec2:MetadataHttpTokens required` — the condition **never matches** (key not in context) so the Deny is inert; `GetInstanceMetadataDefaults` later reflects `optional`.
- *Claim:* No SCP written with the four value keys can constrain this action. → *Oracle:* simulate each key as a Deny condition; all evaluate as "key not present."
- *Adjacent:* does setting the default to v1-optional retroactively affect **existing** instances or only new launches? (Doc: defaults apply to future launches; confirm no silent retro-apply.)
**Doc evidence.** list_ec2.md:8855 (condition keys = `ec2:Attribute/${AttributeName}`,`ec2:Region` only); contrast list_ec2.md:8861 (Modify*Options* has the value keys). **Severity-if-true:** Medium–High (AWS-owned enforcement gap; account-wide silent weakening of the SSRF-defense posture). **Stop:** once Simulate shows the value key is not evaluated.

### Area 2 — `ModifyInstanceMetadataOptions` downgrade-prevention: AWS's own two example policies use *different* condition-key spellings (copy-paste fail-open) *(HEADLINE — highest-value live test)*
**Background.** Unlike the account defaults, the per-instance `ModifyInstanceMetadataOptions` **is** value-scopable (list_ec2.md:8861 — supports `ec2:MetadataHttpTokens`, `…HopLimit`, `…Endpoint`, `ec2:Attribute/${AttributeName}`, and tag-ABAC keys on `instance*`). So a correctly-written Deny *can* block re-enabling IMDSv1 on an instance. That REFUTES the naive "Modify always bypasses the RunInstances guardrail" claim — the launch-time↔modify-time parity (Lens X twin) **holds** at the capability level. The real defect is one layer down, in **which key name AWS tells you to use.**
**Security Concern.** `instance-metadata-transition-to-version-2.md` prose asserts the Metadata* keys *"control the use of the RunInstances **and** the ModifyInstanceMetadataOptions APIs."* But AWS's two canonical example policies in `ExamplePolicies_EC2.md` do **not** match that claim:
- "Require the use of IMDSv2" (RunInstances) uses `"ec2:MetadataHttpTokens": "required"` directly.
- "Deny opt-out of IMDSv2" (ModifyInstanceMetadataOptions) uses a **different** key — `"ec2:Attribute/HttpTokens"` wrapped in a `Null` presence check:
  ```json
  "Condition": {
    "StringNotEquals": {"ec2:Attribute/HttpTokens": "required"},
    "Null": {"ec2:Attribute/HttpTokens": false}
  }
  ```
Both keys are *listed* as valid for Modify in the authorization reference, yet AWS's own example for Modify never uses `ec2:MetadataHttpTokens`. **The fail-open trap:** an operator who (reasonably) copies the RunInstances-style `ec2:MetadataHttpTokens` key into a combined Deny covering `ModifyInstanceMetadataOptions` has a control that silently never fires **if that key does not actually populate in the Modify request context** — exactly the "which naming is checked vs which the operation uses" shape. This is **Lens X (twin/parity) + Lens U (guarantee-vs-enforcement)** and is the single most valuable thing to settle live.
**High-level Test Scenarios.**
- *Claim (decisive):* On a `ModifyInstanceMetadataOptions` call, `ec2:MetadataHttpTokens` is **not** populated in the request authz context (only `ec2:Attribute/HttpTokens` is), so a Deny keyed on `ec2:MetadataHttpTokens` is inert and the downgrade to `optional` succeeds. → *Oracle:* `iam:SimulatePrincipalPolicy` for `ec2:ModifyInstanceMetadataOptions` with each key supplied as a context entry independently; confirm which name the engine actually evaluates. (Doc cannot resolve this — the two pages disagree; a CloudTrail capture of the real request's condition context also settles it.)
- *Claim:* The `Null`-gated spelling is required precisely because omitting `HttpTokens` from a partial Modify (e.g. changing only `InstanceMetadataTags`) leaves the key absent — without the `Null` guard the `StringNotEquals …required` Deny would false-fire; with it, a bare omission correctly leaves the existing value unchanged (not a bypass). Confirm both spellings' absent-key behavior. → *Oracle:* Simulate with the key present/absent.
- *Claim:* Enum **casing** (`Required` vs `required`) — is the IAM string comparison the only gate, or does server-side enum validation reject non-canonical casing first? → *Oracle:* Simulate + EC2 API Reference (outside this corpus — flag as doc-gap). Suspected low severity (closed enum), unconfirmed.
- *Claim:* An org that denies Modify broadly but allows a tag-scoped subset still lets a holder flip `HttpTokens=optional` on any instance carrying a permitted tag they can also set. → *Oracle:* chain with `CreateTags` self-tagging (cross-ref the EC2 tagging/ABAC corpus).
**Doc evidence.** list_ec2.md:8861 (both keys valid for Modify); `instance-metadata-transition-to-version-2.md` (prose claims Metadata* keys cover Modify); `ExamplePolicies_EC2.md` ("Require IMDSv2" uses `ec2:MetadataHttpTokens`; "Deny opt-out" uses `ec2:Attribute/HttpTokens`+`Null`). **Severity-if-true:** Medium–High (an AWS-doc-induced non-functional control deployed by orgs that trust the prose). **Stop:** once Simulate shows which key name actually populates on Modify.

### Area 3 — `ec2:RoleDelivery` consumer-side gate: does it fail open on an absent key?
**Background.** `ec2:RoleDelivery` (list_ec2.md:10147, Numeric) "Filters access by the version of the instance metadata service for retrieving IAM role credentials for EC2." It is the documented way to make v1-delivered (SSRF-stealable) credentials useless: put `Deny if ec2:RoleDelivery < 2` in the instance role's identity policy, a resource policy, or an SCP. It is **not** attached to any EC2 action row — it is populated in the context of the request the *vended credentials* make to AWS.
**Security Concern.** Classic gate fail-open: a `NumericLessThan ec2:RoleDelivery 2` Deny evaluates **false when the key is absent**, so the Deny does **not** fire. The key may be absent for requests not made with IMDS-delivered credentials, for some services that don't forward it, or for credential paths other than `iam/security-credentials` (e.g. the instance-identity role, or AssumeRole-chained sessions). An org relying on `RoleDelivery` to block stolen v1 creds may have a Deny that silently never applies — the gate is the sole control and it fails open.
**High-level Test Scenarios.**
- *Claim:* `Deny NumericLessThan ec2:RoleDelivery 2` does not fire when `ec2:RoleDelivery` is absent from the request context. → *Oracle:* `iam:SimulateCustomPolicy` with the key unset vs set to `1.0`/`2.0`; confirm absent → Allow.
- *Claim:* The safe spelling requires `NumericLessThan` **plus** an explicit "key must be present" guard (or `BoolIfExists`/`Null` check), else fail-open. → *Oracle:* compare both spellings in Simulate.
- *Claim:* `RoleDelivery` is absent (so the Deny is inert) for the instance-identity-role credentials or for AssumeRole-chained sessions derived from the IMDS creds. → *Oracle:* documentation + Simulate; note which credential paths populate the key.
**Doc evidence.** list_ec2.md:10147; target page's note that role creds come from `iam/security-credentials/<role>`. **Severity-if-true:** Medium–High (defeats the primary mitigation that makes SSRF-stolen v1 creds worthless). **Stop:** once absent-key behavior is confirmed.

### Area 4 — SSRF → instance-role credential exfiltration, and which IMDSv2 defenses it defeats *(classic, highest real-world impact when the app bug exists)*
**Background.** The target page's **Warning** is explicit: *"If you use services that use instance metadata with IAM roles, ensure that you don't expose your credentials when the services make HTTP calls on your behalf. The types of services that could expose your credentials include HTTP proxies, HTML/CSS validator services, and XML processors that support XML inclusion."* This is AWS naming SSRF-to-IMDS as the headline risk for this exact item.
**Security Concern.** An application-layer request-forgery primitive on the instance that can reach `http://169.254.169.254/latest/meta-data/iam/security-credentials/<role>` reads live STS credentials. The defenses and their fail-open edges:
- **IMDSv1 enabled (`HttpTokens=optional`)** → a plain `GET` returns credentials. Any GET-only SSRF wins. This is the dominant real-world case and the reason Areas 1–3 (keeping v1 off) matter.
- **IMDSv2 (`HttpTokens=required`)** → attacker must do a `PUT /latest/api/token` with a custom header, then a `GET` with the token header. Most SSRF primitives cannot set the method/headers → defended. But the token is bound **only to the instance** — `configuring-instance-metadata-service.md`: *"The token is an instance-specific key. The token is not valid on other EC2 instances…"* — and **nothing in the docs binds it to a process, user, or application on the instance.** So an SSRF primitive that *can* issue a PUT with an arbitrary header (full-request SSRF, a webhook tester, a 307-redirect-preserving client that keeps verb+headers, HTTP request smuggling) can mint its own token and perform the authorized GET with **no additional barrier** — reducing IMDSv2 to no stronger than IMDSv1 for that attacker class. This is **Lens BB/CC (trusted-context) + Lens G**: IMDSv2's "defense" is really just "most SSRF can't set a method/header," not a caller-identity check.
- **`X-Forwarded-For` PUT rejection** → `configuring-instance-metadata-service.md`: *"PUT requests are rejected if they contain an X-Forwarded-For header."* This specifically kills the "HTTP proxy" class the target-page Warning names (a transparent/forwarding proxy auto-adds XFF, so its token PUT dies). **Fails open** for an SSRF that forges the PUT directly with no proxy hop and no XFF.
- **Hop limit (default 1)** → a request originating one IP hop away (e.g. a container with its own netns behind the host, or a reverse proxy that re-originates) is dropped. If the posture sets hop limit > 1 (common misconfig to make IMDS reachable from containers), a one-hop-removed SSRF succeeds. Areas 1–2 cover how the hop limit gets weakened.
- **Replayability asymmetry (token vs credential).** A stolen **token** is worthless off-instance — *"not valid on other EC2 instances and will be rejected if you attempt to use it outside of the instance on which it was generated"* — so token theft only matters to an attacker already executing on the box. A stolen **credential** (`AccessKeyId`/`SecretAccessKey`/`Token`) is fully **portable**: the target page itself shows off-instance use (*"you must provide the access key, secret key, and the session token"*), nothing device-binds it, and it stays valid until `Expiration` (new creds publish ≥5 min early, so windows overlap). **Net:** IMDSv2's token binding narrows only the *delivery* vector (same-instance, PUT+header-capable); it does **nothing** to shrink the *usability window* once the credential JSON egresses — that is governed solely by the role's session duration and is identical for v1 and v2. Hence Area 3 (`ec2:RoleDelivery`) is the only control that touches the *use* of a v1-delivered credential.
**High-level Test Scenarios.**
- *Claim:* On an instance with `HttpTokens=optional`, a GET-only SSRF returns `{AccessKeyId:"ASIA…", SecretAccessKey, Token}`. → *Oracle:* the credential JSON reflected into an attacker-readable response; the creds authenticate `sts:GetCallerIdentity` off-instance as the instance role.
- *Claim:* On `HttpTokens=required`, a header-controlling SSRF can still mint a token (`PUT`) and read creds. → *Oracle:* same, plus the token round-trip.
- *Claim:* With hop limit > 1, an SSRF from a container one hop from the ENI reaches IMDS. → *Oracle:* reach + credential read from the container context.
- *Adjacent (same path):* read `tags/instance` (if enabled — see Area 5) and `instance-identity/document` over the same SSRF.
**Doc evidence.** Target page Warning + IMDSv2/IMDSv1 curl blocks; `instancedata-data-retrieval.md` token mechanics; hop-limit default in `configuring-instance-metadata-options.md`. **Severity-if-true:** High (full instance-role compromise). **Scope note:** this is a bug in the **customer's app**, not AWS — in-scope only as the delivery vector; the *AWS-owned* defects are Areas 1–3 that let the posture be weak. **Stop:** the moment one valid credential tuple egresses — that is the PoC; do **not** use the creds to pivot or read real data.

### Area 5 — Instance tags in IMDS as a sensitive-data / ABAC-key disclosure over the same SSRF path
**Background.** `work-with-tags-in-IMDS.md`: once `InstanceMetadataTags=enabled`, `GET /latest/meta-data/tags/instance/<key>` returns tag keys and values with no auth. Enabled via `RunInstances --metadata-options InstanceMetadataTags=enabled`, `ModifyInstanceMetadataOptions --instance-metadata-tags enabled`, or a launch template.
**Security Concern.** Tags frequently carry ABAC decision keys (`ec2:ResourceTag/*`), owner emails, cost-center, environment, and sometimes secrets. Exposing them in IMDS turns an SSRF (Area 4) into disclosure of the very ABAC keys that gate the account's access control. Enablement is governed by `ec2:InstanceMetadataTags` (scopable on RunInstances/Modify) but **not** on `ModifyInstanceMetadataDefaults` (Area 1) — so the account default can enable tags-in-IMDS fleet-wide with no value-scoping.
**High-level Test Scenarios.**
- *Claim:* An SSRF on a tags-enabled instance leaks tag values used as ABAC keys. → *Oracle:* `tags/instance/<key>` returns a value that also appears in an `aws:ResourceTag`/`ec2:ResourceTag` policy condition.
- *Claim:* A principal who cannot `DescribeTags` on an instance can still read its tags via IMDS-over-SSRF. → *Oracle:* confirm the IMDS read needs no IAM.
- *Claim:* Account-default tag-enable (Area 1) silently turns this on for future launches. → *Oracle:* set default, launch, read tags.
**Doc evidence.** `work-with-tags-in-IMDS.md`; list_ec2.md `ec2:InstanceMetadataTags` on RunInstances/Modify but not on Defaults. **Severity-if-true:** Medium (info-disclosure; higher if ABAC keys leak). **Stop:** one tag value proven readable.

### Area 6 — IMDS reachable from the VPC network (not just on-instance)
**Background.** `instance-metadata-limiting-access.md`: *"For Nitro-based instances, the IMDS can be reached from your own network when a network appliance within your VPC, such as a virtual router, forwards packets to the IMDS address, and the default source/destination check on the instance is disabled."* AWS recommends dropping packets to `169.254.169.254` / `[fd00:ec2::254]` at the appliance.
**Security Concern.** This is a documented reachability expansion: with a forwarding appliance and source/dest check disabled, a host **other than the target instance** can reach that instance's IMDS and read its credentials/tags. It is still same-account (not cross-tenant), but it breaks the "only from within the instance itself" mental model and widens the SSRF-equivalent surface to any VPC host that can route to the appliance.
**High-level Test Scenarios.**
- *Claim:* With a VPC router forwarding to the IMDS address and source/dest check disabled on the target, a second instance reads the target's `iam/security-credentials/<role>`. → *Oracle:* credential JSON returned to the non-target host. **(Live-network test — authorized account only; stop at one credential proof.)**
- *Claim:* The IPv6 IMDS endpoint (`[fd00:ec2::254]`, enabled via `HttpProtocolIpv6=enabled`) is a second reachable path that the appliance filter must also cover. → *Oracle:* doc + config confirm.
**Doc evidence.** `instance-metadata-limiting-access.md` lines on Nitro VPC reachability + source/dest check. **Severity-if-true:** High (credential read from off the instance). **Stop:** one credential proof; do not pivot.

### Area 7 — Account IMDS-posture recon with a low-privilege principal
**Background.** `GetInstanceMetadataDefaults` (list_ec2.md:8324) has no resource type and only `ec2:Region`; `DescribeInstances` MetadataOptions is likewise an account-wide read.
**Security Concern.** A low-privilege principal can enumerate which instances/accounts run `HttpTokens=optional`, high hop limits, or tags-enabled — selecting soft targets for Area 4/6 without touching them. Consistent with the corpus's "Describe*/Get* = unscopable account-wide oracle" pattern.
**High-level Test Scenarios.**
- *Claim:* `GetInstanceMetadataDefaults` returns the account default posture under a principal with only that List permission, unconstrained by tag/resource. → *Oracle:* Simulate + call returns `optional`/`required`.
- *Claim:* `DescribeInstances` reveals per-instance `MetadataOptions` with no ownership/tag scoping available. → *Oracle:* Simulate.
**Doc evidence.** list_ec2.md:8324. **Severity-if-true:** Low (recon/enabler). **Stop:** once unscopability confirmed.

### Area 8 — Governance blind spots AWS's own docs admit or create (Lens U / Lens S coverage-holes)
Three distinct AWS-owned gaps, grouped because each is a place the authoritative docs either contradict themselves or confess a missing control. All three resolve by documentation + `iam:Simulate*`; none requires live mutation.
- **8a — The IPv6 IMDS endpoint toggle has NO value condition key at all.** `HttpProtocolIpv6=enabled` exposes a second IMDS address (`[fd00:ec2::254]`), set via `RunInstances`/`ModifyInstanceMetadataOptions` (`configuring-IMDS-new-instances.md`, `…-existing-instances.md`). But **`ec2:MetadataHttpProtocolIpv6` does not exist anywhere in list_ec2.md** — not on any action row, not in the condition-key appendix. Consequence: an org **cannot** write an SCP/IAM Deny that enforces "the IPv6 IMDS endpoint must stay disabled" by value — only a coarse all-or-nothing Allow/Deny on the whole action, with zero parameter visibility. This also widens the Area 6 appliance-filter burden (the filter must separately cover the IPv6 address, which no IAM policy can keep from being enabled). *Oracle:* grep the authoritative reference (confirmed absent); `iam:SimulateCustomPolicy` attempting a value Deny shows the key is never evaluated. **Severity:** Medium (an entire IMDS attribute is value-ungovernable — the cleanest net-new Lens S gap on this page).
- **8b — Doc self-contradiction: "no fine-grained access controls" for `ModifyInstanceMetadataOptions`, printed next to a value-based example that uses one.** `ExamplePolicies_EC2.md`'s "Limit who can modify the instance metadata options" section states *"there are currently no fine-grained access controls (conditions) for the ModifyInstanceMetadataOptions API"* and — unlike every sibling section — **ships no JSON policy block at all** (confirmed identical on the live `.html`, not a mirror artifact), yet the same page's "Deny opt-out" example *does* apply a value condition to that exact action, and the authorization reference lists `aws:ResourceTag/${TagKey}` ABAC for it. Read charitably the sentence means *principal*-scoping specifically — but the doc never draws that distinction, so a security team following this page literally believes they cannot restrict **who** can flip a hardened instance back to IMDSv1 beyond a blunt Allow/Deny, and gets no worked example for the one control they most need. **Lens U** (asserted guarantee ≠ actual enforcement surface). *Oracle:* documentation (contradiction is on-page); `iam:Simulate*` demonstrating tag-ABAC *does* in fact scope the action, refuting the "no fine-grained controls" sentence. **Severity:** Medium (AWS doc defect that leaves a real downgrade-authorization control unbuilt in practice).
- **8c — `HttpTokensEnforced` account backstop is the only mechanism that blocks the downgrade regardless of IAM-policy correctness.** `troubleshoot-modifying-an-imdsv1-enabled-instance-fails` shows that with the account-level `HttpTokensEnforced=enabled`, a `ModifyInstanceMetadataOptions … --http-tokens optional` throws `UnsupportedOperation` **independent of IAM**. This is the fail-safe that neutralizes both Area 1 (value-unscopable defaults) and Area 2 (wrong-key-name fail-open): if it is **off**, every downgrade-prevention story collapses back onto getting the IAM condition keys exactly right. *Oracle:* `GetInstanceMetadataDefaults` / account settings reflect `HttpTokensEnforced`; confirm a downgrade attempt is rejected with it on and permitted with it off. **Severity:** this is a *control to check is present* — its **absence** inherits the full Area 1–2 severity (Medium–High); documenting it is what makes Areas 1–2 actionable rather than theoretical. **Stop:** once presence/effect confirmed via Simulate/account read.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Re-enable IMDSv1 account-wide, value-unscopable | `ModifyInstanceMetadataDefaults` | "Set account defaults" governed only by `ec2:Attribute/${AttributeName}`+`ec2:Region` (no value key) |
| Re-enable IMDSv1 per-instance via a Deny that uses the wrong key name | `ModifyInstanceMetadataOptions` | AWS examples split `ec2:MetadataHttpTokens` (RunInstances) vs `ec2:Attribute/HttpTokens`+`Null` (Modify) — copy-paste → inert Deny |
| Enable IPv6 IMDS endpoint despite policy intent | `HttpProtocolIpv6` | **no value condition key exists** (`ec2:MetadataHttpProtocolIpv6` absent from list_ec2.md) |
| "Limit who can modify" with no worked policy / "no fine-grained controls" claim | `ModifyInstanceMetadataOptions` | on-page contradiction; tag-ABAC actually works but doc says it can't |
| Downgrade blocked only when account backstop is on | `HttpTokensEnforced` | account setting rejects `--http-tokens optional` with `UnsupportedOperation`, IAM-independent |
| Stolen v1 creds still accepted | `ec2:RoleDelivery` gate | "Filter by IMDS version used to retrieve role creds" — Numeric, absent-key fail-open; opt-in SCP |
| SSRF reads `iam/security-credentials/<role>` | IMDS v1/v2 endpoint | v1=plain GET; v2 PUT+token+hop-limit=1 + XFF-PUT rejection; token instance-scoped but NOT process-bound |
| SSRF reads tags / identity doc over same path | `tags/instance`, `instance-identity/*` | `InstanceMetadataTags` default-off; no mitigation for identity doc |
| Off-instance VPC host reads IMDS | Nitro IMDS + VPC appliance | source/dest check + appliance drop rule for `169.254.169.254`/`[fd00:ec2::254]` |
| Low-priv posture recon | `GetInstanceMetadataDefaults`/`DescribeInstances` | none (unscopable reads) |

---

## 7. Out-of-Scope Risk Categories (stated as confidently as in-scope)
- **The IMDS backend / Nitro host itself** — AWS service plane, shared-responsibility line. Do not target; any backend credential/identity = HARD STOP + disclose.
- **IMDS on fully-managed hosts** (Lambda, Fargate, managed services) — out of scope per the corpus convention.
- **A customer app's own SSRF bug** — the vulnerability is the customer's; in-scope here only as the *delivery vector* for Area 4. The AWS-owned, reportable defects are the governance gaps (Areas 1–3).
- **A user attacking the IMDS of their own instance from a process they already control** — self-inflicted; IMDS explicitly offers no in-instance authentication ("not protected by authentication or cryptographic methods"). Only becomes a finding when a *trust boundary on the instance* is crossed (an unprivileged process / a different OS user / a container reads creds it shouldn't — then OS firewall rules, Area 6 hop limit, are the controls).
- **Single-tenant self-DoS** against one's own IMDS.
- **Customer-authored IAM policies** that are over-broad — least-privilege footgun, out of scope. (The in-scope IAM items here are the *absence of a value condition key* on an AWS action — Area 1 — and the *fail-open semantics* of AWS-provided keys — Areas 2–3 — which are AWS-owned.)

---

## 8. Null Hypotheses / Doc Gaps (lenses checked, did not fire — with pages read)
- **Lens A/IDOR (cross-tenant):** NULL. IMDS answers only for its own instance; `<role-name>` in the path is not a cross-tenant identifier. Pages read: target, `ec2-instance-metadata.md`, `instancedata-data-retrieval.md`. No resource-by-foreign-id surface.
- **Lens B/PassRole:** NULL for IMDS itself. The target page's "role assumes itself" note (an app calling `sts:AssumeRole` on its own instance role needs an explicit self-assume trust policy, else `AccessDenied`) is an availability/ergonomics note, not a confused-deputy — no cross-principal escalation. Pages read: target page. Flag only if a service is observed assuming the instance role cross-account.
- **Lens F/injection, Lens K/prompt-injection:** NULL — IMDS has no translation layer / LLM. Pages read: whole family.
- **Lens H/KMS, Lens W/attestation:** NULL on this page — no CMK/encryption-context/PCR surface in the credential-vending path. (NitroTPM attestation lives in the separate EC2 security corpus.)
- **Lens Y/transport:** Partial doc-gap. IMDS is link-local plaintext HTTP by design (not an authenticated network endpoint), so TLS does not apply; `instance-identity/pkcs7` signature trust is covered in `instance-identity-documents.md` (defer to Area in that page's own analysis). No `aws:SecureTransport` angle on 169.254.169.254.
- **Lens AA/share-revoke:** NULL — no cross-account share of IMDS.
- **Lens BB/CC (trusted-context / caller-identity):** FIRES but as a *refutation of a stronger claim* — IMDSv2 is **not** a per-process/per-user authorization boundary; the token is only instance-scoped (`configuring-instance-metadata-service.md`). A hypothesis framed "IMDSv2 isolates callers on the same instance" is unsupported by docs — any method+header-capable SSRF mints its own token (Area 4). Pages read: all five IMDS pages. Not a cross-tenant boundary (`ec2-instance-metadata.md` Important box: metadata "not protected by authentication").
- **Doc gap (Area 3):** the exact set of request contexts in which `ec2:RoleDelivery` is **populated vs absent** is not spelled out in the UserGuide — Area 3's fail-open hinges on this; confirm the key-presence surface via Simulate before relying on refute.
- **Doc gap (Area 2):** whether `ec2:MetadataHttpTokens` actually populates in the `ModifyInstanceMetadataOptions` request context (vs only `ec2:Attribute/HttpTokens`) is **undecidable from docs** — the transition page's prose and the ExamplePolicies page disagree. This is the plan's single most valuable unresolved question; settle it first with `iam:SimulatePrincipalPolicy` or a CloudTrail condition-context capture.
- **Doc gap (Area 2 casing):** server-side enum validation vs IAM string-compare ordering for `required`/`optional` casing lives in the EC2 API Reference (outside this corpus) — mark "confirm surface first."
- **Lens U meta-observation:** the "IMDSv2 defeats SSRF / open firewalls / reverse proxies" framing exists only in an **externally-linked blog headline** (`configuring-instance-metadata-service.md`), never asserted in the UserGuide body, which is scrupulously mechanism-only (PUT+token, hop-limit, XFF-rejection). A reader who trusts the headline over-estimates coverage; the authoritative text describes three narrow, individually-bypassable guards.

---

## 9. Suggested kill-chain (chain the primitives)
Area 1 (set account default `HttpTokens=optional` + `InstanceMetadataTags=enabled`, value-unscopable) **→** new launches ship IMDSv1 + tags-in-IMDS **→** Area 4 (a GET-only SSRF in any app on those instances) **→** read `iam/security-credentials/<role>` **and** `tags/instance/*` **→** Area 3 (the org's `ec2:RoleDelivery>=2` Deny fails open on absent key, so the v1 creds are accepted) **→** instance-role compromise with ABAC-key disclosure. Rate at the **end** of the chain: **High** (durable, AWS-governance-enabled instance-role takeover), with the entry primitive (the app SSRF) being the only customer-owned link.
