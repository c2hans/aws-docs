# Amazon EC2 `RebootInstances` (and its instance-control / profile-swap chain) — Attack Research Plan

Source of leads:
- Target page: https://docs.aws.amazon.com/ec2/latest/devguide/example_ec2_RebootInstances_section.html (`.md` mirror fetched online)
- API refs: `API_RebootInstances`, `API_ReplaceIamInstanceProfileAssociation`, `API_IamInstanceProfileSpecification` (EC2 API Reference, online)
- User guide: `ec2-instance-reboot`, `iam-roles-for-amazon-ec2`
- Cross-example: `example_cross_ResilientService_section` ("Build and manage a resilient service")
- SSM: `API_SendCommand`, `AWS-RunShellScript` plugin
- Service Authorization Reference: `list_amazonec2` (actions/resources/condition keys)

**Status: documentation-derived hypotheses only. Nothing in this plan has been tested against a live AWS account.** Every lead is a claim that a boundary *might not hold*, plus the exact observation that would confirm or refute it.

---

## 0. How to use this document

- Each lead reads: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions / Cost → Severity-if-true → Stop condition.** Work in priority order (Section 5 is ordered). Look left and right for adjacent bugs the plan did not anticipate.
- **HARD STOP:** the moment evidence shows an identity / credential / ARN / account belonging to AWS's *own* service plane (not the customer's instances or roles), stop, preserve evidence, and flag for AWS-Security disclosure. Rebooting *your own* authorized test instances and reading *your own* instance's IMDS credentials is in scope; anything that reaches another account or AWS's fleet is not.
- **Scope note for the hunter:** this is a raw SigV4 EC2 Query API plus SSM/IAM. There is no CDN/edge, no JWT authorizer, no customer-supplied URL to fetch, no file upload. The high-value surface is **authorization scoping** (who may reboot / re-profile which instance) and the **profile-swap → reboot → run-as-root privilege-escalation chain**, not web-class injection.

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)

1. Reboot (or otherwise disrupt) an EC2 instance the caller does **not** own — cross-account, or cross-team within one account where the operator believes isolation exists.
2. Attach an IAM instance profile the caller could **not** otherwise pass/use, to a running instance, and obtain that role's credentials off the instance.
3. Turn `ec2:RebootInstances` + `ec2:ReplaceIamInstanceProfileAssociation` + `ssm:SendCommand` (the exact three operations the sample chains) into a **privilege-escalation path** to code execution under a higher-privileged role.
4. Demonstrate an authorization-scoping gap: a Deny/condition the operator wrote (tag-based ABAC) does not actually constrain `RebootInstances` (or a sibling state action).
5. Show a **mass-availability** impact: reboot a large set of instance IDs in one call, or repeatedly, as a cheap disruption primitive.

---

## 2. Components, Assets, and Design

**Customer-facing interface.** EC2 Query/JSON API over SigV4 at the public regional endpoint (`https://ec2.<region>.amazonaws.com`, legacy `ec2.amazonaws.com`). Reached via every SDK, the CLI (`aws ec2 reboot-instances`), and PowerShell (`Restart-EC2Instance`). Fully internet-callable; authorization is pure IAM.

**Actions in scope (from the target example + its cross-example):**
- `RebootInstances` — mutating. Input: `InstanceId.N` (array, required), `DryRun` (bool). "Asynchronous; it only queues a request to reboot." "Succeeds if the instances are valid and **belong to you**." "If an instance does not cleanly shut down within a few minutes, Amazon EC2 performs a **hard reboot**."
- `ReplaceIamInstanceProfileAssociation` — mutating. Input: `AssociationId` (required), `IamInstanceProfile` (Name **or** Arn). "Replaces an IAM instance profile for the specified **running** instance … without having to disassociate the existing … first." Doc example attaches a profile literally named `AdminProfile`/`AdminRole`.
- `DescribeIamInstanceProfileAssociations` — read, used to obtain the `AssociationId`.
- `RebootInstances` is used in the sample specifically to make the instance **pick up the newly-associated profile's credentials**.
- `ssm:SendCommand` with `DocumentName = "AWS-RunShellScript"`, `Parameters.commands = ["cd / && sudo python3 server.py 80"]` — arbitrary shell, run with `sudo` (root).

**Resources & identifier shape.**
- EC2 instance ID: `i-` + 17 hex (older 8 hex). Structured but **region/account-scoped**; not globally guessable, and the API enforces ownership (see Lens A). Appears in request body only.
- IAM instance-profile association ID: `iip-assoc-…`.
- Instance profile / role: referenced **by name** (`IamInstanceProfileSpecification.Name`) or ARN — account-local namespace.

**Identity / privilege.** SigV4 IAM principal. No session/cookie layer. The sensitive identity in play is the **IAM role delivered to the instance via its instance profile**, retrievable from IMDS (`http://169.254.169.254/latest/meta-data/iam/security-credentials/<role>`) by anything running on the box.

**Where untrusted data enters.** `RebootInstances` itself transforms nothing (no parser, no URL, no blob). The only free-form, security-relevant input in the chain is the SSM `commands` array — a raw shell string.

**Pipeline the sample implies:**
```
IAM principal (SigV4)
   │  ec2:ReplaceIamInstanceProfileAssociation (AssociationId, IamInstanceProfile.Name="<high-priv>")
   ▼
EC2 running instance ──(new profile associated)──► IMDS now vends NEW role's creds
   │  ec2:RebootInstances (InstanceId)      # ensures the box picks up the new creds
   ▼
EC2 instance back to 'running'
   │  ssm:SendCommand  AWS-RunShellScript  "sudo ..."   # runs as root on the box
   ▼
code exec on instance, holding the swapped role's IMDS credentials
```
Every arrow is a boundary (Section 3/4). The chain as a whole is the privilege-escalation lead (Lens B/E/C/T, Section 5 #1).

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Caller IAM principal | An EC2 instance in **another account** | `RebootInstances(InstanceId)` | A reboot (CloudTrail event / state change) on an instance that does not belong to the caller's account = breach. **Docs say this must fail** ("belong to you"). |
| Caller IAM principal | Another **team's** instance in the **same account** | `RebootInstances` with `Resource:"*"` grant | Reboot succeeds on an instance the operator's tag/OU model intended to isolate = intra-account footgun (lower sev, but real if ABAC was the control). |
| Caller IAM principal | An **IAM role** more privileged than the caller | `ReplaceIamInstanceProfileAssociation(IamInstanceProfile.Name)` | The service associates a profile the caller could not `iam:PassRole` → role's creds now vended to a box the caller controls = **privilege escalation**. |
| Instance's delivered role creds | Caller's shell on the box | reboot → IMDS → `SendCommand`/`sudo` | Reading `security-credentials/<role>` for a role the caller was never granted = credential exposure across the IAM boundary. |
| Caller IAM principal | Shared-fleet availability | `RebootInstances(InstanceId.N=[…many…])` | One API call degrades/forces hard-reboot across many instances = availability impact; cross-tenant only if it reaches others' instances (which ownership should prevent). |
| Any customer surface | **AWS's own service plane** | — | Any identity/credential/ARN/account belonging to AWS's fleet = **HARD STOP + disclosure**. |

---

## 4. API / Interface Inventory

| Name | Method | Mutating | Ext-facing | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| `RebootInstances` | POST (Query) | **Yes** | Yes | Queue reboot of N instances | Yes | Principals with `ec2:RebootInstances` on the instance(s) | Async; hard-reboot fallback; `DryRun` supported |
| `ReplaceIamInstanceProfileAssociation` | POST | **Yes** | Yes | Swap instance profile on a running instance | Yes | `ec2:ReplaceIamInstanceProfileAssociation` (+ `iam:PassRole`?) | Takes profile by **Name or ARN**; example uses `AdminProfile` |
| `DescribeIamInstanceProfileAssociations` | POST | No | Yes | List association IDs | Yes | `ec2:DescribeIamInstanceProfileAssociations` | Enumeration input for the swap |
| `ssm:SendCommand` (`AWS-RunShellScript`) | POST | **Yes** | Yes | Run shell as root on managed instance | Yes | `ssm:SendCommand` | `commands` = raw shell; not an EC2 API but in the chain |

**Undocumented/behavioral knobs to probe:** `DryRun` on `RebootInstances` is documented to return `DryRunOperation` (authorized) vs `UnauthorizedOperation` (not). The C++ and SAP-ABAP samples on the target page **use `DryRun` as a permission probe.** Per the skill's variant coverage, `DryRunOperation` is **caller-IAM-only — evaluated before resource resolution — NOT an ownership oracle.** Flag this explicitly (Lens A variant / Section 5 #4): a hunter must not treat a `DryRunOperation` success as proof they can reboot a *specific foreign* instance.

"Testing should focus on …" verbatim lead: the sample page itself demonstrates the profile-swap-then-reboot pattern — AWS plants the privilege-chain shape here (Section 5 #1).

---

## 5. Recommended Areas of Focus (one block per firing lens, priority-ordered)

### Area 1 — Instance-profile swap → reboot → run-as-root privilege escalation (Lens B / E / C / T) — **HIGHEST**
**Background.** The target example (and the ResilientService cross-example) chains `ReplaceIamInstanceProfileAssociation` (attach a profile *by name*) → `RebootInstances` (pick up new creds) → `ssm:SendCommand AWS-RunShellScript` (`sudo …`, i.e. root). The sample attaches a profile named `AdminProfile`/`AdminRole` in the EC2 API Reference's own example request.

**Security Concern.** `ec2:ReplaceIamInstanceProfileAssociation` **is** gated by `iam:PassRole` — `permission-to-pass-iam-roles` lists it as one of exactly four actions requiring it (alongside `AssociateIamInstanceProfile`, `DisassociateIamInstanceProfile`, `iam:PassRole`). So the chain is a **config-dependent footgun, not a service bug**: it fires precisely when the operator's `iam:PassRole` is left at `Resource:"*"` (AWS's own documented anti-pattern — *"If you specify the resource for `iam:PassRole` as `*`, this would grant access to pass any of your IAM roles to an instance"*). When PassRole is wildcard, a caller holding `ec2:ReplaceIamInstanceProfileAssociation` + `ec2:RebootInstances` + `ssm:SendCommand` can attach a **more-privileged** role to an instance they control, reboot (and/or rely on IMDS refresh) to vend its credentials, then run code **as root** (`AWS-RunShellScript` runs with root/SYSTEM per `ssm-agent-restrict-root-level-commands`) and harvest those credentials — escalating to the attached role's privileges. No single AWS page names this three-action chain; each mitigating half (scope PassRole; scope SendCommand by tag) is documented in isolation — a documentation gap worth flagging.

**High-level Test Scenarios (falsifiable claims):**
- **Claim:** the escalation fires only when `iam:PassRole` is left wildcard; a correctly scoped PassRole breaks it. → **Mechanism:** `permission-to-pass-iam-roles` (the four PassRole-gated actions + the `Resource:"*"` warning); `IamInstanceProfileSpecification` accepts an arbitrary `Name`/`Arn`; API ref example attaches `AdminProfile`. → **Oracle:** with a scoped test principal holding `ec2:ReplaceIamInstanceProfileAssociation` + `iam:PassRole` for only a *low*-priv role R, call the API attaching a *higher*-priv role's profile — expect `AccessDenied` citing PassRole (scoping holds). Repeat with `iam:PassRole: "*"` — expect `associating` success (escalation confirmed, config-dependent). → **Preconditions:** two self-owned roles (low + high), one self-owned instance; `iam:SimulatePrincipalPolicy` first (no resources touched). → **Severity:** wildcard-PassRole footgun → intra-account non-admin→admin privesc = **High/Critical** (collapses to as-designed when PassRole is scoped).
- **Claim:** The swapped credentials become retrievable from the instance after the reboot, under a principal who was never granted that role. → **Mechanism:** `iam-roles-for-amazon-ec2` — instance-profile creds are delivered via IMDS. → **Oracle:** after swap+reboot, `SendCommand` `curl …/security-credentials/<role>` returns usable creds. → **Severity:** credential exposure across IAM boundary = **High**.
- **Claim (profile-pinning condition key is unused):** `list_ec2.md` defines `ec2:NewInstanceProfile` ("the ARN of the instance profile being attached") — the key that would pin *which* profile may be attached — yet **neither** of AWS's worked example policies uses it; both scope only by instance tag + an `iam:PassRole` **role**-name prefix (e.g. `role/TestRole-*`, or even `Resource:"*"` on the EC2 side). Because `iam:PassRole` inspects the **role** name inside the profile (never the profile's own name, which is independent), a `TestRole-*`-scoped PassRole is satisfied by a profile named anything that happens to contain a role matching the prefix — AWS flags this verbatim: *"ensure that you specify the name of the IAM role and not the instance profile (if the names are different)."* → **Oracle:** policy-sim a principal holding the second AWS example (association on `Resource:"*"` + `iam:PassRole role/TestRole-*`); attach a profile `prof-alpha` containing `TestRole-Admin`; authorized = the role-name wildcard, not profile identity, is the only control. → **Severity:** High — AWS's own recommended example is easy to misapply into an escalation path. Treat as a doc/example gotcha, not a service bug.
- **Look left/right:** `AssociateIamInstanceProfile` (fresh attach) shares the same PassRole gate (Lens X parity, Area 5). Does `ec2:ModifyInstanceAttribute(userData)` reach the same escalation without **any** PassRole at all (confirmed exemplar — enumerate it as an adjacent lead)?

**Doc evidence:** `API_ReplaceIamInstanceProfileAssociation` example (`AdminProfile`); ResilientService chain; `iam-roles-for-amazon-ec2`. **Severity-if-true:** High. **Stop condition:** confirm the role's creds are readable once; do not use them to touch further resources.

### Area 2 — Authorization scoping of `RebootInstances`: resource-level & condition-key enforcement (Lens S / A intra-account)
**Background.** `RebootInstances` is mutating and internet-callable; the only control is IAM. Many operators scope instance control with tag-based (ABAC) policies.

**Security Concern.** If `ec2:RebootInstances` cannot be scoped to a resource ARN, or the tag/condition the operator keyed on is ignored / wrong-cased / non-existent, a principal intended to manage only its own instances can reboot any instance in the account.

**Confirmed baseline (do not re-test as a bug).** `ec2:RebootInstances` **does** support resource-level permissions: `list_ec2.md` marks `instance*` as its (sole, required) resource type with ~21 condition keys — `aws:ResourceTag/${TagKey}`, `ec2:ResourceTag/${TagKey}`, `ec2:Region`, `ec2:InstanceType`, `ec2:InstanceProfile`, `ec2:Tenancy`, `ec2:MetadataHttpTokens`, `ec2:ProductCode`, etc. So a correctly-scoped reboot grant is achievable; the live question is whether operators' ABAC conditions actually bind ownership.

**High-level Test Scenarios:**
- **Claim (ABAC = presence, not ownership):** AWS's canonical instance-state ABAC example allows the action on `instance/*` keyed only on `StringEquals aws:ResourceTag/<k>:<v>` — "belong to the specified **account**," not the specific user. Any same-account instance carrying the tag qualifies. If tag-write (`ec2:CreateTags`/`DeleteTags`) is not *separately* denied, a caller can tag a victim's instance into scope, then reboot it. → **Mechanism:** `ExamplePolicies_EC2.md` + the `iam-policies-for-amazon-ec2` warning: *"you must consider explicitly denying users the ability to add those tags… Otherwise, it's possible for a user to circumvent your restrictions."* → **Oracle:** policy-sim/`DryRun` the operator's real policy against a foreign-but-same-account instance the caller can tag; an ALLOW after self-tagging = gap. → **Severity:** High where ABAC is the isolation control and tag-write isn't locked.
- **Claim (case-sensitivity fail-open):** condition-key **names** are case-insensitive but tag **values** and tag **keys** are case-sensitive, so a Deny written `aws:ResourceTag/Purpose:test` is inert against an instance tagged `purpose=test`. → **Mechanism:** `Using_Tags.md` ("Tag keys and values are case-sensitive"), `supported-iam-actions-tagging` (use `aws:TagKeys` to enforce key case). → **Oracle:** create instances tagged `Purpose=test` vs `purpose=test` vs `purpose=Test`; test Allow and Deny `StringEquals` policies against each; record which direction fails open. A fail-open **Deny** is the dangerous one. → **Severity:** Medium.
- **Claim (enumeration oracle):** reboot of a non-existent vs not-owned instance returns distinguishable errors (`InvalidInstanceID.NotFound` vs other). → **Oracle:** compare error codes/latency for fabricated vs real-but-foreign IDs. → **Severity:** Low.

**Doc evidence:** `list_ec2.md` (action row + condition keys); `ExamplePolicies_EC2.md`; `iam-policies-for-amazon-ec2`; `Using_Tags.md`; `supported-iam-actions-tagging`. **Note for the hunter:** fetch the **`.md`** variant of `list_ec2` — the `.html` authorization tables are JS-rendered and return empty to a plain fetch. **Severity-if-true:** Medium (High if ABAC-gated). **Stop:** one policy-sim ALLOW demonstrating the gap.

### Area 3 — Reboot as an availability / integrity primitive (Lens L, with Lens O)
**Background.** `InstanceId.N` is an **array** — one call targets many instances. Reboot "only queues a request"; if the OS doesn't shut down cleanly within minutes, EC2 performs a **hard reboot** (risking an unstable state, esp. mid-update per the docs' Important note).

**Security Concern.** A principal with over-broad `ec2:RebootInstances` can cheaply disrupt a large fleet (mass reboot / repeated reboot / hard-reboot into an unstable state during updates). No data is exfiltrated, so this is availability, not confidentiality — but it is a real blast-radius concern where the grant is wildcard.

**High-level Test Scenarios:**
- **Claim:** one `RebootInstances` call with a large `InstanceId.N` list reboots all of them with no per-instance rate/consent gate. → **Oracle:** CloudTrail shows N reboot events from one request against self-owned test instances. → **Severity:** single-tenant self-DoS = out-of-scope/Low; **cross-tenant only if ownership is bypassable (see Area 2) → then High**.
- **Claim (Lens O):** a hard reboot vs clean reboot, or a reboot during an update window, leaves a weaker/ambiguous audit trail. → **Oracle:** compare CloudTrail records; note that docs promise "CloudTrail creates an API record of when your instance was rebooted." → **Severity:** Informational enabler.

**Doc evidence:** `API_RebootInstances` (async, hard-reboot); `ec2-instance-reboot` (Important note, CloudTrail promise). **Severity-if-true:** self-DoS Low / cross-tenant High. **Stop:** demonstrate on self-owned instances only.

### Area 4 — `DryRun` as a false-positive authorization oracle (Lens A variant — trap to document, not a bug)
**Background.** The C++ and SAP-ABAP samples on the target page use `DryRun=true` and treat `DryRunOperation` as "you have permission to reboot this instance."

**Security Concern (for the hunter, not the service).** `DryRun` is evaluated on **caller IAM before resource resolution/ownership**. A `DryRunOperation` result proves the caller's *identity policy* allows the action — **not** that a *specific foreign* instance is reachable/ownable. A hunter who treats a DryRun success as an IDOR confirmation will log a false positive.

**High-level Test Scenario:**
- **Claim:** `DryRun=true` against a foreign instance ID returns `DryRunOperation` even though a real reboot would fail ownership. → **Oracle:** compare `DryRun` result vs real-call result for a known not-owned ID. If DryRun says "authorized" but the real call is denied on ownership, the oracle is confirmed misleading. → **Severity:** N/A (methodology guardrail); document so Area 2's IDOR testing uses the **real** call, not DryRun, as the ownership oracle.

**Doc evidence:** `API_RebootInstances` DryRun semantics; C++/SAP-ABAP samples. **Severity:** Informational.

### Area 5 — Action-family authorization parity (Lens X)
**Background.** `RebootInstances` is one of a family: `StartInstances`, `StopInstances`, `TerminateInstances`, plus the two instance-profile actions (`ReplaceIamInstanceProfileAssociation` vs `AssociateIamInstanceProfile` vs `DisassociateIamInstanceProfile`).

**Security Concern.** One action in a family may enforce resource-level/condition scoping while a sibling does not, or `ReplaceIamInstanceProfileAssociation` and `AssociateIamInstanceProfile` may differ in PassRole strictness — a caller blocked on one reaches the same effect via the other.

**Confirmed asymmetry (from `list_ec2.md` condition-key rows):** the four lifecycle actions are **not** condition-key-symmetric. `RebootInstances` and `TerminateInstances` carry `ec2:ProductCode`, `ec2:InstanceAutoRecovery`, and `ec2:InstanceMetadataTags`; **`StopInstances` lacks `ec2:ProductCode`**; **`StartInstances` lacks all three** (`ec2:ProductCode`, `ec2:InstanceAutoRecovery`, `ec2:InstanceMetadataTags`) and uniquely adds the `group` and `license-configuration` resource types. AWS's own example policies group these four actions together without flagging the asymmetry.

**High-level Test Scenarios:**
- **Claim:** an org-wide gate keyed on `ec2:ProductCode` (e.g. "deny lifecycle ops on paid-marketplace AMIs") intended to cover reboot/start/stop/terminate uniformly silently **fails to constrain** `StartInstances`/`StopInstances`, which don't honor that key. → **Mechanism:** `list_ec2.md` rows (ProductCode present for Reboot/Terminate, absent for Start/Stop) + the `iam-policies-for-amazon-ec2` "Important" box on `...IfExists` semantics for multi-action statements. → **Oracle:** write one `Action:[Terminate,Stop]` + `ec2:ProductCode` condition statement; confirm it constrains Terminate but not Stop. → **Severity:** Medium (silent coverage gap).
- **Claim:** `AssociateIamInstanceProfile` (fresh attach) and `ReplaceIamInstanceProfileAssociation` share the same `iam:PassRole` gate, so both are routes to the Area 1 privesc; neither is independently stricter. → **Mechanism:** `permission-to-pass-iam-roles` lists both. → **Oracle:** policy-sim both against the same high-priv profile. → **Severity:** High (second route to Area 1 privesc).

**Doc evidence:** `list_ec2.md` action/condition-key rows; `permission-to-pass-iam-roles`; `API_AssociateIamInstanceProfile`. **Severity-if-true:** Medium–High.

### Area 6 — SSM `AWS-RunShellScript` command surface (Lens K / command-injection) — in-chain, lower standalone priority
**Background.** The sample's final step runs `AWS-RunShellScript` with a `commands` array containing a raw shell string executed as root.

**Security Concern.** `commands` is free-form shell with **no AWS-side sanitization** (`API_SendCommand`: "String to array of strings map"). AWS's own plugin reference admits parameter interpolation is executable absent the opt-in `interpolationType` ("treating parameter inputs as string literals rather than **potentially executable commands**"). And `AWS-RunShellScript` runs with **root (Linux) / SYSTEM (Windows)** — `ssm-agent-restrict-root-level-commands` states plainly: *"any trusted entity that has been granted permission to send commands to SSM Agent has root or SYSTEM permissions."* So any wrapper/automation (like the sample) that builds `commands` from caller- or data-controlled input (instance ID, profile name, a parameter read from SSM/DynamoDB) is a root-RCE command-injection sink. The sample hardcodes its command (safe), but it is the template others copy.

**High-level Test Scenario:**
- **Claim:** a downstream tool that interpolates untrusted input into the `commands` string yields root RCE on the managed instance. → **Mechanism:** `AWS-RunShellScript` runs as root; `commands` unparsed. → **Oracle:** in a derived/customer tool, an input containing `; id` executes. → **Severity:** High (root on the box), but owner-to-fix is the **customer's** copied code, not AWS — note scope.
- **Guardrail:** `ssm:SendCommand` itself is the authorization gate; confirm whether it can be scoped per-instance by tag (parity with Area 2). Reaching another account's managed instance via SendCommand would be a cross-boundary breach (HARD-STOP check).

**Doc evidence:** `API_SendCommand`, `AWS-RunShellScript` plugin, sample `commands` payload. **Severity-if-true:** High (customer-owned fix for the injection; AWS-owned for any cross-account SendCommand).

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Reboot a foreign-account instance | `RebootInstances` | "succeeds if the instances … belong to you" — attack the ownership check (prove it's not just an existence check) |
| Attach a more-privileged profile | `ReplaceIamInstanceProfileAssociation` | `iam:PassRole` + `PassedToService` scoping — prove it's missing/wildcard |
| Harvest swapped role creds | IMDS + reboot | instance-profile cred delivery — prove creds readable by a principal never granted the role |
| ABAC tag scope on reboot | IAM condition keys | `ec2:ResourceTag/*` — prove case-sensitivity / ignored-key fail-open |
| Mass/hard reboot disruption | `RebootInstances` array + hard-reboot | no documented per-call fleet cap — prove blast radius on self-owned instances |
| Family parity gap | Start/Stop/Terminate, Associate vs Replace | per-action condition-key rows — prove the weaker sibling |
| DryRun misread as ownership oracle | `DryRun` | caller-IAM-only evaluation — document, don't false-positive |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **Rebooting the caller's own instances / single-tenant self-DoS** — not a vulnerability; only cross-ownership reboot is in scope.
- **Reading the caller's own instance's IMDS credentials** — expected behavior; the finding is *cross-privilege* reach (a role the caller was never granted), not IMDS access per se.
- **Command injection in a customer's own copied wrapper** around `AWS-RunShellScript` — customer-owned defect (note it, don't file against AWS) unless it reaches another account's instance.
- **AWS's own fleet / service plane** — HARD STOP + disclosure; never exploit.
- **Third-party reference repos** (the aws-doc-sdk-examples code) — report quality issues upstream, not as AWS service vulns, except where a sample demonstrates an AWS-side authorization gap.

---

## 8. Null hypotheses / doc gaps (lenses checked that did not fire)

- **Lens G (SSRF) — N/A.** Read `API_RebootInstances`, `API_ReplaceIamInstanceProfileAssociation`, `IamInstanceProfileSpecification`: no field the service dereferences as a URL/host. No server-side fetch.
- **Lens Q (upload) — N/A.** No blob/file/image field in any action in the chain.
- **Lens F (translation/parser injection) — N/A for reboot.** `RebootInstances` parses only an instance-ID array (format-validated). The only free-form transform is SSM `commands` (covered under Lens K, Area 6).
- **Lens H (KMS / encryption context) — N/A.** No key/encryption-context parameter in these actions.
- **Lens W (attestation), BB (canonicalization), CC (upstream-context), DD (cache-key), FF (JWT/token) — N/A.** These are edge/CDN/authorizer/token shapes; this is a raw SigV4 Query API with no such layer. Checked the API refs and target page.
- **Lens EE (predictable-name land-grab) — weak/N/A.** `IamInstanceProfile.Name` is resolved in the **caller's own account** (account-local namespace), not a global/first-come namespace; no cross-account name-squat. Noted for completeness.
- **Lens A cross-*account* IDOR — likely a genuine null** ("belong to you" ownership is documented and historically enforced), but **confirm with the real (non-DryRun) call**, and the embedded-structure instance ID is not fabricable cross-account. The *intra-account* wildcard footgun (Area 2) is the live part.
- **~~Doc-gap~~ RESOLVED:** `ReplaceIamInstanceProfileAssociation` **does** require `iam:PassRole` — `permission-to-pass-iam-roles` lists it as one of four PassRole-gated actions (with `AssociateIamInstanceProfile`, `DisassociateIamInstanceProfile`). Area 1 is live as a *config-dependent* footgun (wildcard PassRole), not a service bug.
- **Remaining doc-gap (needs live test):** whether the sample's `RebootInstances` step is *load-bearing* for IMDS to vend the swapped profile's credentials, or merely restarts the demo web server. AWS documents IMDS eventual-consistency only for the "remove role from profile" path, not for `ReplaceIamInstanceProfileAssociation`. Confirm with a curl of `security-credentials/<role>` before vs after reboot. Does not change Area 1's severity (code-exec harvests creds either way), only the *mechanism narrative*.

---

*This plan claims no bug exists; it names the boundaries that might not hold and the exact observation that settles each. A clean run against any area is a valid negative result.*
