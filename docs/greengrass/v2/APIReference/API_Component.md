---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_Component.html
---

# Component
<a name="API_Component"></a>

Contains information about a component.

## Contents
<a name="API_Component_Contents"></a>

 ** arn **   <a name="greengrassv2-Type-Component-arn"></a>
The [ARN](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the component version.
Type: String
Pattern: `arn:[^:]*:greengrass:[^:]*:(aws|[0-9]+):components:[^:]+`
Required: No

 ** componentName **   <a name="greengrassv2-Type-Component-componentName"></a>
The name of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** latestVersion **   <a name="greengrassv2-Type-Component-latestVersion"></a>
The latest version of the component and its details.
Type: [ComponentLatestVersion](API_ComponentLatestVersion.md) object
Required: No

## See Also
<a name="API_Component_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/Component)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/Component)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/Component)
