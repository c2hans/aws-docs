---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_BatchItemError.html
---

# BatchItemError
<a name="API_BatchItemError"></a>

Contains the batch request error details associated with the request.

## Contents
<a name="API_BatchItemError_Contents"></a>

 ** Code **   <a name="location-Type-BatchItemError-Code"></a>
The error code associated with the batch request error.
Type: String
Valid Values: `AccessDeniedError | ConflictError | InternalServerError | ResourceNotFoundError | ThrottlingError | ValidationError`
Required: No

 ** Message **   <a name="location-Type-BatchItemError-Message"></a>
A message with the reason for the batch request error.
Type: String
Required: No

## See Also
<a name="API_BatchItemError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/BatchItemError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/BatchItemError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/BatchItemError)
