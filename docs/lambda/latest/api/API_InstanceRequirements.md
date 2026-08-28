---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_InstanceRequirements.html
---

# InstanceRequirements
<a name="API_InstanceRequirements"></a>

Specifications that define the characteristics and constraints for compute instances used by the capacity provider.

## Contents
<a name="API_InstanceRequirements_Contents"></a>

 ** AllowedInstanceTypes **   <a name="lambda-Type-InstanceRequirements-AllowedInstanceTypes"></a>
A list of EC2 instance types that the capacity provider is allowed to use. If not specified, all compatible instance types are allowed.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 400 items.
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[a-zA-Z0-9\.\-]+`
Required: No

 ** Architectures **   <a name="lambda-Type-InstanceRequirements-Architectures"></a>
A list of supported CPU architectures for compute instances. Valid values include `x86_64` and `arm64`.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `x86_64 | arm64`
Required: No

 ** ExcludedInstanceTypes **   <a name="lambda-Type-InstanceRequirements-ExcludedInstanceTypes"></a>
A list of EC2 instance types that the capacity provider should not use, even if they meet other requirements.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 400 items.
Length Constraints: Minimum length of 1. Maximum length of 30.
Pattern: `[a-zA-Z0-9\.\-]+`
Required: No

## See Also
<a name="API_InstanceRequirements_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/InstanceRequirements)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/InstanceRequirements)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/InstanceRequirements)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
