---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_TableOptimizerVpcConfiguration.html
---

# TableOptimizerVpcConfiguration
<a name="API_TableOptimizerVpcConfiguration"></a>

An object that describes the VPC configuration for a table optimizer.

This configuration is necessary to perform optimization on tables that are in a customer VPC.

## Contents
<a name="API_TableOptimizerVpcConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** glueConnectionName **   <a name="Glue-Type-TableOptimizerVpcConfiguration-glueConnectionName"></a>
The name of the AWS Glue connection used for the VPC for the table optimizer.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_TableOptimizerVpcConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/TableOptimizerVpcConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/TableOptimizerVpcConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/TableOptimizerVpcConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
