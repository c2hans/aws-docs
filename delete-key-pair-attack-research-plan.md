# Delete your key pair (`delete-key-pair.html`) — Attack Research Plan

Source of leads: `https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/delete-key-pair.html` (offline twin `/work/aws-docs/.../delete-key-pair.md`, 45 lines; online `.md` fetched 2026-10-15 — **byte-identical, no drift**). Authoritative IAM surface: `https://docs.aws.amazon.com/service-authorization/latest/reference/list_ec2.html` (`list_ec2`, 35,512 lines, fetched live 2026-10-15). API Reference: `API_DeleteKeyPair.html`.

Status: documentation-derived hypotheses only. Nothing tested against a live AWS account.

> **Relationship to siblings — read this first.** This is a **page-level deep-dive CHILD** of the key-pairs cluster HUB `ec2-key-pairs-attack-research-plan.md`, which already *consumes* `delete-key-pair.md` as one of its 5 sources. It is the DELETE-page twin of `create-key-pairs-attack-research-plan.md` (the create/import page child). This plan **COMPLEMENTS, does not restate** the hub: it develops only net-new DELETE-specific surface and cross-references shared leads. The hub owns the headline **CFN-generated private-key-via-SSM reachability (Lens T, hub Area 1)**, the **`DescribeKeyPairs` unscopable account-wide read oracle (hub Area 2)**, the **Create/Import condition-key asymmetry (hub Area 3)**, the **ImportKeyPair land-grab (hub Area 4)**, the **sample-policy `key-pair/*` audit (hub Area 5)**, the **fingerprint confusion (hub Area 6)**, and the **EC2 Instance Connect twin (hub Area 7)**. See [[create-key-pairs-plan-note]], [[ec2-key-pairs hub]], [[ec2-security-hub-plan-note]].

## 0. How to use this document
- Each lead: Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity → Stop condition. Work in priority order; look left and right for adjacent bugs.
- HARD STOP: the moment evidence shows an identity/credential/ARN/account belonging to AWS's own service plane, stop, preserve evidence, flag for AWS-Security disclosure. (Not expected on this control-plane-only page.)

## 1. Pentest Objectives (DELETE-specific)
1. Determine whether `DeleteKeyPair` ("Delete your key pair") actually revokes SSH access, or whether — exactly as the page states — it removes only the EC2-stored public key while leaving every running instance's `authorized_keys`, every private-key file, and every referencing launch template/launch configuration untouched (**delete-as-false-revocation**).
2. Determine whether a least-privilege `DeleteKeyPair` policy scoped by `ec2:KeyPairName` (the *only* family member that supports name scoping) can be bypassed by targeting the key pair via its **`KeyPairId`** instead of `--key-name`, because **no `ec2:KeyPairId` condition key exists** and the key-pair ARN is name-derived.
3. Determine whether deleting a key pair that is still referenced by a launch template / launch configuration / Auto Scaling group is a usable **latent availability/DoS primitive** against future auto-recovery, and whether it is cross-team reachable.
4. Determine whether `DeleteKeyPair` provides a resource-existence/enumeration oracle (not-found vs access-denied vs idempotent-success) distinct from the hub's `DescribeKeyPairs` oracle.
5. Confirm the exact enabling link between DELETE and the hub's Area 4 land-grab: delete frees the per-account+Region name namespace, and the page's own Auto Scaling warning proves a workflow will later *re-reference that freed name*.

## 2. Components, Assets, and Design (delta vs hub)

**Customer-facing interface (this page):** `ec2:DeleteKeyPair` via API, CLI (`aws ec2 delete-key-pair --key-name {{my-key-pair}}`), PowerShell (`Remove-EC2KeyPair -KeyName`), and the EC2 console (**"Key Pairs → Actions → Delete", with a type-`Delete`-to-confirm text gate**). CloudFormation reaches it via `AWS::EC2::KeyPair` stack deletion (→ hub Area 1 / orphaned SSM parameter — deferred).

**The asset the page is about — and what it does NOT touch (verbatim):**
- `delete-key-pair.md:6` — "Deleting a key pair, which removes the public key that is stored in Amazon EC2. **Deleting a key pair does not delete the matching private key.**"
- `:8` — "Deleting a public key **doesn't remove the public key from any instances to which you've added it**, either when you launched the instance or later. It also **doesn't delete the private key on your local computer**. **You can continue to connect to instances that you launched using a public key that you've deleted** from Amazon EC2 as long as you still have the private key (`.pem`) file."
- `:11` (Important) — "If you're using an Auto Scaling group ... ensure that the public key you're deleting is **not specified in an associated launch template or launch configuration**. If Amazon EC2 Auto Scaling detects an unhealthy instance, it launches a replacement instance. However, **the instance launch fails if the public key cannot be found**."

**Design fact that drives Objective 2:** the `key-pair` resource ARN is `arn:${Partition}:ec2:${Region}:${Account}:key-pair/${KeyPairName}` (`list_ec2:33256`) — **name-keyed**. `DeleteKeyPair` (`list_ec2:18892–18901`) lists resource type `key-pair` (**no asterisk → resource-level permission is OPTIONAL, i.e. `Resource:"*"` is accepted**) with condition keys `aws:ResourceTag/${TagKey}`, `ec2:KeyPairName`, `ec2:KeyPairType`, `ec2:Region`, `ec2:ResourceTag/${TagKey}`. The `DeleteKeyPair` **API accepts either `KeyName` OR `KeyPairId`** (`API_DeleteKeyPair`), but **`ec2:KeyPairId` is not a condition key anywhere in `list_ec2`** (`grep -ci ec2_KeyPairId` = 0). `ec2:KeyPairName` is defined as "Filters access by the name of a key pair" — a resource-derived value.

**Identity model / roles:** standard SigV4 IAM; no key-pair-specific roles. No role-ARN/URL/token/upload field on this page.

## 3. Trust-Boundary Map (DELETE-specific rows; shared rows → hub)

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Operator who deletes a key pair believing it revokes access | Running instances still trusting the deleted public key in `authorized_keys` | `DeleteKeyPair` removes only the EC2-stored public key; data-plane `authorized_keys` is never touched (`:8`) | **Guarantee-gap (Lens U/AA):** the holder of the still-valid private key authenticates to a running instance *after* the key pair was "deleted" — the console action labeled **Delete** performs no revocation on the data plane. |
| Principal holding `ec2:DeleteKeyPair` scoped by `ec2:KeyPairName` (e.g. `team-*`) | A key pair *outside* that name scope | Call `DeleteKeyPair --key-pair-id key-xxxx` instead of `--key-name`; no `ec2:KeyPairId` condition key exists to scope the id path | **Breach (Lens S/A):** the id-targeted delete succeeds against a name the policy intended to forbid, because `ec2:KeyPairName` fails to populate (or is evaluated before id→name resolution) and the scoped Allow/Deny goes vacuous. |
| Principal holding only `ec2:DeleteKeyPair` (name-scopable) | Future Auto Scaling / launch-template auto-recovery that references the deleted key | Delete a key still named in a launch template / launch config (`:11`); the deletion does not update the referencing config | **Breach (Lens L/U):** a later unhealthy-instance replacement launch **fails** ("instance launch fails if the public key cannot be found") — a time-delayed availability break armed by a single delete. |
| Attacker chaining delete → re-import | A key-pair name a victim launch workflow will re-reference | Delete frees the flat per-account+Region `key-pair/${KeyPairName}` namespace; `ImportKeyPair` re-claims the freed name with attacker key material | **Breach (Lens EE/AA — enabling half of hub Area 4):** the next launch against that name boots with the attacker's public key in `authorized_keys`. The DELETE page both frees the name and (`:11`) documents that a workflow *will* re-reference it. |

## 4. API / Interface Inventory (this page)

| Name | Method | Mutating | Internet-callable | Authorized callers | Notes |
|---|---|---|---|---|---|
| `ec2:DeleteKeyPair` | API / CLI / Console / PowerShell | Mutating | Yes (SigV4) | Any IAM principal w/ grant | Resource `key-pair` (**optional** — `Resource:"*"` accepted). Condition keys `aws:ResourceTag`, `ec2:KeyPairName`, `ec2:KeyPairType`, `ec2:Region`, `ec2:ResourceTag`. **Only family member scopable by name** — but accepts `KeyName` *or* `KeyPairId`, and **no `ec2:KeyPairId` key exists** (Objective 2). API returns success; **no `authorized_keys`/private-key/launch-template side effect** (Objective 1). |
| Console "Delete" confirmation field | Console only | — | — | Console user | Type-`Delete`-to-confirm text gate exists **only in the console**; the CLI/API/PowerShell paths have **no confirmation step** → the UI guard is not an authorization control (Lens U, informational). |
| `AWS::EC2::KeyPair` stack delete | CFN | Mutating | Yes | Stack exec role / caller | Deletes EC2 public key + (for generated keys) the SSM private-key parameter via a **separate `ssm:DeleteParameter` check** → orphaned-secret / fabricated-name probe. **Deferred to hub Area 1 / §9.** |

**Undocumented-knob note:** the console-only confirmation gate and the `KeyPairId`-vs-`KeyName` dual-naming of a single resource (with only the name path condition-keyed) are the two interface deltas this page introduces over the create/import child.

## 5. Recommended Areas of Focus (net-new; shared → hub)

### Area D1 — Delete-as-false-revocation: "Delete your key pair" revokes nothing on the data plane (Lens U + Lens AA) [PRIMARY, net-new]
**Background:** The entire page is a documented statement that `DeleteKeyPair` is a *public-key-registry* delete, not a *credential revocation*. Verbatim (`:6`, `:8`): deleting does not delete the private key, does not remove the public key from any instance's `authorized_keys`, and "you can continue to connect to instances ... as long as you still have the private key."

**Security Concern:** This is Lens AA (revocation completeness) applied to a resource that is *not* a share — the revoke-side gap exists even without cross-account sharing. An operator responding to a compromised credential or an off-boarded employee by "deleting the key pair" (the obvious, console-labeled action) achieves **no** reduction in standing access to any already-running instance. There is **no EC2 action that revokes a key pair from running instances** (confirmed: the key-pair family is Create/Import/Delete/Describe only; removal from `authorized_keys` is a manual in-instance / config-management operation the docs push to the customer). The security *promise* a reader infers from the word "Delete" is enforced by nothing.

**High-level Test Scenarios:**
1. Launch an instance with key pair K; confirm SSH with K's private key.
2. `DeleteKeyPair` K (by name). Re-run the SSH connection with the same private key — **confirm it still succeeds** (oracle: authenticated shell after delete).
3. Confirm no control-plane action exists to force-revoke: grep `list_ec2` for any `*KeyPair*`/`authorized_keys`/revoke action beyond Create/Import/Delete/Describe (expected: none). Document that revocation requires EC2 Instance Connect / SSM / manual edit — a *different* IAM surface than the one the operator just exercised.
4. Variant: confirm the deleted key pair's absence from `DescribeKeyPairs` while access persists — i.e. the control-plane inventory now *under-reports* live credentials (a detection/audit blind spot, Lens O adjacency).

**Doc evidence:** `delete-key-pair.md:6,8`.
**Severity-if-true:** Medium as a documentation/guarantee finding (AWS-owned: the console verb "Delete" + the absence of any revoke mechanism); the *access* that persists is by-design SSH, so the finding is the **false sense of revocation**, not a new access path. Highest value as the framing that makes D3 (land-grab) and the Auto Scaling warning coherent.
**Stop condition:** once persistence-after-delete is shown once, stop; do not iterate across instances.

### Area D2 — `KeyPairId` bypass of an `ec2:KeyPairName`-scoped Delete policy (Lens S / Lens A "two names, one checked") [net-new, sharp]
**Background:** `DeleteKeyPair` is the *only* key-pair action that supports `ec2:KeyPairName` (hub Area 3). A defender's natural least-privilege policy is therefore `Allow ec2:DeleteKeyPair` (or `Deny`) `Condition {StringLike ec2:KeyPairName: "team-*"}`. But the API also accepts `--key-pair-id`, the ARN is name-keyed (`key-pair/${KeyPairName}`), and **`ec2:KeyPairId` is not a condition key** (0 hits in `list_ec2`).

**Security Concern:** When the caller names the resource by `KeyPairId`, does IAM resolve id→name *before* evaluating `ec2:KeyPairName` (so the condition populates and the scope holds), or does it evaluate against a request context where `ec2:KeyPairName` is **absent** (so a `StringLike` Allow never matches → effectively no-op, and a `StringNotLike`/`Null`-naive Deny fails open)? Because the resource row allows `Resource:"*"`, a policy written as `Allow DeleteKeyPair on key-pair/team-* ` would *fail closed* on an id-call (good), but a policy written as `Allow DeleteKeyPair on * + Deny unless ec2:KeyPairName like team-*` could **fail open** on an id-call if the key does not populate. This is the catalog's documented Lens-S "null/absent-key resolution asymmetry" and the Lens-A "two ways to name one resource, only one checked" shape — on an action AWS specifically made name-scopable.

**High-level Test Scenarios:**
1. `iam:SimulateCustomPolicy` (no resources touched): simulate `ec2:DeleteKeyPair` with the request context carrying `ec2:KeyPairName` **present** vs **absent**, under (a) `Allow ... Resource: key-pair/team-*`, (b) `Allow ... Resource:* , Condition StringLike ec2:KeyPairName team-*`, (c) `Allow Resource:* + Deny StringNotLike ec2:KeyPairName team-*`. Record which combinations go vacuous when the name key is absent.
2. Live, scoped canary: create key pairs `team-a` and `prod-a`. Under a role holding policy (b)/(c), attempt `delete-key-pair --key-pair-id <id-of-prod-a>` and `--key-name prod-a`. Oracle: id-call succeeds where name-call is `AccessDenied` ⇒ confirmed bypass.
3. Confirm the ARN resolver behavior: does the id-call's CloudTrail `requestParameters` show `keyName` back-filled (resolution happened pre-authz) or only `keyPairId`?

**Doc evidence:** `list_ec2:18892–18901` (DeleteKeyPair resource/condition set), `:33256` (name-keyed ARN), `grep ec2_KeyPairId`=0, `API_DeleteKeyPair` (accepts `KeyPairId`).
**Severity-if-true:** Medium–High — defeats the one condition key AWS provides for scoping destructive key-pair deletes; cross-team within an account. If refuted (resolution is pre-authz and the key populates), downgrade to a documented null and note that `Resource`-ARN scoping (not condition-key scoping) is the safe pattern.
**Stop condition:** settle at the Simulate stage first; only canary if Simulate shows the key can be absent.

### Area D3 — Delete → re-import land-grab: the enabling half of hub Area 4 (Lens EE / AA) [net-new linkage]
**Background:** Deleting a key pair frees its name in the flat per-account+Region `key-pair/${KeyPairName}` namespace. The page's own Important box (`:11`) establishes that a launch template / launch configuration / ASG **keeps referencing the deleted name** and that EC2 Auto Scaling **will fire a replacement launch** against it. The hub's Area 4 develops the `ImportKeyPair` land-grab abstractly; **this page supplies the two concrete enabling facts**: (a) delete is what frees the name, and (b) a workflow is documented to re-reference it.

**Security Concern:** A principal who can delete key pair K (name-scopable per D2, or broadly) and import under the freed name K (import is **not** name-scopable — hub Area 3) can swap the credential a victim launch path will use. The ASG warning says the launch *fails* when the key is missing — but if the attacker re-imports K between delete and the next replacement, the launch *succeeds* with the attacker's public key in `authorized_keys`, converting the documented availability footgun into a **credential-substitution** primitive.

**High-level Test Scenarios:**
1. Create a launch template referencing key pair K; create key pair K; place an instance under an ASG using that template.
2. Delete K; `ImportKeyPair` under name K with an attacker public key.
3. Trigger a replacement (terminate the ASG instance / fail its health check).
4. Oracle: the attacker's private key authenticates to the replacement instance's default user.

**Doc evidence:** `delete-key-pair.md:11`; hub Area 4; `create-key-pairs.md` (import = no authenticity/name/type condition key).
**Severity-if-true:** High if it lands on a shared/production launch path. **Defers** the generic ImportKeyPair-land-grab mechanics, the `ec2:KeyPairName`-absent-on-import fact, and the name-namespace analysis to **hub Area 4** — this area owns only the delete→free→re-reference chain.
**Stop condition:** one confirmed credential substitution; do not enumerate other templates.

### Area D4 — Delete of a referenced key as a latent availability/DoS primitive (Lens L / Lens U) [net-new]
**Background:** `:11` states plainly that a replacement instance launch **fails if the public key cannot be found**, and that nothing updates the referencing launch template/launch configuration when you delete the key.

**Security Concern:** `DeleteKeyPair` is the arming action for a time-delayed availability break that manifests only when an instance later becomes unhealthy — long after the delete, decoupling the destructive act from its effect in both time and CloudTrail attribution. Because `DeleteKeyPair` can be `Resource:"*"`/tag-scoped, a principal with delete over another team's key (or broad delete) can disable that team's auto-recovery without ever touching their ASG, launch template, or instances. No synchronous error warns the deleter that the key is still referenced (the doc puts the burden entirely on the operator: "ensure that the public key you're deleting is not specified in an associated launch template").

**High-level Test Scenarios:**
1. Create key pair K referenced by a launch template behind an ASG. Delete K. Confirm no synchronous "still in use" rejection (oracle: delete returns success despite the live reference).
2. Force a replacement launch; confirm it fails with a missing-key error → the ASG cannot self-heal.
3. Scope question: confirm whether a `DeleteKeyPair` grant tag/`Resource`-scoped to one team can still delete a key another team's launch template depends on (cross-team blast radius via a shared or mis-scoped delete grant).

**Doc evidence:** `delete-key-pair.md:11`; linked Auto Scaling launch-templates guide.
**Severity-if-true:** Medium (single-account availability; cross-team if the delete grant is broad). Not cross-tenant → not Critical. Record as a doc-stated footgun that AWS leaves entirely to the operator with no synchronous guardrail.

### Area D5 — Delete enumeration/idempotency oracle (Lens A, minor) [net-new, likely null]
**Background:** `DeleteKeyPair` is a mutating action callable by name or id.
**Security Concern:** Does deleting a nonexistent key return a distinct not-found vs access-denied vs idempotent-success response that forms a resource-existence oracle (confirming a key pair's existence to a principal that cannot `DescribeKeyPairs`)? The hub's Area 2 oracle is `DescribeKeyPairs`; this asks whether Delete leaks the same signal to a principal denied Describe.
**High-level Test Scenarios:** Under a role with `ec2:DeleteKeyPair` but **not** `ec2:DescribeKeyPairs`, call delete on (a) a key that exists but is outside a name scope, (b) a nonexistent name, (c) a nonexistent id. Compare error codes/messages/latency. (Expectation from AWS semantics: `DeleteKeyPair` is idempotent and returns success for a missing key → **weak/no oracle**; but confirm the by-id path and the scoped-deny path, which may differ.)
**Doc evidence:** `API_DeleteKeyPair` (return shape); `delete-key-pair.md` (name/id).
**Severity-if-true:** Low–Informational (existence oracle only). Likely a documented null once idempotency is confirmed.

## 6. Threat Model Test Objectives

| Threat / Test Case | Component | Documented mitigation to attack |
|---|---|---|
| "Delete key pair" leaves a compromised/off-boarded credential fully live on running instances | Data-plane `authorized_keys` vs EC2 control plane | Attack the assumption that the console "Delete" verb revokes access — the docs say it does not; there is no revoke action |
| Bypass an `ec2:KeyPairName`-scoped delete policy by naming the key via `KeyPairId` | `ec2:DeleteKeyPair` authz, name-keyed ARN, no `ec2:KeyPairId` key | Attack the assumption that `ec2:KeyPairName` scoping covers the id-targeting path |
| Substitute an attacker key into a victim launch path via delete-then-import of a freed name | `ec2:DeleteKeyPair` + `ec2:ImportKeyPair` + flat name namespace | Attack the assumption that deleting a key and the name being re-usable is harmless (chains hub Area 4) |
| Disable a team's Auto Scaling self-healing with a single delete | `ec2:DeleteKeyPair` + launch template / ASG reference | Attack the assumption that delete is rejected or warned when the key is still referenced |
| Confirm a key pair's existence via Delete without `DescribeKeyPairs` | `ec2:DeleteKeyPair` error/idempotency behavior | Attack the assumption that delete leaks no existence signal |

## 7. Out-of-Scope Risk Categories
- SSH client/server internals (OpenSSH/PuTTY), the content of `authorized_keys` manipulation inside the guest OS — the finding in D1 is the *control-plane guarantee gap*, not an SSH bug.
- The CFN-generated private-key-via-SSM path, the SSM/KMS managed-key internals, and the orphaned-parameter / fabricated-name probe — **owned by hub Area 1 / hub §9** (reached from this page only via `AWS::EC2::KeyPair` stack delete).
- `DescribeKeyPairs` unscopable account-wide inventory read — **hub Area 2**.
- Create/Import condition-key asymmetry and the generic `ImportKeyPair` land-grab mechanics — **hub Areas 3 and 4**.
- EC2 Instance Connect `SendSSHPublicKey` as a parallel SSH-credential path — **hub Area 7** (relevant to D1 as the *actual* ephemeral-key revoke/push mechanism, but its authz-parity analysis belongs to the hub).
- Customer-authored over-broad `Resource:"*"` on `DeleteKeyPair` that the customer wrote without an AWS sample as the source — a least-privilege footgun the customer owns (unless it originates from an AWS-published sample → then Lens R, hub Area 5).

## 8. Null hypotheses / doc gaps (pages checked: `delete-key-pair.md` in full; `list_ec2` DeleteKeyPair block + condition-key defs; `API_DeleteKeyPair`)
- **Lens G (SSRF):** N/A — the page has no URL/host/reference field the service dereferences; the only parameter is a key name/id identifier.
- **Lens B/C (PassRole/vending):** N/A — no role-ARN/token parameter on delete.
- **Lens Q (upload):** N/A — delete takes no blob (import does → hub).
- **Lens T (cross-service secret):** present only via the CFN delete path → **deferred to hub Area 1**, not re-derived here.
- **Lens H (CMK):** N/A on the EC2-side delete; the SSM `SecureString` KMS question is the hub's (resolved in hub §9).
- **Lens K/F/D/W/N/J/M/BB/CC/DD/FF:** N/A — no LLM, parser/translation, network/control-plane path, attestation, namespace migration, 3P-OAuth, session-id, multi-parser routing, upstream-header identity, caching, or JWT on this page. Checked the full 45-line page and the DeleteKeyPair IAM block.
- **Lens O (audit):** adjacency only — D1 notes that post-delete the control-plane inventory under-reports a still-live credential; no CloudTrail text on the page itself (confirm against the general EC2 CloudTrail reference if a hunter needs it — doc-gap, not a page claim).
- **Lens P (proofing):** the console type-`Delete`-to-confirm field is a UI-only gate with no API equivalent (noted in §4, informational); not an anti-abuse workflow.
- **Open doc-gap carried for the hunter (D2):** AWS does not document the authz-evaluation ordering of `ec2:KeyPairName` relative to `KeyPairId`→name resolution for `DeleteKeyPair`. Settle at the `iam:SimulateCustomPolicy` stage before any canary. This is the single most valuable net-new question on the page.
- **Offline==online:** `delete-key-pair.md` offline == live `.md` (2026-10-15), no drift.
```
