---
source_url: https://docs.aws.amazon.com/cloudfront/latest/APIReference/API_FunctionList.html
---

# FunctionList
<a name="API_FunctionList"></a>

A list of CloudFront functions.

## Contents
<a name="API_FunctionList_Contents"></a>

 ** MaxItems **   <a name="cloudfront-Type-FunctionList-MaxItems"></a>
The maximum number of functions requested.
Type: Integer
Required: Yes

 ** Quantity **   <a name="cloudfront-Type-FunctionList-Quantity"></a>
The number of functions returned in the response.
Type: Integer
Required: Yes

 ** Items **   <a name="cloudfront-Type-FunctionList-Items"></a>
Contains the functions in the list.
Type: Array of [FunctionSummary](API_FunctionSummary.md) objects
Required: No

 ** NextMarker **   <a name="cloudfront-Type-FunctionList-NextMarker"></a>
If there are more items in the list than are in this response, this element is present. It contains the value that you should use in the `Marker` field of a subsequent request to continue listing functions where you left off.
Type: String
Required: No

## See Also
<a name="API_FunctionList_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudfront-2020-05-31/FunctionList)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudfront-2020-05-31/FunctionList)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudfront-2020-05-31/FunctionList)
