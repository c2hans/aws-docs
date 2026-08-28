---
source_url: https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/API_WarmThroughput.html
---

# WarmThroughput
<a name="API_WarmThroughput"></a>

Provides visibility into the number of read and write operations your table or secondary index can instantaneously support. The settings can be modified using the `UpdateTable` operation to meet the throughput requirements of an upcoming peak event.

## Contents
<a name="API_WarmThroughput_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ReadUnitsPerSecond **   <a name="DDB-Type-WarmThroughput-ReadUnitsPerSecond"></a>
Represents the number of read operations your base table can instantaneously support.
Type: Long
Required: No

 ** WriteUnitsPerSecond **   <a name="DDB-Type-WarmThroughput-WriteUnitsPerSecond"></a>
Represents the number of write operations your base table can instantaneously support.
Type: Long
Required: No

## See Also
<a name="API_WarmThroughput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dynamodb-2012-08-10/WarmThroughput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dynamodb-2012-08-10/WarmThroughput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dynamodb-2012-08-10/WarmThroughput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DynamoDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazondynamodb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
