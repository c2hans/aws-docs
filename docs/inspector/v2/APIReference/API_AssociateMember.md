---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_AssociateMember.html
---

# AssociateMember
<a name="API_AssociateMember"></a>

Associates an AWS account with an Amazon Inspector delegated administrator. An HTTP 200 response indicates the association was successfully started, but doesn’t indicate whether it was completed. You can check if the association completed by using [ListMembers](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListMembers.html) for multiple accounts or [GetMembers](https://docs.aws.amazon.com/inspector/v2/APIReference/API_GetMember.html) for a single account.

## Request Syntax
<a name="API_AssociateMember_RequestSyntax"></a>

```
POST /members/associate HTTP/1.1
Content-type: application/json

{
   "accountId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AssociateMember_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_AssociateMember_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountId](#API_AssociateMember_RequestSyntax) **   <a name="inspector2-AssociateMember-request-accountId"></a>
The AWS account ID of the member account to be associated.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: Yes

## Response Syntax
<a name="API_AssociateMember_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "accountId": "string"
}
```

## Response Elements
<a name="API_AssociateMember_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [accountId](#API_AssociateMember_ResponseSyntax) **   <a name="inspector2-AssociateMember-response-accountId"></a>
The AWS account ID of the successfully associated member account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`

## Errors
<a name="API_AssociateMember_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 For `Enable`, you receive this error if you attempt to use a feature in an unsupported AWS Region.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed due to an internal failure of the Amazon Inspector service.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
You have exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use Service Quotas to request a service quota increase.
 ** resourceId **
The ID of the resource that exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation due to missing required fields or having invalid inputs.
 ** fields **
The fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_AssociateMember_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/AssociateMember)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/AssociateMember)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/AssociateMember)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/AssociateMember)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/AssociateMember)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/AssociateMember)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/AssociateMember)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/AssociateMember)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/AssociateMember)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/AssociateMember)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
