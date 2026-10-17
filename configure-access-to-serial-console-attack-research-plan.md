# EC2 Serial Console — *Configure Access* — Attack Research Plan

**Target page:** https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configure-access-to-serial-console.html
(mirror: `/work/aws-docs/docs/AWSEC2/latest/UserGuide/configure-access-to-serial-console.md`)
**Source of leads:** the target page + its API/IAM references (`API_EnableSerialConsoleAccess`, `API_DisableSerialConsoleAccess`, `API_GetSerialConsoleAccessStatus`, `API_SendSerialConsoleSSHPublicKey`), the Service Authorization Reference (`list_ec2.md`, `list_ec2-instance-connect.md`), the SAC troubleshooting page, and the AWS-authored SSM runbook `AWSSupport-EnableWindowsEC2SerialConsole`. **Status: documentation-derived hypotheses only — nothing has been tested against a live account.**

**Scope of THIS plan.** This plan is scoped to the *access-control / IAM-configuration surface* that the **configure-access** page uniquely defines: the four-tier access model (Organization SCP → Instance → User → OS), the three AWS-authored sample IAM policies, the account-level enable/disable toggle, the ABAC resource-tag example, and the OS-user password gate. The *connect/session* surface and the *prerequisites/boot* surface are covered by two sibling plans already in this directory — **do not duplicate them; chain into them:**
- `ec2-serial-console-attack-research-plan.md` — connect path, shared fleet, browser `oneclickv2-proxy`, session lifecycle.
- `ec2-serial-console-prerequisites-attack-research-plan.md` — boot-time credential disclosure, GRUB single-user, SysRq, host-key MITM.

---

## 0. How to use this document
- Each lead is: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition.** Work in priority order; look left and right for adjacent bugs.
- Most "serial console risk" is **customer-config footgun** (weak root password, account toggle flipped broadly). This plan deliberately separates those from the **AWS-service-owned** boundaries and the **AWS-authored uneditable artifacts** (Lens R/S) that are genuinely reportable.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's own serial-console service fleet (`serial-console.ec2-instance-connect.<region>.aws`, `ec2-serial-console.<region>.api.aws`, `prod.<region>.oneclickv2-proxy.ec2.aws.dev`), **stop, preserve evidence, flag for AWS-Security disclosure.** The multi-tenant fleet is AWS's responsibility, not a customer resource.
- ⚠️ **Suspected prompt-injection note:** none of the fetched doc text attempted to instruct the agent. All content treated as data.

---

## 1. Pentest Objectives (boundary-breach goals, as concrete outcomes)
1. Obtain an interactive serial-console session (or push a key) to an EC2 instance the caller is **not** IAM-authorized for — same account (cross-team) or, higher value, **cross-account**.
2. Flip the **account-wide** serial-console switch (`EnableSerialConsoleAccess`) with a principal the operator believed was scoped to a narrow role → silently expose *every* instance in the account/region.
3. Defeat an **instance-scoped** or **ABAC tag-scoped** serial-console IAM policy (reach an instance the `Resource`/`Condition` was meant to exclude), e.g. by self-tagging, tag-key-presence matching, or naming the instance a second way.
4. Demonstrate that the documented access-control story ("restrict access to specific instances", "admin-equivalent on Windows") is **advisory-only** at a layer IAM does not reach (the OS login, the SAC pre-auth command set, the IAM-free SSH session).
5. Show an **AWS-authored artifact** (sample policy, or the `AWSSupport-EnableWindowsEC2SerialConsole` runbook's required-permissions policy) grants more than its description implies — intra-account privesc or broad `PassRole`.
6. Enumerate instance existence / type across a trust boundary via the API error taxonomy.

---

## 2. Components, Assets, and Design

**Customer-facing interface (control-plane, IAM-gated):**
- `ec2:EnableSerialConsoleAccess` / `ec2:DisableSerialConsoleAccess` / `ec2:GetSerialConsoleAccessStatus` — **account-wide, per-Region** toggle + status. All three: **no condition keys, no resource-level permissions, `Resource` must be `*`** (confirmed in `list_ec2.md`: each action's "Condition key:" and "Possible value(s):" rows are empty).
- `ec2-instance-connect:SendSerialConsoleSSHPublicKey` — pushes a 60-second SSH public key. **Resource type `instance*`** (`arn:${Partition}:ec2:${Region}:${Account}:instance/${InstanceId}`); **condition keys only `aws:ResourceTag/${TagKey}` + `ec2:ResourceTag/${TagKey}`** — notably **NO `ec2:osuser`** (contrast `SendSSHPublicKey`, which has it).

**Data-plane interface (NOT IAM-gated — see sibling plans):** SSH to `serial-console.ec2-instance-connect.<region>.aws` username `<instance-id>.port0`; browser WebSocket to `prod.<region>.oneclickv2-proxy.ec2.aws.dev:443`.

**The four documented access tiers (the page's core model):**
| Tier | Control | Enforced by |
|---|---|---|
| Organization | SCP / **declarative policy** allowing the account toggle | AWS Organizations; `ManagedBy=declarative-policy` locks the account from self-modifying |
| Instance | IAM `Resource` = instance ARN, or `ec2:ResourceTag` ABAC | IAM authorizer on the key-push |
| User | IAM allow/deny `SendSerialConsoleSSHPublicKey` per principal | IAM authorizer on the key-push |
| OS | Linux password-based OS user (any user incl. root); Windows SAC | **OS / SAC only — IAM does not reach here** |

**Assets:** the account-wide access flag (per Region); every running Nitro instance's `ttyS0`/`COM1`; OS credentials typed at the serial login; the AWS multi-tenant serial-console fleet (hard-stop zone).

**Identity & key facts:**
- InstanceId pattern `^i-[a-f0-9]+$`, len 10–32 (carries an embedded value; not freely fabricable cross-account).
- SSH key lives 60 s; 1 session/instance; 30 s teardown; session persists past IAM-credential expiry; max ~1 h.
- **Windows: "Granting serial console permissions is equivalent to granting admin-level privileges on the instance."** SAC out-of-band commands (`restart`, `shutdown`, `crashdump`, `i` network-reconfig, `k/l/r/m` process control, `t/d/id`) **require no sign-in**; only the `cmd` channel needs OS admin creds.

**ASCII pipeline:**
```
                         ┌─ ORG tier: SCP / declarative policy ─┐
                         │   (can lock account; ManagedBy=...)  │
caller (IAM principal) ──┤                                      │
   │ ec2:EnableSerialConsoleAccess (Resource:* , no conditions) │ ──► ACCOUNT-WIDE flag (per Region)
   │ ec2:GetSerialConsoleAccessStatus                           │
   │                                                            │
   │ ec2-instance-connect:SendSerialConsoleSSHPublicKey         │
   │   (Resource: instance ARN; ec2:ResourceTag only; 60s key)  │
   ▼                                                            ▼
[IAM authorizer] ──authz on INSTANCE ARN──► push key to instance's serial port
   │                                                            │
   │  === IAM BOUNDARY ENDS HERE (documented) ===               │
   ▼                                                            ▼
SSH to serial-console.ec2-instance-connect.<region>.aws  (username i-….port0)
   │  "not subject to the IAM policies"  — authz = private key + username only
   ▼
OS login prompt  ──►  Linux: any password OS user (incl. root)  |  Windows SAC: pre-auth cmd set + cmd(admin)
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Narrowly-scoped IAM principal | Account-wide serial flag (all instances, the Region) | `ec2:EnableSerialConsoleAccess` — unscopable (`Resource:*`, no conditions) | Flag flips to `enabled` from a principal the operator believed couldn't widen exposure → every Nitro instance now reachable |
| IAM principal scoped to instance set A | Instance set B (same account) | `SendSerialConsoleSSHPublicKey` push + ABAC/tag or resource-pattern evasion | Push returns `Success:true` (or a session opens) for an instance the policy's `Resource`/`Condition` meant to exclude |
| IAM principal in account X | Instance in account Y | key-push authz on instance ARN (ARN embeds account) | Any push/session success against a foreign-account instance = **cross-account breach (Critical)** |
| IAM-authorized caller (push only) | OS identity on the box | OS password / SAC; **`ec2:osuser` absent for serial** | Logging in as root / any OS user the IAM policy never named; on Windows, running SAC admin commands |
| Holder of narrow serial IAM only | Admin on the instance | Windows SAC "admin-equivalent"; Linux GRUB/SysRq (→ prereq sibling) | Admin-level control from a permission whose description implies troubleshooting-only |
| Principal holding ONLY an AWS sample/runbook policy | Higher privilege / broad action | Lens R/S audit of the AWS-authored JSON | `SimulatePrincipalPolicy` shows the artifact alone authorizes an action its description disclaims (e.g. `PassRole` to any role) |
| Any customer surface | AWS serial-console fleet (`*.aws`, `*.api.aws`, `oneclickv2-proxy`) | shared multi-tenant service | **HARD STOP** — any fleet identity/credential/cross-tenant reach → disclosure |

---

## 4. API / Interface Inventory

| Name | Method | Mutating? | Internet-callable? | Authorized callers | Resource scoping | Conditions | Notes |
|---|---|---|---|---|---|---|---|
| `ec2:EnableSerialConsoleAccess` | POST (EC2 query) | **Yes — account-wide** | Yes | IAM principal w/ action | **`*` only** | **none** | Supports `DryRun`. Blast radius = whole account/Region. No way to scope to a subset. |
| `ec2:DisableSerialConsoleAccess` | POST | Yes — account-wide | Yes | IAM principal w/ action | `*` only | none | Availability lever (disable to lock out legit responders). |
| `ec2:GetSerialConsoleAccessStatus` | GET | No | Yes | IAM principal w/ action | `*` only | none | Returns `ManagedBy` (`account`\|`declarative-policy`) + `serialConsoleAccessEnabled`. `DryRun`. |
| `ec2-instance-connect:SendSerialConsoleSSHPublicKey` | POST (JSON) | Yes (pushes key) | Yes | IAM principal w/ action on instance ARN | instance ARN | `aws:ResourceTag`, `ec2:ResourceTag` — **no `ec2:osuser`** | Body: `InstanceId` (`^i-[a-f0-9]+$`), `SerialPort` (fixed 0), `SSHPublicKey` (80–4096). Rich error taxonomy (→ Lens A oracle). |
| `AWSSupport-EnableWindowsEC2SerialConsole` | SSM Automation | Yes (BCD edits + reboot) | via SSM | runbook invoker or `AutomationAssumeRole` | mixed (see Lens R) | mixed | **AWS-authored artifact.** Only *checks* account flag (`GetSerialConsoleAccessStatus`), does not flip it. Persistent `bcdedit /ems on`. |

**Undocumented/hidden-knob sweep:** `SerialPort` accepts only fixed `0` (nothing to widen). No console-hidden auth-weakening enum found on these APIs. The genuinely under-surfaced facts are *negative*: the three account-toggle actions silently support **zero** condition keys, and the serial push silently **drops** `ec2:osuser` — both are "the knob you'd want to scope with does not exist," which is itself the lead (Lens U/S).

---

## 5. Recommended Areas of Focus (priority order)

### Area 1 — Account-wide toggle is unscopable & sticky — Lens E / U / S  [TOP PRIORITY, customer-impacting + AWS-design]
**Background:** `EnableSerialConsoleAccess`/`Disable`/`GetStatus` support **no condition keys and no resource-level permissions** — `Resource` must be `*` (the page says so for the describe/status trio; `list_ec2.md` confirms empty condition rows for all three). The sample "manage account access" policy grants all three on `Resource:"*"`.
**Security Concern:** any principal holding `ec2:EnableSerialConsoleAccess` flips serial access **for the entire account in that Region** — there is no "enable for these instances only." An operator cannot express "this role may manage serial access but only for dev instances." Combined with the key-push, enabling the flag is the precondition that turns every Nitro instance into a serial-reachable box that **bypasses SG/NACL** ("does not use the instance security group or the subnet network ACL").
**High-level Test Scenarios (falsifiable claims):**
- *Claim:* a principal granted only the docs' "manage account access" policy can flip the account-wide flag with no ability for the operator to scope it. → *Oracle:* `aws ec2 enable-serial-console-access` returns `SerialConsoleAccessEnabled:true` under that scoped role; `SimulateCustomPolicy` shows no condition could have narrowed it. → *Severity:* Medium (account-wide exposure amplifier; customer-inflicted but **the unscopability is AWS-owned**).
- *Claim:* a declarative-policy lock (`ManagedBy=declarative-policy`) cannot be overridden from within the account. → *Oracle:* with a declarative policy set, `EnableSerialConsoleAccess` from the account fails / status shows `declarative-policy`. Refute = account-level call silently wins. → Integrity-of-control test (Lens U).
**Preconditions:** a role holding the account-mgmt action. **Cost:** 1 API call (reversible — disable after). **Stop:** once the flag flips.

### Area 2 — The three AWS-authored sample policies + the runbook policy — Lens R / S  [HIGH, reportable if weak]
**Background:** the page prints **three** copy-verbatim IAM policies (manage-account-access; explicit-allow-instance; explicit-deny; tag-ABAC) and the Windows runbook ships a "Required IAM permissions" policy. These are AWS-authored artifacts the customer attaches as-is → a weak default is AWS's defect, not a footgun.
**Security Concern / statement-by-statement questions:**
- The **explicit-deny** sample relies on Allow-`*` + Deny-one-instance. *Claim:* the Deny is **case-/ARN-form-sensitive** or can be out-voted by a second Allow → an instance the author meant to deny is still reachable. → *Oracle:* `SimulatePrincipalPolicy` for `SendSerialConsoleSSHPublicKey` on the denied instance ARN variants (different casing/partition/`instance/*`) returns `allowed`.
- The **ABAC** sample keys on `aws:ResourceTag/SerialConsole == aws:PrincipalTag/SerialConsole`. *Claim:* it fails open if the tag is **absent** on an instance, or the holder can **self-set** the matching tag (via `ec2:CreateTags`) to self-authorize. → *Oracle:* instance with no `SerialConsole` tag → does the StringEquals deny (good) or a looser variant allow? And: can the scoped role call `CreateTags` to stamp a matching value, then push? (chains to Lens I/S — see Area 4).
- **Runbook `AWSSupport-EnableWindowsEC2SerialConsole`:** its required policy contains **`iam:PassRole` on `Resource:"*"` gated only by `iam:PassedToService ∈ {ssm,ec2}.amazonaws.com`** — any role, scoped only by destination service, not by role name/path. *Claim:* a principal holding the runbook's policy can pass a **high-privilege** role to ssm/ec2 and have the automation act with it. → *Oracle:* `SimulatePrincipalPolicy` confirms `PassRole` on an admin-ish role to `ssm.amazonaws.com` is `allowed` under the artifact. Also: `HelperInstanceProfileName` auto-creation — *what role does the auto-created profile receive, and who can reuse it after?*
- *Severity:* non-admin→broad-action = **High**; cross-workload reach = Medium–High. **Reportable (Tier 2, route `aws-security`)** because the artifacts are AWS-authored/uneditable.
**Move:** resolve each printed JSON; audit with `iam:SimulatePrincipalPolicy`/`SimulateCustomPolicy` first (no resources touched); escalate to a scoped live call only with canary data.

### Area 3 — `ec2:osuser` gap → OS-user least-privilege is unexpressible — Lens U / X  [HIGH, AWS-design gap]
**Background:** `SendSSHPublicKey` (standard EC2 Instance Connect) supports the **`ec2:osuser`** condition key and a required `InstanceOSUser` param; **`SendSerialConsoleSSHPublicKey` has neither** (confirmed `list_ec2-instance-connect.md`; the serial API request body is only `InstanceId`/`SerialPort`/`SSHPublicKey`). The page then says the OS user is chosen *at the login prompt*, and you may set a password for *any* user "including the root user."
**Security Concern:** IAM **cannot** restrict which OS user a serial-console principal logs in as. A principal authorized to push a serial key to an instance can attempt OS login as **any** password-configured user, including root — the one control that exists for standard Instance Connect is absent here. This is the sibling-parity shape (Lens X): two actions in one family, one isolation-checkable, the twin not.
**Test Scenarios:**
- *Claim:* no IAM policy can constrain the serial-console login to a non-root OS user. → *Oracle:* enumerate the full condition-key set for `SendSerialConsoleSSHPublicKey`; confirm no `osuser`/user key exists; demonstrate a push + root login where `SendSSHPublicKey` would have denied root via `ec2:osuser`. → *Severity:* High where root has a password; the gap is **AWS-owned and uncloseable by the customer**.
- *Windows variant:* "serial console permission ≈ admin." → trace to SAC: the no-sign-in command set (shutdown/crashdump/network-reconfig/process-kill) is reachable with only the push permission. → *Oracle:* SAC `SAC>` responds to `t`/`d`/`restart` without OS auth.

### Area 4 — ABAC resource-tag self-widening — Lens I / S  [MEDIUM–HIGH]
**Background:** the tag-ABAC sample grants serial push when `aws:ResourceTag/SerialConsole` equals the caller's `aws:PrincipalTag/SerialConsole`.
**Security Concern:** ABAC is only as strong as who controls the tags. If the scoped role also holds `ec2:CreateTags` (common, and *not* denied in the sample), it can stamp its own `SerialConsole=<value>` on an arbitrary instance to self-authorize; if the principal can influence its own `aws:PrincipalTag` (via a session tag on `AssumeRole` / SAML attribute), it widens from the other side.
**Test Scenarios:**
- *Claim:* a holder of the ABAC policy + `CreateTags` can self-authorize serial access to any instance by tagging it. → *Oracle:* under the scoped role, `CreateTags SerialConsole=foo` on a target, then `SendSerialConsoleSSHPublicKey` → `Success:true`. Refute = `CreateTags` denied or tag-on-push re-evaluation blocks it.
- *Claim:* session-tag injection sets `aws:PrincipalTag/SerialConsole` to match a target. → *Oracle:* `AssumeRole --tags Key=SerialConsole,Value=<target's value>` then push. → *Severity:* High where ABAC *is* the access-control mechanism.
- Variant (Lens S): does the StringEquals **fail open on an absent tag**? Test an instance with no `SerialConsole` tag.

### Area 5 — Instance-level IDOR & enumeration oracle — Lens A  [MEDIUM–HIGH; cross-account = Critical]
**Background:** `SendSerialConsoleSSHPublicKey` authorizes against the instance ARN (account-embedded). Error taxonomy is rich: `AuthException` (creds-OR-no-access, deliberately conflated), `EC2InstanceNotFoundException`, `EC2InstanceStateInvalidException`, `EC2InstanceTypeInvalidException` ("Only Nitro…"), `SerialConsoleAccessDisabledException`.
**Security Concern:** AWS conflated `AuthException` on purpose, **but** Not-Found vs Auth vs TypeInvalid still differ. For a caller holding broad `Resource:"*"` (the docs' own un-scoped examples), the Not-Found/Type/State split leaks **existence and instance-type family** of instances the policy covers — and whether the split survives across accounts is undocumented.
**Test Scenarios:**
- *Claim (same-account):* a `Resource:"*"` holder can enumerate which instance IDs exist / are Nitro via the error differential. → *Oracle:* probe known-good vs random valid-format IDs → distinct exceptions.
- *Claim (cross-account, high value):* a foreign instance ID yields anything other than a uniform `AuthException`. → *Oracle:* push to an out-of-account instance ID; **any** Not-Found/Type/State leakage = cross-tenant enumeration (Medium); a `Success` = **Critical + hard-stop-adjacent**. → *Preconditions:* a valid foreign instance ID (hard to fabricate — IDs embed non-sequential value). **Stop** at first cross-account signal; preserve evidence.

### Area 6 — Session persistence vs credential revocation; disable-as-lockout — Lens C / AA / L  [MEDIUM]
**Background:** "The duration of the connection is not determined by the duration of your IAM credentials… the connection continues to persist until the maximum duration… is reached." One session/instance; 30 s teardown.
**Security Concern:** revoking/expiring the IAM principal does **not** kill a live serial session (no documented admin kill-switch beyond `Disable` at account scope). Conversely `DisableSerialConsoleAccess` is an availability lever (lock out incident responders). Single-session + push-to-contend enables a **console-slot DoS / slot-seizure race** (push repeatedly to hold `SerialConsoleSessionLimitExceededException` against a legit holder, or win the slot right after the 30 s teardown).
**Test Scenarios:** revoke the pushing principal's creds mid-session → session survives? (Lens C). Disable account access → does it terminate existing sessions or only block new ones? Race the teardown window (Lens L/M). → *Severity:* Medium (single-tenant availability / stale access); the revocation-completeness gap is AWS-owned.

### Area 7 — Windows SAC persistent weakening & default-on drift — Lens U / R  [MEDIUM]
**Background:** the runbook's `EnableSACAndBootMenu` writes persistent `bcdedit /ems on` + boot-menu edits and reboots; SAC's no-sign-in command set then persists. Subagent noted SAC is **enabled by default** on some Windows Server 2019 AMIs from version `2026.09.09`. Enabling SAC also **breaks EC2-console password retrieval** ("services that rely on password retrieval will not work"), nudging operators toward the serial channel.
**Security Concern:** running the AWS-authored runbook durably moves a Windows instance into the "serial permission ≈ admin" posture and makes it harder to recover the normal password path. Default-on AMIs mean the admin-equivalent exposure can exist without an explicit opt-in.
**Test Scenarios:** confirm the BCD state survives reboot and is only reversible by the explicit disable procedure; verify which AMIs ship SAC-on by default; assess whether the password-retrieval breakage is a documented, intended trade-off. → *Severity:* Medium (persistent exposure posture; largely by-design but under-communicated).

### Area 8 — IAM-free SSH session & fingerprint TOFU (chain to siblings) — Lens U / M / Y  [HIGH — but owned by sibling plan]
**Background:** "After pushing the SSH key… the SSH connection is **not subject to the IAM policies**." Fingerprint check is "(Optional)", shown once; endpoints under AWS-controlled `.aws`/`.api.aws`/`.aws.dev` gTLDs.
**Security Concern:** the entire SSH-session authorization reduces to *possession of the 60 s private key + the `i-….port0` username*; whether the fleet rejects a key pushed for instance X when presented with username `Y.port0` is **undocumented** (candidate confused-deputy). Optional TOFU fingerprint → MITM if skipped.
**Action:** **do not re-derive here** — this is developed in `ec2-serial-console-attack-research-plan.md` (Areas 1–4). Cross-link and carry forward the finding that the *configure-access* page is where AWS asserts the IAM boundary that the connect page then explicitly ends. Treat the undocumented cross-instance username binding as a **doc-gap hypothesis** for a live, authorized test — and a **HARD STOP** if any cross-tenant reach appears.

---

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| Narrow role flips account-wide serial flag | `EnableSerialConsoleAccess` | "configured at the account level … in each Region" — but **no condition keys / no resource scoping** exist to narrow it |
| Explicit-deny sample out-voted / ARN-form bypass | sample IAM policy | "explicitly denies access … of a specific instance" |
| ABAC self-authorization via `CreateTags` / session tag | tag-ABAC sample | `StringEquals aws:ResourceTag == aws:PrincipalTag` |
| Serial login as root despite scoped IAM | OS tier | "set the password for any OS user, including the root user" + **no `ec2:osuser`** |
| Windows admin via SAC with push-only permission | SAC | "equivalent to granting admin-level privileges"; SAC cmds "do not require you to sign in" |
| Runbook `PassRole:*` → pass high-priv role | `AWSSupport-EnableWindowsEC2SerialConsole` | `iam:PassedToService ∈ {ssm,ec2}` (service-scoped only) |
| Cross-account instance enumeration via errors | `SendSerialConsoleSSHPublicKey` | conflated `AuthException`; account-embedded ARN |
| Live session survives IAM revocation | session lifecycle | "duration … not determined by … IAM credentials" |
| Declarative-policy lock bypass from account | account toggle | `ManagedBy=declarative-policy` "can't be modified by the account" |

---

## 7. Out-of-Scope Risk Categories (state as confidently as in-scope)
- **Customer-authored** least-privilege mistakes (operator grants `Resource:"*"` serial push to everyone) — footgun, not AWS defect. *(But the AWS **sample/runbook** policies in Area 2 ARE in scope.)*
- Weak/absent OS passwords, GRUB single-user, SysRq — **boot/OS layer**, developed in the prerequisites sibling plan; by-design that serial reaches the OS.
- The shared AWS serial-console fleet internals, cross-tenant multiplexing, host-key custody — **HARD STOP / service-plane**; escalate to disclosure, do not probe destructively.
- IMDS on managed hosts; DNS rebinding against private-only endpoints; product/feature-parity gaps.
- The fact that serial console bypasses SG/NACL — **documented by design** ("outside of the VPC network"); in scope only insofar as it amplifies Areas 1/5, not as a bug itself.
- A user steering their own instance's OS via serial where they already hold admin — no boundary crossed.

---

## 8. Null Hypotheses / Doc Gaps (lenses checked, with pages read)
- **Lens F (injection/translation):** N/A — read all five UserGuide serial pages + the four API refs; no customer-input-to-backend-language translation layer in the *access-config* surface. (The SSH/serial wire parsing lives in the fleet — sibling/HARD-STOP territory.)
- **Lens G (SSRF):** N/A — read configure-access + prerequisites + connect; no field the service dereferences server-side on behalf of the caller (the pushed SSH key is not a URL; `SSHPublicKey` is key material).
- **Lens H (KMS):** N/A — no CMK/encryption-context in the access-config surface.
- **Lens K (prompt injection):** N/A — no LLM/agent.
- **Lens Q (upload):** N/A — `SSHPublicKey` is bounded key material (80–4096), not a parsed blob/file.
- **Lens J/FF (OAuth/JWT):** N/A — SigV4 IAM only; no 3P linking or bearer-token validation on these APIs.
- **Doc gaps (treat as open hypotheses, not closed):**
  1. **No published cross-tenant isolation statement** for the shared serial-console fleet — absence is itself a flag for the HARD-STOP-bounded test in the sibling plan.
  2. **Key→instance binding mechanism undocumented** — whether a key pushed for instance X can be presented with username `Y.port0` is unstated (confused-deputy candidate).
  3. **Session kill on IAM revocation / admin kill-switch** — docs state persistence but no teardown-on-revoke control is documented.
  4. **Runbook SSM-document `allowedPattern`** on parameters not rendered in the user-guide page — pull the actual SSM document JSON to audit input validation (injection via loose pattern).
  5. **Default-SAC-on AMI list** (`2026.09.09`+) — enumerate which images ship the admin-equivalent exposure out-of-the-box.

---

### Hunter hand-off summary
Start with **Area 1** (unscopable account toggle — fastest, highest customer impact, reversible) and **Area 2** (audit the AWS-authored sample + runbook policies with `SimulatePrincipalPolicy` — the only cleanly *reportable* Tier-2 set; the runbook's `PassRole:*` is the standout). **Area 3** (`ec2:osuser` gap) and **Area 5** (cross-account error oracle) are the AWS-design-owned leads worth confirming. Everything touching the SSH session, fleet, or OS/boot layer is **owned by the two sibling plans** — chain, don't duplicate — and **the fleet is a HARD STOP**: the instant any evidence names an AWS-fleet identity or reaches another tenant, stop and preserve for disclosure.

*Generated as a documentation-derived research plan; no live testing performed.*
