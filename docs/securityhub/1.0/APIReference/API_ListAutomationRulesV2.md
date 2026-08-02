---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ListAutomationRulesV2.html
---

# ListAutomationRulesV2
<a name="API_ListAutomationRulesV2"></a>

Returns a list of automation rules and metadata for the calling account.

## Request Syntax
<a name="API_ListAutomationRulesV2_RequestSyntax"></a>

```
GET /automationrulesv2/list?MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAutomationRulesV2_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListAutomationRulesV2_RequestSyntax) **   <a name="securityhub-ListAutomationRulesV2-request-uri-MaxResults"></a>
The maximum number of results to return.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_ListAutomationRulesV2_RequestSyntax) **   <a name="securityhub-ListAutomationRulesV2-request-uri-NextToken"></a>
The token required for pagination. On your first call, set the value of this parameter to `NULL`. For subsequent calls, to continue listing data, set the value of this parameter to the value returned in the previous response.

## Request Body
<a name="API_ListAutomationRulesV2_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAutomationRulesV2_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Rules": [
      {
         "Actions": [
            {
               "Type": "string"
            }
         ],
         "CreatedAt": "string",
         "Description": "string",
         "RuleArn": "string",
         "RuleId": "string",
         "RuleName": "string",
         "RuleOrder": number,
         "RuleStatus": "string",
         "UpdatedAt": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListAutomationRulesV2_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListAutomationRulesV2_ResponseSyntax) **   <a name="securityhub-ListAutomationRulesV2-response-NextToken"></a>
The pagination token to use to request the next page of results. Otherwise, this parameter is null.
Type: String

 ** [Rules](#API_ListAutomationRulesV2_ResponseSyntax) **   <a name="securityhub-ListAutomationRulesV2-response-Rules"></a>
An array of automation rules.
Type: Array of [AutomationRulesMetadataV2](API_AutomationRulesMetadataV2.md) objects

## Errors
<a name="API_ListAutomationRulesV2_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

 ** ConflictException **
The request causes conflict with the current state of the service resource.
HTTP Status Code: 409

 ** InternalServerException **
 The request has failed due to an internal failure of the service.
HTTP Status Code: 500

 ** ThrottlingException **
 The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation because it's missing required fields or has invalid inputs.
HTTP Status Code: 400

## See Also
<a name="API_ListAutomationRulesV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/ListAutomationRulesV2)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/ListAutomationRulesV2)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ListAutomationRulesV2)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/ListAutomationRulesV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ListAutomationRulesV2)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/ListAutomationRulesV2)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/ListAutomationRulesV2)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/ListAutomationRulesV2)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/ListAutomationRulesV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ListAutomationRulesV2)
