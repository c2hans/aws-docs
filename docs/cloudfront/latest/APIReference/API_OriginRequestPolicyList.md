---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_OriginRequestPolicyList.html
---

# OriginRequestPolicyList
<a name="API_OriginRequestPolicyList"></a>

A list of origin request policies.

## Contents
<a name="API_OriginRequestPolicyList_Contents"></a>

 ** MaxItems **   <a name="cloudfront-Type-OriginRequestPolicyList-MaxItems"></a>
The maximum number of origin request policies requested.
Type: Integer
Required: Yes

 ** Quantity **   <a name="cloudfront-Type-OriginRequestPolicyList-Quantity"></a>
The total number of origin request policies returned in the response.
Type: Integer
Required: Yes

 ** Items **   <a name="cloudfront-Type-OriginRequestPolicyList-Items"></a>
Contains the origin request policies in the list.
Type: Array of [OriginRequestPolicySummary](API_OriginRequestPolicySummary.md) objects
Required: No

 ** NextMarker **   <a name="cloudfront-Type-OriginRequestPolicyList-NextMarker"></a>
If there are more items in the list than are in this response, this element is present. It contains the value that you should use in the `Marker` field of a subsequent request to continue listing origin request policies where you left off.
Type: String
Required: No

## See Also
<a name="API_OriginRequestPolicyList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/OriginRequestPolicyList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/OriginRequestPolicyList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/OriginRequestPolicyList)
