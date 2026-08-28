---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_BatchDeleteAutomationRules.html
---

# BatchDeleteAutomationRules
<a name="API_BatchDeleteAutomationRules"></a>

 Deletes one or more automation rules.

## Request Syntax
<a name="API_BatchDeleteAutomationRules_RequestSyntax"></a>

```
POST /automationrules/delete HTTP/1.1
Content-type: application/json

{
   "AutomationRulesArns": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchDeleteAutomationRules_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchDeleteAutomationRules_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AutomationRulesArns](#API_BatchDeleteAutomationRules_RequestSyntax) **   <a name="securityhub-BatchDeleteAutomationRules-request-AutomationRulesArns"></a>
 A list of Amazon Resource Names (ARNs) for the rules that are to be deleted.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Pattern: `.*\S.*`
Required: Yes

## Response Syntax
<a name="API_BatchDeleteAutomationRules_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ProcessedAutomationRules": [ "string" ],
   "UnprocessedAutomationRules": [
      {
         "ErrorCode": number,
         "ErrorMessage": "string",
         "RuleArn": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchDeleteAutomationRules_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProcessedAutomationRules](#API_BatchDeleteAutomationRules_ResponseSyntax) **   <a name="securityhub-BatchDeleteAutomationRules-response-ProcessedAutomationRules"></a>
 A list of properly processed rule ARNs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Pattern: `.*\S.*`

 ** [UnprocessedAutomationRules](#API_BatchDeleteAutomationRules_ResponseSyntax) **   <a name="securityhub-BatchDeleteAutomationRules-response-UnprocessedAutomationRules"></a>
 A list of objects containing `RuleArn`, `ErrorCode`, and `ErrorMessage`. This parameter tells you which automation rules the request didn't delete and why.
Type: Array of [UnprocessedAutomationRule](API_UnprocessedAutomationRule.md) objects

## Errors
<a name="API_BatchDeleteAutomationRules_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

## See Also
<a name="API_BatchDeleteAutomationRules_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/BatchDeleteAutomationRules)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/BatchDeleteAutomationRules)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/BatchDeleteAutomationRules)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/BatchDeleteAutomationRules)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/BatchDeleteAutomationRules)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/BatchDeleteAutomationRules)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/BatchDeleteAutomationRules)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/BatchDeleteAutomationRules)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/BatchDeleteAutomationRules)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/BatchDeleteAutomationRules)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
