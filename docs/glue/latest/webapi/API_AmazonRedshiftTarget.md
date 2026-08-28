---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_AmazonRedshiftTarget.html
---

# AmazonRedshiftTarget
<a name="API_AmazonRedshiftTarget"></a>

Specifies an Amazon Redshift target.

## Contents
<a name="API_AmazonRedshiftTarget_Contents"></a>

 ** Data **   <a name="Glue-Type-AmazonRedshiftTarget-Data"></a>
Specifies the data of the Amazon Redshift target node.
Type: [AmazonRedshiftNodeData](API_AmazonRedshiftNodeData.md) object
Required: No

 ** Inputs **   <a name="Glue-Type-AmazonRedshiftTarget-Inputs"></a>
The nodes that are inputs to the data target.
Type: Array of strings
Array Members: Fixed number of 1 item.
Pattern: `[A-Za-z0-9_-]*`
Required: No

 ** Name **   <a name="Glue-Type-AmazonRedshiftTarget-Name"></a>
The name of the Amazon Redshift target.
Type: String
Pattern: `([^\r\n])*`
Required: No

## See Also
<a name="API_AmazonRedshiftTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/AmazonRedshiftTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/AmazonRedshiftTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/AmazonRedshiftTarget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
