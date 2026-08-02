---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_UpdateCaseRule.html
---

# UpdateCaseRule
<a name="API_connect-cases_UpdateCaseRule"></a>

Updates a case rule. In the Connect Customer admin website, case rules are known as *case field conditions*. For more information about case field conditions, see [Add case field conditions to a case template](https://docs.aws.amazon.com/connect/latest/adminguide/case-field-conditions.html).

## Request Syntax
<a name="API_connect-cases_UpdateCaseRule_RequestSyntax"></a>

```
PUT /domains/{{domainId}}/case-rules/{{caseRuleId}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "name": "{{string}}",
   "rule": { ... }
}
```

## URI Request Parameters
<a name="API_connect-cases_UpdateCaseRule_RequestParameters"></a>

The request uses the following URI parameters.

 ** [caseRuleId](#API_connect-cases_UpdateCaseRule_RequestSyntax) **   <a name="connect-connect-cases_UpdateCaseRule-request-uri-caseRuleId"></a>
Unique identifier of a case rule.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [domainId](#API_connect-cases_UpdateCaseRule_RequestSyntax) **   <a name="connect-connect-cases_UpdateCaseRule-request-uri-domainId"></a>
Unique identifier of a Cases domain.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Request Body
<a name="API_connect-cases_UpdateCaseRule_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_connect-cases_UpdateCaseRule_RequestSyntax) **   <a name="connect-connect-cases_UpdateCaseRule-request-description"></a>
Description of a case rule.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

 ** [name](#API_connect-cases_UpdateCaseRule_RequestSyntax) **   <a name="connect-connect-cases_UpdateCaseRule-request-name"></a>
Name of the case rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*[\S]`
Required: No

 ** [rule](#API_connect-cases_UpdateCaseRule_RequestSyntax) **   <a name="connect-connect-cases_UpdateCaseRule-request-rule"></a>
Represents what rule type should take place, under what conditions.
Type: [CaseRuleDetails](API_connect-cases_CaseRuleDetails.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## Response Syntax
<a name="API_connect-cases_UpdateCaseRule_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_connect-cases_UpdateCaseRule_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_connect-cases_UpdateCaseRule_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.
HTTP Status Code: 409

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

 ** ServiceQuotaExceededException **
The service quota has been exceeded. For a list of service quotas, see [Connect Customer Service Quotas](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html) in the *Connect Customer Administrator Guide*.
HTTP Status Code: 402

 ** ThrottlingException **
The rate has been exceeded for this API. Please try again after a few minutes.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. Check the syntax and try again.
HTTP Status Code: 400

## See Also
<a name="API_connect-cases_UpdateCaseRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcases-2022-10-03/UpdateCaseRule)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcases-2022-10-03/UpdateCaseRule)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/UpdateCaseRule)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcases-2022-10-03/UpdateCaseRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/UpdateCaseRule)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcases-2022-10-03/UpdateCaseRule)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcases-2022-10-03/UpdateCaseRule)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcases-2022-10-03/UpdateCaseRule)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcases-2022-10-03/UpdateCaseRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/UpdateCaseRule)
