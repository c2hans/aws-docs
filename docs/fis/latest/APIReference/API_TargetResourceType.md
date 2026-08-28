---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_TargetResourceType.html
---

# TargetResourceType
<a name="API_TargetResourceType"></a>

Describes a resource type.

## Contents
<a name="API_TargetResourceType_Contents"></a>

 ** description **   <a name="fis-Type-TargetResourceType-description"></a>
A description of the resource type.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `[\s\S]+`
Required: No

 ** parameters **   <a name="fis-Type-TargetResourceType-parameters"></a>
The parameters for the resource type.
Type: String to [TargetResourceTypeParameter](API_TargetResourceTypeParameter.md) object map
Key Length Constraints: Maximum length of 64.
Key Pattern: `[\S]+`
Required: No

 ** resourceType **   <a name="fis-Type-TargetResourceType-resourceType"></a>
The resource type.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[\S]+`
Required: No

## See Also
<a name="API_TargetResourceType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/TargetResourceType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/TargetResourceType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/TargetResourceType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Fault Injection Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fis` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
