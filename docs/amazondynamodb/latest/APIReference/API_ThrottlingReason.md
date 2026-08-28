---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_ThrottlingReason.html
---

# ThrottlingReason
<a name="API_ThrottlingReason"></a>

Represents the specific reason why a DynamoDB request was throttled and the ARN of the impacted resource. This helps identify exactly what resource is being throttled, what type of operation caused it, and why the throttling occurred.

## Contents
<a name="API_ThrottlingReason_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** reason **   <a name="DDB-Type-ThrottlingReason-reason"></a>
The reason for throttling. The throttling reason follows a specific format: `ResourceType+OperationType+LimitType`:
+ Resource Type (What is being throttled): Table or Index
+ Operation Type (What kind of operation): Read or Write
+ Limit Type (Why the throttling occurred):
  +  `ProvisionedThroughputExceeded`: The request rate is exceeding the [provisioned throughput capacity](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/provisioned-capacity-mode.html) (read or write capacity units) configured for a table or a global secondary index (GSI) in provisioned capacity mode.
  +  `AccountLimitExceeded`: The request rate has caused a table or global secondary index (GSI) in on-demand mode to exceed the [per-table account-level service quotas](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/ServiceQuotas.html#default-limits-throughput) for read/write throughput in the current AWS Region.
  +  `KeyRangeThroughputExceeded`: The request rate directed at a specific partition key value has exceeded the [internal partition-level throughput limits](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/bp-partition-key-design.html), indicating uneven access patterns across the table's or GSI's key space.
  +  `MaxOnDemandThroughputExceeded`: The request rate has exceeded the [configured maximum throughput limits](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/on-demand-capacity-mode-max-throughput.html) set for a table or index in on-demand capacity mode.
Examples of complete throttling reasons:
+ TableReadProvisionedThroughputExceeded
+ IndexWriteAccountLimitExceeded
This helps identify exactly what resource is being throttled, what type of operation caused it, and why the throttling occurred.
Type: String
Required: No

 ** resource **   <a name="DDB-Type-ThrottlingReason-resource"></a>
The Amazon Resource Name (ARN) of the DynamoDB table or index that experienced the throttling event.
Type: String
Required: No

## See Also
<a name="API_ThrottlingReason_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/ThrottlingReason)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/ThrottlingReason)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/ThrottlingReason)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
