---
source_url: https://docs.aws.amazon.com/fis/latest/APIReference/API_ResolvedTarget.html
---

# ResolvedTarget
<a name="API_ResolvedTarget"></a>

Describes a resolved target.

## Contents
<a name="API_ResolvedTarget_Contents"></a>

 ** resourceType **   <a name="fis-Type-ResolvedTarget-resourceType"></a>
The resource type of the target.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `[\S]+`
Required: No

 ** targetInformation **   <a name="fis-Type-ResolvedTarget-targetInformation"></a>
Information about the target.
Type: String to string map
Key Length Constraints: Maximum length of 64.
Key Pattern: `[\S]+`
Value Length Constraints: Maximum length of 2048.
Value Pattern: `[\S]+`
Required: No

 ** targetName **   <a name="fis-Type-ResolvedTarget-targetName"></a>
The name of the target.
Type: String
Length Constraints: Maximum length of 64.
Pattern: `[\S]+`
Required: No

## See Also
<a name="API_ResolvedTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fis-2020-12-01/ResolvedTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fis-2020-12-01/ResolvedTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fis-2020-12-01/ResolvedTarget)
