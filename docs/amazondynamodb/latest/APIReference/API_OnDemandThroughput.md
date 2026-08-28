---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_OnDemandThroughput.html
---

# OnDemandThroughput
<a name="API_OnDemandThroughput"></a>

Sets the maximum number of read and write units for the specified on-demand table. If you use this parameter, you must specify `MaxReadRequestUnits`, `MaxWriteRequestUnits`, or both.

## Contents
<a name="API_OnDemandThroughput_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** MaxReadRequestUnits **   <a name="DDB-Type-OnDemandThroughput-MaxReadRequestUnits"></a>
Maximum number of read request units for the specified table.
To specify a maximum `OnDemandThroughput` on your table, set the value of `MaxReadRequestUnits` as greater than or equal to 1. To remove the maximum `OnDemandThroughput` that is currently set on your table, set the value of `MaxReadRequestUnits` to -1.
Type: Long
Required: No

 ** MaxWriteRequestUnits **   <a name="DDB-Type-OnDemandThroughput-MaxWriteRequestUnits"></a>
Maximum number of write request units for the specified table.
To specify a maximum `OnDemandThroughput` on your table, set the value of `MaxWriteRequestUnits` as greater than or equal to 1. To remove the maximum `OnDemandThroughput` that is currently set on your table, set the value of `MaxWriteRequestUnits` to -1.
Type: Long
Required: No

## See Also
<a name="API_OnDemandThroughput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/OnDemandThroughput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/OnDemandThroughput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/OnDemandThroughput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
