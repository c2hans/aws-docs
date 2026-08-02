---
source_url: https://docs.aws.amazon.com/entityresolution/latest/apireference/API_DeleteUniqueIdError.html
---

# DeleteUniqueIdError
<a name="API_DeleteUniqueIdError"></a>

The error information provided when the delete unique ID operation doesn't complete.

## Contents
<a name="API_DeleteUniqueIdError_Contents"></a>

 ** errorType **   <a name="API-Type-DeleteUniqueIdError-errorType"></a>
 The error type for the delete unique ID operation.
The `SERVICE_ERROR` value indicates that an internal service-side problem occurred during the deletion operation.
The `VALIDATION_ERROR` value indicates that the deletion operation couldn't complete because of invalid input parameters or data.
Type: String
Valid Values: `SERVICE_ERROR | VALIDATION_ERROR`
Required: Yes

 ** uniqueId **   <a name="API-Type-DeleteUniqueIdError-uniqueId"></a>
The unique ID that couldn't be deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 780.
Pattern: `[a-zA-Z_0-9-+=/,]*`
Required: Yes

## See Also
<a name="API_DeleteUniqueIdError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/entityresolution-2018-05-10/DeleteUniqueIdError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/entityresolution-2018-05-10/DeleteUniqueIdError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/entityresolution-2018-05-10/DeleteUniqueIdError)
