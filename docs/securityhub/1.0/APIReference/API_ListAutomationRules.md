---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListAutomationRules.html
---

# ListAutomationRules
<a name="API_ListAutomationRules"></a>

 A list of automation rules and their metadata for the calling account.

## Request Syntax
<a name="API_ListAutomationRules_RequestSyntax"></a>

```
GET /automationrules/list?MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAutomationRules_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListAutomationRules_RequestSyntax) **   <a name="securityhub-ListAutomationRules-request-uri-MaxResults"></a>
 The maximum number of rules to return in the response. This currently ranges from 1 to 100.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListAutomationRules_RequestSyntax) **   <a name="securityhub-ListAutomationRules-request-uri-NextToken"></a>
 A token to specify where to start paginating the response. This is the `NextToken` from a previously truncated response. On your first call to the `ListAutomationRules` API, set the value of this parameter to `NULL`.

## Request Body
<a name="API_ListAutomationRules_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAutomationRules_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AutomationRulesMetadata": [
      {
         "CreatedAt": "string",
         "CreatedBy": "string",
         "Description": "string",
         "IsTerminal": boolean,
         "RuleArn": "string",
         "RuleName": "string",
         "RuleOrder": number,
         "RuleStatus": "string",
         "UpdatedAt": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAutomationRules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AutomationRulesMetadata](#API_ListAutomationRules_ResponseSyntax) **   <a name="securityhub-ListAutomationRules-response-AutomationRulesMetadata"></a>
 Metadata for rules in the calling account. The response includes rules with a `RuleStatus` of `ENABLED` and `DISABLED`.
Type: Array of [AutomationRulesMetadata](API_AutomationRulesMetadata.md) objects

 ** [NextToken](#API_ListAutomationRules_ResponseSyntax) **   <a name="securityhub-ListAutomationRules-response-NextToken"></a>
 A pagination token for the response.
Type: String

## Errors
<a name="API_ListAutomationRules_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account or throttling limits. The error code describes the limit exceeded.
HTTP Status Code: 429

## See Also
<a name="API_ListAutomationRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/ListAutomationRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/ListAutomationRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ListAutomationRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/ListAutomationRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ListAutomationRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/ListAutomationRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/ListAutomationRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/ListAutomationRules)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/ListAutomationRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ListAutomationRules)
