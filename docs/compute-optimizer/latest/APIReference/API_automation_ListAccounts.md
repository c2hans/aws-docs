---
source_url: https://docs.aws.amazon.com/compute-optimizer/latest/APIReference/API_automation_ListAccounts.html
---

# ListAccounts
<a name="API_automation_ListAccounts"></a>

 Lists the accounts in your organization that are enrolled in Compute Optimizer and whether they have enabled Automation.

**Note**
Only the management account or a delegated administrator can perform this action.

## Request Syntax
<a name="API_automation_ListAccounts_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_automation_ListAccounts_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_automation_ListAccounts_RequestSyntax) **   <a name="computeoptimizer-automation_ListAccounts-request-maxResults"></a>
 The maximum number of results to return in a single call.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 1000.
Required: No

 ** [nextToken](#API_automation_ListAccounts_RequestSyntax) **   <a name="computeoptimizer-automation_ListAccounts-request-nextToken"></a>
 The token for the next page of results.
Type: String
Pattern: `[A-Za-z0-9+/=]+`
Required: No

## Response Syntax
<a name="API_automation_ListAccounts_ResponseSyntax"></a>

```
{
   "accounts": [
      {
         "accountId": "string",
         "lastUpdatedTimestamp": number,
         "organizationRuleMode": "string",
         "status": "string",
         "statusReason": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_automation_ListAccounts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accounts](#API_automation_ListAccounts_ResponseSyntax) **   <a name="computeoptimizer-automation_ListAccounts-response-accounts"></a>
 The list of accounts in your organization enrolled in Compute Optimizer
Type: Array of [AccountInfo](API_automation_AccountInfo.md) objects

 ** [nextToken](#API_automation_ListAccounts_ResponseSyntax) **   <a name="computeoptimizer-automation_ListAccounts-response-nextToken"></a>
 The token to use to retrieve the next page of results.
Type: String
Pattern: `[A-Za-z0-9+/=]+`

## Errors
<a name="API_automation_ListAccounts_Errors"></a>

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

 ** NotManagementAccountException **
 The operation can only be performed by a management account.
HTTP Status Code: 400

 ** OptInRequiredException **
 The account must be opted in to Compute Optimizer Automation before performing this action.
HTTP Status Code: 400

 ** ServiceUnavailableException **
 The service is temporarily unavailable.
HTTP Status Code: 500

 ** ThrottlingException **
 The request was denied due to request throttling.
HTTP Status Code: 400

## See Also
<a name="API_automation_ListAccounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/compute-optimizer-automation-2025-09-22/ListAccounts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/compute-optimizer-automation-2025-09-22/ListAccounts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/compute-optimizer-automation-2025-09-22/ListAccounts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/compute-optimizer-automation-2025-09-22/ListAccounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/compute-optimizer-automation-2025-09-22/ListAccounts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/compute-optimizer-automation-2025-09-22/ListAccounts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/compute-optimizer-automation-2025-09-22/ListAccounts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/compute-optimizer-automation-2025-09-22/ListAccounts)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/compute-optimizer-automation-2025-09-22/ListAccounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/compute-optimizer-automation-2025-09-22/ListAccounts)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Compute Optimizer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query compute-optimizer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
