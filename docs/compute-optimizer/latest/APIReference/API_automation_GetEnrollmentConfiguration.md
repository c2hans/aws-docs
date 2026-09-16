---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_GetEnrollmentConfiguration.html
---

# GetEnrollmentConfiguration
<a name="API_automation_GetEnrollmentConfiguration"></a>

 Retrieves the current enrollment configuration for Compute Optimizer Automation.

## Response Syntax
<a name="API_automation_GetEnrollmentConfiguration_ResponseSyntax"></a>

```
{
   "lastUpdatedTimestamp": number,
   "organizationRuleMode": "string",
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_automation_GetEnrollmentConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [lastUpdatedTimestamp](#API_automation_GetEnrollmentConfiguration_ResponseSyntax) **   <a name="computeoptimizer-automation_GetEnrollmentConfiguration-response-lastUpdatedTimestamp"></a>
 The timestamp of the last update to the enrollment configuration.
Type: Timestamp

 ** [organizationRuleMode](#API_automation_GetEnrollmentConfiguration_ResponseSyntax) **   <a name="computeoptimizer-automation_GetEnrollmentConfiguration-response-organizationRuleMode"></a>
Specifies whether the management account can create Automation rules that implement optimization actions for this account.
Type: String
Valid Values: `AnyAllowed | NoneAllowed`

 ** [status](#API_automation_GetEnrollmentConfiguration_ResponseSyntax) **   <a name="computeoptimizer-automation_GetEnrollmentConfiguration-response-status"></a>
 The current enrollment status.
Type: String
Valid Values: `Active | Inactive | Pending | Failed`

 ** [statusReason](#API_automation_GetEnrollmentConfiguration_ResponseSyntax) **   <a name="computeoptimizer-automation_GetEnrollmentConfiguration-response-statusReason"></a>
 The reason for the current enrollment status.
Type: String

## Errors
<a name="API_automation_GetEnrollmentConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You do not have sufficient permissions to perform this action.
HTTP Status Code: 400

 ** ForbiddenException **
 You are not authorized to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
 An internal error occurred while processing the request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
 One or more parameter values are not valid.
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
<a name="API_automation_GetEnrollmentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-automation-2025-09-22/GetEnrollmentConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-automation-2025-09-22/GetEnrollmentConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/GetEnrollmentConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-automation-2025-09-22/GetEnrollmentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/GetEnrollmentConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-automation-2025-09-22/GetEnrollmentConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-automation-2025-09-22/GetEnrollmentConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-automation-2025-09-22/GetEnrollmentConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-automation-2025-09-22/GetEnrollmentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/GetEnrollmentConfiguration)
