---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_UpdateEnrollmentConfiguration.html
---

# UpdateEnrollmentConfiguration
<a name="API_automation_UpdateEnrollmentConfiguration"></a>

Updates your account’s Compute Optimizer Automation enrollment configuration.

## Request Syntax
<a name="API_automation_UpdateEnrollmentConfiguration_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "status": "{{string}}"
}
```

## Request Parameters
<a name="API_automation_UpdateEnrollmentConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_automation_UpdateEnrollmentConfiguration_RequestSyntax) **   <a name="computeoptimizer-automation_UpdateEnrollmentConfiguration-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. Must be 1-64 characters long and contain only alphanumeric characters, underscores, and hyphens.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,64}`
Required: No

 ** [status](#API_automation_UpdateEnrollmentConfiguration_RequestSyntax) **   <a name="computeoptimizer-automation_UpdateEnrollmentConfiguration-request-status"></a>
The desired enrollment status.
+ Active - Enables the Automation feature for your account.
+ Inactive - Disables the Automation feature for your account and stops all of your automation rules. If you opt in again later, all rules will be inactive, and you must enable the rules you want to run. You must wait at least 24 hours after opting out to opt in again.
The `Pending` and `Failed` options cannot be used to update the enrollment status of an account. They are returned in the response of a request to update the enrollment status of an account.
If you are a member account, your account must be disassociated from your organization’s management account before you can disable Automation. Contact your administrator to make this change.
Type: String
Valid Values: `Active | Inactive | Pending | Failed`
Required: Yes

## Response Syntax
<a name="API_automation_UpdateEnrollmentConfiguration_ResponseSyntax"></a>

```
{
   "lastUpdatedTimestamp": number,
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_automation_UpdateEnrollmentConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [lastUpdatedTimestamp](#API_automation_UpdateEnrollmentConfiguration_ResponseSyntax) **   <a name="computeoptimizer-automation_UpdateEnrollmentConfiguration-response-lastUpdatedTimestamp"></a>
 The timestamp when the enrollment configuration was last updated.
Type: Timestamp

 ** [status](#API_automation_UpdateEnrollmentConfiguration_ResponseSyntax) **   <a name="computeoptimizer-automation_UpdateEnrollmentConfiguration-response-status"></a>
 The updated enrollment status.
Type: String
Valid Values: `Active | Inactive | Pending | Failed`

 ** [statusReason](#API_automation_UpdateEnrollmentConfiguration_ResponseSyntax) **   <a name="computeoptimizer-automation_UpdateEnrollmentConfiguration-response-statusReason"></a>
 The reason for the updated enrollment status.
Type: String

## Errors
<a name="API_automation_UpdateEnrollmentConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You do not have sufficient permissions to perform this action.
HTTP Status Code: 400

 ** ForbiddenException **
 You are not authorized to perform this action.
HTTP Status Code: 400

 ** IdempotencyTokenInUseException **
 The specified client token is already in use.
HTTP Status Code: 400

 ** IdempotentParameterMismatchException **
Exception thrown when the same client token is used with different parameters, indicating a mismatch in idempotent request parameters.
HTTP Status Code: 400

 ** InternalServerException **
 An internal error occurred while processing the request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
 One or more parameter values are not valid.
HTTP Status Code: 400

 ** NotManagementAccountException **
 The operation can only be performed by a management account.
HTTP Status Code: 400

 ** OptInRequiredException **
 The account must be opted in to Compute Optimizer Automation before performing this action.
HTTP Status Code: 400

 ** ResourceNotFoundException **
 The specified resource was not found.
HTTP Status Code: 400

 ** ServiceUnavailableException **
 The service is temporarily unavailable.
HTTP Status Code: 500

 ** ThrottlingException **
 The request was denied due to request throttling.
HTTP Status Code: 400

## See Also
<a name="API_automation_UpdateEnrollmentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-automation-2025-09-22/UpdateEnrollmentConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-automation-2025-09-22/UpdateEnrollmentConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/UpdateEnrollmentConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-automation-2025-09-22/UpdateEnrollmentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/UpdateEnrollmentConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-automation-2025-09-22/UpdateEnrollmentConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-automation-2025-09-22/UpdateEnrollmentConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-automation-2025-09-22/UpdateEnrollmentConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-automation-2025-09-22/UpdateEnrollmentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/UpdateEnrollmentConfiguration)
