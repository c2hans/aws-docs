---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/govern-tool-access-with-aws-agent-registry-metadata.html
---

# Governing AI agent tool quotas with AWS Agent Registry and Amazon Bedrock AgentCore Gateway
<a name="govern-tool-access-with-aws-agent-registry-metadata"></a>

*Prashanth Sivarajan, Amazon Web Services*

## Summary
<a name="govern-tool-access-with-aws-agent-registry-metadata-summary"></a>

AWS Agent Registry is a centralized catalog within Amazon Bedrock AgentCore that lets organizations register, discover, and govern AI agents, MCP servers, and the tools they expose. It stores rich metadata - including custom fields - on each registry record, supports lifecycle statuses (draft, approved, deprecated), and emits events as records change, giving platform teams a single control plane for the growing fleet of AI agents and tools in their environment.

As organizations scale to dozens or hundreds of AI agents, ungoverned tool access creates operational and financial risk. Without per-tool quotas, a single misconfigured agent can saturate a downstream API or drive unexpected costs, and there is no centralized place to define, approve, or audit those limits.

This pattern uses Agent Registry as a policy-as-metadata layer. You define quota policies (calls per hour, cost tier, burst limits) as custom metadata on tool records, use EventBridge-driven approval workflows to gate tool discoverability, and deploy a Gateway REQUEST interceptor that reads quota metadata and enforces limits with DynamoDB sliding-window counters. This gives platform teams a single, auditable control point that prevents runaway costs and protects shared infrastructure - without modifying agent code.

## Prerequisites and limitations
<a name="govern-tool-access-with-aws-agent-registry-metadata-prereqs"></a>

*Prerequisites*

*Preview notice:* *AWS Agent Registry is in Preview (launched April 2026). APIs, event schemas, and service limits described in this pattern may change before general availability. Do not use Preview services for production workloads that require stable API contracts. Verify all API names and behaviors against the *[*current documentation*](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html)* before implementation.*
+ An active AWS account with permissions to create and manage Amazon Bedrock AgentCore resources (Gateway, Agent Registry)
+ An existing Agent Registry with at least one MCP server record registered
+ Familiarity with the Model Context Protocol (MCP) and agent-to-tool invocation patterns
+ AWS CDK or AWS CloudFormation experience for deploying infrastructure
+ Basic understanding of Amazon DynamoDB, AWS Lambda, and Amazon EventBridge
+ An Amazon Bedrock AgentCore Gateway configured with at least one MCP target

*Limitations*

**Preview service:** AWS Agent Registry is in Preview (April 2026). The limitations below reflect Preview behavior and may change at GA.
+ **Interceptor latency.** The REQUEST interceptor adds a minor latency to every tool call (registry query \+ DynamoDB read/write). Mitigate with in-memory caching (60-second TTL) and provisioned concurrency.
+ **API names subject to change.** This pattern references API operations (`SearchRegistryRecords`, `GetRegistryRecord`, `UpdateRegistryRecordStatus`) and EventBridge detail types based on Preview documentation. Verify these names against the [current API reference](https://docs.aws.amazon.com/bedrock-agentcore/latest/APIReference/) before implementing, as they may change before GA
+ The pattern considers a single-region scope (no cross-region quota enforcement)
+  **Custom metadata size.** Registry record ‘inlineContent’ field is limited to 409,600 characters. Sufficient for quota policies but relevant if combining metadata with large schemas.

## Architecture
<a name="govern-tool-access-with-aws-agent-registry-metadata-architecture"></a>

The architecture uses AWS Agent Registry as the single source of truth for tool quota policies. Custom metadata schemas on registry records declare rate limits, cost tiers, and burst allowances. A Gateway REQUEST interceptor reads these policies at invocation time and enforces them with DynamoDB-backed sliding-window counters. EventBridge notifications trigger approval workflows that validate quota policies before tools become discoverable.

*Runtime quota enforcement*

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/45ced596-4b24-4993-9cf2-9df8c605402e/images/c7828209-9423-40c7-b9e8-a2f9d3b1ff1a.png)

1. **User **- Access the AI Agent via the business application

1. **AI Agent** - Invokes tools through the AgentCore Gateway.

1. **Amazon Bedrock AgentCore Gateway** - Routes tool calls through a REQUEST interceptor Lambda before reaching the MCP target.

1. **Amazon Bedrock AgentCore Identity** - Used to manage the inbound and outbound authentication.

1. **REQUEST Interceptor Lambda** - Queries the Agent Registry via the SearchRegistryRecords API for the target tool's quota metadata, reads and increments a DynamoDB counter, and either allows or denies the request based on quota limits.

1. **AWS Agent Registry** - Central catalog storing tool records with custom quota metadata (calls\_per\_hour, cost\_tier, burst\_limit). Exposes the SearchRegistryRecords API for programmatic lookup by the interceptor.

1. **Amazon DynamoDB** - Stores sliding-window usage counters keyed by agent ID \+ tool name \+ time window.

*Governance and approval workflow*

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/45ced596-4b24-4993-9cf2-9df8c605402e/images/2758bbbe-b717-42c6-a1d0-5f1144cab621.png)

1. **Publisher** - Submits tool records with quota metadata to the Agent Registry via the control-plane API.

1.   **AWS Agent Registry **- Receives the record, stores it in PENDING\_APPROVAL status, and emits a status change event to EventBridge.

1.  **Amazon EventBridge **- Receives record-submission events from Agent Registry and triggers a validation Lambda that validates quota metadata completeness before approving records.

1.   **Quota Validation Lambda **- Evaluates submitted records for required quota fields, rejects incomplete submissions, and approves well-formed records via the UpdateRegistryRecordStatus API.

1.  ** AWS Agent Registry** - Updates the record status to APPROVED (discoverable by agents) or REJECTED (with feedback to the publisher).

1.   **AWS CloudTrail **- Logs all registry control-plane operations, providing an audit trail of quota policy changes across the tool lifecycle.

*Cost considerations*
+ **DynamoDB**: On-demand pricing is recommended for unpredictable agent traffic. Please refer [Amazon DynamoDB Pricing](https://aws.amazon.com/dynamodb/pricing/) for detailed calculation.
+ **Lambda**: Use provisioned concurrency or Lambda SnapStart (Java) to minimize cold starts if latency is critical.
+ **Agent Registry**: No additional charge for custom metadata. SearchRegistryRecords API calls are included in AgentCore pricing.

## Tools
<a name="govern-tool-access-with-aws-agent-registry-metadata-tools"></a>

|
|
| AWS Service | Role in the pattern |
| --- |--- |
| Amazon Bedrock AgentCore Gateway | Routes agent tool calls; hosts REQUEST interceptor |
| AWS Agent Registry | Central catalog for tool records; stores quota policies as custom metadata |
| AWS Lambda | Implements the REQUEST interceptor that enforces quotas; implements the quota validation workflow triggered by EventBridge |
| Amazon DynamoDB | Stores sliding-window usage counters for rate limiting |
| Amazon EventBridge | Delivers record-submission events to trigger the validation Lambda |
| AWS CloudTrail | Provides audit trail of all registry changes |
| Amazon CloudWatch | Publishes quota metrics (invocations, denials) and triggers alarms |
| AWS CDK | Infrastructure as code for deploying the solution |

## Best practices
<a name="govern-tool-access-with-aws-agent-registry-metadata-best-practices"></a>

*Quota metadata design*
+ **Use a consistent JSON schema** for quota metadata across all tool records. Define a schema template that includes `calls_per_hour`, `cost_tier` (low, medium, high, premium), `burst_limit`, and `cooldown_seconds`.
+ **Version your schema.** Include a `schema_version` field in quota metadata so the interceptor can handle backward-compatible changes.
+ **Separate quotas by consumer tier.** Store multiple quota tiers (e.g., `standard`, `premium`) in the same record metadata, allowing the interceptor to select the appropriate limits based on the calling agent's identity.

*Rate-limiting strategy*
+ **Use DynamoDB TTL for automatic cleanup.** Set TTL on counter items equal to the window duration so expired counters are removed without manual intervention.
+ **Implement sliding windows, not fixed windows.** A sliding-window counter (current window count \+ weighted previous window count) avoids the burst-at-boundary problem inherent in fixed-window counters.
+ **Return retry-after headers.** When denying a request, include a `retry_after_seconds` value in the interceptor response so agents can implement exponential backoff.

*Governance workflow*
+ **Never auto-approve records without quota metadata.** Configure EventBridge rules that route submissions to the validation workflow; only records passing all quota checks are approved.
+ **Use DEPRECATED status for sunset.** When retiring a tool, deprecate the record rather than deleting it, preserving the audit trail and existing usage data.
+ **Validate on record synchronization.** When records synchronize with external MCP servers, trigger re-validation to ensure quota metadata remains intact after updates.

*Security and observability*
+ **Fail-open default.** The interceptor allows requests when the Agent Registry is unreachable, prioritizing agent availability over strict enforcement. For tools that modify production data or incur high costs, switch to fail-closed by denying requests when quota metadata cannot be retrieved.
+ **Scope interceptor permissions.** Grant the interceptor Lambda only `SearchRegistryRecords` on the registry resource, plus `dynamodb:GetItem`/`dynamodb:UpdateItem` on the DynamoDB counter table. The interceptor uses the `bedrock-agentcore` runtime client (not the control-plane MCP endpoint). *(Verify these IAM action names against current documentation - Preview APIs may change.)*
+ **Log quota denials to CloudWatch Metrics.** Publish custom metrics (tool name, agent ID, denial reason) for operational dashboards.
+ **Enable CloudTrail for compliance.** All UpdateRegistryRecordStatus calls (approvals, deprecations) are automatically logged, meeting audit requirements.

## Epics
<a name="govern-tool-access-with-aws-agent-registry-metadata-epics"></a>

### Define the quota metadata schema and register tools
<a name="define-the-quota-metadata-schema-and-register-tools"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Design the quota metadata JSON schema | 1. Define a JSON schema for tool quota metadata:<pre>{<br />  "schema_version": "1.0",<br />  "quotas": {<br />    "standard": {<br />      "calls_per_hour": 100,<br />      "burst_limit": 20,<br />      "cooldown_seconds": 60<br />    },<br />    "premium": {<br />      "calls_per_hour": 1000,<br />      "burst_limit": 200,<br />      "cooldown_seconds": 10<br />    }<br />  },<br />  "cost_tier": "medium",<br />  "rate_limit_strategy": "sliding_window"<br />}<br /></pre>1. Document the schema in your team's registry usage guidelines.<br />2. Validate that the schema works with Agent Registry's custom metadata field by creating a test record. | Cloud architect |
| Register MCP server tools with quota metadata | 1. Create or update MCP server records in Agent Registry with the quota metadata schema in the custom metadata field.<br />2. For each tool exposed by the MCP server, include tool-specific quota overrides in the record's custom metadata:<pre>{<br />  "tool_quotas": {<br />    "query_database": {<br />      "calls_per_hour": 50,<br />      "cost_tier": "high"<br />    },<br />    "list_items": {<br />      "calls_per_hour": 500,<br />      "cost_tier": "low"<br />    }<br />  }<br />}<br /></pre>1. Submit the record for approval. | Cloud architect |

### Build the EventBridge-driven approval workflow
<a name="build-the-eventbridge-driven-approval-workflow"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the EventBridge rule for record submissions | 1. Create an EventBridge rule on the default bus matching Agent Registry `RegistryRecordSubmitted` events:<pre>{<br />  "source": ["aws.bedrock-agentcore"],<br />  "detail-type": ["Registry Record State changed to Pending Approval"]<br />}<br /></pre>1. Set the target to the quota validation Lambda function. | Cloud architect |
| Implement the quota validation logic | 1. Create a Lambda function that receives the EventBridge event. The event detail contains registryRecordId and registryId.<br />2. Fetch the record metadata using the Agent Registry API.<br />3. Validate required quota fields:`schema_version` is presentAt least one quota tier is defined with `calls_per_hour` > 0`cost_tier` is one of: low, medium, high, premium`burst_limit` ≤ `calls_per_hour`<br />4. If validation passes, call `UpdateRegistryRecordStatus` with status `APPROVED`.<br />5. If validation fails, call `UpdateRegistryRecordStatus` with status `REJECTED` and include feedback describing the missing or invalid fields. | Cloud architect |
| Test the end-to-end approval flow | 1. Submit a record with valid quota metadata - verify it transitions to APPROVED.<br />2. Submit a record with missing `calls_per_hour` - verify it is REJECTED with appropriate feedback.<br />3. Submit a record with `burst_limit` exceeding `calls_per_hour` - verify rejection.<br />4. Confirm the approved record is discoverable via the SearchRegistryRecords API. | Cloud architect |

### Build the Gateway REQUEST interceptor for quota enforcement
<a name="build-the-gateway-request-interceptor-for-quota-enforcement"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the DynamoDB counter table | 1. Create a DynamoDB table with the following schema:`pk` (String, partition key) – Composite key in the format `{agent_id}#{tool_name}`.`sk` (String, sort key) – Window timestamp (for example, `2026-06-16T07:00`).`count` (Number) – Invocation count in the current window.`ttl` (Number) – Unix epoch expiry for automatic cleanup.<br />2. Enable DynamoDB TTL on the `ttl` attribute.<br />3. Configure on-demand capacity mode (or provisioned with auto-scaling based on expected agent traffic). | Cloud architect |
| Implement the REQUEST interceptor Lambda | 1. Create a Lambda function that receives the Gateway interceptor event.<br />2. Extract the tool name from `event.mcp.gatewayRequest.body.params.name` (for `tools/call` method).<br />3. Extract the agent identity from the `x-agent-id` request header (passed through via `passRequestHeaders: true` on the interceptor configuration).<br />4. Query the Agent Registry using `SearchRegistryRecords` to retrieve quota metadata for the target tool.<br />5. Check the DynamoDB sliding-window counter against the quota limit.<br />6. **Allow**: Return the original request body in the interceptor output format:<pre>return {"interceptorOutputVersion": "1.0",<br />        "mcp": {"transformedGatewayRequest": {"body": request_body}}}<br /></pre>1. **Deny**: Raise an exception with a JSON-encoded error - the Gateway relays it to the caller:<pre>raise Exception(json.dumps({<br />    "error": "Rate limit exceeded",<br />    "tool": tool_name,<br />    "retry_after_seconds": cooldown_seconds,<br />}))<br /></pre>See the full implementation in the [code repository](https://github.com/aws-samples/sample-agentcore-tool-quota-enforcement) (`lambda/interceptor/interceptor.py`). | Cloud architect |
| Attach the interceptor to the Gateway | 1. Using AWS CDK, attach the Lambda as a REQUEST interceptor:<pre>import * as agentcore from 'aws-cdk-lib/aws-bedrockagentcore';<br /><br />const gateway = new agentcore.Gateway(this, 'QuotaGateway', {<br />  gatewayName: 'tool-quota-gw',<br />  authorizerConfiguration: agentcore.GatewayAuthorizer.usingAwsIam(),<br />  exceptionLevel: agentcore.GatewayExceptionLevel.DEBUG,<br />  interceptorConfigurations: [<br />    agentcore.LambdaInterceptor.forRequest(quotaInterceptorFn, { passRequestHeaders: true }),<br />  ],<br />});<br /></pre>1. Grant the Lambda permission to call `SearchRegistryRecords` on the Agent Registry and read/write DynamoDB.<br />2. Deploy and test with a sample tool invocation. | Cloud architect |
| Implement sliding-window rate limiting | 1. Implement the sliding-window algorithm: compute a weighted estimate using the current window count plus the previous window count scaled by `(1 - minutes_elapsed / 60)`. This avoids the burst-at-boundary problem of fixed windows.<pre>estimated_usage = previous_count × (1 - minute/60) + current_count<br /></pre>1. Store a separate burst counter keyed by minute (`{agent}#{tool}#burst` / `HH:MM`) to enforce short-term burst limits independently of the hourly quota.<br />2. Test that burst-at-boundary scenarios are correctly handled. | Cloud architect |

### Implement observability and operational dashboards
<a name="implement-observability-and-operational-dashboards"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Publish custom CloudWatch metrics | 1. In the interceptor Lambda, publish CloudWatch metrics on each invocation:+ `ToolInvocationCount` (dimensions: tool\_name, agent\_id)<br />+ `QuotaDenialCount` (dimensions: tool\_name, agent\_id, reason)<br />+ `ToolDeprecatedInvocation` (dimensions: tool\_name, agent\_id)1. Create a CloudWatch dashboard displaying:Top tools by invocation countTools approaching quota limits (utilization > 80%)Quota denial trends over time | Cloud architect |
| Set up CloudTrail audit for quota policy changes (Recommendation - Not implemented in code repo) | 1. Verify CloudTrail is logging Agent Registry control-plane calls (this is enabled by default).<br />2. Create CloudWatch Logs Insights queries to track:Who changed quota metadata (UpdateRegistryRecord)Approval/rejection decisions (UpdateRegistryRecordStatus)Record deprecations<br />3. Create alarms for unexpected patterns:Quota policy changes outside business hoursHigh rejection rates indicating publisher confusion | Cloud architect |
| Configure alerting for quota exhaustion (Recommendation - Not implemented in code repo) | 1. Create CloudWatch alarms that trigger when:A tool's denial rate exceeds 10% of invocations over a 5-minute windowA single agent consistently hits limits (possible misconfiguration)<br />2. Route alarms to an SNS topic for notification to platform operators. | Cloud architect |

### Handle quota policy updates and record lifecycle
<a name="handle-quota-policy-updates-and-record-lifecycle"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Implement quota metadata versioning (Recommendation - Not implemented in code repo) | 1. When updating quota metadata on existing records, increment the `schema_version`.<br />2. The interceptor Lambda caches quota metadata with a short TTL (60 seconds). On cache miss, it queries the registry using SearchRegistryRecords for fresh data.<br />3. Document the caching behavior so publishers understand that quota changes take up to 60 seconds to propagate. | Cloud architect |
| Handle record deprecation gracefully | 1. When a record is deprecated, the interceptor should:Detect the DEPRECATED status from the registry query response.Deny the request with a descriptive error ("Tool has been deprecated; contact your platform team").Publish a `ToolDeprecatedInvocation` metric.<br />2. Update DynamoDB counters to stop incrementing for deprecated tools. | Cloud architect |
| Support quota overrides per agent | 1. Extend the interceptor to check for agent-specific quota overrides stored in a separate DynamoDB table or in the agent's own registry record metadata.<br />2. Priority order: agent-specific override > tool-level quota > default quota.<br />3. Document the override mechanism for platform operators. | Cloud architect |

## Troubleshooting
<a name="govern-tool-access-with-aws-agent-registry-metadata-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Tool calls are not being rate-limited | Ensure the tool names registered in the Agent Registry match the names agents use at invocation time, including any MCP server prefixes. |
| Records remain in PENDING\_APPROVAL indefinitely | Verify the EventBridge rule's source and detail-type fields align with the event schema emitted by Agent Registry. Check EventBridge rule invocation metrics in CloudWatch. |
| Agents are denied immediately with no prior usage | Confirm DynamoDB TTL is enabled and working. Clear leftover counter items from previous test runs if needed. |
| Quota changes are not taking effect | Wait at least 65 seconds (registry propagation \+ cache TTL) after updating metadata, then retry. |
| Interceptor adds noticeable latency to tool calls | Enable provisioned concurrency on the interceptor Lambda and confirm that in-memory caching is reducing registry API calls. |

## Related resources
<a name="govern-tool-access-with-aws-agent-registry-metadata-resources"></a>
+ [**Code repository**](https://github.com/aws-samples/sample-agentcore-tool-quota-enforcement) - CDK project, Lambda source, and deployment instructions for this pattern.
+ [AWS Agent Registry documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry.html)
+ [Agent Registry key capabilities](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-key-capabilities.html)
+ [Secure AI agents with Policy and Lambda interceptors in Amazon Bedrock AgentCore Gateway](https://aws.amazon.com/blogs/machine-learning/secure-ai-agents-with-policy-and-lambda-interceptors-in-amazon-bedrock-agentcore-gateway/)
+ [Amazon Bedrock AgentCore Gateway documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway.html)
+ [Gateway interceptors documentation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/gateway-interceptors.html)
+ [AWS CDK LambdaInterceptor API reference](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_bedrockagentcore.LambdaInterceptor.html)
+ [Amazon EventBridge User Guide](https://docs.aws.amazon.com/eventbridge/latest/userguide/)
+ [DynamoDB TTL documentation](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/TTL.html)
+ [The future of managing agents at scale: AWS Agent Registry now in preview](https://aws.amazon.com/blogs/machine-learning/the-future-of-managing-agents-at-scale-aws-agent-registry-now-in-preview/)

## Additional information
<a name="govern-tool-access-with-aws-agent-registry-metadata-additional"></a>

All epics and stories above are fully implemented in the [code repository](https://github.com/aws-samples/sample-agentcore-tool-quota-enforcement), except those marked as **(recommendation)** - which are operational best practices you should adopt but are not automated by the sample code.

*Quota metadata schema reference*

The quota metadata JSON schema defines the structure for tool rate limits stored as custom metadata on Agent Registry records. It is introduced in Epic 1 (Story 1.1) and enforced at runtime by the interceptor (Epic 3, Story 3.2) and the validation workflow (Epic 2, Story 2.2).

```
{
  "$schema": "https://json-schema.org/draft/2020-12/schema",
  "title": "ToolQuotaMetadata",
  "type": "object",
  "required": ["schema_version", "quotas", "cost_tier"],
  "properties": {
    "schema_version": {
      "type": "string",
      "pattern": "^\\d+\\.\\d+$"
    },
    "quotas": {
      "type": "object",
      "patternProperties": {
        "^(standard|premium|enterprise)$": {
          "type": "object",
          "required": ["calls_per_hour"],
          "properties": {
            "calls_per_hour": { "type": "integer", "minimum": 1 },
            "burst_limit": { "type": "integer", "minimum": 1 },
            "cooldown_seconds": { "type": "integer", "minimum": 0 }
          }
        }
      }
    },
    "cost_tier": {
      "type": "string",
      "enum": ["low", "medium", "high", "premium"]
    },
    "tool_quotas": {
      "type": "object",
      "description": "Per-tool overrides within an MCP server record",
      "additionalProperties": {
        "type": "object",
        "properties": {
          "calls_per_hour": { "type": "integer" },
          "cost_tier": { "type": "string" }
        }
      }
    }
  }
}
```

*FAQs*

**What happens if the Agent Registry is unreachable?** The interceptor fails open - requests are allowed when the registry cannot be queried. This avoids blocking agents during transient outages. To implement fail-closed behavior, modify the interceptor to deny requests when the registry returns an error, accepting the tradeoff of agent disruption during outages.

**How long do quota policy changes take to propagate?** Agent Registry metadata is eventually consistent (a few seconds), and the interceptor caches quota data for 60 seconds. In the worst case, changes take up to \~65 seconds to take effect.

**Can different agents have different quotas for the same tool?** Yes. The override table (Epic 5, Story 5.3) stores per-agent quota overrides. Priority order: agent-specific override > tool-level quota > default quota tier. Insert a record into the `QuotaOverrides` DynamoDB table with `agent_id`, `tool_name`, and the fields to override (e.g., `calls_per_hour`, `burst_limit`).

**Is the rate limiter exactly accurate under high concurrency?** DynamoDB counter updates use atomic `ADD` operations, but the read-then-decide-then-write flow is not transactional. Under high concurrency, a small number of requests may slip through before the counter reflects the true count. For strict enforcement, use DynamoDB conditional writes with a version attribute.

## Attachments
<a name="attachments-45ced596-4b24-4993-9cf2-9df8c605402e"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/45ced596-4b24-4993-9cf2-9df8c605402e/attachments/attachment.zip)
