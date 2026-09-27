# Amazon RDS — Monitoring Events — Attack Research Plan

**Source of leads:** `docs.aws.amazon.com/AmazonRDS/latest/UserGuide/working-with-events.html` and its sub-tree, read from the offline mirror `/work/aws-docs/docs/AmazonRDS/latest/UserGuide/` and cross-checked online. Pages consumed:
- `working-with-events.md` (hub: Monitoring RDS events)
- `USER_Events.md`, `USER_Events.overview.md` (event notification overview + EventBridge JSON examples)
- `USER_Events.GrantingPermissions.md` (SNS topic policy — **confused-deputy artifact**)
- `USER_Events.Subscribing.md`, `USER_Events.AddingSource.md`, `USER_Events.RemovingSource.md`, `USER_Events.Modifying.md`, `USER_Events.Deleting.md`, `USER_Events.ListSubscription.md`, `USER_Events.ListingCategories.md`
- `USER_Events.TagsAttributesForFiltering.md` (message attributes + event tags)
- `USER_ListEvents.md` (Viewing events / `DescribeEvents`)
- `USER_Events.Messages.md` (event categories + message catalog)
- `rds-cloud-watch-events.md` (EventBridge rule + tutorial)
- `cross-service-confused-deputy-prevention.md`
- API Reference `CreateEventSubscription` (parameters, errors, cross-account sample).

**Status:** documentation-derived hypotheses only; nothing has been tested against a live account.

---

## 0. How to use this document

- Each lead: **Claim → Mechanism (doc evidence) → Confirm/Refute oracle → Preconditions → Cost → Severity-if-true → Stop condition.** Work in priority order (Section 5 is ordered). Look left and right for adjacent bugs.
- **HARD STOP:** the moment evidence shows an identity/credential/ARN/account belonging to AWS's **own service plane** (e.g. the `events.rds.amazonaws.com` / `rds.amazonaws.com` fleet identity signing to a target you chose, or reaching the RDS control plane), stop, preserve evidence, and flag for AWS-Security disclosure. Do not exploit beyond existence.
- This feature is a **notification/observability fan-out**, not a data-plane. Its boundary story is almost entirely about **which principal is allowed to publish/deliver an event where**, and **whether downstream automation trusts event content**. Keep the SNS/EventBridge boundary in view on every lead — much of the enforcement lives in a *resource policy the customer authors*, which is exactly where confused-deputy and cross-account leads concentrate.

---

## 1. Pentest Objectives (boundary-breach goals, concrete)

1. **Cross-account event injection / confused deputy:** cause RDS in an attacker account to publish (via `events.rds.amazonaws.com`) into a *victim* account's SNS topic or EventBridge bus, so victim-side automation (Lambda/SQS/Step Functions) processes an attacker-triggered or attacker-named event.
2. **Cross-tenant subscription / event read:** create a subscription (or `DescribeEvents` / `DescribeEventSubscriptions`) that returns events or subscription config for a resource the caller does not own.
3. **Detection evasion:** perform a security-relevant RDS mutation that produces **no event**, an **out-of-order** event, or a **dropped** event — defeating a customer detection pipeline built on RDS events.
4. **Downstream trust abuse:** get attacker-chosen strings (resource identifier, `Message`, tags) into an event body that a downstream consumer parses for an authorization/routing/business decision.
5. **IAM-artifact defect:** find that an AWS-authored sample policy / EventBridge role snippet in these pages ships an over-broad or under-scoped grant a customer copies verbatim.
6. **Doc-vs-enforcement gap:** find a security guarantee the pages assert ("only … same account", "delivered in near-real time") that no mechanism actually enforces.

---

## 2. Components, Assets, and Design

### Customer-facing interface
RDS control-plane API (SigV4, `rds.<region>.amazonaws.com`) event-subscription actions + read actions. No new data-plane; delivery rides **Amazon SNS** and **Amazon EventBridge** (the default bus `aws.rds` source).

### Processes / owners
- **RDS control plane (service account/fleet)** — emits events; publishes to SNS/EventBridge under an **RDS service principal**. Two distinct principals appear in the docs:
  - `events.rds.amazonaws.com` → holds `sns:Publish` on the destination topic (see `USER_Events.GrantingPermissions.md`).
  - `rds.amazonaws.com` → `sts:AssumeRole` in the generic confused-deputy example (`cross-service-confused-deputy-prevention.md`).
- **Amazon SNS topic (customer-owned, possibly cross-account)** — resource-policy-gated publish target. Its topic policy is the **primary access-control artifact** for event notification.
- **Amazon EventBridge default bus** — receives `source:"aws.rds"` events "in near-real time"; rules + targets are customer-owned (`rds-cloud-watch-events.md`).
- **Downstream consumers** — email/SMS/HTTP(S) endpoints (SNS), Lambda, SQS, Step Functions, EventBridge targets — parse event bodies.

### Assets
- Event **content**: `account`, `region`, `SourceArn`, `SourceIdentifier`, `SourceType`, `EventCategories`, `EventID`, free-text `Message` (e.g. *"Updated parameter time_zone to UTC…"*, *"Deleted manual snapshot"*), and **resource tags "current state … when the notification is sent."**
- **Subscription config**: `SubscriptionName`, `SnsTopicArn` (may be cross-account), `SourceType`, `SourceIds`, `EventCategories`, `Enabled`, tags.
- Trust asset: downstream automation's implicit trust that a `source:"aws.rds"` event with a given `account`/`SourceArn` is genuine and owner-scoped.

### Resource-identifier shapes
- Subscription is named by `SubscriptionName` (customer-chosen string, `<255` chars) and by `SnsTopicArn`.
- `SourceIds` are **plain resource *names*** (`DBInstanceIdentifier`, `DBClusterIdentifier`, `DBSnapshotIdentifier`, `DBParameterGroupName`, `DBSecurityGroupName`, `DBClusterSnapshotIdentifier`, `DBProxyName`) — **account-scoped, not ARNs** → resolved within the caller's account. Naming rule: "begin with a letter … only ASCII letters, digits, hyphens … can't end with a hyphen or contain two consecutive hyphens."
- Events surface the **full resource ARN** (incl. account id) in the `Resource` message attribute and `SourceArn`.

### Identity
SigV4 IAM for all RDS control-plane calls. Delivery leg uses **RDS service-principal identity** publishing to SNS/EventBridge — the confused-deputy-sensitive hop. No `iam:PassRole` in the subscription APIs themselves (delivery auth is on the *topic/bus resource policy* side).

### ASCII pipeline
```
                            (RDS service fleet identity)
 attacker/victim RDS  --emits event-->  RDS control plane
      resource                              |
                                            | publish as events.rds.amazonaws.com
                                            |   (gated ONLY by SNS topic policy)
                        +-------------------+--------------------+
                        v                                        v
                Amazon SNS topic                        EventBridge default bus
             (customer-owned, may be                    source:"aws.rds"
              CROSS-ACCOUNT: sample shows                     |
              topic acct 802… vs sub acct 803…)               | rule + target(role)
                        |                                      v
        email / SMS / HTTPS / Lambda / SQS          Lambda / SQS / SFN / cross-acct bus
              (parses event body)                     (parses event body, may PassRole)
```

---

## 3. Trust-Boundary Map

| From (actor / zone) | To (resource / zone) | Crossing mechanism | **Breach oracle** |
|---|---|---|---|
| Attacker AWS account (its own RDS) | Victim account's SNS topic | `events.rds.amazonaws.com` `sns:Publish`, gated only by the topic's resource policy | An event triggered/named by the attacker is delivered into the victim's topic → **cross-account confused-deputy breach** |
| Attacker AWS account (its own RDS) | Victim account's EventBridge bus | cross-account bus resource policy / `source:"aws.rds"` | A `source:"aws.rds"` event from the attacker lands on the victim bus and matches a victim rule |
| Caller | `SourceIds` naming another account's resource | `CreateEventSubscription`/`AddSourceIdentifierToSubscription` resolves the name | Subscription accepts and delivers events for a resource the caller does not own (expected NULL — names are account-scoped; prove or refute) |
| Caller | Another account's/tenant's events | `DescribeEvents`, `DescribeEventSubscriptions` | Read returns an event/subscription for a resource the caller does not own |
| RDS service fleet identity | Attacker-chosen `SnsTopicArn` | `SNSNoAuthorization` publish-permission check at create time | RDS's fleet identity is coerced to publish to a target the caller could not publish to directly (**service-plane hard stop if the fleet identity is the lever**) |
| Downstream consumer (trusted) | Attacker-influenced event body | consumer parses `SourceIdentifier`/`Message`/tags | Consumer makes an authz/routing/business decision on an attacker-chosen string |
| Any customer surface | RDS control plane / AWS service plane | (should be none) | Any RDS-fleet credential/ARN/account reached = **hard stop, disclose** |

---

## 4. API / Interface Inventory

| Name | Method | Mut/Non-mut | Int/Ext | Functionality | Callable from Internet | Authorized callers | Notes |
|---|---|---|---|---|---|---|---|
| `CreateEventSubscription` | POST (SigV4) | Mutating | External | Create subscription (`SnsTopicArn` req, `SourceType`, `SourceIds`, `EventCategories`, `Enabled`, `Tags`) | Yes | IAM principal w/ `rds:CreateEventSubscription` | **`SnsTopicArn` may be cross-account** (API sample: topic 802… vs owner 803…). `SNSNoAuthorization`/`SNSTopicArnNotFound`/`SNSInvalidTopic`/`SourceNotFound` errors. SourceType enum broader than UserGuide list. |
| `ModifyEventSubscription` | POST | Mutating | External | Change name, source ids, categories, **topic ARN**, enabled | Yes | owner IAM | Can re-point topic ARN post-create → re-validate publish auth? |
| `AddSourceIdentifierToSubscription` | POST | Mutating | External | Add a `SourceIdentifier` (name) | Yes | owner IAM | `SourceNotFound` existence oracle |
| `RemoveSourceIdentifierFromSubscription` | POST | Mutating | External | Remove a source id | Yes | owner IAM | revocation completeness (Lens AA) |
| `DeleteEventSubscription` | POST | Mutating | External | Delete subscription | Yes | owner IAM | |
| `DescribeEventSubscriptions` | POST | Non-mutating | External | List subscriptions (incl. `SnsTopicArn`) | Yes | owner IAM | account-scoped? confirm |
| `DescribeEvents` | POST | Non-mutating | External | Read events (`SourceIdentifier`, `SourceType`, `Duration`, `StartTime`/`EndTime`, `EventCategories`) | Yes | owner IAM | 14-day retention; enumeration oracle? (subagent-covered) |
| `DescribeEventCategories` | POST | Non-mutating | External | List categories (no required params) | Yes | any | enumerates category taxonomy |
| EventBridge rule/target (`events:PutRule`, `PutTargets`) | — | Mutating | External | Route `aws.rds` events to targets | Yes | customer IAM | Target invocation role → **Lens B/PassRole** (subagent-covered) |

**Doc-vs-API surface delta (Step 3 "hunt the hidden knob"):** `CreateEventSubscription` `SourceType` valid values = `db-instance | db-cluster | db-parameter-group | db-security-group | db-snapshot | db-cluster-snapshot | db-proxy | zero-etl | custom-engine-version | blue-green-deployment`. The UserGuide *"RDS resources eligible for event subscription"* list only enumerates DB instance, DB snapshot, DB parameter group, DB security group, RDS Proxy, Custom engine version — **omitting `db-cluster`, `db-cluster-snapshot`, `zero-etl`, `blue-green-deployment`.** → Lens U informational delta; also confirm each accepted type actually emits events (a subscribable-but-silent type is a detection footgun).

---

## 5. Recommended Areas of Focus (one block per firing lens, priority order)

### Area 1 — Cross-account confused-deputy on the SNS publish hop  (Lens B / R / U)  — PRIORITY
**Background.** RDS delivers event notifications by having its service principal `events.rds.amazonaws.com` call `sns:Publish` on the destination topic. `USER_Events.GrantingPermissions.md`: *"By default, an Amazon SNS topic has a policy allowing all Amazon RDS resources within the same account to publish notifications to it. You can attach a custom policy to allow cross-account notifications, or to restrict access to certain resources."* The CreateEventSubscription API sample response shows a **live cross-account configuration** (SnsTopicArn account `802#########`, subscription `CustomerAwsId` `803#########`). The only create-time gate is the `SNSNoAuthorization` error (*"You do not have permission to publish to the SNS topic ARN"*).

**Security Concern.** The access-control decision for "whose RDS events may enter this topic" lives entirely in the **topic resource policy the customer authors** — the RDS side does not restrict the destination account. If a victim's topic policy allows `events.rds.amazonaws.com` to publish with a loose or missing `aws:SourceAccount`/`aws:SourceArn` condition, an **attacker in a different account can drive their own RDS events into the victim's topic** (confused deputy). AWS's own sample policy is the artifact customers copy — audit whether it fails safe, whether the wildcard guidance (`arn:aws:rds:*:{{123456789012}}:*`) genuinely pins the owner account, and whether the two documented principals (`events.rds.amazonaws.com` vs `rds.amazonaws.com`) are used consistently.

**High-level Test Scenarios (falsifiable):**
- **Claim:** With a victim SNS topic policy that grants `events.rds.amazonaws.com` `sns:Publish` conditioned only on `aws:SourceArn ArnLike arn:aws:rds:*:*:*` (no `aws:SourceAccount`), an RDS event from *any* account is accepted. → **Mechanism:** GrantingPermissions sample + confused-deputy page's wildcard guidance. → **Oracle:** attacker account B `CreateEventSubscription` → topic in victim A succeeds (no `SNSNoAuthorization`) and a B-triggered event body is delivered to A's subscribers. → **Precondition:** loose victim topic policy. → **Cost:** low. → **Severity:** cross-account injection into victim automation = **High**. → **Stop:** on first delivered cross-account event; do not flood.
- **Claim:** The auto-created default topic policy (when the RDS console creates the topic) omits `aws:SourceArn`/`aws:SourceAccount`, or scopes only by owner account, leaving `events.rds.amazonaws.com` publish open to same-account resources the operator did not intend. → **Oracle:** inspect the actual generated topic policy; check whether cross-account publish is denied by default. → **Severity:** Medium (same-account) / High (if cross-account default-open).
- **Claim (Lens R artifact audit):** The GrantingPermissions sample policy, copied verbatim, is well-formed only if the customer substitutes *both* `SourceArn` and `SourceAccount`; the ARN-wildcard variant still pins the account, so a customer who supplies `arn:aws:rds:*:{{VICTIM_ACCT}}:*` is protected — **confirm the account segment is mandatory** and there is no documented `arn:aws:rds:*:*:*` example that drops account pinning. → **Oracle:** re-read every printed policy; flag any wildcard that leaves the account segment `*`. → **Severity:** Informational→Medium if a wildcard example drops the account.
- **Claim (Lens U principal consistency):** `events.rds.amazonaws.com` (SNS publish) and `rds.amazonaws.com` (AssumeRole) are distinct principals; a customer copying the confused-deputy `rds.amazonaws.com` template onto a *topic* policy grants nothing (fails closed) — but a doc that mixes them could produce a non-enforcing policy the customer believes is protective. → **Oracle:** verify each page uses the correct principal for its resource type. → **Severity:** Low (doc integrity) but enables a false sense of protection.

**Doc evidence:** `USER_Events.GrantingPermissions.md` (default-policy sentence + sample), `cross-service-confused-deputy-prevention.md`, `CreateEventSubscription` sample (802 vs 803), `SNSNoAuthorization` error.  **Severity-if-true:** High.

### Area 2 — Downstream trust of attacker-influenced event content  (Lens CC / K / A)
**Background.** Event bodies carry `SourceIdentifier` (a resource *name* the resource owner chooses), a free-text `Message`, `SourceArn`/`account`, and **tags** ("RDS adds the current state of the tags in the message body when the notification is sent"). Consumers (Lambda, HTTPS endpoints) parse these. Combined with Area 1, attacker-account events (with attacker-chosen names/tags) can reach a victim consumer.
**Security Concern.** A downstream consumer that keys an authorization, routing, or business decision on `SourceIdentifier`, `Message` substrings, or tag values trusts a field the *event producer* controls. `source:"aws.rds"` and the `account` field look authoritative but, on a loose topic/bus (Area 1), the producing account may not be the consumer's.
**High-level Test Scenarios:**
- **Claim:** A consumer that treats `detail.SourceIdentifier` as an owned-resource name can be fed an attacker-named instance (e.g. a name colliding with a victim resource, or a string with control characters) → mis-routing / injection into logs/downstream systems. → **Oracle:** craft an instance name with delimiter/format-string/JSON-breaking chars and observe consumer parsing. → **Severity:** depends on consumer; up to High if it drives an action.
- **Claim:** `Message` free text (e.g. *"Updated parameter time_zone to UTC with apply method immediate"*) is not schema-constrained and can carry parameter *values* the owner set → a consumer surfacing `Message` verbatim (email/Slack/webhook) is a stored-content sink (log/HTML injection). → **Oracle:** set a parameter value / tag with markup and see if it renders unescaped downstream. → **Severity:** Low–Medium (Medium if it reaches a browser-rendered surface → XSS).
- **Claim (Lens A disclosure via `Resource` attribute):** the `Resource` message attribute exposes the **full ARN incl. account id**; on a cross-account/misconfigured topic this discloses the producing account/resource naming to a subscriber that should not see it. → **Oracle:** compare `Resource`/`SourceArn` account against the subscriber's account on a cross-account delivery. → **Severity:** Low (account-id/name disclosure).

**Doc evidence:** `USER_Events.overview.md` JSON examples; `USER_Events.TagsAttributesForFiltering.md`.  **Severity-if-true:** Medium (High when chained from Area 1 into an acting consumer).

### Area 3 — Stale-tag filtering divergence  (Lens I)
**Background.** `USER_Events.TagsAttributesForFiltering.md`: RDS adds *"the current state of the tags in the message body when the notification is sent"*, and `working-with-events.md`: *"Event notifications include tags from when the message was sent and may not reflect tags at the time when the event occurred."*
**Security Concern.** SNS/EventBridge **content-based filtering** and downstream ABAC-style routing keyed on event tags act on a **point-in-time snapshot** that may diverge from the tag state at the moment of the event. A subscriber relying on a tag filter (e.g. route "prod" events to an alerting path) can be **evaded or mis-routed** by mutating a tag between event occurrence and notification send.
**High-level Test Scenarios:**
- **Claim:** Removing/renaming a routing tag in the window between event occurrence and notification send causes the event to slip past an SNS filter policy keyed on that tag (detection evasion). → **Oracle:** subscribe with a filter policy `tag == prod`; trigger an event on a `prod`-tagged resource while flipping the tag; observe whether the notification is filtered out. → **Severity:** Medium (detection evasion), Low if only cosmetic.
- **Claim:** Email/SMS notifications *"will not have event tags"* (per doc Note) — a customer who built tag-based filtering assuming tags are present on all channels has a silent gap on email/SMS. → **Oracle:** compare tag presence across delivery channels. → **Severity:** Low (doc-vs-behavior).

**Doc evidence:** the two quoted sentences; email/SMS Note.  **Severity-if-true:** Medium.

### Area 4 — Detection blind spots: best-effort / missing / out-of-order events  (Lens O)
**Background.** `working-with-events.md` Note: *"Amazon RDS emits events on a best effort basis… they might be out of sequence or missing."* `USER_Events.overview.md`: *"Amazon RDS doesn't guarantee the order of events… subject to change"* and delivery *"might take up to five minutes."* FIFO topics are **not supported** (`CreateEventSubscription` doc).
**Security Concern.** Any customer security control built on RDS events (detecting a rogue snapshot copy, a public-accessibility flip, a master-password change, a parameter-group change) inherits a **producer-side blind spot**: an attacker action may generate no event, a delayed event (>5 min), or an out-of-order event that defeats correlation. This is not a bug to fix but a boundary to characterize — and it becomes a *finding* if a security-relevant category is entirely missing from the catalog (subagent-covered enumeration).
**High-level Test Scenarios:**
- **Claim:** A security-relevant mutation (e.g. modify DB to `PubliclyAccessible=true`, rotate master password, alter a security group, share a snapshot) produces **no event** in any subscribable category → a detection pipeline never fires. → **Oracle:** enumerate `USER_Events.Messages.md` categories vs the set of security-relevant `Modify*`/`Create*` actions; any action with no corresponding event = blind spot. → **Severity:** Low–Informational alone; enabler for a higher-severity evasion.
- **Claim:** The ≤5-minute delivery delay and best-effort drop let an attacker complete an action and tear down evidence before the event lands. → **Oracle:** measure delivery latency and drop behavior under load. → **Severity:** Informational (evasion enabler).

**Doc evidence:** best-effort/order/latency/FIFO quotes.  **Severity-if-true:** Low–Informational (raises severity as an enabler).  *(Deep category enumeration → subagent section below.)*

### Area 5 — Subscription-config isolation & revocation completeness  (Lens A / AA)
**Background.** `SourceIds` are account-scoped names; `DescribeEventSubscriptions` lists the caller's subscriptions incl. `SnsTopicArn`. `Remove/AddSourceIdentifier` mutate membership; `ModifyEventSubscription` can re-point the topic ARN.
**Security Concern.** Two shapes: (a) cross-tenant read/modify of a subscription or its events; (b) revocation completeness — does removing a source or disabling a subscription actually stop delivery, and does re-pointing the topic ARN (`ModifyEventSubscription`) re-run the `SNSNoAuthorization` publish check?
**High-level Test Scenarios:**
- **Claim:** `ModifyEventSubscription` re-points `SnsTopicArn` to a topic the RDS principal cannot publish to (or to a cross-account topic) **without** re-validating publish authorization → events silently stop, or start flowing cross-account. → **Oracle:** modify to a foreign/unauthorized topic; check for `SNSNoAuthorization` at modify time vs create time. → **Severity:** Medium (delivery integrity / cross-account).
- **Claim (Lens A, expected NULL):** `AddSourceIdentifierToSubscription` accepts a `SourceIdentifier` naming a resource in another account and delivers its events. → **Oracle:** add a foreign-account resource name; observe `SourceNotFound` vs acceptance. **Expected refute** (names resolve within the caller's account) — record as null hypothesis unless proven. → **Severity:** High if it *doesn't* refute.
- **Claim (Lens AA):** After `RemoveSourceIdentifierFromSubscription` / `Enabled=false`, delivery for that source actually ceases immediately (no lingering delivery). → **Oracle:** remove/disable, then trigger the source event, confirm no notification. → **Severity:** Low (revocation completeness).

**Doc evidence:** `USER_Events.Modifying.md`, `AddingSource/RemovingSource`, `Deleting.md`, `CreateEventSubscription` errors.  **Severity-if-true:** Medium.

### Area 6 — EventBridge integration (rules, targets, roles, cross-account bus)  (Lens B / R / A / CC)
*Deep-dive delegated to a subagent; findings merged below. Baseline concerns: a target **invocation role** the customer copies from the tutorial (PassRole / over-broad `Resource`), cross-account event-bus delivery, and downstream trust of the `source:"aws.rds"`/`account` fields on a bus that also accepts customer `PutEvents` (event spoofing).*

**Boundary note.** `rds-cloud-watch-events.md` documents a *customer-authored automation seam*, not an RDS API: RDS emits `source:"aws.rds"` events onto the customer's default EventBridge bus; the customer writes a rule (event-pattern match) → target (Lambda/SNS/SQS/Step Functions), and **EventBridge (not RDS) invokes the target using an IAM role**. Page verified byte-identical online (no drift). **No IAM/event-pattern/CFN JSON is printed on the page** — the console click-path is opaque about what it creates (this is a *doc-gap* for Lens R, not a clean null: the artifacts exist but can't be audited from the docs). Trust-relevant crossings: (1) RDS event → bus (delivery guarantee, O/U); (2) rule → IAM role → target (PassRole/confused-deputy, B); (3) event fields (`source`,`account`,`detail.SourceArn`) → downstream authz logic that trusts them (CC).

**B-1 — auto-created "role for this specific resource" may be under-scoped (Lens B, PRIORITY-adjacent).**
- **Claim:** The EventBridge-auto-created invocation role is not actually scoped to the one rule/target pair — trust policy `Principal: events.amazonaws.com` may lack an `aws:SourceArn` condition tying it to the originating rule ARN, and/or the permission policy wildcards the target `Resource` (`lambda:InvokeFunction` on `*`) instead of pinning the one function ARN.
- **Mechanism:** step 7 offers *"Create a new role for this specific resource"* / *"Use existing role"* — UI labels, never the resulting JSON. Customer accepts a role whose contents they never see.
- **Oracle:** run the tutorial exactly, then `iam:GetRole` + `GetRolePolicy`/`GetPolicyVersion` on the generated role. (a) trust policy conditioned on `aws:SourceArn = this rule ARN` or unconditioned? (b) permission `Resource` pinned or wildcarded? Safe first check: `iam:SimulatePrincipalPolicy` against a *different* Lambda ARN in-account.
- **Precondition:** console `PutRule`+`PutTargets`. **Cost:** trivial. **Severity:** Medium (same-account least-priv gap in an AWS-generated, not customer-authored, artifact) → **High** if the missing `SourceArn` condition lets a *different attacker-created rule* reuse the role to invoke a target the attacker couldn't `iam:PassRole` for directly (classic confused-deputy chain). **Stop:** refuted if resource is pinned to the exact target ARN AND trust policy carries rule-scoped `aws:SourceArn`.
- *(Lambda execution role "basic Lambda permissions" = CloudWatch-Logs-only, benign — not pursued.)*

**CC-1 — downstream automation cannot distinguish a genuine RDS event from a same-account `PutEvents` forgery (Lens CC / K, PRIORITY).**
- **Claim:** A rule matching `source:"aws.rds"`, `detail-type:"RDS DB Instance Event"` fires equally on a customer/attacker `events:PutEvents` call that fills the same fields — the sample payload shows `source`/`account`/`detail.SourceArn` as ordinary JSON with **no signature or provenance marker**, and no RDS page claims EventBridge validates a `PutEvents` caller's asserted `Source` against the calling identity.
- **Mechanism:** verbatim sample event in `rds-cloud-watch-events.md` step 3 (`"source":"aws.rds"`, `"account":"111111111111"`, `"detail":{"SourceArn":"...","Message":"DB instance stopped"}`); tutorial Lambda just logs `JSON.stringify(event)` — zero authenticity check modeled.
- **Oracle:** from a same-account principal with `events:PutEvents` on the target bus, `PutEvents` an entry replicating the sample shape (fabricated `SourceArn`/`Message` for an instance the caller doesn't own) → does the tutorial's rule fire and the consumer act on the forged event identically? Yes ⇒ pattern-match has no provenance check; the security decision (`source=aws.rds`) is asserted by the same plane that consumes it.
- **Precondition:** any `events:PutEvents` grant on the bus (see R-1 below — plausibly over-broad in an AWS-published policy) + a tutorial-shaped rule with no consumer-side validation. **Cost:** trivial (one call). **Severity:** **High** if any automation built exactly as the tutorial recommends takes a privileged action (auto-remediation, paging, access change) keyed off the forged `detail-type`/`source`/`Message`. Doc-shape hypothesis — the tutorial itself models zero validation. **Stop:** refuted only if EventBridge is confirmed (via its own service docs) to reject/rewrite a caller-`PutEvents` claiming an `aws.*` `Source`; even then, note the consumer-side no-validation as a Lens U doc-gap.

**R-1 — adjacent AWS-published policy: RDS Custom for Oracle instance profile grants `events:PutEvents` on `Resource:"*"` (Lens R/S).** *(Different feature/page `custom-setup-orcl.md`, flagged because it is the concrete primitive that arms CC-1.)*
- **Claim:** The AWS-published RDS-Custom-for-Oracle instance-profile policy (Sid "6") grants `events:PutEvents` unconditioned on `Resource:["*"]`, letting that role (living on customer compute) publish to **any** event bus in the account/region with no bus scoping.
- **Mechanism:** verbatim JSON — `{"Sid":"6","Effect":"Allow","Action":["events:PutEvents"],"Resource":["*"]}`.
- **Oracle:** static read already shows the defect; `iam:SimulatePrincipalPolicy` against `arn:aws:events:*:*:event-bus/*`, or a live `PutEvents` to a non-default bus, confirms reach. **Severity:** Medium (over-broad, same-account) and it directly supplies the `PutEvents` primitive for CC-1. **Stop:** refuted if a newer revision scopes `Resource` to the specific bus.

**O / U — best-effort delivery + unenforced "near-real time" (matches Areas 4/7).** `working-with-events.md`: *"Amazon RDS emits events on a best effort basis… out of sequence or missing"* immediately after *"delivers events to EventBridge in near-real time"* — the timeliness claim is prose with no SLA/queue/retry model and no delivery-receipt API to verify it. Any EventBridge automation built on this tutorial (alert/remediate on `"Message":"DB instance stopped"`) can silently never fire. Enabler multiplier for every delivery-dependent lead; grep confirmed no RDS-event DLQ/retry/guarantee guidance anywhere in the mirror.

**Lens A / D–FF — N/A for this page** (null, pages checked `rds-cloud-watch-events.md`+`working-with-events.md`): no resource-by-ID API, no shared multi-tenant bus, no cross-account bus routing documented for the DB-event path (`account` field is informational echo, not an addressable parameter); thin console tutorial with no network/RBAC/KMS/prompt/upload/attestation/TLS/lifecycle/cache/JWT surface. Real surface concentrates in B, R/S, CC, O, U.

### Area 7 — Event data content & viewing (DescribeEvents, message catalog, tags)  (Lens O / A / T / U / I)
*Deep-dive delegated to a subagent; findings merged below. Baseline concerns: which security-relevant operations do/don't emit events (blind-spot enumeration), what sensitive data the `Message`/tags disclose, and whether `DescribeEvents` is strictly account-scoped.*

**What events carry (per `USER_ListEvents.md` / `USER_Events.Messages.md` / `USER_Events.TagsAttributesForFiltering.md`, no drift):** `SourceIdentifier`, `SourceType`, `SourceArn` (full ARN incl. account+region), `Date`, `EventCategories[]`, free-text templated `Message` (`{{name}}`/`{{value}}`/`{{message}}` filled with real config/resource data). Routed to SNS/EventBridge: message **attributes** `EventID`+`Resource`(ARN) alongside body, plus resource's **current tags in the body**. Native `DescribeEvents` retention **14 days** (console: 24h / "recent events" 2 wk); longer requires forwarding to EventBridge — RDS events are **not a durable log store**. `DescribeEvents` `SourceType` enum: `db-instance | db-parameter-group | db-security-group | db-snapshot | db-cluster | db-cluster-snapshot | custom-engine-version | db-proxy | blue-green-deployment | db-shard-group | zero-etl` — **no VPC/modern security-group source type at all**.

**O-1 — category mislabeling defeats `EventCategories=["security"]` detection (Lens O, PRIORITY within this area).**
- **Claim:** A pipeline subscribed to category `security` receives *nothing* for master-credential resets, legacy security-group changes, KMS-access failures, or TDE key rotation — because none are tagged `security`.
- **Mechanism:** across the *entire* `USER_Events.Messages.md` catalog the **`security` category contains exactly one event** — RDS-EVENT-0068 *"Decrypting hsm partition password…"*. Everything else is elsewhere: master-cred reset RDS-EVENT-0016 = **configuration change**; legacy SG RDS-EVENT-0038/0039 = **configuration change/failure**; TDE rotate RDS-EVENT-0064 = **notification**; KMS-access-fail RDS-EVENT-0418/419/420 = **availability/failure**.
- **Oracle:** subscribe category `security` only; reset master creds / rotate TDE key; confirm zero events on that channel while unfiltered `describe-events` shows them under another category. **Cost:** trivial. **Severity:** Low–Informational alone (Lens O cap) but an AWS-documented evasion enabler that raises severity of any chained credential/config attack relying on a `security`-scoped filter. **Stop:** generalize after one reproduction.

**O-2 — structural blind spot: public-exposure / network / protection toggles emit NO event (Lens O).**
- **Claim:** Adding `0.0.0.0/0` ingress to the instance's VPC security group, flipping `PubliclyAccessible=true`, disabling **deletion protection**, or disabling **IAM database authentication** leaves **no RDS-native event** — absent, not just miscategorized.
- **Mechanism:** exhaustive review of every table in `USER_Events.Messages.md` shows no message for these four; the `DescribeEvents` `SourceType` enum has **no security-group/network-exposure type at all**.
- **Oracle:** `ModifyDBInstance` for each of the four on a test instance, then `describe-events --source-type db-instance --duration 20160`; absence (vs CloudTrail, which *does* log the API call) confirms. **Severity:** Low–Informational per cap, flagged as an **enabler for the single most common high-impact RDS misconfig (public exposure) going undetected** by anyone relying on RDS Events rather than CloudTrail/Config. **Stop:** doc-completeness gap — no further live refinement needed.

**A-1 — Secrets Manager ARN disclosure via event `Message` (Lens A/T).**
- **Claim:** RDS-EVENT-0327 *"Amazon RDS could not find the secret {{SECRET ARN}}."* puts a full Secrets Manager ARN into plaintext `Message`, readable by any principal with only `rds:DescribeEvents`, regardless of any `secretsmanager:*` permission on that secret.
- **Oracle:** break/delete a referenced secret to trigger the failure; `DescribeEvents` under a principal with `rds:DescribeEvents` but explicit `Deny` on `secretsmanager:GetSecretValue`/`DescribeSecret` — confirm the ARN string is still readable (reconnaissance primitive). **Severity:** Low (ARN, not secret value, same-account); chain start-point for Secrets-Manager reachability (routes to that service's owner).

**A-2 — parameter-value disclosure bypassing `DescribeDBParameters` scoping (Lens A/T).**
- **Claim:** RDS-EVENT-0037 *"Updated parameter {{name}} to {{value}} with apply method {{method}}."* discloses the literal new parameter value to any `rds:DescribeEvents` holder even if denied `rds:DescribeDBParameters`/`ModifyDBParameterGroup` on that group.
- **Oracle:** set an operationally sensitive parameter under a role denied param-group read; confirm value visible via `DescribeEvents`. **Severity:** Low–Medium by parameter sensitivity — least-priv footgun class; escalates to an AWS defect **iff** a default AWS-managed read-only RDS policy grants `DescribeEvents` while intending to withhold parameter values (**doc-gap — needs the IAM Actions/Resources/Conditions page**).

**A-3 — cross-account enumeration via `DescribeEvents` = NULL.** API request shape (`SourceIdentifier`+`SourceType`) has no account parameter; identifiers are account+region-namespaced; SigV4 scopes to caller's account. **Residual open lead (doc-gap):** whether IAM resource-level ARN `Condition` on `rds:DescribeEvents` is enforced *per-`SourceIdentifier`* within one account (can a role scoped to `db:allowed-instance` still `DescribeEvents` with `SourceIdentifier=other-instance`?) — needs the RDS IAM actions/resources reference page.

**I-1 — stale-tag SNS/EventBridge filter-policy bypass (Lens I, chains O+U).**
- **Claim:** An actor who can retag a resource can route a security event's notification *away* from its intended alert destination by changing the tag between the triggering action and the async best-effort send.
- **Mechanism:** `working-with-events.md` *"Event notifications include tags from when the message was sent and may not reflect tags at the time when the event occurred"* + `TagsAttributesForFiltering.md` *"RDS adds the current state of the tags in the message body when the notification is sent"* — combined with SNS payload / EventBridge content filtering being the *documented, encouraged* tag-routing mechanism.
- **Attack:** trigger a security event on a resource tagged `AlertTier=critical` (matched by the SecOps filter), then immediately `UntagResource`/`TagResource` before the best-effort notification sends → filter evaluates the *new* tag, alert never routes. **Oracle:** tag to match a filter policy, trigger a filtered-category event, immediately retag to non-matching, confirm the matching subscriber never receives it while an unfiltered one does. **Precondition:** `TagResource`/`UntagResource` + a tag-filtered security pipeline. **Cost:** trivial (best-effort async widens the race window — Lead U-1). **Severity:** **Medium** — alerting-suppression primitive, chains directly with O-1/O-2 (evade category *and* tag filtering together). **Stop:** demonstrate once; timing precision unnecessary (docs concede no ordering guarantee).

**I-2 — tag disclosure differs by SNS protocol (informational).** `TagsAttributesForFiltering.md`: *"The notification sent in an email or a text message will not have event tags"* ⇒ HTTPS/SQS/Lambda subscribers on the *same topic* get full current tags in the body while email/SMS don't. Diff payloads across protocols to confirm. Low/same-account — escalates to Lens A cross-account tag disclosure only if the topic policy allows cross-account subscription (→ Area 1).

**U-3 — `DescribeEvents` `Filters` parameter is a documented no-op (Lens U).** API ref: *"Filters.Filter.N — This parameter isn't currently supported."* A tool assuming server-side filtering silently over-fetches/under-filters rather than erroring — a data-handling correctness footgun, Informational. Also a doc-vs-doc inconsistency: UserGuide implies a 14-day (`--duration ≤20160`) hard cap while `API_DescribeEvents.html` states no max for `Duration` (Default 60) — worth a quick live clamp check.

**Lens B/…/FF — N/A for this area** (null, pages checked `USER_Events.Messages.md`, `USER_ListEvents.md`, `USER_Events.TagsAttributesForFiltering.md`, `working-with-events.md`, `API_DescribeEvents`): no PassRole/role fields, KMS context, OAuth, LLM/prompt, upload, printed IAM JSON, attestation, TLS-version, share/revoke, JWT, cache, or predictable-namespace surface; cross-account addressing absent (A-3). Those lenses belong to the IAM-actions, subscription-creation (`USER_Events.md` — Area 1), and KMS pages.

---

## 6. Threat Model Test Objectives

| Threat / Test case | Component | Documented mitigation to attack |
|---|---|---|
| Cross-account RDS event injected into victim topic | SNS topic policy / `events.rds.amazonaws.com` publish | `aws:SourceArn` + `aws:SourceAccount` conditions (GrantingPermissions / confused-deputy sample) |
| RDS fleet identity coerced to publish to attacker target | `SNSNoAuthorization` create-time check | topic resource policy |
| Downstream consumer acts on attacker-chosen `SourceIdentifier`/`Message`/tag | event body → Lambda/HTTPS | none documented — consumer's responsibility |
| Detection evasion via missing/out-of-order/dropped event | RDS event producer | "best effort" disclaimer (no mitigation — inherent) |
| SNS filter bypass via stale tag snapshot | tag snapshot at send-time | none (documented as by-design) |
| Cross-tenant subscription/event read | `Describe*` account scoping | IAM (confirm scoping) |
| Re-point topic ARN without re-auth | `ModifyEventSubscription` | re-validate publish? (confirm) |
| Over-broad EventBridge target role copied from tutorial | tutorial IAM snippet | audit statement-by-statement (subagent) |

---

## 7. Out-of-Scope Risk Categories (state confidently)

- **SNS/EventBridge internals** — the confirmation-email/SMS subscription flow, SNS message signing, SNS/EventBridge fleet security: these are separate services' shared-responsibility surface; only RDS's *use* of them (topic-policy defaults, service principal, event content) is in scope here.
- **Shared RDS/Aurora/Grover data-plane infra** — not touched by this feature.
- **Customer-authored downstream automation bugs** — a customer's Lambda that mis-parses an event is the customer's defect *unless* the input crosses an AWS-owned trust boundary (Area 1/2).
- **Customer-authored SNS topic policy footgun** — a self-inflicted loose policy on the customer's *own* topic is a least-privilege footgun; it becomes in-scope only where the **AWS-authored sample/default** is the weak artifact (Area 1, Lens R).
- **Single-tenant self-DoS** — `EventSubscriptionQuotaExceeded` and per-account subscription caps.
- **IMDS / host-level** on managed RDS hosts.

---

## 8. Null Hypotheses / Doc Gaps

- **Lens G (SSRF):** no field on this surface is dereferenced server-side by RDS. `SnsTopicArn` is validated as an ARN and publish-authorized, not fetched; HTTP(S) delivery endpoints are dereferenced by **SNS**, not RDS. Pages checked: Subscribing, GrantingPermissions, overview, TagsAttributes. **N/A (SNS-owned delivery).**
- **Lens F (translation/injection), H (KMS confusion), W (attestation), Y (transport), BB (canonicalization), DD (cache), EE (predictable-name), FF (JWT):** no triggering mechanism on the events surface. (KMS appears only as a pointer to SNS SSE key permissions — SNS-owned; note it if the destination topic is SSE-encrypted and RDS must be granted `kms:GenerateDataKey`, but that grant is on the SNS/KMS side.) Pages checked: all sub-pages listed in Section 0. **N/A.**
- **Lens P (proofing):** the SNS subscription-confirmation email/SMS is the anti-abuse gate but is **SNS-owned**; RDS's `CreateEventSubscription` has no proofing step of its own. **N/A for RDS.**
- **Lens A cross-tenant via SourceIds:** expected NULL because `SourceIds` are account-scoped names resolved within the caller's account (`SourceNotFound` otherwise) — but explicitly listed as a lead to *refute*, not assume (Area 5).
- **Doc gaps to confirm on a live account first:**
  1. Whether `ModifyEventSubscription` re-validates `SNSNoAuthorization` when re-pointing `SnsTopicArn`.
  2. The exact contents of the **auto-created default topic policy** when the RDS console creates a topic (is cross-account publish denied by default?).
  3. Whether `DescribeEvents`/`DescribeEventSubscriptions` are strictly account-scoped (no cross-tenant leakage).
  4. Whether each API-accepted `SourceType` (`zero-etl`, `db-cluster`, `db-cluster-snapshot`, `blue-green-deployment`) actually emits subscribable events, and why they're absent from the UserGuide overview list.

---

*Sections 6/7 (EventBridge + Event-data deep dives) are populated from delegated subagent analysis below.*
