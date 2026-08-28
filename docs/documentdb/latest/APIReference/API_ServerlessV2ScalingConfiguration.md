---
source_url: https://docs.aws.amazon.com/documentdb/latest/APIReference/API_ServerlessV2ScalingConfiguration.html
---

# ServerlessV2ScalingConfiguration
<a name="API_ServerlessV2ScalingConfiguration"></a>

Sets the scaling configuration of an Amazon DocumentDB Serverless cluster.

## Contents
<a name="API_ServerlessV2ScalingConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** MaxCapacity **
The maximum number of Amazon DocumentDB capacity units (DCUs) for an instance in an Amazon DocumentDB Serverless cluster. You can specify DCU values in half-step increments, such as 32, 32.5, 33, and so on.
Type: Double
Required: No

 ** MinCapacity **
The minimum number of Amazon DocumentDB capacity units (DCUs) for an instance in an Amazon DocumentDB Serverless cluster. You can specify DCU values in half-step increments, such as 8, 8.5, 9, and so on.
Type: Double
Required: No

## See Also
<a name="API_ServerlessV2ScalingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/docdb-2014-10-31/ServerlessV2ScalingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/docdb-2014-10-31/ServerlessV2ScalingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/docdb-2014-10-31/ServerlessV2ScalingConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DocumentDB. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query documentdb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
