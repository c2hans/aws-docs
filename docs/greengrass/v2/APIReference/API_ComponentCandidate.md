---
source_url: https://docs.aws.amazon.com/greengrass/v2/APIReference/API_ComponentCandidate.html
---

# ComponentCandidate
<a name="API_ComponentCandidate"></a>

Contains information about a component that is a candidate to deploy to a Greengrass core device.

## Contents
<a name="API_ComponentCandidate_Contents"></a>

 ** componentName **   <a name="greengrassv2-Type-ComponentCandidate-componentName"></a>
The name of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** componentVersion **   <a name="greengrassv2-Type-ComponentCandidate-componentVersion"></a>
The version of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** versionRequirements **   <a name="greengrassv2-Type-ComponentCandidate-versionRequirements"></a>
The version requirements for the component's dependencies. Greengrass core devices get the version requirements from component recipes.
 AWS IoT Greengrass V2 uses semantic version constraints. For more information, see [Semantic Versioning](https://semver.org/).
Type: String to string map
Key Length Constraints: Minimum length of 1.
Value Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_ComponentCandidate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/greengrassv2-2020-11-30/ComponentCandidate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/greengrassv2-2020-11-30/ComponentCandidate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/greengrassv2-2020-11-30/ComponentCandidate)
