---
name: eventbridgev2-unreachable
description: EventBridge v2 (eventbridgev2, API 2025-05-15) is NOT deployed/reachable in accounts A/B us-east-1 — availability probe BLOCKED all leads (run 2026-10-02)
metadata:
  type: project
---

EventBridge v2 attack plan (`/work/aws-docs/EventBridgeV2-attack-research-plan.md`, API `2025-05-15`) was availability-probed 2026-10-02 against A (183174222929) and B (289531347876), us-east-1. **Verdict: service NOT REACHABLE — every lead (L1-L5, G1, H1, T1, N1 + the finding-004 v2 re-tread) is BLOCKED on availability.** No resources created; teardown is a no-op.

Evidence:
- **No botocore client** (botocore/awscli 1.43.95): only `events` (legacy, API 2015-10-07) and `schemas`. No `eventbridgev2` model, no `2025-05-15` event model bundled anywhere.
- **Dedicated endpoint NXDOMAIN** in every form: `eventbridgev2.{us-east-1,us-west-2,eu-west-1,us-east-2,ap-southeast-2}.{amazonaws.com,api.aws}`, `eventbridgev2.amazonaws.com`, `eventbridge-v2.*`, `event-bus.*`, `eventbus.*`. Only `events.us-east-1.amazonaws.com` resolves (legacy, 44.216.196.176).
- **Not co-hosted on legacy awsjson frontend.** Doc shape = awsjson (body-only params, no HTTP URI → JSON-RPC, targetPrefix style). Signed JSON1.1 probes to `events.us-east-1.amazonaws.com` for v2-only ops (`CreateSubscriber`, `PutRawEvents`, `PutResourcePolicy`, `RevokeResource`, `ListSubscribers`) under prefixes `AWSEvents / AWSEventsV2 / EventBridge / EventBridgeV2 / AmazonEventBridgeV2 / AWSEvents20250515` ALL returned HTTP 400 `{"__type":"UnknownOperationException"}`.
- **Positive control:** same harness, `AWSEvents.ListEventBuses` on the legacy endpoint → HTTP 200 `{"EventBuses":[{"Arn":"arn:aws:events:us-east-1:183174222929:event-bus/default",...}]}` (rid eda1a1e2-...). So harness + signing name `events` work; UnknownOperation is specific to v2 ops.

Legacy EventBridge (`events`, 2015-10-07, protocol json1.1, targetPrefix `AWSEvents`, endpoint `events`, serviceId EventBridge) IS deployed and functional. It has CreateEventBus/PutEvents/ListEventBuses/PutPermission but NOT the v2 ops. The prior legacy finding-004 (API-destination connection-secret exfil) remains the only confirmed EventBridge issue; v2 cannot be tested to see if it reintroduces that primitive.

SigV4 hand-craft helper used: `/tmp/sig.py` (AWSRequest + SigV4Auth, urllib3, prints status/rid/ts). Reusable pattern; see [[omni-nsm-probing-facts]] and [[aws-env-setup]].

**To unblock:** re-probe once the service is actually provisioned — need either a botocore model (`eventbridgev2`) or a resolving endpoint host; then re-run L1-L5/G1/H1/T1/N1.
