---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_BillingModeSummary.html
---

# BillingModeSummary
<a name="API_BillingModeSummary"></a>

Contains the details for the read/write capacity mode. This page talks about `PROVISIONED` and `PAY_PER_REQUEST` billing modes. For more information about these modes, see [Read/write capacity mode](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/HowItWorks.ReadWriteCapacityMode.html).

**Note**
You may need to switch to on-demand mode at least once in order to return a `BillingModeSummary` response.

## Contents
<a name="API_BillingModeSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** BillingMode **   <a name="DDB-Type-BillingModeSummary-BillingMode"></a>
Controls how you are charged for read and write throughput and how you manage capacity. This setting can be changed later.
+  `PROVISIONED` - Sets the read/write capacity mode to `PROVISIONED`. We recommend using `PROVISIONED` for predictable workloads.
+  `PAY_PER_REQUEST` - Sets the read/write capacity mode to `PAY_PER_REQUEST`. We recommend using `PAY_PER_REQUEST` for unpredictable workloads.
Type: String
Valid Values: `PROVISIONED | PAY_PER_REQUEST`
Required: No

 ** LastUpdateToPayPerRequestDateTime **   <a name="DDB-Type-BillingModeSummary-LastUpdateToPayPerRequestDateTime"></a>
Represents the time when `PAY_PER_REQUEST` was last set as the read/write capacity mode.
Type: Timestamp
Required: No

## See Also
<a name="API_BillingModeSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/BillingModeSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/BillingModeSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/BillingModeSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
