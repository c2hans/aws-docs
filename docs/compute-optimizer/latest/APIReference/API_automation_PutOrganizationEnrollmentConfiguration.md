---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_PutOrganizationEnrollmentConfiguration.html
---

# PutOrganizationEnrollmentConfiguration

 Creates or updates an organization enrollment configuration. The organization enrollment configuration sets the organization rule mode on the specified account, organizational unit (OU), or organization root and enables Automation for affected member accounts that have opted in to Compute Optimizer, including accounts that join later. Changes on an OU or the organization root can take up to 5 minutes. Organization enrollment configurations take precedence over settings made by `AssociateAccounts` and `DisassociateAccounts`. You must specify at least one configuration in the request.

**Note**
Only the management account or a delegated administrator can perform this action.
Organization enrollment configurations can't be created for the management account.

## Request Syntax
<a name="API_automation_PutOrganizationEnrollmentConfiguration_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "organizationRuleMode": "{{string}}",
   "target": { ... }
}
```

## Request Parameters
<a name="API_automation_PutOrganizationEnrollmentConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_automation_PutOrganizationEnrollmentConfiguration_RequestSyntax) **   <a name="computeoptimizer-automation_PutOrganizationEnrollmentConfiguration-request-clientToken"></a>
 A unique identifier to ensure idempotency of the request.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,64}`
Required: No

 ** [organizationRuleMode](#API_automation_PutOrganizationEnrollmentConfiguration_RequestSyntax) **   <a name="computeoptimizer-automation_PutOrganizationEnrollmentConfiguration-request-organizationRuleMode"></a>
 The organization rule mode to set on the target. An organization enrollment configuration with either `AnyAllowed` or `NoneAllowed` enables Automation for affected member accounts. `AnyAllowed` permits organization rules to apply to those accounts, while `NoneAllowed` doesn't.
Type: String
Valid Values: `AnyAllowed | NoneAllowed`
Required: No

 ** [target](#API_automation_PutOrganizationEnrollmentConfiguration_RequestSyntax) **   <a name="computeoptimizer-automation_PutOrganizationEnrollmentConfiguration-request-target"></a>
 The account, organizational unit (OU), or organization root on which to create or update the organization enrollment configuration. You can't specify the management account.
Type: [OrganizationTarget](API_automation_OrganizationTarget.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Elements
<a name="API_automation_PutOrganizationEnrollmentConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_automation_PutOrganizationEnrollmentConfiguration_Errors"></a>

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
<a name="API_automation_PutOrganizationEnrollmentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-automation-2025-09-22/PutOrganizationEnrollmentConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-automation-2025-09-22/PutOrganizationEnrollmentConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/PutOrganizationEnrollmentConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-automation-2025-09-22/PutOrganizationEnrollmentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/PutOrganizationEnrollmentConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-automation-2025-09-22/PutOrganizationEnrollmentConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-automation-2025-09-22/PutOrganizationEnrollmentConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-automation-2025-09-22/PutOrganizationEnrollmentConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-automation-2025-09-22/PutOrganizationEnrollmentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/PutOrganizationEnrollmentConfiguration)
