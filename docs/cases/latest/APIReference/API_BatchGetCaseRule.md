---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_BatchGetCaseRule.html
---

# BatchGetCaseRule
<a name="API_connect-cases_BatchGetCaseRule"></a>

Gets a batch of case rules. In the Connect Customer admin website, case rules are known as *case field conditions*. For more information about case field conditions, see [Add case field conditions to a case template](https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html).

## Request Syntax
<a name="API_connect-cases_BatchGetCaseRule_RequestSyntax"></a>

```
POST /domains/{{domainId}}/rules-batch HTTP/1.1
Content-type: application/json

{
   "caseRules": [
      {
         "id": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_connect-cases_BatchGetCaseRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainId](#API_connect-cases_BatchGetCaseRule_RequestSyntax) **   <a name="connect-connect-cases_BatchGetCaseRule-request-uri-domainId"></a>
Unique identifier of a Cases domain.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Request Body
<a name="API_connect-cases_BatchGetCaseRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [caseRules](#API_connect-cases_BatchGetCaseRule_RequestSyntax) **   <a name="connect-connect-cases_BatchGetCaseRule-request-caseRules"></a>
A list of case rule identifiers.
Type: Array of [CaseRuleIdentifier](API_connect-cases_CaseRuleIdentifier.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: Yes

## Response Syntax
<a name="API_connect-cases_BatchGetCaseRule_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "caseRules": [
      {
         "caseRuleArn": "string",
         "caseRuleId": "string",
         "createdTime": "string",
         "deleted": boolean,
         "description": "string",
         "lastModifiedTime": "string",
         "name": "string",
         "rule": { ... },
         "tags": {
            "string" : "string"
         }
      }
   ],
   "errors": [
      {
         "errorCode": "string",
         "id": "string",
         "message": "string"
      }
   ],
   "unprocessedCaseRules": [ "string" ]
}
```

## Response Elements
<a name="API_connect-cases_BatchGetCaseRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [caseRules](#API_connect-cases_BatchGetCaseRule_ResponseSyntax) **   <a name="connect-connect-cases_BatchGetCaseRule-response-caseRules"></a>
A list of detailed case rule information.
Type: Array of [GetCaseRuleResponse](API_connect-cases_GetCaseRuleResponse.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [errors](#API_connect-cases_BatchGetCaseRule_ResponseSyntax) **   <a name="connect-connect-cases_BatchGetCaseRule-response-errors"></a>
A list of case rule errors.
Type: Array of [CaseRuleError](API_connect-cases_CaseRuleError.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [unprocessedCaseRules](#API_connect-cases_BatchGetCaseRule_ResponseSyntax) **   <a name="connect-connect-cases_BatchGetCaseRule-response-unprocessedCaseRules"></a>
A list of unprocessed case rule identifiers.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 500.

## Errors
<a name="API_connect-cases_BatchGetCaseRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
We couldn't process your request because of an issue with the server. Try again later.
 ** retryAfterSeconds **
Advice to clients on when the call can be safely retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **
We couldn't find the requested resource. Check that your resources exists and were created in the same AWS Region as your request, and try your request again.
 ** resourceId **
Unique identifier of the resource affected.
 ** resourceType **
Type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
The rate has been exceeded for this API. Please try again after a few minutes.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. Check the syntax and try again.
HTTP Status Code: 400

## See Also
<a name="API_connect-cases_BatchGetCaseRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcases-2022-10-03/BatchGetCaseRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcases-2022-10-03/BatchGetCaseRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/BatchGetCaseRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcases-2022-10-03/BatchGetCaseRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/BatchGetCaseRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcases-2022-10-03/BatchGetCaseRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcases-2022-10-03/BatchGetCaseRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcases-2022-10-03/BatchGetCaseRule)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connectcases-2022-10-03/BatchGetCaseRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/BatchGetCaseRule)
