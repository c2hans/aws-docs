---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_DeleteOrganizationEnrollmentConfiguration.html
---

# DeleteOrganizationEnrollmentConfiguration

 Deletes the specified configuration types from an organization enrollment configuration. After deletion, Automation stays enabled for affected accounts and earlier account associations aren't restored. Affected accounts inherit the organization rule mode from the closest parent that has an organization enrollment configuration, or get None allowed if no parent has one.

**Note**
Only the management account or a delegated administrator can perform this action.

## Request Syntax
<a name="API_automation_DeleteOrganizationEnrollmentConfiguration_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "configurationTypes": [ "{{string}}" ],
   "target": { ... }
}
```

## Request Parameters
<a name="API_automation_DeleteOrganizationEnrollmentConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_automation_DeleteOrganizationEnrollmentConfiguration_RequestSyntax) **   <a name="computeoptimizer-automation_DeleteOrganizationEnrollmentConfiguration-request-clientToken"></a>
 A unique identifier to ensure idempotency of the request.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,64}`
Required: No

 ** [configurationTypes](#API_automation_DeleteOrganizationEnrollmentConfiguration_RequestSyntax) **   <a name="computeoptimizer-automation_DeleteOrganizationEnrollmentConfiguration-request-configurationTypes"></a>
 The organization enrollment configuration types to delete from the target.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `OrganizationRuleMode`
Required: Yes

 ** [target](#API_automation_DeleteOrganizationEnrollmentConfiguration_RequestSyntax) **   <a name="computeoptimizer-automation_DeleteOrganizationEnrollmentConfiguration-request-target"></a>
 The account, organizational unit (OU), or organization root whose organization enrollment configuration you want to delete.
Type: [OrganizationTarget](API_automation_OrganizationTarget.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Elements
<a name="API_automation_DeleteOrganizationEnrollmentConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_automation_DeleteOrganizationEnrollmentConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ConflictException **
 The request conflicts with a concurrent change to the same resource. Retry the request.
HTTP Status Code: 409

 ** ForbiddenException **
 You are not authorized to perform this action.
HTTP Status Code: 403

 ** IdempotencyTokenInUseException **
 The specified client token is already in use.
HTTP Status Code: 409

 ** IdempotentParameterMismatchException **
Exception thrown when the same client token is used with different parameters, indicating a mismatch in idempotent request parameters.
HTTP Status Code: 409

 ** InternalServerException **
 An internal error occurred while processing the request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
 One or more parameter values are not valid.
HTTP Status Code: 400

 ** OptInRequiredException **
 The account must be opted in to Compute Optimizer Automation before performing this action.
HTTP Status Code: 403

 ** ServiceUnavailableException **
 The service is temporarily unavailable.
HTTP Status Code: 503

 ** ThrottlingException **
 The request was denied due to request throttling.
HTTP Status Code: 429

## See Also
<a name="API_automation_DeleteOrganizationEnrollmentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-automation-2025-09-22/DeleteOrganizationEnrollmentConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-automation-2025-09-22/DeleteOrganizationEnrollmentConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/DeleteOrganizationEnrollmentConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-automation-2025-09-22/DeleteOrganizationEnrollmentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/DeleteOrganizationEnrollmentConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-automation-2025-09-22/DeleteOrganizationEnrollmentConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-automation-2025-09-22/DeleteOrganizationEnrollmentConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-automation-2025-09-22/DeleteOrganizationEnrollmentConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-automation-2025-09-22/DeleteOrganizationEnrollmentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/DeleteOrganizationEnrollmentConfiguration)
