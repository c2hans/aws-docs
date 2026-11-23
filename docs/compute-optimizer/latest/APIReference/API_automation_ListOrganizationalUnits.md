---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ListOrganizationalUnits.html
---

# ListOrganizationalUnits

 Lists the organization root and organizational units (OUs), including whether an applicable organization enrollment configuration enables Automation for member accounts and the effective organization rule mode for each root or OU.

**Note**
Only the management account or a delegated administrator can perform this action.

## Request Syntax
<a name="API_automation_ListOrganizationalUnits_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "organizationalUnitIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_automation_ListOrganizationalUnits_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_automation_ListOrganizationalUnits_RequestSyntax) **   <a name="computeoptimizer-automation_ListOrganizationalUnits-request-maxResults"></a>
 The maximum number of organizational units to return in a single response. If you don't specify a value, the default is 1,000.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_automation_ListOrganizationalUnits_RequestSyntax) **   <a name="computeoptimizer-automation_ListOrganizationalUnits-request-nextToken"></a>
 The token to use to retrieve the next page of results.
Type: String
Pattern: `[A-Za-z0-9+/=]+`
Required: No

 ** [organizationalUnitIds](#API_automation_ListOrganizationalUnits_RequestSyntax) **   <a name="computeoptimizer-automation_ListOrganizationalUnits-request-organizationalUnitIds"></a>
 The organizational unit (OU) or organization root IDs to return. If you don't specify this parameter, the operation returns the organization root and every OU.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 68.
Pattern: `(r-[0-9a-z]{4,32}|ou-[0-9a-z]{4,32}-[a-z0-9]{8,32})`
Required: No

## Response Syntax
<a name="API_automation_ListOrganizationalUnits_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "organizationalUnits": [
      {
         "autoEnrollMemberAccounts": "string",
         "organizationalUnitId": "string",
         "organizationRuleMode": "string",
         "organizationRuleModeSource": {
            "sourceTargetId": "string",
            "sourceType": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_automation_ListOrganizationalUnits_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_automation_ListOrganizationalUnits_ResponseSyntax) **   <a name="computeoptimizer-automation_ListOrganizationalUnits-response-nextToken"></a>
 The token to use to retrieve the next page of results.
Type: String
Pattern: `[A-Za-z0-9+/=]+`

 ** [organizationalUnits](#API_automation_ListOrganizationalUnits_ResponseSyntax) **   <a name="computeoptimizer-automation_ListOrganizationalUnits-response-organizationalUnits"></a>
 The organizational units and organization root returned in this page of results, including the organization rule mode that applies to each.
Type: Array of [OrganizationalUnitInfo](API_automation_OrganizationalUnitInfo.md) objects

## Errors
<a name="API_automation_ListOrganizationalUnits_Errors"></a>

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
<a name="API_automation_ListOrganizationalUnits_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-automation-2025-09-22/ListOrganizationalUnits)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-automation-2025-09-22/ListOrganizationalUnits)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/ListOrganizationalUnits)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-automation-2025-09-22/ListOrganizationalUnits)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/ListOrganizationalUnits)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-automation-2025-09-22/ListOrganizationalUnits)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-automation-2025-09-22/ListOrganizationalUnits)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-automation-2025-09-22/ListOrganizationalUnits)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-automation-2025-09-22/ListOrganizationalUnits)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/ListOrganizationalUnits)
