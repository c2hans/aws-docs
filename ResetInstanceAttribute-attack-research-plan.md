# Amazon EC2 `ResetInstanceAttribute` (instance-attribute family: Describe / Modify / Reset) — Attack Research Plan

**Source of leads:** docs.aws.amazon.com, verified against the offline mirror `/work/aws-docs/docs` (online == offline confirmed 2026-10-20 for the API ref and devguide target):
- Target devguide page: `ec2/latest/devguide/example_ec2_ResetInstanceAttribute_section.html` (`.md` mirror identical)
- `AWSEC2/latest/APIReference/`: `API_ResetInstanceAttribute.md` (target), `API_ModifyInstanceAttribute.md` (write twin), `API_DescribeInstanceAttribute.md` (read twin), `API_AttributeBooleanValue.md`, `API_AttributeValue.md`
- `AWSEC2/latest/UserGuide/`: `iam-policies-for-amazon-ec2.md` (`#attribute-key` section — `ec2:Attribute`), `Using_ChangingDisableAPITermination.md`, `Using_ChangingInstanceInitiatedShutdownBehavior.md`, `UserProvidedKernels.md` (PV-GRUB), `instancedata-add-user-data.md`, `iam-roles-for-amazon-ec2`
- `service-authorization/latest/reference/list_ec2.md` (IAM actions, per-action condition keys, `instance` resource ARN)
- `config/latest/developerguide/ec2-enis-source-destination-check-enabled.md` (NAT/source-dest Config rule)
- `AmazonVPC/latest/UserGuide/VPC_NAT_Instance.html` (NAT instance requires `sourceDestCheck=false`)

**Status:** documentation-derived hypotheses only. **Nothing has been tested against a live AWS account.** Every lead is a boundary the docs imply *should* hold, written so a hunter with two cooperating, self-owned test accounts can confirm or refute it with synthetic/canary resources.

---

## 0. How to use this document

- Each lead reads: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost → Severity-if-true → Stop condition.** Work in priority order (Section 5 is ordered). Look left and right for adjacent bugs the plan did not anticipate.
- **`DryRun` is NOT an ownership or attribute oracle.** On `ResetInstanceAttribute` / `ModifyInstanceAttribute` / `DescribeInstanceAttribute`, `DryRun=true` returns `DryRunOperation` vs `UnauthorizedOperation` based on **caller IAM only**, evaluated *before* resource ownership/attribute resolution. A `DryRunOperation` against a foreign instance ID never proves you can touch it. Confirm ownership questions with a **real (canary) call**, not DryRun.
- **Instance IDs are account-scoped.** The `instance` ARN is `arn:${Partition}:ec2:${Region}:${Account}:instance/${InstanceId}` — the resolver binds `i-…` within the caller's account+region. A fabricated foreign `i-…` normally resolves to `InvalidInstanceID.NotFound`, so pure-guess cross-account IDOR is expected to be a genuine null (confirm, don't assume). Intra-account enumeration (sequential/low-entropy legacy 8-hex IDs, or IDs observed via `DescribeInstances`) is the realistic reach.
- **HARD STOP:** the moment any evidence shows an identity, credential, ARN, or account belonging to **AWS's own service plane** (not the customer's own instances/roles), stop, preserve evidence, and flag for AWS-Security disclosure. Resetting attributes on *your own* authorized test instances, and reading *your own* instance's IMDS/userData, is in scope; anything reaching another account or AWS's fleet is not.
- Use **synthetic/canary instances** only. Never reset or modify attributes on an instance you do not own in a test account, and never on production or third-party instances (a reset of `sourceDestCheck` or `kernel` can cause an outage — see Area 2).

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)

Each maps to a firing lens in Section 5:

1. **Attribute-scoping escape (crown jewel).** An admin who scopes `ec2:ModifyInstanceAttribute` with the `ec2:Attribute` / `ec2:Attribute/${AttributeName}` condition key (e.g. "you may modify tags but **not** `userData`/`groupSet`/`disableApiTermination`") believes the instance's sensitive attributes are protected. Prove the scoping does **not** carry to the sibling actions: `ec2:ResetInstanceAttribute` and `ec2:DescribeInstanceAttribute` do **not** expose `ec2:Attribute`, so an `ec2:Attribute`-keyed statement is **inert** for them (Lens X / S / U).
2. **Case-sensitivity fail-open on `ec2:Attribute`.** Even where `ec2:Attribute` *is* honored (Modify), prove a `Deny StringEquals ec2:Attribute "UserData"` (wrong case / wrong spelling) is inert against the real request value `userData` → the intended block fails open (Lens S variant).
3. **Availability via `sourceDestCheck` reset.** As a principal with only `ec2:ResetInstanceAttribute`, reset `sourceDestCheck` to its default `true` on a NAT / router / firewall / VPN appliance instance (allowed while *running* — no stop needed) and break packet forwarding for every subnet routed through it (Lens L / U — integrity/availability).
4. **Boot-integrity via `kernel`/`ramdisk` reset.** Reset `kernel`/`ramdisk` to AMI default on a PV instance → render it unbootable / change boot behavior on next start (Lens L).
5. **Write-twin privilege-escalation chain.** Via the Reset→Modify family, reach `ec2:ModifyInstanceAttribute(userData)` — the confirmed **non-PassRole** privesc exemplar: edit user data → code execution as the instance-profile role via IMDS on next boot; and `groupSet`/`GroupId.N` replacement → open ingress; `disableApiTermination` reset → strip termination protection; `blockDeviceMapping DeleteOnTermination` → data-destruction-on-terminate (Lens B / X).
6. **Sensitive-attribute disclosure via the read twin.** `ec2:DescribeInstanceAttribute` reads `userData` (bootstrap secrets/credentials) and `groupSet` (SG topology) and is **not** `ec2:Attribute`-constrainable → information disclosure a per-attribute Deny cannot stop (Lens A disclosure / U).
7. **Intra-account ABAC bypass.** Defeat a `aws:ResourceTag`-keyed Allow/Deny guarding these actions by self-tagging a same-account victim instance into scope, or via tag case-sensitivity (Lens S / A intra-account).
8. **Doc-vs-reference discrepancy.** The API reference restricts Reset `Attribute` to `kernel | ramdisk | sourceDestCheck`, but the devguide PowerShell examples "reset" `sriovNetSupport`, `ebsOptimized`, `disableApiTermination`, `instanceInitiatedShutdownBehavior`. Determine whether the API silently accepts an undocumented wider set or the SDK translates (Lens U / undocumented-knob).

---

## 2. Components, Assets, and Design

### What the target actually is
`ResetInstanceAttribute(InstanceId, Attribute[, DryRun])` resets **one** instance attribute to its **default value**. Per the API reference the **only valid `Attribute` values are `kernel | ramdisk | sourceDestCheck`** (Required: Yes). State preconditions:
- `kernel`, `ramdisk` → instance must be **stopped**.
- `sourceDestCheck` → instance may be **running or stopped**.

On success: no payload change signalled beyond `<return>true</return>`. There is **no `Value` parameter** — unlike Modify, Reset takes no new value; it always restores the documented default (`sourceDestCheck` default = `true`; `kernel`/`ramdisk` default = the AMI's).

It is the "restore to default" member of a **three-API family** that manages instance attributes:

| API | Role | Attributes it covers | `ec2:Attribute` key exposed? |
|---|---|---|---|
| `DescribeInstanceAttribute` (Access level **List**) | **Read** one attribute | `instanceType, kernel, ramdisk, userData, disableApiTermination, instanceInitiatedShutdownBehavior, rootDeviceName, blockDeviceMapping, productCodes, sourceDestCheck, groupSet, ebsOptimized, sriovNetSupport, enaSupport, enclaveOptions, disableApiStop` | **NO** |
| `ModifyInstanceAttribute` (Access level **Write**) | **Set** one attribute to a chosen value | `disableApiTermination, instanceType, kernel, ramdisk, instanceInitiatedShutdownBehavior, blockDeviceMapping, userData, sourceDestCheck, groupSet, ebsOptimized, sriovNetSupport, enaSupport, nvmeSupport, disableApiStop, enclaveOptions` | **YES** (`ec2:Attribute` + `ec2:Attribute/${AttributeName}`) |
| `ResetInstanceAttribute` (Access level **Write**) | **Reset** one attribute to default | `kernel, ramdisk, sourceDestCheck` only (per API ref) | **NO** |

### Assets
- **Instance runtime configuration** — the security-relevant attributes above. The high-value ones: `userData` (contains bootstrap scripts, sometimes secrets; executed with the instance-profile role), `groupSet` (the instance's security groups — its network exposure), `disableApiTermination` (termination protection), `sourceDestCheck` (NAT/routing enablement), `kernel`/`ramdisk` (boot image).
- **The instance-profile role credentials** reachable via IMDS once attacker-controlled `userData` runs (cross-service blast radius).
- **The instance's packet-forwarding function** when it is a NAT/router/firewall — a VPC-wide availability asset governed by `sourceDestCheck`.

### Identity / authorization model
- Identity: SigV4 IAM principals. Authorization: IAM `Write` action `ec2:ResetInstanceAttribute` on resource `instance*` (required). Ownership is **account-scoped** via ARN `…:${Account}:instance/${InstanceId}`.
- **Per-action condition keys for `ResetInstanceAttribute` (`list_ec2.md`):** `aws:ResourceTag/${TagKey}`, `ec2:AvailabilityZone`, `ec2:AvailabilityZoneId`, `ec2:CpuOptionsAmdSevSnp`, `ec2:EbsOptimized`, `ec2:InstanceAutoRecovery`, `ec2:InstanceBandwidthWeighting`, `ec2:InstanceID`, `ec2:InstanceMarketType`, `ec2:InstanceMetadataTags`, `ec2:InstanceProfile`, `ec2:InstanceType`, `ec2:ManagedResourceOperator`, `ec2:MetadataHttp*`, `ec2:ProductCode`, `ec2:Region`, `ec2:ResourceTag/${TagKey}`, `ec2:RootDeviceType`, `ec2:Tenancy`. **Notably absent: `ec2:Attribute` and `ec2:Attribute/${AttributeName}`.**
- The **`instance` resource type** *does* list `ec2:Attribute`/`ec2:Attribute/${AttributeName}` as supported keys, but a condition key is only populated into the request context for an **action that exposes it**. `ModifyInstanceAttribute` exposes it; `ResetInstanceAttribute` and `DescribeInstanceAttribute` do not → an `ec2:Attribute` condition attached to Reset/Describe is never satisfied (for a **Deny** that means it never fires → fail-open; for an **Allow** it means the condition can never be met → the grant is dead, usually not the attacker's concern).

### ASCII — the attribute-scoping asymmetry (the central seam)
```
                      ec2:Attribute / ec2:Attribute/${AttributeName}
                      ┌───────────────┬────────────────┬───────────────┐
 Admin's intent:      │  Describe     │    Modify      │    Reset      │
 "limit which         │  (read)       │   (write any)  │  (write dflt) │
  attribute a         ├───────────────┼────────────────┼───────────────┤
  principal touches"  │  key ABSENT   │  key PRESENT   │  key ABSENT   │
                      │   → Deny      │  → Deny can    │   → Deny      │
                      │   inert       │   match (but   │   inert       │
                      │  (reads       │   case-        │  (resets      │
                      │   userData,   │   sensitive —  │   kernel/     │
                      │   groupSet    │   Area 1b)     │   ramdisk/    │
                      │   anyway)     │                │   sourceDest  │
                      └───────────────┴────────────────┴───────────────┘
 Result: a per-attribute control written for Modify does NOT constrain its
         read twin (Describe) or its default-restore twin (Reset).
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Low-priv IAM principal (same account) scoped by `ec2:Attribute` on Modify | A sensitive attribute of a same-account instance | Call `ResetInstanceAttribute` / `DescribeInstanceAttribute` (no `ec2:Attribute` evaluation) | The reset/read **succeeds** on an attribute the admin's `ec2:Attribute` Deny was meant to block → scoping escaped. |
| IAM principal with `ec2:ResetInstanceAttribute` | A running NAT/router instance's forwarding function | Reset `sourceDestCheck`→`true` (no stop required) | Packet forwarding stops for every subnet whose route table targets that ENI → **availability breach of a shared network path**. |
| Low-priv principal (same account) | Instance-profile role credentials | Reach `ModifyInstanceAttribute(userData)` → run-as-role on boot → IMDS | Reading, under a principal never granted that role, credentials the role holds → **cross-IAM-boundary credential exposure**. |
| Caller with `aws:ResourceTag`-gated grant | A same-account instance not "theirs" | Self-tag the victim instance into scope, or exploit tag case-sensitivity | A reset/modify/describe **ALLOW** against an instance the operator intended to exclude → **intra-account ABAC bypass**. |
| Any caller | A foreign-account instance via raw `i-…` | Supply foreign `InstanceId` | Expected `InvalidInstanceID.NotFound` (account-scoped resolver). A **success** would be a cross-account IDOR = Critical (expected null — confirm). |
| Any customer surface | **AWS's own service plane** | — | Any identity/credential/ARN/account belonging to AWS's fleet = **HARD STOP + disclosure**. |

---

## 4. API / Interface Inventory

| Name | Method | Mutating | Internet-callable | Authorized callers | Functionality | Notes |
|---|---|---|---|---|---|---|
| `ResetInstanceAttribute` | SigV4 query/SDK | **Yes** (Write) | Yes (regional `ec2.*` endpoint) | IAM principals with `ec2:ResetInstanceAttribute` on the instance | Reset `kernel`/`ramdisk`/`sourceDestCheck` to default | **No `ec2:Attribute` key**; no `Value` param; `sourceDestCheck` resettable while running |
| `ModifyInstanceAttribute` | SigV4 query/SDK | **Yes** (Write) | Yes | `ec2:ModifyInstanceAttribute` | Set any of ~15 attributes, incl. `userData`, `groupSet`, `disableApiTermination` | **Has `ec2:Attribute` + `ec2:Attribute/${AttributeName}`**; the write twin & privesc vector |
| `DescribeInstanceAttribute` | SigV4 query/SDK | No (List) | Yes | `ec2:DescribeInstanceAttribute` | Read one attribute (incl. `userData`, `groupSet`) | **No `ec2:Attribute` key**; the disclosure twin |
| (reference) `ResetNetworkInterfaceAttribute`, `ResetImageAttribute`, `ResetSnapshotAttribute`, `ResetFpgaImageAttribute` | SigV4 | Yes | Yes | varies | Sibling "Reset…Attribute" actions on other resources | Family-parity cross-check (Lens X); each has its own condition-key set |

Doc-planted lead to keep: **the devguide examples reset attributes (`disableApiTermination`, `ebsOptimized`, `sriovNetSupport`, `instanceInitiatedShutdownBehavior`) that the API reference's `Valid Values` list excludes.** Either the SDK/PowerShell cmdlet maps these to `ModifyInstanceAttribute` under the hood, or the wire API silently accepts more than it documents. Flag as Area 5.

---

## 5. Recommended Areas of Focus (one block per firing lens, priority-ordered)

### Area 1 — Attribute-scoping asymmetry across the Describe/Modify/Reset family (Lens X / S / U) — **HIGHEST**

**Background.** AWS ships a per-attribute IAM condition key, `ec2:Attribute` ("Filters access by an attribute of a resource") and `ec2:Attribute/${AttributeName}` ("…an attribute being set on a resource"). `iam-policies-for-amazon-ec2.md#attribute-key` demonstrates it on `ModifyImageAttribute` (`"Deny" … "ec2:Attribute":"Description"`). On instances, **only `ec2:ModifyInstanceAttribute` exposes these keys** — the per-action condition-key lists in `list_ec2.md` show them present on Modify (line ~8808) and absent on Reset (line ~9513) and Describe (line ~6924).

**Security Concern.** An operator who wants a principal to touch only innocuous attributes writes a Deny/Allow keyed on `ec2:Attribute` for `ModifyInstanceAttribute`. That control **does not transfer** to the two sibling actions on the same resource: `ResetInstanceAttribute` (can still reset `sourceDestCheck`, `kernel`, `ramdisk`) and `DescribeInstanceAttribute` (can still read `userData`, `groupSet`). The key is simply not in the request context for those actions, so a `StringEquals ec2:Attribute …` **Deny never matches and fails open**.

**High-level Test Scenarios (falsifiable claims):**
- **Claim 1a (Reset not attribute-scopable).** → **Mechanism:** `list_ec2.md` Reset action row omits `ec2:Attribute`. → **Oracle:** author a scoped test role: `Allow ec2:ResetInstanceAttribute` on `instance/*` **plus** `Deny ec2:ModifyInstanceAttribute` when `ec2:Attribute` ∈ {`userData`,`groupSet`,`sourceDestCheck`}. Use `iam:SimulateCustomPolicy`/`SimulatePrincipalPolicy` first (no resources touched); then a real canary call resetting `sourceDestCheck` on a self-owned instance → **expected: ALLOWED**, proving Reset ignores the attribute Deny. → **Severity:** Medium–High (the control the admin believes bounds attribute access is porous; escalates to High when chained to Area 2 availability or Area 3 privesc).
- **Claim 1b (case-sensitivity fail-open on Modify).** `ec2:Attribute` values are case-sensitive strings; a Deny `StringEquals ec2:Attribute "UserData"` is inert against the real request attribute `userData`. → **Mechanism:** the UserGuide example uses PascalCase `"Description"`, but `ModifyInstanceAttribute` wire attributes are camelCase (`userData`, `groupSet`, `sourceDestCheck`); mismatched case = no match. → **Oracle:** policy-sim/canary a Deny with each casing against a real `userData` modify; record which casing fails open. A fail-open **Deny** is the dangerous direction. → **Severity:** Medium–High (silent bypass of an attribute lockdown).
- **Claim 1c (Describe not attribute-scopable → secret disclosure).** → **Mechanism:** `list_ec2.md` Describe row omits `ec2:Attribute`; `API_DescribeInstanceAttribute` returns `userData` and `groupSet`. → **Oracle:** scoped role with `ec2:DescribeInstanceAttribute` + an `ec2:Attribute`-keyed Deny on `userData`; real call `DescribeInstanceAttribute Attribute=userData` → **expected: returns the base64 user data** (Deny inert). → **Severity:** High if `userData` carries secrets (bootstrap credentials, tokens) — info disclosure across the intended attribute boundary.
- **Claim 1d (structured-field path may not populate `ec2:Attribute` even on Modify).** On `ModifyInstanceAttribute`, the generic `Attribute`/`Value` pair is only used for 5 of ~15 attributes (`API_ModifyInstanceAttribute` line 107: `kernel, ramdisk, userData, disableApiTermination, instanceInitiatedShutdownBehavior`). The two most security-sensitive — `groupSet` and `blockDeviceMapping` — are set via **dedicated structured fields** (`GroupId.N`, `BlockDeviceMapping.N`), not the generic pair. The UserGuide also says `ec2:Attribute/${AttributeName}` binds only primitive / single-`Value` objects, **not** multi-property objects (e.g. `LaunchPermission`). Whether `ec2:Attribute` is even populated into the request context for a `GroupId.N`-shaped call is undocumented — if it is not, a Deny `ec2:Attribute=groupSet` is inert against the actual security-group-replacement call even on Modify. → **Oracle:** policy-sim an `ec2:Attribute=groupSet` / `ec2:Attribute/GroupSet` Deny, then a real `ModifyInstanceAttribute GroupId.1=sg-…` on a self-owned instance; if the SG swap succeeds, the key does not cover the structured path. → **Severity:** Medium–High (the attribute key fails to protect the single most impactful Modify sub-operation — network-exposure change — in the one action that is supposed to support it).

**Doc evidence:** `list_ec2.md` (per-action condition-key rows for Modify/Reset/Describe; `instance` resource row), `iam-policies-for-amazon-ec2.md#attribute-key`, `API_DescribeInstanceAttribute.md`. **Severity-if-true:** Medium–High. **Stop condition:** one policy-sim + one self-owned canary call demonstrating the Deny is inert for Reset or Describe.

### Area 2 — `sourceDestCheck` reset as a network availability/integrity primitive (Lens L / U) — **HIGH**

**Background.** `sourceDestCheck` defaults to `true` (checking enabled). A NAT instance, software router, firewall, or VPN appliance **must** have `sourceDestCheck=false` to forward packets it is not the source/destination of (`API_ResetInstanceAttribute` note + `AmazonVPC VPC_NAT_Instance`; the Config rule `ec2-enis-source-destination-check-enabled` exists precisely because this toggle is security-relevant). `ResetInstanceAttribute` restores it to `true`, and — uniquely among the reset-able attributes — this is allowed **while the instance is running** (no stop/consent gate).

**Security Concern.** A principal holding only `ec2:ResetInstanceAttribute` (a seemingly "harmless, restore-to-default" permission) can silently re-enable source/dest checking on a forwarding instance, dropping all transit traffic and taking down connectivity for **every subnet whose route table points at that instance's ENI** — a blast radius far larger than the single instance, with no data change beyond `return=true`.

**High-level Test Scenarios:**
- **Claim 2a.** One `ResetInstanceAttribute Attribute=sourceDestCheck` call against a running NAT/router instance stops forwarding immediately. → **Oracle:** on a self-owned test NAT instance with a private-subnet client routing through it, call the reset; observe the client loses egress and `DescribeInstanceAttribute sourceDestCheck` now reads `true`. → **Preconditions:** a self-owned NAT/router instance + a client instance behind it. → **Severity:** single-tenant self-inflicted = Low/out-of-scope; **High** if the actor is a low-priv principal whose role was never intended to affect networking (i.e. combined with Area 1 "reset isn't attribute-scopable") — then it is a privilege-to-outage escalation within the account.
- **Claim 2b (no stop/consent gate).** Unlike `kernel`/`ramdisk`, `sourceDestCheck` reset needs no stopped state → no operational signal/approval precedes the outage. → **Oracle:** confirm the reset succeeds against a `running` instance. → **Severity:** raises 2a's likelihood.
- **Claim 2c (Config-rule lag).** The Config rule detects non-compliant source/dest only on ENIs; a reset flips to compliant-looking `true` so detective controls will **not** flag the outage as a misconfiguration. → **Severity:** Informational (the detective control is blind to this specific abuse).

**Doc evidence:** `API_ResetInstanceAttribute.md` (sourceDestCheck default/NAT note; "running or stopped"), `VPC_NAT_Instance`, `ec2-enis-source-destination-check-enabled.md`. **Severity-if-true:** High (network availability within account). **Stop condition:** demonstrate forwarding loss once on self-owned instances.

### Area 3 — Write-twin privilege-escalation & destructive chain via the attribute family (Lens B / X) — **HIGH**

**Background.** The family's write member, `ModifyInstanceAttribute`, is the confirmed **non-PassRole** privesc exemplar (per the corpus): it can set `userData`, `groupSet`/`GroupId.N`, `disableApiTermination`, `blockDeviceMapping` `DeleteOnTermination`, `instanceType`, `kernel`/`ramdisk`. Reset is the "restore to default" face of the same attribute surface; a hunter reaching Reset almost always also holds, or can reach, Modify.

> **Scope-limiting refutation — state up front so the hunter does not burn budget:** `userData` is **absent** from `ResetInstanceAttribute`'s valid-value enum (`kernel|ramdisk|sourceDestCheck` only). The `userData → IMDS → instance-profile-role` privesc chain is therefore **reachable only via `ModifyInstanceAttribute`, NOT via `ResetInstanceAttribute`.** Probing Reset for a userData vector is a confirmed dead end (unless Area 5 shows the wire API silently accepts an undocumented wider enum). This Area is included because Reset and Modify are the same IAM family and a principal reaching one usually reaches the other — but the privesc itself belongs to Modify.

**Security Concern.** Editing `userData` lets a low-priv principal (no `iam:PassRole`) achieve code execution as the **instance-profile role** on the next boot, reading its credentials via IMDS → cross-service blast radius. `groupSet` replacement opens ingress. `disableApiTermination` reset (to default `false`) strips termination protection, enabling a follow-on `TerminateInstances`. `blockDeviceMapping DeleteOnTermination=true` arms data destruction on terminate.

**High-level Test Scenarios:**
- **Claim 3a (userData → role creds).** `ModifyInstanceAttribute userData=<payload>` then stop/start → payload runs as the instance-profile role; `curl …/latest/meta-data/iam/security-credentials/<role>` returns usable creds. → **Mechanism:** `instancedata-add-user-data` (user data runs at boot), `iam-roles-for-amazon-ec2` (creds via IMDS). → **Oracle:** on a self-owned instance with a self-owned low-priv instance profile, confirm the creds are readable under a principal never granted that role. → **Severity:** High (credential exposure across IAM boundary); **Critical only if it reaches cross-account/service-plane — HARD STOP there.**
- **Claim 3b (disableApiTermination strip then terminate).** Reset/modify `disableApiTermination`→`false`, then `TerminateInstances`. → **Oracle:** termination succeeds on a previously-protected self-owned instance. → **Severity:** High (destructive; `Using_ChangingInstanceInitiatedShutdownBehavior` warns termination is irreversible and deletes DeleteOnTermination volumes).
- **Claim 3c (instanceInitiatedShutdownBehavior=terminate).** Set shutdown behavior to `terminate`, then any in-guest shutdown destroys the instance (+ DoT volumes). → **Severity:** High (destructive, bypasses `disableApiTermination` which the docs note does **not** cover OS-initiated shutdown).
- **Claim 3d (parity: are these Modify-only, or also reachable via Reset?).** Reset's documented valid set is `kernel|ramdisk|sourceDestCheck` only — so the destructive attributes above are **Modify-only**. Confirm Reset cannot reach `disableApiTermination`/`userData` on the wire (if it can, that is itself a finding — Area 5). → **Severity:** methodology/parity.

**Doc evidence:** `API_ModifyInstanceAttribute.md` (attribute list incl. `UserData`, `GroupId.N`, `DisableApiTermination`, `BlockDeviceMapping`), `Using_ChangingDisableAPITermination.md`, `Using_ChangingInstanceInitiatedShutdownBehavior.md`, `iam-roles-for-amazon-ec2`. **Severity-if-true:** High (Critical only if it crosses account/service-plane → stop). **Stop condition:** read your own instance's creds once; do not use them to touch further resources.

### Area 4 — Intra-account authorization scoping & ABAC of `ResetInstanceAttribute` (Lens S / A intra-account) — **MEDIUM**

**Background.** Reset supports `aws:ResourceTag/${TagKey}`, `ec2:ResourceTag/${TagKey}`, `ec2:InstanceProfile`, `ec2:Tenancy`, `ec2:Region`, `ec2:InstanceType`, etc. The common pattern is a tag-based ABAC Allow on `instance/*`.

**Security Concern.** Tag-ABAC binds **presence of a tag**, not ownership. If `ec2:CreateTags`/`DeleteTags` is not separately denied, a caller can self-tag a same-account instance into scope, then reset its attributes. Tag **keys and values are case-sensitive**, so a Deny `aws:ResourceTag/Env:prod` is inert against `env=prod`.

**High-level Test Scenarios:**
- **Claim 4a (self-tag into scope).** → **Oracle:** scoped role allowing reset on `aws:ResourceTag/team:x`; tag a foreign-but-same-account self-owned instance `team=x`; real reset succeeds → ABAC-presence bypass. → **Severity:** Medium (High where ABAC is the sole isolation and tag-write isn't locked).
- **Claim 4b (tag case fail-open).** → **Oracle:** instances tagged `Env=prod` vs `env=prod`; test Allow/Deny `StringEquals`; record the fail-open direction. → **Severity:** Medium.
- **Claim 4c (enumeration oracle).** Reset of a non-existent vs not-owned vs wrong-state instance returns distinguishable errors (`InvalidInstanceID.NotFound` vs `IncorrectInstanceState` vs `UnauthorizedOperation`). → **Oracle:** compare codes/latency for fabricated vs real-foreign vs real-own-stopped IDs. → **Severity:** Low (existence/state oracle).

**Doc evidence:** `list_ec2.md` (Reset condition keys), `iam-policies-for-amazon-ec2.md` (self-tag warning), `API_ResetInstanceAttribute.md` (state preconditions → `IncorrectInstanceState`). **Severity-if-true:** Medium. **Stop condition:** one policy-sim/real-call ALLOW demonstrating the gap. **Hunter note:** fetch the **`.md`** variant of `list_ec2` — the `.html` authorization tables are JS-rendered and return empty to a plain fetch.

### Area 5 — Doc-vs-API `Attribute` valid-value discrepancy & undocumented knob (Lens U) — **MEDIUM**

**Background.** `API_ResetInstanceAttribute` lists `Valid Values: kernel | ramdisk | sourceDestCheck`. The target devguide page's PowerShell examples instead "reset" `sriovNetSupport`, `ebsOptimized`, `disableApiTermination`, `instanceInitiatedShutdownBehavior`.

**Security Concern.** Either (a) the PowerShell cmdlet silently maps "reset X" to `ModifyInstanceAttribute X=<default>` (so "reset" is a client-side convenience, and the IAM action actually invoked is `ModifyInstanceAttribute` — which *does* carry `ec2:Attribute`, changing which control applies), or (b) the wire `ResetInstanceAttribute` accepts a wider, undocumented attribute set than its `Valid Values` admits. Case (a) means an operator auditing "who can reset termination protection" must watch `ModifyInstanceAttribute`, not `ResetInstanceAttribute`. Case (b) is an undocumented-knob finding with real teeth: **reset is a one-way ratchet toward the *less-safe* default.** `disableApiTermination` defaults to `false` (protection OFF), so if the wire API honours `Attribute=disableApiTermination` under `ec2:ResetInstanceAttribute`, a principal holding only the "harmless, restore-to-default" Reset permission can **silently strip termination protection** — a team that denied `ModifyInstanceAttribute` believing it locked termination posture would have an undocumented bypass. Reset can only move an attribute toward its default; where the default is the weaker setting, "reset" is an attack.

**High-level Test Scenarios:**
- **Claim 5a.** The wire API rejects `Attribute=disableApiTermination` with `InvalidParameterValue` (confirming the ref) while the SDK/PowerShell silently routes it to Modify. → **Oracle:** send a raw SigV4 `ResetInstanceAttribute Attribute=disableApiTermination` and compare to the PowerShell path's CloudTrail event name (`ResetInstanceAttribute` vs `ModifyInstanceAttribute`). → **Severity:** Low–Medium (audit/scoping confusion; Medium if the wire API accepts an undocumented attribute).

**Doc evidence:** `API_ResetInstanceAttribute.md` (`Valid Values`), target devguide PowerShell examples. **Severity-if-true:** Low–Medium. **Stop condition:** one raw-wire probe on a self-owned instance + CloudTrail diff.

### Area 6 — `DryRun` as a false-positive authorization oracle (Lens A variant — trap to document, not a bug) — **INFORMATIONAL**

**Claim.** `DryRun=true` against a foreign or wrong-state instance returns `DryRunOperation` (caller-IAM-only) even though a real reset would fail on ownership/state. → **Oracle:** compare `DryRun` result vs real-call result for a known not-owned ID; if DryRun says "authorized" but the real call is denied, the oracle is confirmed misleading. → **Severity:** N/A (methodology guardrail) — document so Areas 1/4 use the **real** canary call, never DryRun, as the ownership/attribute oracle. **Doc evidence:** `API_ResetInstanceAttribute.md` DryRun semantics.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| `ec2:Attribute` Deny on Modify evaded via Reset/Describe | IAM authz for the attribute family | Per-action condition-key coverage (`list_ec2.md`) — prove it is non-uniform |
| Case-mismatched `ec2:Attribute` Deny fails open | IAM policy eval | `StringEquals` case-sensitivity of the attribute value |
| `sourceDestCheck` reset → VPC transit outage | NAT/router instance + route tables | `sourceDestCheck=false` requirement for forwarding (VPC NAT doc) |
| `userData` edit → run-as-instance-role | Modify twin + IMDS + instance profile | `iam:PassRole` is **not** required for ModifyInstanceAttribute(userData) — the gap |
| Strip `disableApiTermination` → terminate | Termination protection | `DisableApiTermination` attribute; irreversibility warning |
| Self-tag victim instance into ABAC scope | Tag-based Allow on `instance/*` | `iam-policies-for-amazon-ec2` self-tag warning (deny `CreateTags`) |
| Cross-account reset via raw `i-…` | Account-scoped ARN resolver | `arn:…:${Account}:instance/${InstanceId}` scoping (expected null) |
| SDK "reset" actually calls Modify | CloudTrail attribution | API-ref `Valid Values` vs devguide examples |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **Cross-account IDOR by fabricated instance ID** — the ARN is account-scoped; a foreign `i-…` resolves `NotFound`. Confirm once, then treat as null; do **not** brute-force foreign IDs.
- **Single-tenant self-DoS** — resetting `sourceDestCheck`/`kernel` on your *own* instance with your *own* admin role is a footgun, not a vuln (in scope only when the acting principal was scoped to *not* be able to do it — Area 1/2 chain).
- **Least-privilege footguns in CUSTOMER-authored IAM policies** — a customer who grants broad `ec2:ResetInstanceAttribute` owns that. **In scope** only for AWS-authored managed/sample policies the customer copies verbatim (none specific to Reset were found — see §8).
- **IMDS on managed hosts / the instance OS internals** beyond reading your own instance's role creds once.
- **AWS's own fleet / service plane** — HARD STOP + disclosure; never exploit.
- **Memory-safety of the EC2 control-plane request parser** — no customer-reachable parser surface is documented for this simple 2-string API; out of scope.

---

## 8. Null hypotheses / doc gaps (lenses checked, pages named)

- **Lens G (SSRF) — N/A.** Read `API_ResetInstanceAttribute/Modify/Describe` and the UserGuide attribute pages: no field in Reset/Describe is a URL/host the service dereferences. (`userData` is executed *on the customer's own instance*, not fetched by the service plane.) No server-side-fetch surface.
- **Lens H (KMS/encryption context) — N/A for Reset.** Reset touches `kernel|ramdisk|sourceDestCheck`; none involves a CMK or encryption context. (Volume encryption lives on `ModifyVolume`/snapshots — different plan.)
- **Lens K (prompt injection) — N/A.** No LLM/agent in this API path.
- **Lens R/S (AWS-authored IAM artifact) — doc-gap/partial.** No AWS-managed policy or CFN/runbook was found that grants `ec2:ResetInstanceAttribute` specifically; the `ec2:Attribute` UserGuide examples are illustrative (ModifyImageAttribute), not shipped managed policies. If a hunter finds `ec2:ResetInstanceAttribute` inside an AWS-managed policy, re-open Lens R. The **Area 1 asymmetry is reportable on its own** as a doc/enforcement gap (Lens U), AWS-owned.
- **Lens W (attestation), Lens Y (transport/SigV4), Lens BB/CC/DD/FF (edge/token/cache) — N/A.** This is a plain SigV4 EC2 control-plane action with no authorizer/edge/caching/JWT layer; standard EC2 endpoint TLS applies (not specific to this API).
- **Lens N (namespace migration) — N/A.** No dual ARN/namespace for this action.
- **Doc gap to confirm first:** whether the SDK/PowerShell "reset" of non-ref attributes maps to Modify (Area 5) — settles which IAM action/CloudTrail event an auditor must watch.

---

**Deeper per-area analysis (for the hunter):** two documentation-only deep-dives back this plan with exact line citations and doc-gap notes —
- `/work/aws-docs/_resetinstanceattr_research/area_attribute_scoping.md` — the `ec2:Attribute` asymmetry across Describe/Modify/Reset (H1–H4 + doc-gaps G1–G5), incl. the case-sensitivity-of-AWS's-own-example angle and the structured-field-path question.
- `/work/aws-docs/_resetinstanceattr_research/area_attribute_semantics.md` — reset semantics (ratchet-toward-unsafe-default), `sourceDestCheck`/NAT outage, `kernel`/`ramdisk` PV boot integrity, and the explicit refutation that userData→IMDS privesc is Modify-only.

*Prepared from AWS public documentation only (offline mirror + docs.aws.amazon.com, 2026-10-20; online == offline confirmed for the API reference and target devguide page). No live AWS account was contacted. Downstream hunter: `aws-vuln-hunter` with two self-owned test accounts; start at Area 1 (IAM policy simulator first), then Area 2, using real canary calls — never `DryRun` — as the ownership/attribute oracle. Fetch the `.md` variant of `list_ec2` / authorization pages (the `.html` tables are JS-rendered and return empty). Stop and disclose on any service-plane evidence.*
