---
source_url: https://docs.aws.amazon.com/partner-central/latest/APIReference/API_account_StartVerification.html
---

# StartVerification
<a name="API_account_StartVerification"></a>

Initiates a new verification process for a partner account. This operation begins the verification workflow for either business registration or individual registrant identity verification as required by AWS Partner Central.

## Request Syntax
<a name="API_account_StartVerification_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "VerificationDetails": { ... }
}
```

## Request Parameters
<a name="API_account_StartVerification_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [ClientToken](#API_account_StartVerification_RequestSyntax) **   <a name="AWSPartnerCentral-account_StartVerification-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This prevents duplicate verification processes from being started accidentally.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9-_]+`
Required: No

 ** [VerificationDetails](#API_account_StartVerification_RequestSyntax) **   <a name="AWSPartnerCentral-account_StartVerification-request-VerificationDetails"></a>
The specific details required for the verification process, including business information for business verification or personal information for registrant verification.
Type: [VerificationDetails](API_account_VerificationDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## Response Syntax
<a name="API_account_StartVerification_ResponseSyntax"></a>

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
<a name="API_account_StartVerification_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [StartedAt](#API_account_StartVerification_ResponseSyntax) **   <a name="AWSPartnerCentral-account_StartVerification-response-StartedAt"></a>
The timestamp when the verification process was successfully initiated.
Type: Timestamp

 ** [VerificationResponseDetails](#API_account_StartVerification_ResponseSyntax) **   <a name="AWSPartnerCentral-account_StartVerification-response-VerificationResponseDetails"></a>
Initial response details specific to the type of verification started, which may include next steps or additional requirements.
Type: [VerificationResponseDetails](API_account_VerificationResponseDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [VerificationStatus](#API_account_StartVerification_ResponseSyntax) **   <a name="AWSPartnerCentral-account_StartVerification-response-VerificationStatus"></a>
The initial status of the verification process after it has been started. Typically this will be pending or in-progress.
Type: String
Valid Values: `PENDING_CUSTOMER_ACTION | IN_PROGRESS | FAILED | SUCCEEDED | REJECTED`

 ** [VerificationType](#API_account_StartVerification_ResponseSyntax) **   <a name="AWSPartnerCentral-account_StartVerification-response-VerificationType"></a>
The type of verification that was started based on the provided verification details.
Type: String
Valid Values: `BUSINESS_VERIFICATION | REGISTRANT_VERIFICATION`

 ** [CompletedAt](#API_account_StartVerification_ResponseSyntax) **   <a name="AWSPartnerCentral-account_StartVerification-response-CompletedAt"></a>
The timestamp when the verification process was completed. This field is typically null for newly started verifications unless they complete immediately.
Type: Timestamp

 ** [VerificationStatusReason](#API_account_StartVerification_ResponseSyntax) **   <a name="AWSPartnerCentral-account_StartVerification-response-VerificationStatusReason"></a>
Additional information about the initial verification status, including any immediate feedback about the submitted verification details.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `[\u0020-\u007E\u00A0-\uD7FF\uE000-\uFFFD]+`

## Errors
<a name="API_account_StartVerification_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied due to insufficient permissions. The caller does not have the required permissions to perform this operation.
 ** Reason **
The specific reason for the access denial.
HTTP Status Code: 400

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the resource. This typically occurs when trying to create a resource that already exists or modify a resource that has been changed by another process.
 ** Reason **
The specific reason for the conflict.
HTTP Status Code: 400

 ** InternalServerException **
An internal server error occurred while processing the request. This is typically a temporary condition and the request may be retried.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The request was rejected because it would exceed a service quota or limit. This may occur when trying to create more resources than allowed by the service limits.
 ** Reason **
The specific reason for the service quota being exceeded.
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
<a name="API_account_StartVerification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/partnercentral-account-2025-04-04/StartVerification)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/partnercentral-account-2025-04-04/StartVerification)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/partnercentral-account-2025-04-04/StartVerification)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/partnercentral-account-2025-04-04/StartVerification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/partnercentral-account-2025-04-04/StartVerification)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/partnercentral-account-2025-04-04/StartVerification)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/partnercentral-account-2025-04-04/StartVerification)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/partnercentral-account-2025-04-04/StartVerification)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/partnercentral-account-2025-04-04/StartVerification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/partnercentral-account-2025-04-04/StartVerification)
