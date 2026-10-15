# EC2 Update Management — Attack / Research Plan

**Target page:** `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/update-management.html` (`.md` twin confirmed byte-identical, 12 lines)
**Method:** `security-questionbuilder` skill (boundary-first threat modeling), documentation-only. Nothing was executed against a live account. Produced by a single skill pass + three parallel deep-dive subagents.
**Date:** 2026-10-15

---

## §0 — How to use this plan

`update-management.html` is a **thin pointer page**. It carries no API surface of its own; its entire content is three recommendations:

1. Use **AWS Systems Manager Patch Manager** to patch EC2 instances.
2. For instances in an **Auto Scaling group**, use the **`AWS-PatchAsgInstance`** SSM Automation runbook "to help avoid instances that are undergoing patching from being replaced."
3. Links to **guest-OS** update mechanisms (AL2023, AL2, Windows best-practices).

So the real attack surface is **entirely cross-service and inherited** — EC2 has *zero* native patch actions (confirmed against `list_ec2`; patching is a full `ssm:*` delegation). The page's security value therefore reduces to the IAM artifacts, control-plane APIs, and guest-OS trust roots it points at. This plan is organized around those three inherited surfaces.

**A downstream hunter should start here:** the single highest-value, lowest-cost lead is the `AWS-PatchAsgInstance` runbook's AWS-authored "Required IAM permissions" block (§5, Area 1) — it composes into a documented, copy-verbatim privilege-escalation-to-administrator primitive, confirmable with a **no-touch `iam:SimulatePrincipalPolicy`** call before any resource is created. The second tier is the Patch Manager control-plane scoping gaps (§5, Areas 2–6), all confirmable the same no-touch way. The guest-OS leads (§5, Area 7) are lower severity (transport/reproducibility, not RCE).

**Scope reminder for the hunter:** every finding below is **customer-account-local** (one principal in an account escalating/forging against another team's resources in the *same* account) or a guest-OS/transport issue. **No finding implicates AWS's own service plane** — no hard stop was triggered in any of the three deep-dives. If live testing ever surfaces AWS-fleet credentials/ARNs/accounts, stop and preserve evidence.

**Provenance of leads (so another agent need not start from zero):**
- Runbook deep-dive → `AWS-PatchAsgInstance` page (`/tmp/runbook.md`), `AmazonSSMAutomationRole.md`, `automation-setup-iam.md`, `list_ssm/list_autoscaling/list_ec2`.
- Patch Manager deep-dive → `patch-manager-*` User Guide pages, `AmazonSSMManagedInstanceCore.md`, `compliance-permissions.md`, `configuring-maintenance-window-permissions-console.md`, `list_ssm`.
- Guest-OS + managed-policy audit → `install-updates.html`, AL2023/AL2 update pages, Windows best-practices, `list_iam`.

---

## §1 — Pentest objectives

1. Prove that a role provisioned exactly as AWS's own docs instruct for `AWS-PatchAsgInstance` is account-admin-equivalent, and that a non-admin who can pass it escalates to full account takeover.
2. Prove that Patch Manager's patch-group / default-baseline binding model lets one team hijack another team's patching (withhold security patches, or stage malicious packages) because the binding key is a free-text tag string with no IAM condition key.
3. Prove that a custom Linux patch baseline's "alternative patch source repository" field is an unauthenticated, root-level package-install primitive.
4. Prove that the default EC2 instance role (`AmazonSSMManagedInstanceCore`) permits cross-instance compliance forgery and patch-recon, and that AWS's own documented "best practice" mitigation is inert for the standard EC2 instance-profile auth path.
5. Characterize guest-OS trust roots (AL2 repo transport, AL2023 version lock) for downgrade / stale-patch exposure.

---

## §2 — Components, Assets, and Design

**Customer-facing interface:** none native to the page. All operations are SSM control-plane APIs (SigV4 IAM) + the SSM Agent's outbound channel from each instance.

**Processes / fleets behind it:**
- **SSM Patch Manager control plane** — resolves baselines, patch groups, compliance.
- **SSM Automation** executing `AWS-PatchAsgInstance` — an AWS-owned document that, per its permission list, creates a **CloudFormation stack**, a **Lambda function** (+ a transient IAM role), and calls EC2 `RunInstances`.
- **SSM Agent** on each managed instance, running `AWS-RunPatchBaseline` → drives the native package manager (`yum`/`dnf`/`apt` as **root** on Linux; WSUS/PowerShell as **SYSTEM** on Windows).
- **Guest OS package pipeline** — AL2023 (dnf, `releasever`-locked), AL2 (`amazon-linux-https`), Windows (Windows Update, off by default on Server AMIs).

**Identity / roles in play:**
- `AutomationAssumeRole` (call it **R**) — the role the runbook assumes. AWS tells customers to build it from the managed policy **`AmazonSSMAutomationRole`** (`ssm:*` on `*`, CFN on `*`, EC2 lifecycle on `*`; **no `iam:*`**, Lambda scoped to `function:Automation*`) **plus** the runbook page's literal, **unscoped** `iam:CreateRole/AttachRolePolicy/PutRolePolicy/PassRole/DeleteRole…` + `lambda:CreateFunction/InvokeFunction…` + `cloudformation:*` + `ec2:RunInstances` bullets.
- `LambdaRoleArn` — a second, caller-supplied role passed to the Lambda the runbook creates.
- **`AmazonSSMManagedInstanceCore`** — the default instance-profile policy on essentially every SSM-managed EC2 instance; `Resource:"*"`, **no `Condition`**, including `ssm:PutComplianceItems/UpdateInstanceInformation/PutInventory/GetDeployablePatchSnapshotForInstance/GetParameter(s)`.
- Maintenance-window service role — AWS's base sample grants `ssm:SendCommand` on `Resource:"*"`.

**What a "resource" is here:** patch **baselines** (`pb-…`, account-scoped ARN, IAM-tag-scopable); **patch groups** (NOT a resource — a free-text tag value on `Patch Group`/`PatchGroup`); **default baseline** (per-OS account setting); **compliance items** (per-instance mutable, last-writer-wins record); SSM **documents** (`AWS-RunPatchBaseline`, `AWS-PatchAsgInstance`).

**Untrusted-data entry points:** the custom-baseline **alternative-repo config string** (fed raw into the OS package manager), the **`LambdaRoleArn`** parameter, and the **patch-group tag value** used for binding.

```
EC2 User Guide (update-management.html)  ── points to ──┐
                                                        │
  ┌─────────────────────────────────────────────────────────────────────────┐
  │ SSM Patch Manager control plane                                           │
  │   RegisterPatchBaselineForPatchGroup ── binds by free-text tag string ────┼──> every instance tagged "Patch Group=X"
  │   RegisterDefaultPatchBaseline ─────── per-OS, no OS condition key ────────┼──> every untagged instance of an OS
  │   Create/UpdatePatchBaseline(alt-repo) ─ raw repo cfg, no GPG enforced ────┼──> SSM Agent runs AWS-RunPatchBaseline
  └─────────────────────────────────────────────────────────────────────────┘        (root/SYSTEM) → native pkg mgr
                                                        │
  ┌─────────────────────────────────────────────────────────────────────────┐
  │ SSM Automation: AWS-PatchAsgInstance                                      │
  │   AssumeRole R (ssm:* + iam:CreateRole/AttachRolePolicy/PassRole + lambda)─┼──> CreateRole→AttachRolePolicy(Admin)
  │   LambdaRoleArn (caller-supplied) ──> Lambda exec role                     │     →PassRole→Lambda→ADMIN STS session
  └─────────────────────────────────────────────────────────────────────────┘
```

---

## §3 — Trust-boundary map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Non-admin principal who can `PassRole R` + `StartAutomationExecution` | Account administrator | R's documented perms = `CreateRole`+`AttachRolePolicy`+`PassRole`+`CreateFunction`+`InvokeFunction`, unscoped | `SimulatePrincipalPolicy` returns `allowed` for all five → admin STS session obtainable |
| Caller of `AWS-PatchAsgInstance` | A role `T` the caller cannot pass directly | `LambdaRoleArn=T` relayed through R's broader PassRole | Lambda runs under `T` though caller holds no `PassRole(T)` |
| Any principal with `RegisterPatchBaselineForPatchGroup` on *their own* baseline | Every instance tagged with another team's patch-group value | Binding keyed on free-text string, **no condition key for the patch-group name** | `get-patch-baseline-for-patch-group --patch-group <victim value>` returns attacker's baseline |
| Custom-baseline author | Every instance in the patch group, as root | Alt-repo config string → native pkg mgr, no GPG/TLS enforced by Patch Manager | Package from attacker `http://` repo installs with no baseline-level rejection |
| Any principal with `RegisterDefaultPatchBaseline` on one tagged baseline | Every untagged instance of **any** OS, account-wide | Default set per-OS, **no OS-type condition key** | Attacker's baseline becomes default for an OS they don't operate |
| Any SSM-managed EC2 instance (via instance profile) | Every other instance's compliance / patch-snapshot records | `AmazonSSMManagedInstanceCore` grants the writes on `Resource:"*"`, no `Condition` | Instance A `PutComplianceItems(ResourceId=B)` succeeds / forges B `COMPLIANT` |
| Non-admin with `AmazonSSMFullAccess` + scoped `PassRole` | Any instance account-wide, as root/SYSTEM | AWS's own maintenance-window base policy grants `ssm:SendCommand` on `Resource:"*"` | Maintenance-window task on another team's prod instance executes |
| Guest OS (AL2, IPv6-only subnet) | Package repo transport | Doc instructs `amazon-linux-https disable` → HTTP | Repo metadata/packages fetched over cleartext HTTP |
| **Any of the above** | **AWS service plane** (Lambda runtime, CFN control plane, SSM fleet) | — | **HARD STOP** — none observed; all findings customer-account-local |

---

## §4 — API / interface inventory

| Name | Mut. | Facing | Authorized callers | Scopability (per `list_ssm`) | Notes |
|---|---|---|---|---|---|
| `ssm:StartAutomationExecution` | Y | External | IAM principals | `document*`/`automation-definition` by ARN+`ssm:DocumentType/Version` | Scoping the *document* does NOT bind which `AutomationAssumeRole` is passed |
| `ssm:SendCommand` | Y | External | IAM principals | `instance`/`managed-instance` tag-scopable (`aws:ResourceTag`,`ssm:resourceTag`) | AWS's own MW sample leaves it `Resource:"*"` |
| `ssm:RegisterPatchBaselineForPatchGroup` | Y | External | IAM principals | `patchbaseline*` only (by **its own** tags) | **No condition key for the patch-group string** |
| `ssm:RegisterDefaultPatchBaseline` | Y | External | IAM principals | `patchbaseline*` only | **No OS-type condition key** |
| `ssm:CreatePatchBaseline` / `UpdatePatchBaseline` | Y | External | IAM principals | create: only `aws:RequestTag`; update: `patchbaseline*` tag-scopable | Carries the alt-repo config field |
| `ssm:PutComplianceItems` | Y | External/instance | instances via `AmazonSSMManagedInstanceCore` | `instance`/`managed-instance` + `ec2:SourceInstanceARN`/`ssm:SourceInstanceARN` **exist but unused by the managed policy** | Compliance forgery primitive |
| `ssm:GetDeployablePatchSnapshotForInstance` | N | Instance | instances via core policy | **No resource type, no condition key** — structurally unscopable | Returns presigned S3 snapshot URL; cross-instance recon |
| `ssm:UpdateInstanceInformation` / `PutInventory` | Y | Instance | instances via core policy | self-scope keys exist, unused | On `Resource:"*"` in managed policy |
| `iam:PassRole` | — | External | IAM principals | supports `iam:PassedToService` | AWS's "minimum" MW sample omits the condition; present in a sibling sample (doc-vs-doc) |
| EC2 native patch actions | — | — | — | — | **None exist** — full `ssm:*` delegation |

---

## §5 — Recommended areas of focus

### Area 1 — `AWS-PatchAsgInstance` role = documented privesc-to-admin (Lens R + Lens B, chained) — **HEADLINE, High→Critical**

**Background.** `update-management.html` sends ASG users straight to the `AWS-PatchAsgInstance` runbook with no scoping caveat. AWS's setup walkthrough tells customers to build the `AutomationAssumeRole` (**R**) from the managed policy `AmazonSSMAutomationRole`, then add the actions the runbook's own page lists.

**Security concern.** The runbook page's "Required IAM permissions" is a flat, **unscoped** action list — `iam:CreateRole`, `iam:AttachRolePolicy`, `iam:PutRolePolicy`, `iam:PassRole`, `lambda:CreateFunction`, `lambda:InvokeFunction`, `cloudformation:CreateStack`, `ec2:RunInstances` — **no `Resource`, no `Condition`**. Composed with the baseline's `ssm:*` on `*`, R is account-admin-equivalent. The baseline deliberately withholds `iam:*` and scopes Lambda to `function:Automation*`; **the runbook page is what tells the customer to add IAM self-service back, unscoped.**

**High-level test scenarios.**
1. The core chain: as a principal holding R (or able to `PassRole R` + `StartAutomationExecution`): `CreateRole`(trust `lambda.amazonaws.com`)→`AttachRolePolicy`(`AdministratorAccess`)→`PassRole`→`CreateFunction`(attacker code)→`InvokeFunction` → admin STS session. The attacker **never runs the runbook's real logic** — R's baseline `ssm:*` also lets them `StartAutomationExecution` on a custom attacker document.
2. `LambdaRoleArn` second PassRole surface: supply `LambdaRoleArn=T` (a role the caller cannot pass directly) and rely on R's broader `PassRole` to relay it to `lambda.amazonaws.com`.
3. Confused-deputy trust-policy gap: a customer following only `update-management.html → runbook page` never visits `automation-setup-iam.html`, whose `aws:SourceArn`/`aws:SourceAccount` hardening is "we recommend" prose *after* the console creation steps — so R's trust policy likely accepts `ssm.amazonaws.com` assumption unconditionally.

**Doc evidence.** `/tmp/runbook.md:39-43` (`LambdaRoleArn` "transient role will be created"), `:59-84` (unscoped required-perms list); `AmazonSSMAutomationRole.md` v9 (`ssm:*`/`cfn:*`/EC2 on `*`, no `iam:*`, Lambda `function:Automation*`); `automation-setup-iam.md:30-45` (attach-managed-policy guidance + `Resource:"*"` worked examples), `:47-49` ("we recommend" confused-deputy fix on a different page).

**Confirm/Refute oracle (no-touch).** `iam:SimulatePrincipalPolicy` on a synthetic principal holding exactly `AmazonSSMAutomationRole` + the runbook's documented delta (as `Resource:"*"`): expect `CreateRole`, `AttachRolePolicy`, `PassRole`(ctx `iam:PassedToService=lambda.amazonaws.com`), `CreateFunction`, `InvokeFunction` all `allowed`. Escalate to a canary role/function in an authorized account only to confirm the invoked Lambda's STS session carries admin.

**Severity.** High (Critical if R's `PassRole` is unscoped — likely). Lens R Tier-2: AWS-authored, copy-verbatim artifact — AWS's defect, not a customer footgun.

---

### Area 2 — Patch-group tag land-grab (Lens I / EE) — **High**

**Background.** A "patch group" is **not an AWS resource** — it is a free-text tag value (`Patch Group` or `PatchGroup`) on instances. `RegisterPatchBaselineForPatchGroup` binds a baseline to that string by value equality, first-registered-wins.

**Security concern.** `list_ssm` shows the action's only required resource type is `patchbaseline*`, condition keys apply only to **the baseline's own tags** — **there is no IAM resource type and no condition key for the patch-group string being registered**. A principal scoped to only their own baseline can rebind another team's patch-group name to it. The dual-key aliasing (`Patch Group` vs `PatchGroup`, "identical values ⇒ same group") widens the match surface.

**High-level test scenarios.** With `RegisterPatchBaselineForPatchGroup` on an attacker-owned baseline (commonly granted via `AmazonSSMFullAccess`), call `--patch-group <victim team's value>` (often predictable: `PROD`, `prod-web`). Impact is bidirectional: (a) withhold security patches (baseline with no approved patches = patch-pipeline DoS), or (b) approve a malicious package set the victim's baseline would reject (chains into Area 3).

**Doc evidence.** `patch-manager-patch-groups.md:14,21,31-34,62`; `list_ssm.md:1672-1676` (resource/condition rows); `patch-manager-tag-a-patch-group.md:48` (tag instances not yet SSM-configured).

**Oracle.** Under the tightest scoping the service allows (`Resource: patchbaseline/<attacker>` + own-baseline tag condition), `register-patch-baseline-for-patch-group --patch-group <victim>` succeeds and `get-patch-baseline-for-patch-group` returns the attacker baseline → confirmed via `SimulatePrincipalPolicy` first.

**Severity.** High — structural (no condition key exists), cross-team within a shared account.

---

### Area 3 — Alternative patch source repository → unauthenticated root package install (Lens G) — **High (Critical chained with Area 2)**

**Background.** A custom Linux patch baseline can specify an "alternative patch source repository" — a raw package-manager config string Patch Manager hands to `yum`/`dnf`/`apt` running as root under `AWS-RunPatchBaseline`.

**Security concern.** AWS's own example `Configuration` field has **no `gpgcheck`** key and shows a bare `baseurl=https://…`; the Debian example is a plain `deb http://… ` sources.list line (cleartext HTTP explicitly shown as acceptable). The alt-repo page's only documented "important consideration" is availability (`skip_if_unavailable`), **nothing about GPG/signature/TLS**. PPAs (arbitrary third-party repos) are explicitly endorsed. No doc states Patch Manager layers any signature check of its own.

**High-level test scenarios.** Create a custom baseline whose repo config points at an attacker `http://` repo with `gpgcheck=0`/no `Signed-By`, bind it (directly or via Area 2), run `AWS-RunPatchBaseline Install`. Breach = attacker package installs with no Patch-Manager-level rejection. Chained with Area 2 this is unauthenticated root RCE on every instance in a hijacked patch group, triggered by the victim's own schedule.

**Doc evidence.** `patch-manager-alternative-source-repository.md:12,34-36,59`; `patch-manager-create-a-patch-baseline-for-linux.md:77-108`; `patch-manager-aws-runpatchbaseline.md:27-30`.

**Oracle (safe first).** `DescribeEffectivePatchesForPatchBaseline` confirms the baseline resolves the attacker package as "approved" before any `Install`.

**Doc-gap.** Whether Patch Manager enforces `gpgcheck=1`/rejects `http://` independent of the baseline string is undocumented — flag "confirm surface first," not null.

**Severity.** High standalone, Critical chained.

---

### Area 4 — `RegisterDefaultPatchBaseline` account-wide OS override (Lens S / U) — **High**

**Background.** The account-wide default baseline is set **per-OS**, with the OS implied by the baseline's own `OperatingSystem` attribute — never passed or scoped in the IAM authorization.

**Security concern.** `list_ssm` gives `RegisterDefaultPatchBaseline` the same condition surface as Area 2 — `patchbaseline*` by its own tags only, **no OS-type condition key**. A principal scoped to "only baselines I tagged" can overwrite the account-wide default for whichever OS their one allowed baseline represents, hitting every untagged instance of that OS.

**High-level test scenarios.** Scope a principal to `RegisterDefaultPatchBaseline` on one attacker-tagged baseline (built for, e.g., Windows), call `register-default-patch-baseline` → it becomes default for that OS fleet-wide; narrow baseline-tag scoping did nothing to stop OS targeting. Make vulnerable fleets report `Compliant`, or systematically block critical patches.

**Doc evidence.** `patch-manager-default-patch-baseline.md:11,46`; `list_ssm.md:1660-1664`; `patch-manager-patch-groups.md:62,106-110` (untagged instances inherit default).

**Severity.** High (stealthy, account-wide, one OS family at a time). Applies to the legacy patch-group/maintenance-window model (not patch-policy/Quick Setup).

---

### Area 5 — `AmazonSSMManagedInstanceCore` over-grant + inert "best practice" (Lens R / U) — **Medium-High**

**Background.** The default instance-profile policy on every SSM-managed EC2 instance.

**Security concern.** It grants `ssm:PutComplianceItems`, `UpdateInstanceInformation`, `PutInventory`, `GetDeployablePatchSnapshotForInstance`, `GetParameter(s)` on `Resource:"*"` with **no `Condition`** — even though SSM defines self-scoping keys (`ec2:SourceInstanceARN`/`ssm:SourceInstanceARN`) for the compliance writes. `GetDeployablePatchSnapshotForInstance` is **structurally unscopable** (no resource type/condition key at all) and returns a presigned S3 snapshot URL scoped only to account/patch-group/OS/snapshot-ID, not caller identity. `ssm:GetParameter(s)` on `*` = account-wide Parameter Store read from any instance (chains to secret-exposure, Lens T).

**The inert mitigation (Lens U).** AWS's `compliance-permissions.md` ships a "best practice" to restrict `PutComplianceItems`: statement 1 compares `ec2:SourceInstanceARN` **to itself** (tautology, constrains nothing — never references the target `ResourceId`, which isn't a condition key); statement 2 uses `ssm:SourceInstanceARN`, which `list_ssm:1996` states is **absent when the request comes from an EC2 instance-profile role** — so it is dead code for the dominant EC2 auth path and only ever matches `mi-*` hybrid nodes. AWS's documented defense against cross-instance compliance forgery provides **zero real restriction for standard EC2**.

**High-level test scenarios.** From an instance holding only this policy, `PutComplianceItems(ResourceId=<other instance>, status=COMPLIANT)`, `GetDeployablePatchSnapshotForInstance(<other instance>)`, `GetParameter` across workloads. IAM alone cannot deny (prove via `SimulatePrincipalPolicy` against the exact managed-policy ARN — no-touch).

**Doc evidence.** `AmazonSSMManagedInstanceCore.md:35-82`; `compliance-permissions.md:10,19-48`; `list_ssm.md:1636-1639,1983-1996`; `patch-manager-aws-runpatchbaseline.md:39`.

**Doc-gap.** Whether an undocumented SSM backend cross-checks caller↔target is unknown; IAM is proven insufficient regardless. Flag "confirm surface first."

**Severity.** Medium-High. Lens R Tier-2 (AWS-authored, uneditable, shipped as the explicit setup instruction).

---

### Area 6 — `SendCommand` root-exec via AWS's maintenance-window sample + compliance integrity (Lens B / R + Lens U / O) — **High / Medium-High**

**Background.** Patch Manager's documented scheduling path is a maintenance-window Run-Command task running `AWS-RunPatchBaseline` (root/SYSTEM).

**Security concern — SendCommand (High).** `ssm:SendCommand` *is* tag-scopable per `list_ssm`, but AWS's own "base policy you can adapt" for the maintenance-window service role grants it on `Resource:"*"`; the surrounding guidance suggests narrowing Lambda/StepFunctions ARNs but **never the SendCommand target instances**. The companion "minimum permissions to register tasks" sample grants `iam:PassRole` to that role with **no `iam:PassedToService`** condition — while a sibling sample on the same page *does* include it (doc-vs-doc inconsistency). Net: any principal who can register a patching task gets general-purpose root-RCE-as-a-service against any instance in the account.

**Security concern — compliance integrity (Medium-High).** Compliance state is a single mutable, last-writer-wins record with no provenance binding (a looser scan silently replaces a stricter one). Combined with Area 5's forgeable `PutComplianceItems`, an attacker masks any instance's non-compliance from Security Hub CSPM / dashboards until the victim's next real scan.

**High-level test scenarios.** Grant a test user `AmazonSSMFullAccess` + the scoped `PassRole` (no `PassedToService`), register a MW task (or `SendCommand` directly) against another team's instance running an arbitrary document → executes. Separately, `PutComplianceItems(ResourceId=B, COMPLIANT)` from instance A persists on B's dashboard.

**Doc evidence.** `configuring-maintenance-window-permissions-console.md:38-110,208-237`; `patch-manager.md:116,122,129`; `patch-manager-aws-runpatchbaseline.md:73`; `patch-manager-compliance-data-overwrites.md:12,18`.

**Severity.** High (SendCommand) / Medium-High (compliance forgery). `iam:PassedToService` existence vs non-use in this chain's own guidance is itself a Lens U doc-vs-enforcement note.

---

### Area 7 — Guest-OS trust roots (Lens Y / U) — **Medium / Low-Medium**

**A1 — AL2 HTTPS→HTTP downgrade (Lens Y, Medium).** AL2's repo trust root is an AWS-owned S3 dual-stack endpoint; `install-updates.html`'s Important box instructs `sudo amazon-linux-https disable` for IPv6-only subnets — a **doc-sanctioned cleartext downgrade** of repo transport. No `--nogpgcheck` was found anywhere, so package integrity (renewed GPG key) likely holds; this is confidentiality/MITM-observability, not code-exec. Oracle: observe repo fetches over HTTP after the documented disable.

**A2 — AL2023 `releasever` lock (Lens U, Low-Medium).** The version lock is for build reproducibility, not security; nothing forces a re-pin, so a stale lock silently withholds security patches. Reportable as a doc-vs-intent gap (operators may believe a locked system is "patched").

**A3 — Windows (Lens R, null-scoped).** The Windows Update Management best-practices section has **no** `Set-ExecutionPolicy Unrestricted` / unsigned-script / SYSTEM pattern (null for this page). "Windows Server AMIs don't receive updates through Windows Update by default" — a patching-posture note. **Doc-gap:** `ec2launch-v2-install` was not checked.

---

## §6 — Threat model test objectives (ranked for the hunter)

1. **[High→Critical] Area 1** — `SimulatePrincipalPolicy` the `AWS-PatchAsgInstance` role → confirm admin-equivalence. Lowest cost, highest impact, no-touch. **Start here.**
2. **[High/Critical] Areas 2+3 chained** — patch-group land-grab + poisoned alt-repo = unauthenticated root RCE on a victim fleet via their own schedule.
3. **[High] Area 6 SendCommand** — root-RCE-as-a-service from AWS's unscoped MW sample policy.
4. **[High] Area 4** — account-wide default-baseline OS override.
5. **[Med-High] Area 5** — cross-instance compliance forgery + the inert "best practice"; Parameter Store cross-read.
6. **[Med-High] Area 6 compliance integrity** — forge `COMPLIANT`, defeat CSPM.
7. **[Medium] Area 7 A1** — AL2 HTTP transport downgrade.

All Area 1–6 oracles are no-touch `iam:SimulatePrincipalPolicy` first, then canary resources in an authorized account only to confirm.

---

## §7 — Out of scope

- AWS service-plane infrastructure (Lambda runtime, CloudFormation control plane, SSM fleet, the AWS-owned S3 repo endpoints) — **hard stop** if ever implicated. None was in any deep-dive.
- Non-HTTP/non-API layers (DNS, ports, subdomains).
- Guest-OS internals beyond the documented update mechanisms on the linked pages.
- Live execution — this is a plan; the hunter executes it against an authorized account with synthetic canaries only.

---

## §8 — Null hypotheses & doc-gaps (with pages checked)

**Confirmed nulls:**
- **ASG standby/detach orphaning (Lens AA):** **refuted by evidence.** The runbook's complete required-perms list (`/tmp/runbook.md:59-84`) contains **zero `autoscaling:*`** actions and no `ec2:SetInstanceProtection`/`ModifyInstanceAttribute`; `autoscaling:EnterStandby/ExitStandby/DetachInstances` are real Resource-scoped actions (`list_autoscaling:748-790`) that would have to appear if called. The "avoid replacement" behavior is most plausibly passive (health-check grace via `WaitForInstance`/`WaitForReboot`, or the `AutoPatchInstanceInASG` tag as a re-entrancy guard). This refutes the original standby/detach hypothesis **and** is itself a reportable Lens U doc-integrity issue — the User Guide's plain-English claim is unsubstantiated by the runbook's own permission surface.
- **Runbook parameter injection (Lens F/EE/G):** null — the complete parameter set is `AutomationAssumeRole`, `InstanceId`, `LambdaRoleArn`, `WaitForInstance`, `WaitForReboot`; no URL/baseline/bucket parameter. Only identity-shaped input is `LambdaRoleArn` (→ Area 1).
- **EC2 native patch actions:** none exist (`list_ec2`) — confirms full `ssm:*` delegation framing.
- **Patch Manager control-plane escape (Lens D), attestation-gated KMS (Lens W):** N/A — no control-ENI/enclave mechanism in any `patch-manager-*` page checked.

**Doc-gaps (confirm surface first, not null):**
- GPG/signature/TLS enforcement on alt-repos independent of the baseline string (Area 3).
- Undocumented SSM backend caller↔target ownership check on `PutComplianceItems`/`GetDeployablePatchSnapshotForInstance` (Area 5).
- `AWS-PatchAsgInstance` real step graph (AWS doesn't publish step JSON for owned documents) — needs live `aws ssm get-document`.
- `$DEFAULT`/`$LATEST` document-version late-binding on the AWS-owned runbook, and whether AWS revises owned documents in place (`ssm:DocumentVersion` key exists service-wide).
- Whether the `document` ARN `${Account}` placeholder resolves to the caller's account or Amazon's for an AWS-owned public document (affects whether a customer's `Resource:` scoping of `StartAutomationExecution` actually matches).
- CloudTrail attribution format for runbook sub-steps under R (Lens O; standard AssumeRole session-name behavior assumed, not confirmed).
- Windows `ec2launch-v2-install` not checked (Area 7 A3).
