---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/APIReference/API_TerraformSource.html
---

# TerraformSource
<a name="API_TerraformSource"></a>

 The Terraform s3 state file you need to import.

## Contents
<a name="API_TerraformSource_Contents"></a>

 ** s3StateFileUrl **   <a name="resiliencehub-Type-TerraformSource-s3StateFileUrl"></a>
 The URL of the Terraform s3 state file you need to import.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Pattern: `((https://([^/]+)\.s3((-|\.)[^/]+)?\.amazonaws\.com(.cn)?)|(s3://([^/]+)))/\S{1,2000}`
Required: Yes

## See Also
<a name="API_TerraformSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehub-2020-04-30/TerraformSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehub-2020-04-30/TerraformSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehub-2020-04-30/TerraformSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
