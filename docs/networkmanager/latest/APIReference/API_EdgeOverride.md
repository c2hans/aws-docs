---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_EdgeOverride.html
---

# EdgeOverride
<a name="API_EdgeOverride"></a>

Describes the edge that's used for the override.

## Contents
<a name="API_EdgeOverride_Contents"></a>

 ** EdgeSets **   <a name="networkmanager-Type-EdgeOverride-EdgeSets"></a>
The list of edge locations.
Type: Array of arrays of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** UseEdge **   <a name="networkmanager-Type-EdgeOverride-UseEdge"></a>
The edge that should be used when overriding the current edge order.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_EdgeOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/EdgeOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/EdgeOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/EdgeOverride)
