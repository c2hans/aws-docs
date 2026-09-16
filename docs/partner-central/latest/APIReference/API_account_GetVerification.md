---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_GetVerification.html
---

# GetVerification
<a name="API_account_GetVerification"></a>

Retrieves the current status and details of a verification process for a partner account. This operation allows partners to check the progress and results of business or registrant verification processes.

## Request Syntax
<a name="API_account_GetVerification_RequestSyntax"></a>

```
{
   "VerificationType": "{{string}}"
}
```

## Request Parameters
<a name="API_account_GetVerification_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [VerificationType](#API_account_GetVerification_RequestSyntax) **   <a name="AWSPartnerCentral-account_GetVerification-request-VerificationType"></a>
The type of verification to retrieve information for. Valid values include business verification for company registration details and registrant verification for individual identity confirmation.
Type: String
Valid Values: `BUSINESS_VERIFICATION | REGISTRANT_VERIFICATION`
Required: Yes

## Response Syntax
<a name="API_account_GetVerification_ResponseSyntax"></a>

```
{
   "CompletedAt": "string",
   "StartedAt": "string",
   "VerificationResponseDetails": { ... },
   "VerificationStatus": "string",
   "VerificationStatusReason": "string",
   "VerificationType": "string"
}
```

## Response Elements
<a name="API_account_GetVerification_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [StartedAt](#API_account_GetVerification_ResponseSyntax) **   <a name="AWSPartnerCentral-account_GetVerification-response-StartedAt"></a>
The timestamp when the verification process was initiated.
Type: Timestamp

 ** [VerificationResponseDetails](#API_account_GetVerification_ResponseSyntax) **   <a name="AWSPartnerCentral-account_GetVerification-response-VerificationResponseDetails"></a>
Detailed response information specific to the type of verification performed, including any verification-specific data or results.
Type: [VerificationResponseDetails](API_account_VerificationResponseDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [VerificationStatus](#API_account_GetVerification_ResponseSyntax) **   <a name="AWSPartnerCentral-account_GetVerification-response-VerificationStatus"></a>
The current status of the verification process. Possible values include pending, in-progress, completed, failed, or expired.
Type: String
Valid Values: `PENDING_CUSTOMER_ACTION | IN_PROGRESS | FAILED | SUCCEEDED | REJECTED`

 ** [VerificationType](#API_account_GetVerification_ResponseSyntax) **   <a name="AWSPartnerCentral-account_GetVerification-response-VerificationType"></a>
The type of verification that was requested and processed.
Type: String
Valid Values: `BUSINESS_VERIFICATION | REGISTRANT_VERIFICATION`

 ** [CompletedAt](#API_account_GetVerification_ResponseSyntax) **   <a name="AWSPartnerCentral-account_GetVerification-response-CompletedAt"></a>
The timestamp when the verification process was completed. This field is null if the verification is still in progress.
Type: Timestamp

 ** [VerificationStatusReason](#API_account_GetVerification_ResponseSyntax) **   <a name="AWSPartnerCentral-account_GetVerification-response-VerificationStatusReason"></a>
Additional information explaining the current verification status, particularly useful when the status indicates a failure or requires additional action.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[\u0020-\u007E\u00A0-\uD7FF\uE000-\uFFFD]+`

## Errors
<a name="API_account_GetVerification_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.
 ** Reason **
The specific reason for the access denial.
HTTP Status Code: 400

 ** InternalServerException **
An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource could not be found. This may occur when referencing a resource that does not exist or has been deleted.
 ** Reason **
The specific reason why the resource was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was throttled due to too many requests being sent in a short period of time. The client should implement exponential backoff and retry the request.
 ** QuotaCode **
The quota code associated with the throttling error.
 ** ServiceCode **
The service code associated with the throttling error.
HTTP Status Code: 400

 ** ValidationException **
The request failed validation. One or more input parameters are invalid, missing, or do not meet the required format or constraints.
 ** ErrorDetails **
A list of detailed validation errors that occurred during request processing.
 ** Reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_account_GetVerification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-account-2025-04-04/GetVerification)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-account-2025-04-04/GetVerification)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/GetVerification)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-account-2025-04-04/GetVerification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/GetVerification)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-account-2025-04-04/GetVerification)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-account-2025-04-04/GetVerification)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-account-2025-04-04/GetVerification)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-account-2025-04-04/GetVerification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/GetVerification)
