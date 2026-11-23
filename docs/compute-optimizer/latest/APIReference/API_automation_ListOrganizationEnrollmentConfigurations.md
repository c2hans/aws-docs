---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ListOrganizationEnrollmentConfigurations.html
---

# ListOrganizationEnrollmentConfigurations

 Lists the organization enrollment configurations that are stored directly on accounts, organizational units (OUs), and the organization root.

**Note**
Only the management account or a delegated administrator can perform this action.

## Request Syntax
<a name="API_automation_ListOrganizationEnrollmentConfigurations_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "targetType": "{{string}}"
}
```

## Request Parameters
<a name="API_automation_ListOrganizationEnrollmentConfigurations_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_automation_ListOrganizationEnrollmentConfigurations_RequestSyntax) **   <a name="computeoptimizer-automation_ListOrganizationEnrollmentConfigurations-request-maxResults"></a>
 The maximum number of organization enrollment configurations to return in a single response. If you don't specify a value, the default is 1,000.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_automation_ListOrganizationEnrollmentConfigurations_RequestSyntax) **   <a name="computeoptimizer-automation_ListOrganizationEnrollmentConfigurations-request-nextToken"></a>
 The token to use to retrieve the next page of results.
Type: String
Pattern: `[A-Za-z0-9+/=]+`
Required: No

 ** [targetType](#API_automation_ListOrganizationEnrollmentConfigurations_RequestSyntax) **   <a name="computeoptimizer-automation_ListOrganizationEnrollmentConfigurations-request-targetType"></a>
 The target type to use to filter the results. If you specify `OrganizationalUnit`, the results also include configurations stored on the organization root. If you don't specify a target type, the operation returns configurations for every target type.
Type: String
Valid Values: `Account | OrganizationalUnit`
Required: No

## Response Syntax
<a name="API_automation_ListOrganizationEnrollmentConfigurations_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "organizationEnrollmentConfigurations": [
      {
         "organizationRuleMode": "string",
         "targetId": "string",
         "targetType": "string"
      }
   ]
}
```

## Response Elements
<a name="API_automation_ListOrganizationEnrollmentConfigurations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_automation_ListOrganizationEnrollmentConfigurations_ResponseSyntax) **   <a name="computeoptimizer-automation_ListOrganizationEnrollmentConfigurations-response-nextToken"></a>
 The token to use to retrieve the next page of results.
Type: String
Pattern: `[A-Za-z0-9+/=]+`

 ** [organizationEnrollmentConfigurations](#API_automation_ListOrganizationEnrollmentConfigurations_ResponseSyntax) **   <a name="computeoptimizer-automation_ListOrganizationEnrollmentConfigurations-response-organizationEnrollmentConfigurations"></a>
 The organization enrollment configurations stored on each target in this page of results.
Type: Array of [OrganizationEnrollmentConfiguration](API_automation_OrganizationEnrollmentConfiguration.md) objects

## Errors
<a name="API_automation_ListOrganizationEnrollmentConfigurations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
 You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** ForbiddenException **
 You are not authorized to perform this action.
HTTP Status Code: 403

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
<a name="API_automation_ListOrganizationEnrollmentConfigurations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-automation-2025-09-22/ListOrganizationEnrollmentConfigurations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-automation-2025-09-22/ListOrganizationEnrollmentConfigurations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/ListOrganizationEnrollmentConfigurations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-automation-2025-09-22/ListOrganizationEnrollmentConfigurations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/ListOrganizationEnrollmentConfigurations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-automation-2025-09-22/ListOrganizationEnrollmentConfigurations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-automation-2025-09-22/ListOrganizationEnrollmentConfigurations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-automation-2025-09-22/ListOrganizationEnrollmentConfigurations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-automation-2025-09-22/ListOrganizationEnrollmentConfigurations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/ListOrganizationEnrollmentConfigurations)
