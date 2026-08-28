---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_VpcConfig.html
---

# VpcConfig
<a name="API_VpcConfig"></a>

VPC configuration for workflow runs.

## Contents
<a name="API_VpcConfig_Contents"></a>

 ** securityGroupIds **   <a name="omics-Type-VpcConfig-securityGroupIds"></a>
List of security group IDs. Maximum of 5 security groups allowed.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Length Constraints: Minimum length of 4. Maximum length of 128.
Pattern: `sg-[0-9a-f]+`
Required: No

 ** subnetIds **   <a name="omics-Type-VpcConfig-subnetIds"></a>
List of subnet IDs. Maximum of 16 subnets allowed.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 16 items.
Length Constraints: Minimum length of 8. Maximum length of 128.
Pattern: `subnet-[0-9a-f]+`
Required: No

## See Also
<a name="API_VpcConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/VpcConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/VpcConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/VpcConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
