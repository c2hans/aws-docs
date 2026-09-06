---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_AthenaError.html
---

# AthenaError
<a name="API_AthenaError"></a>

Provides information about an Athena query error. The `AthenaError` feature provides standardized error information to help you understand failed queries and take steps after a query failure occurs. `AthenaError` includes an `ErrorCategory` field that specifies whether the cause of the failed query is due to system error, user error, or other error.

## Contents
<a name="API_AthenaError_Contents"></a>

 ** ErrorCategory **   <a name="athena-Type-AthenaError-ErrorCategory"></a>
An integer value that specifies the category of a query failure error. The following list shows the category for each integer value.
 **1** - System
 **2** - User
 **3** - Other
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 3.
Required: No

 ** ErrorMessage **   <a name="athena-Type-AthenaError-ErrorMessage"></a>
Contains a short description of the error that occurred.
Type: String
Required: No

 ** ErrorType **   <a name="athena-Type-AthenaError-ErrorType"></a>
An integer value that provides specific information about an Athena query error. For the meaning of specific values, see the [Error Type Reference](https://docs.aws.amazon.com/athena/latest/ug/error-reference.html#error-reference-error-type-reference) in the *Amazon Athena User Guide*.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 9999.
Required: No

 ** Retryable **   <a name="athena-Type-AthenaError-Retryable"></a>
True if the query might succeed if resubmitted.
Type: Boolean
Required: No

## See Also
<a name="API_AthenaError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/AthenaError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/AthenaError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/AthenaError)
