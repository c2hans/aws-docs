# ModifyNetworkInterfaceAttribute (modify-network-interface-attributes.html) — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/modify-network-interface-attributes.html` (+ `.md` twin); API Reference `API_ModifyNetworkInterfaceAttribute.html` / `API_ResetNetworkInterfaceAttribute.html`; IAM Service Authorization Reference `list_ec2.md` (actions @8966 `ModifyNetworkInterfaceAttribute`, @9519 `ResetNetworkInterfaceAttribute`). Status: documentation-derived hypotheses only; nothing tested against a live account. Target page + both API-ref `.md` twins + `list_ec2.md` verified **offline == online byte-identical, 2026-10-15**.

> **Position in the corpus.** This is a **page-level deep-dive child of the `ec2-networking` hub** and a **procedural complement of [[using-eni-plan]]** (`using-eni-attack-research-plan.md`), which owns the ENI *resource* lifecycle/attribute/grant surface and already carries `ModifyNetworkInterfaceAttribute` (its lead #3) and `ResetNetworkInterfaceAttribute` (its lead #4) at summary level. **Treat `using-eni` as authoritative for the ENI-grant / Attach-cross-VPC / Describe-oracle leads; this plan owns the per-attribute modify surface of this one page** and develops three things the sibling left open:
> 1. the **console-hidden API-vs-UserGuide parameter delta** (the API accepts 5 security-relevant knobs this page never lists) — the headline, net-new to the whole corpus;
> 2. the **corrected 4-resource-row IAM structure** of the action (the sibling recorded only the `network-interface*` row);
> 3. the **per-attribute value-level-key audit** mapping each modifiable attribute to its security consequence and confirming which have no condition key.
>
> **Explicitly defers (does NOT restate):** `DeleteNetworkInterfacePermission` revoke-asymmetry, `AttachNetworkInterface` cross-VPC, unscopable `DescribeNetworkInterfaces` oracle → [[using-eni-plan]]; create-time attribute unscopability + `trunk`/`Operator` + EFA create → [[create-network-interface-plan]]; IP-value / `AllowReassignment` takeover / EIP ride-along → [[using-instance-addressing]] / [[working-with-ip-addresses]] / [[instance-secondary-ip-addresses]]; EIP transfer / shared-VPC isolation / EFA-SRD cross-tenant mechanism → the `ec2-networking` hub; Windows guest split-brain → [[config-windows-multiple-ip-plan]]. See [[reference-aws-iam-service-auth-ref-url]].

---

## 0. How to use this document
- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- Primary safe oracle for every IAM-scoping lead here is `iam:SimulateCustomPolicy` / `iam:SimulatePrincipalPolicy` — it settles "is this key inert on this action?" **without creating or mutating any resource.** `DryRunOperation` is **caller-IAM only, evaluated before resource resolution — NOT an ownership oracle** (false-positive trap).
- **HARD STOP:** the page's own Considerations block — *"You can't change the attributes of a requester-managed network interface."* The moment a probe reaches a **requester-managed** or **`Operator`/`Managed=true`** ENI (EKS Auto Mode, ELB/NAT-GW/Lambda/service-owned), that is **AWS's own service plane** — stop, preserve evidence, flag for AWS-Security disclosure. Do not attempt to modify it.

---

## 1. Pentest Objectives (boundary-breach goals, concrete)
1. **Change an ENI's security-relevant attribute (source/dest-check, security-group set, delete-on-termination, conntrack timeout, public-IP association, primary-IPv6, ENA-SRD) that a scoped IAM policy was written to forbid** — proving the policy's intended value-level guardrail is inert.
2. **Flip a private-subnet instance's primary ENI to a public IPv4 address via the console-hidden `AssociatePublicIpAddress` parameter**, with no IAM key on this action able to deny it.
3. **Disable `SourceDestCheck` on an ENI to turn its instance into an undeclared MITM / NAT / transit node**, then (chained with the sibling's cross-VPC attach) a cross-VPC interception appliance.
4. **Flip `DeleteOnTermination=false` to leave a persistent/orphan ENI (carrying a private IP + any associated EIP) that survives instance termination**, or `=true` to destroy an ENI another workload depends on.
5. **Set a maximal (432000 s / 5-day) idle TCP conntrack timeout to amplify conntrack-table exhaustion** on a shared ENI, defeating the docs' own "configure the shortest timeout possible" guidance with no enforcement.
6. **Irreversibly enable primary IPv6 (`EnablePrimaryIpv6`) on a victim ENI** — a one-way state change the page never documents.
7. **Re-enable `SourceDestCheck=true` via `ResetNetworkInterfaceAttribute` on a routing/NAT/firewall appliance ENI (incl. requester-managed, where Modify is blocked)** to break its forwarding = availability takedown that routes around the Modify guardrail.

---

## 2. Components, Assets, and Design

**Interface.** Single mutating control-plane action, `ec2:ModifyNetworkInterfaceAttribute` (SigV4, EC2 Query/SDK), callable from the internet with EC2 credentials. Companion `ec2:ResetNetworkInterfaceAttribute`. No data-plane component; the "resource" is an **Elastic Network Interface (ENI)**, ARN `arn:${Partition}:ec2:${Region}:${Account}:network-interface/${NetworkInterfaceId}` (id `eni-<17 hex>`, ~68-bit — **not fabricable**, so blind cross-tenant IDOR is a genuine partial-null; residual = known/shared/same-account ids).

**The attribute set — User Guide page (5) vs control-plane API (10).** The page lists only: Description, Security groups, Delete-on-termination, Source/destination check, Idle connection-tracking timeout. The API (`API_ModifyNetworkInterfaceAttribute`) additionally accepts, **none surfaced on this page or (mostly) the console**:

| Parameter | Type | On UG page? | Security meaning | IAM value-level key? |
|---|---|---|---|---|
| `Description` | AttributeValue | yes | free-text, shown in Describe/console | **none** (`ec2:Description` = 0 hits) |
| `SecurityGroupId.N` | Array | yes | "new set **replaces** current set", min 1 | **`ec2:SecurityGroupID` + `ec2:Vpc`** (on the `security-group` row — the ONLY value-scopable attribute) |
| `Attachment{DeleteOnTermination}` | NetworkInterfaceAttachmentChanges | yes | ENI survives/destroyed on instance terminate | **none** (`ec2:DeleteOnTermination` = 0 hits) |
| `SourceDestCheck` | AttributeBooleanValue | yes | disable → instance may route/NAT/firewall | **none** (`ec2:SourceDestCheck` = 0 hits) |
| `ConnectionTrackingSpecification` | object | yes | TCP idle timeout 60–432000 s, UDP 30–60, UDP-stream 60–180 | **none** (`ec2:ConnectionTracking`/`IdleTimeout`/`TcpEstablishedTimeout`/`UdpTimeout` = 0 hits) |
| `AssociatePublicIpAddress` | Boolean | **NO** | assign a **public IPv4** to the primary ENI (eth0) | **`ec2:AssociatePublicIpAddress` KEY EXISTS but is ABSENT from this action's rows** (see §5.2) |
| `EnablePrimaryIpv6` | Boolean | **NO** | **one-way irreversible** primary-IPv6 GUA enable | **none** (`ec2:EnablePrimaryIpv6`/`ec2:PrimaryIpv6` = 0 hits) |
| `EnaSrdSpecification` | EnaSrdSpecification | **NO** | ENA Express / SRD transport reconfig on an attached ENI | **none** (`EnaSrd` = 0 hits) |
| `AssociatedSubnetId.N` | Array | **NO** | associate subnet IDs with the ENI | **none** (`AssociatedSubnet` = 0 hits) |

**IAM structure (corrects [[using-eni-plan]], which recorded only the `network-interface*` row).** `list_ec2.md` @8968–8971 — `ModifyNetworkInterfaceAttribute` has **four** resource rows:
- `instance` (non-`*`required): 22 instance keys (`ec2:InstanceID`, `ec2:InstanceType`, `ec2:Tenancy`, `ec2:MetadataHttpTokens`, `ec2:InstanceProfile`, …) — a defender lever the sibling missed (scope modify to ENIs attached to instances tagged/typed X).
- `network-interface*` (`*`required, always evaluated): `aws:ResourceTag`, `ec2:Attribute`, `ec2:Attribute/${AttributeName}`, `ec2:AvailabilityZone`, `ec2:ManagedResourceOperator`, `ec2:NetworkInterfaceID`, `ec2:Region`, `ec2:ResourceTag`, `ec2:Subnet`, `ec2:Vpc` — scopes **which ENI** and **which attribute *name***, never an attribute *value*.
- `security-group` (non-`*`): `ec2:SecurityGroupID`, `ec2:Vpc`, `ec2:Region`, tag — the one row that scopes a *value* (which SG may be attached).
- `subnet` (non-`*`): `ec2:AvailabilityZone(Id)`, `ec2:Vpc`, `ec2:Region`, tag.

`ResetNetworkInterfaceAttribute` @9521–9522: `network-interface*` only, keys `aws:ResourceTag`, `ec2:AvailabilityZone`, `ec2:ManagedResourceOperator`, `ec2:NetworkInterfaceID`, `ec2:Region`, `ec2:ResourceTag`, `ec2:Subnet`, `ec2:Vpc` — **no `ec2:Attribute` key at all**; API resets exactly one attribute: `SourceDestCheck` → `true`.

```
 Caller (EC2 creds)                      ENI resource (eni-xxxx)
    │  ec2:ModifyNetworkInterfaceAttribute   ┌───────────────────────────┐
    ├────────────────────────────────────►   │ attrs: desc / SGset /     │
    │   (one attribute per call)              │ DeleteOnTerm / SrcDstChk /│
    │                                         │ conntrack / AssocPubIP /  │
    │   authz rows: instance | NI* | SG | subnet │ PrimaryIPv6(1-way)/EnaSRD│
    │   value-level keys: ONLY which-SG       └───────────┬───────────────┘
    │                                                     │ attached to
    ▼  ec2:ResetNetworkInterfaceAttribute                 ▼
  resets SrcDstChk→true (works on requester-managed)   instance / data path
                                                        (MITM, exposure, persistence)
```

---

## 3. API / Interface Inventory

| Name | Method | New/Existing | Mutating | Internal/External | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|---|
| `ec2:ModifyNetworkInterfaceAttribute` | SigV4 | Existing (params grew) | **Yes** | External | Change one ENI attribute per call | Yes | Any principal allowed the action on the ENI | **5 of 10 accepted params are undocumented on this page**; one-attribute-at-a-time |
| `ec2:ResetNetworkInterfaceAttribute` | SigV4 | Existing | Yes | External | Reset `SourceDestCheck`→true | Yes | Any principal allowed the action | No `ec2:Attribute` key; works on requester-managed ENIs |

**Console-hidden / under-surfaced knobs (Step-3 hunt):** `AssociatePublicIpAddress`, `EnablePrimaryIpv6`, `EnaSrdSpecification`, `AssociatedSubnetId.N` — accepted by the control-plane API/SDK but absent from this UserGuide page and (per the page's own console walkthrough, which exposes only the 5 "Actions" menu items) absent from the console. The delta is the lead (§5.1).

---

## 4. Trust-Boundary Map

| From (actor/zone) | To (resource/zone) | Crossing mechanism | Breach oracle |
|---|---|---|---|
| Scoped IAM principal (intra-account, team A) | ENI owned/used by team B | `ModifyNetworkInterfaceAttribute` with a value-level attribute | A policy intended to forbid *disabling src/dest-check* / *flipping public-IP* / *long conntrack* / *DeleteOnTermination=false* does not stop the call → attribute changes = **inert-guardrail breach** |
| Caller | Data path of the attached instance | disable `SourceDestCheck`; set `EnaSrdSpecification`; `AssociatePublicIpAddress=true` | Instance now routes/NATs traffic it shouldn't, or is reachable on a new public IPv4, where the segmentation model said no |
| RAM-share participant / owner | Each other's ENI in a shared subnet | Modify across the share | **Foreclosed by design** (owner "cannot modify" participant ENIs; participant can't name owner's) — confirm it stays foreclosed, don't assume |
| Any caller | **requester-managed / `Operator`-owned ENI** | `ModifyNetworkInterfaceAttribute` (blocked) / `ResetNetworkInterfaceAttribute` (allowed) | **HARD STOP** — service plane; a Reset that re-enables src/dest-check on a service ENI is an availability hit on AWS infra |

---

## 5. Recommended Areas of Focus

### 5.1 — Area 1 (HEADLINE, Lens U "console-hidden knob" + Lens S "key-not-attached"): the API accepts 5 security-relevant attributes this page never documents, none with a value-level IAM key
**Background.** The UserGuide page enumerates exactly 5 modifiable attributes and builds the operator's mental model (and their least-privilege policy) around them. The control-plane API accepts **4 more** security-relevant parameters — `AssociatePublicIpAddress`, `EnablePrimaryIpv6`, `EnaSrdSpecification`, `AssociatedSubnetId.N` — plus the 5 documented ones. An operator who audits "what can `ec2:ModifyNetworkInterfaceAttribute` do?" from this page underestimates the action.

**Security Concern.** For every one of these attributes except security-group membership, there is **no condition key that scopes the attribute's *value*** — only `ec2:Attribute/${AttributeName}` (the attribute *name*) exists on the `network-interface*` row. Confirmed 0-hit in `list_ec2.md`: `ec2:SourceDestCheck`, `ec2:DeleteOnTermination`, `ec2:ConnectionTracking`/`IdleTimeout`/`TcpEstablishedTimeout`/`UdpTimeout`, `ec2:Description`, `ec2:EnablePrimaryIpv6`/`ec2:PrimaryIpv6`, `EnaSrd`, `AssociatedSubnet`. So a policy that grants `ec2:ModifyNetworkInterfaceAttribute` (even scoped to one ENI, one attribute-name) **cannot** express "…but never disable source/dest-check", "…never set a 5-day conntrack timeout", "…never flip DeleteOnTermination", "…never enable a public IP", "…never enable primary-IPv6". The grant is all-or-nothing per attribute name; `ec2:Attribute/${AttributeName}` even keys on the PascalCase attribute name and is in the known **case-sensitivity fail-open** class (a Deny written against a lowercase enum is inert).

**High-level Test Scenarios.**
- **Claim:** a principal allowed `ec2:ModifyNetworkInterfaceAttribute` on `eni-X` can set *any* value of *any* of the 10 attributes, regardless of a Deny that tries to pin the value. → **Oracle:** `iam:SimulateCustomPolicy` with a policy `Allow ModifyNetworkInterfaceAttribute on eni-X` + `Deny` conditioned on each hypothesized value key → every value-key Deny evaluates as **no-op** (key not in the request context for this action) while the Allow stands. No resource touched. → **Severity:** Medium (intra-account least-priv control gap; **AWS-owned/reportable** because the gap is in the service's own condition-key coverage, not a customer artifact).
- **Claim:** the console-hidden params are honored by the SDK/API even though no console path exists. → **Oracle:** `aws ec2 modify-network-interface-attribute --network-interface-id <canary> --associate-public-ip-address` and `--enable-primary-ipv6` succeed against a self-owned canary ENI (live, own resource only). → settles that the delta is real surface, not a stale doc.

**Doc evidence.** `API_ModifyNetworkInterfaceAttribute` Request Parameters (AssociatePublicIpAddress / EnablePrimaryIpv6 / EnaSrdSpecification / AssociatedSubnetId.N) vs the page's 5-item list (`modify-network-interface-attributes.md:8–13`). `list_ec2.md` @8968–8971 + 0-hit value-key grep. **Severity-if-true:** Medium (control-gap, Tier-2 reportable).

### 5.2 — Area 2 (Lens S inert-key + Lens X action-family asymmetry): `AssociatePublicIpAddress` is unscopable on *this* action though the key exists on `RunInstances`
**Background.** `ec2:AssociatePublicIpAddress` **is** a real IAM key (Bool, def `list_ec2.md:10050`) and appears on the `network-interface` **resource-type** row (@9982) and on **`RunInstances`'s `network-interface*` row** (@9595) — so "no public IP at launch" is (partially) expressible on the launch path. But it is **absent from all four `ModifyNetworkInterfaceAttribute` rows** (@8968–8971).

**Security Concern.** The action lets you **flip an existing primary ENI (eth0) to a public IPv4 after the fact** (`AssociatePublicIpAddress=true`), yet the one key that could govern it is not wired to the action. A defender who blocked public-IP exposure at launch via `ec2:AssociatePublicIpAddress` on `RunInstances` has **no equivalent lever on the modify path** → an attacker (or a careless automation) re-exposes a private-subnet box's primary ENI to the internet. This is the Lens-X "one action in the family is scopable, its sibling is not" shape, and the Lens-S "capability exists but not attached" shape, together.

**High-level Test Scenarios.**
- **Claim:** `Deny ec2:ModifyNetworkInterfaceAttribute … Condition {Bool ec2:AssociatePublicIpAddress true}` does not block the flip because the key is undefined for this action. → **Oracle:** `iam:SimulateCustomPolicy` — the Deny is inert; a parallel sim on `RunInstances` with the same condition **does** deny → asymmetry confirmed. → **Severity:** Medium–High (private→public exposure change with no governing key; High if the subnet/instance was relied on as private).
- **Adjacent:** does the flip actually assign a public IP on a *non-primary* ENI? API says it "will only apply to the primary network interface (eth0)" → confirm the scope so the hunter doesn't over-claim on secondary ENIs.

**Doc evidence.** `list_ec2.md:10050` (key def), `:9595` (RunInstances NI row has it), `:9982` (resource-type row has it), `@8968–8971` (Modify rows lack it); `API_ModifyNetworkInterfaceAttribute` AssociatePublicIpAddress note. **Severity-if-true:** Medium–High. Cross-ref [[working-with-ip-addresses]] Area 1 (the launch-time twin of this key).

### 5.3 — Area 3 (Lens S/U/D): disabling `SourceDestCheck` is an unscopable MITM/NAT/transit enablement
**Background.** The page ships a verbatim example that *enables* src/dest-check (`--source-dest-check`) and the API default is `true`; the API note states *"You must disable source/destination checks if the instance runs services such as network address translation, routing, or firewalls."* Disabling it is precisely what converts an instance into a device that forwards traffic for other IPs/MACs.

**Security Concern.** No `ec2:SourceDestCheck` key exists (0 hits) → granting modify of the `sourceDestCheck` attribute = granting the ability to turn any reachable instance into an undeclared router/NAT/sniffer, with no guardrail on the value. The page gives the example with **no warning** that disabling it has this effect (the operational meaning lives only in the API ref and the SG/routing docs). **Chain:** combine with [[using-eni-plan]] lead #2 (`AttachNetworkInterface` instance row has no `ec2:Vpc` → same-account cross-VPC attach is unfenceable) → attach a src/dest-check-disabled ENI across VPCs = a cross-VPC interception/transit node that IAM cannot forbid at either step.

**High-level Test Scenarios.**
- **Claim:** a principal scoped to "modify ENI attributes" can disable src/dest-check on an instance it does not administer, enabling forwarding. → **Oracle (live, own canary):** two canary instances in one subnet; disable src/dest-check on A; route B's traffic for a third IP through A; packet arrives = forwarding enabled. **IAM oracle:** sim shows no value-key Deny can stop the disable. → **Severity:** Medium intra-account; **High** when chained to cross-VPC attach (lateral interception).

**Doc evidence.** `modify-network-interface-attributes.md:53–59, 112–119`; `API_ModifyNetworkInterfaceAttribute` SourceDestCheck note; `list_ec2.md` 0-hit `ec2:SourceDestCheck`. Cross-ref [[using-eni-plan]] #3 (owns the base finding) + #2 (cross-VPC attach). **Severity-if-true:** Medium–High.

### 5.4 — Area 4 (Lens AA/U integrity): `DeleteOnTermination` flip = persistence/orphan or destruction, unscopable
**Background.** `Attachment{DeleteOnTermination}` is modifiable per-attachment (`--attachment AttachmentId=…,DeleteOnTermination=false`).

**Security Concern.** No `ec2:DeleteOnTermination` key (0 hits). Two directions:
- **→ false (persistence/orphan):** the ENI — with its private IP and any **associated EIP** (EIP rides along per the addressing siblings) — **survives instance termination**, leaving a dangling, attacker-retained interface/address (reputation/dangling-DNS; cross-ref [[using-eni-plan]] #6 public-IPv4 persistence footgun).
- **→ true (destruction):** forcing `=true` on an ENI another workload depends on causes it to be deleted when the instance terminates = integrity/availability loss the owner didn't choose.

**High-level Test Scenarios.** **Claim:** the flip is accepted on an attachment the caller does not own the lifecycle of, with no value-key able to forbid either direction. → **Oracle:** `iam:SimulateCustomPolicy` (value-key Deny inert) + live own-canary flip confirming the attribute persists. → **Severity:** Medium (intra-account integrity/persistence).

**Doc evidence.** `modify-network-interface-attributes.md:45–51, 103–109`; `API_NetworkInterfaceAttachmentChanges`; 0-hit `ec2:DeleteOnTermination`. **Severity-if-true:** Medium.

### 5.5 — Area 5 (Lens L/U): idle conntrack timeout up to 432000 s (5 days) amplifies table exhaustion, "shortest possible" guidance unenforceable
**Background.** `ConnectionTrackingSpecification` sets `TcpEstablishedTimeout` (60–432000 s), `UdpTimeout` (30–60), `UdpStreamTimeout` (60–180). The linked `security-group-connection-tracking` guidance recommends short timeouts to avoid conntrack-table exhaustion.

**Security Concern.** No IAM key caps any of the three timeouts (0 hits). A principal can set the **maximum 5-day TCP timeout** on an ENI → idle connections pin conntrack entries far longer, accelerating per-ENI conntrack-table exhaustion (dropped new connections) — a noisy-neighbor / self-DoS amplifier that the docs' own "configure the shortest timeout possible" cannot enforce. Overlaps [[create-network-interface-plan]] Area 3 (same exhaustion vector at *create*; this is the *modify* path on a live, possibly busy ENI).

**High-level Test Scenarios.** **Claim:** a scoped modify grant can set `TcpEstablishedTimeout=432000` with no policy able to cap it. → **Oracle:** `iam:SimulateCustomPolicy` (no timeout key to condition on) + live own-canary set. → **Severity:** Low–Medium single-tenant; Medium if the ENI is on a shared/high-connection appliance.

**Doc evidence.** `modify-network-interface-attributes.md:61–78, 121–128`; 0-hit `ec2:ConnectionTracking`/`IdleTimeout`/`TcpEstablishedTimeout`/`UdpTimeout`. **Severity-if-true:** Low–Medium.

### 5.6 — Area 6 (Lens U/AA): `EnablePrimaryIpv6` is a one-way irreversible state the page never documents
**Background.** The API: *"Once you enable an IPv6 GUA address to be a primary IPv6, you cannot disable it … until the instance is terminated or the network interface is detached."* The UserGuide page does **not** list `EnablePrimaryIpv6` among modifiable attributes.

**Security Concern.** A modify grant can **irreversibly** enable primary-IPv6 on a victim ENI (griefing/pinning an address state the owner can only undo by terminate/detach), via a parameter the page's reader never knew existed, with no condition key (`ec2:EnablePrimaryIpv6`/`ec2:PrimaryIpv6` = 0 hits). This **corrects [[create-network-interface-plan]] Area 5**, which noted this page "has no disable" — true, but it *does* have the irreversible **enable**, undocumented here.

**High-level Test Scenarios.** **Claim:** enable succeeds and cannot be reverted via any modify call. → **Oracle:** live own-canary: enable, then confirm no API path disables it (only detach/terminate). **IAM:** no governing key. → **Severity:** Low–Medium (irreversible state griefing).

**Doc evidence.** `API_ModifyNetworkInterfaceAttribute` EnablePrimaryIpv6; absence from `modify-network-interface-attributes.md:8–13`. **Severity-if-true:** Low–Medium.

### 5.7 — Area 7 (Lens U/V, defers mechanism to hub): `EnaSrdSpecification` reconfigures ENA Express / SRD transport post-hoc, unscopable
**Background.** The API accepts `EnaSrdSpecification` ("Updates the ENA Express configuration for the network interface that's attached to the instance") — a console-hidden knob on this page.

**Security Concern.** No `EnaSrd` condition key (0 hits). Enabling/altering SRD changes the L4 transport path; the `ec2-networking` hub's lead #3 flags EFA/SRD as a potential cross-tenant OS-bypass frame-injection surface whose enforcement layer the docs never name. This action is a **modify-time** entry to that surface with no IAM value lever. **Defer the SRD cross-tenant mechanism itself to the hub**; own here only the "SRD is reconfigurable via this unscopable, undocumented-on-page param" fact.

**High-level Test Scenarios.** **Claim:** SRD config can be toggled on an attached ENI by a modify-scoped principal, no key to forbid. → **Oracle:** `iam:SimulateCustomPolicy` + live own-canary toggle (observe `DescribeNetworkInterfaces` ENA-SRD state). Do **not** attempt cross-tenant SRD frame injection — that is the hub's lead and risks the service plane. → **Severity:** Informational here (surface-mapping); inherits the hub's severity if the cross-tenant SRD question resolves positive.

**Doc evidence.** `API_ModifyNetworkInterfaceAttribute` EnaSrdSpecification; 0-hit `EnaSrd`. Cross-ref `ec2-networking` hub #3. **Severity-if-true:** Informational → High (via hub).

### 5.8 — Area 8 (Lens S positive note + asymmetry): security-group replacement is the ONE value-scopable attribute, but removal is still unbounded
**Background.** `SecurityGroupId.N` — *"The new set of groups you specify replaces the current set. You must specify at least one group."* The `security-group` resource row **does** carry `ec2:SecurityGroupID` + `ec2:Vpc`.

**Security Concern.** A defender **can** scope *which* SGs may be attached (good — note this as the one working value lever, contrary to the "everything unscopable" theme). **But:** because the set is a wholesale **replace** and the only key constrains the *new* SG's identity, a policy that allows attaching `sg-allowed` cannot prevent **removing a protective SG** (the attacker supplies `sg-allowed` alone, dropping a restrictive SG that was also attached). And the service enforces same-VPC (console: "must be created for the same VPC") so cross-VPC SG injection is foreclosed. Net: SG *addition* is scopable; SG *removal/replacement semantics* are not expressible.

**High-level Test Scenarios.** **Claim:** with `Allow` conditioned on `ec2:SecurityGroupID = sg-allowed`, a caller can still strip a co-attached restrictive SG by replacing the set with `sg-allowed` only. → **Oracle:** `iam:SimulateCustomPolicy` shows the replace is permitted (new set satisfies the condition) + live own-canary confirming the restrictive SG is gone. → **Severity:** Medium (firewall-weakening via a scoped grant).

**Doc evidence.** `API_ModifyNetworkInterfaceAttribute` SecurityGroupId.N; `list_ec2.md:8970` (security-group row keys). **Severity-if-true:** Medium.

### 5.9 — Area 9 (Lens X/S/U + HARD STOP): `ResetNetworkInterfaceAttribute` re-enables src/dest-check on ENIs where Modify is blocked, with no `ec2:Attribute` key
**Background.** The page's Considerations: *"You can't change the attributes of a requester-managed network interface."* Yet `ResetNetworkInterfaceAttribute` (resets `SourceDestCheck`→`true`) **works on requester-managed ENIs** (per `requester-managed-eni.md`, owned by [[using-eni-plan]] #4) and has **no `ec2:Attribute` key at all** (@9521–9522).

**Security Concern.** Reset is a narrower primitive than I'd otherwise fear — it can **only set `SourceDestCheck=true`** (the "safe" default direction). But forcing `=true` on a **NAT/router/firewall appliance ENI** *breaks its forwarding* = availability takedown, and the modify-deny-but-reset-allowed asymmetry means a principal denied `ModifyNetworkInterfaceAttribute` can still reach this via `ResetNetworkInterfaceAttribute`, un-narrowable by attribute name. **HARD STOP:** requester-managed ENIs are AWS/service-owned (ELB, NAT-GW, Lambda, EKS Auto Mode managed ENIs); resetting src/dest-check on one is touching the service plane — confirm the asymmetry with `iam:SimulateCustomPolicy` only, never fire Reset at a managed ENI.

**High-level Test Scenarios.** **Claim:** `Deny ModifyNetworkInterfaceAttribute` + `Allow ResetNetworkInterfaceAttribute` lets a principal re-enable src/dest-check on an ENI the Modify deny was meant to protect. → **Oracle:** `iam:SimulateCustomPolicy` (Reset allowed, no attribute-name condition possible) + live own-canary routing instance (reset → forwarding stops). → **Severity:** Medium (availability/guardrail-routing bypass; **do not test against managed ENIs**).

**Doc evidence.** `API_ResetNetworkInterfaceAttribute` (SourceDestCheck→true only); `list_ec2.md:9521–9522` (no `ec2:Attribute`); page Considerations `:15–16`. Cross-ref [[using-eni-plan]] #4. **Severity-if-true:** Medium.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Flip ENI to public IPv4 via console-hidden `AssociatePublicIpAddress` | `ModifyNetworkInterfaceAttribute` | None on this action — key exists only on `RunInstances` (§5.2) |
| Disable src/dest-check → MITM/NAT, chain cross-VPC attach | Modify + `AttachNetworkInterface` | Service default `true`; no value key; cross-VPC attach unfenceable (§5.3) |
| `DeleteOnTermination=false` → persistent/orphan ENI+EIP | Modify (attachment) | No value key; EIP ride-along undocumented (§5.4) |
| 5-day conntrack timeout → table exhaustion | Modify (conntrack) | Prose "shortest possible", unenforceable; no key (§5.5) |
| Irreversible `EnablePrimaryIpv6` on victim ENI | Modify | One-way per API; undocumented on page; no key (§5.6) |
| Reconfigure ENA-SRD transport post-hoc | Modify (`EnaSrdSpecification`) | No key; mechanism deferred to hub (§5.7) |
| Strip protective SG via wholesale replace | Modify (`SecurityGroupId.N`) | `ec2:SecurityGroupID` scopes *additions* only (§5.8) |
| Re-enable src/dest-check on routing/managed ENI via Reset | `ResetNetworkInterfaceAttribute` | Modify-deny bypass; no attribute key; **HARD STOP on managed** (§5.9) |
| Value-level guardrail (any attribute) proven inert | both actions | `iam:SimulateCustomPolicy` (§5.1) |

---

## 7. Out-of-Scope Risk Categories
- **Shared/managed infrastructure & the service plane** — requester-managed / `Operator`-owned / `Managed=true` ENIs (EKS Auto Mode, ELB, NAT-GW, Lambda, etc.). Modify is blocked; Reset reaching them = **HARD STOP, disclosure**, never a test target.
- **Cross-account modify of ENIs** — foreclosed by shared-VPC design (owner cannot modify participant ENIs; participant cannot name owner ENIs). Note as foreclosed; do not spend budget unless a doc change reopens it.
- **Blind cross-tenant IDOR by fabricated `eni-id`** — ids are ~68-bit, not fabricable (genuine partial-null). Residual = known/shared/same-account ids only.
- **Customer-authored least-privilege footguns** — a customer who writes an over-broad `ModifyNetworkInterfaceAttribute` grant is their own problem; the **in-scope, reportable** item is the *service's own* missing value-level condition keys (§5.1/§5.2 — AWS-owned, Tier-2).
- **IMDS on managed hosts, DNS rebinding against private endpoints, product/feature-parity gaps.**

## 8. Null hypotheses / doc gaps (pages checked)
- **Lens A (cross-tenant IDOR):** NULL — single mutating action on an `eni-<17hex>` resource; ownership bound by the credential + required `network-interface*` row; no body-vs-path dual-id; ids not fabricable. (Checked: target page, both API refs, `list_ec2` rows.)
- **Lens B/C (PassRole/STS):** NULL — no role ARN / credential-vending / token param; runs under caller identity. (API-ref param list read in full.)
- **Lens G (SSRF):** NULL — no field the service dereferences; `Description` is stored free-text (shown in Describe/console), the IDs are identifiers, not fetched URLs. (Checked target page + API ref — no `*Url`/`*Uri`/webhook/fetch field.)
- **Lens Q (upload):** NULL — no blob/file param. **Lens F/K/H/W/Y/J/FF/N/BB/CC/DD/EE/T/P/M:** NULL — no parser/LLM/KMS/attestation/transport-choice/OAuth/JWT/namespace-migration/multi-parser/upstream-context/cache/predictable-name/secret-persistence/registration/session-id surface on this single control-plane action. (Attribute set + both API refs enumerated.)
- **Lens O (audit):** partial doc-gap — no purpose-built EventBridge event for ENI attribute changes (consistent with sibling findings); CloudTrail management event is logged by default; `DescribeNetworkInterfaceAttribute`/`DescribeNetworkInterfaces` are unscopable (owned by [[using-eni-plan]]). Did the `AssociatePublicIpAddress`/`EnaSrd` modify produce a distinct, alarmable CloudTrail detail? **Open — needs live confirmation.**
- **Doc gaps to settle live:** (1) does `AssociatePublicIpAddress=true` on a non-primary ENI silently no-op or error (API says primary-only)? (2) does the `DeleteOnTermination=false` orphan carry its associated **EIP** (ride-along claimed by addressing siblings, not restated here)? (3) does the ENA-SRD modify path reach the hub's cross-tenant question? (4) does Reset re-enabling src/dest-check actually break a live routing appliance?

---

*End of plan. Nothing herein has been tested against a live AWS account; every lead is a documentation-derived hypothesis with a falsifiable oracle. The safe first oracle for all IAM-scoping leads is `iam:SimulateCustomPolicy` (no resources touched); escalate to a self-owned canary ENI only, and HARD STOP on any requester-managed / `Operator`-owned ENI.*
