---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_PathComponent.html
---

# PathComponent
<a name="API_PathComponent"></a>

Describes a path component.

## Contents
<a name="API_PathComponent_Contents"></a>

 ** DestinationCidrBlock **   <a name="networkmanager-Type-PathComponent-DestinationCidrBlock"></a>
The destination CIDR block in the route table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** Resource **   <a name="networkmanager-Type-PathComponent-Resource"></a>
The resource.
Type: [NetworkResourceSummary](API_NetworkResourceSummary.md) object
Required: No

 ** Sequence **   <a name="networkmanager-Type-PathComponent-Sequence"></a>
The sequence number in the path. The destination is 0.
Type: Integer
Required: No

## See Also
<a name="API_PathComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/PathComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/PathComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/PathComponent)
