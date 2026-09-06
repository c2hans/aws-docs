---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_LFTagError.html
---

# LFTagError
<a name="API_LFTagError"></a>

A structure containing an error related to a `TagResource` or `UnTagResource` operation.

## Contents
<a name="API_LFTagError_Contents"></a>

 ** Error **   <a name="lakeformation-Type-LFTagError-Error"></a>
An error that occurred with the attachment or detachment of the LF-tag.
Type: [ErrorDetail](API_ErrorDetail.md) object
Required: No

 ** LFTag **   <a name="lakeformation-Type-LFTagError-LFTag"></a>
The key-name of the LF-tag.
Type: [LFTagPair](API_LFTagPair.md) object
Required: No

## See Also
<a name="API_LFTagError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/LFTagError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/LFTagError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/LFTagError)
