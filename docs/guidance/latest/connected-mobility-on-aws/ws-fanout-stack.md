---
source_url: https://docs.aws.amazon.com/guidance/latest/connected-mobility-on-aws/ws-fanout-stack.html
---

# WebSocket telemetry fan-out (WsFanoutStack)
<a name="ws-fanout-stack"></a>

The WsFanoutStack deploys an ECS Fargate task that consumes per-fleet Kafka topics and pushes live telemetry updates to connected Fleet Manager UI clients over WebSocket.

## Fan-out architecture
<a name="ws-fanout-architecture"></a>

The ECS Fargate worker maintains an active Kafka consumer group (`cms-{stage}-ws-fanout-consumer`) and subscribes to per-fleet telemetry topics derived from the MSK cluster. On each Kafka message, the worker queries the `cms-{stage}-storage-ws-connections` DynamoDB table to find all active WebSocket connection IDs for the vehicle’s fleet, then calls the API Gateway Management API (`@connections/{connectionId}`) to push the telemetry payload to each connected browser.

 **Key components:**
+  **MSK consumer** — Reads from per-fleet telemetry topics using SASL/IAM authentication.
+  **DynamoDB connections table** (`cms-{stage}-storage-ws-connections`) — Stores active connection ID, fleet ID, and connection timestamp for each connected client.
+  **API Gateway WebSocket API** — Manages WebSocket lifecycle (`$connect`, `$disconnect`, `$default` routes).
+  ** `$connect` Lambda authorizer** — A Cognito JWT REQUEST authorizer validates the `?token=<jwt>` query parameter on every WebSocket upgrade request. Connections without a valid token receive HTTP 401 and are rejected before establishing. Fleet-operator connections are scoped to their authorized fleet IDs from the JWT `custom:fleetIds` claim.

## WebSocket security posture
<a name="ws-fanout-security"></a>

Anonymous WebSocket upgrades are disabled by default. The `cms.allow_unauth_websocket` CDK context flag (default `false`) controls whether the `$connect` authorizer allows unauthenticated connections. Set this flag to `true` only for demo or development environments where anonymous map access is acceptable.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Connected Mobility on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
