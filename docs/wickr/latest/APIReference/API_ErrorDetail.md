---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_ErrorDetail.html
---

# ErrorDetail
<a name="API_ErrorDetail"></a>

Contains detailed error information explaining why an operation failed, including which field caused the error and the reason for the failure.

## Contents
<a name="API_ErrorDetail_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** field **   <a name="wickr-Type-ErrorDetail-field"></a>
The name of the field that contains an error or warning.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** reason **   <a name="wickr-Type-ErrorDetail-reason"></a>
A detailed description of the error or warning.
Type: String
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_ErrorDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/ErrorDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/ErrorDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/ErrorDetail)
