---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateResourcePolicy.html
---

# UpdateResourcePolicy
<a name="API_UpdateResourcePolicy"></a>

Replaces the existing resource policy for a bot or bot alias with a new one. If the policy doesn't exist, Amazon Lex returns an exception.

## Request Syntax
<a name="API_UpdateResourcePolicy_RequestSyntax"></a>

```
PUT /policy/{{resourceArn}}/?expectedRevisionId={{expectedRevisionId}} HTTP/1.1
Content-type: application/json

{
   "policy": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateResourcePolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [expectedRevisionId](#API_UpdateResourcePolicy_RequestSyntax) **   <a name="lexv2-UpdateResourcePolicy-request-uri-expectedRevisionId"></a>
The identifier of the revision of the policy to update. If this revision ID doesn't match the current revision ID, Amazon Lex throws an exception.
If you don't specify a revision, Amazon Lex overwrites the contents of the policy with the new values.
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^[0-9]+$`

 ** [resourceArn](#API_UpdateResourcePolicy_RequestSyntax) **   <a name="lexv2-UpdateResourcePolicy-request-uri-resourceArn"></a>
The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.
Length Constraints: Minimum length of 1. Maximum length of 1011.
Required: Yes

## Request Body
<a name="API_UpdateResourcePolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [policy](#API_UpdateResourcePolicy_RequestSyntax) **   <a name="lexv2-UpdateResourcePolicy-request-policy"></a>
A resource policy to add to the resource. The policy is a JSON structure that contains one or more statements that define the policy. The policy must follow the IAM syntax. For more information about the contents of a JSON policy document, see [ IAM JSON policy reference ](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies.html).
If the policy isn't valid, Amazon Lex returns a validation exception.
Type: String
Length Constraints: Minimum length of 2.
Required: Yes

## Response Syntax
<a name="API_UpdateResourcePolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "resourceArn": "string",
   "revisionId": "string"
}
```

## Response Elements
<a name="API_UpdateResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [resourceArn](#API_UpdateResourcePolicy_ResponseSyntax) **   <a name="lexv2-UpdateResourcePolicy-response-resourceArn"></a>
The Amazon Resource Name (ARN) of the bot or bot alias that the resource policy is attached to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.

 ** [revisionId](#API_UpdateResourcePolicy_ResponseSyntax) **   <a name="lexv2-UpdateResourcePolicy-response-revisionId"></a>
The current revision of the resource policy. Use the revision ID to make sure that you are updating the most current version of a resource policy when you add a policy statement to a resource, delete a resource, or update a resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5.
Pattern: `^[0-9]+$`

## Errors
<a name="API_UpdateResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

 ** PreconditionFailedException **
Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.
HTTP Status Code: 412

 ** ResourceNotFoundException **
You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
You have reached a quota for your bot.
HTTP Status Code: 402

 ** ThrottlingException **
Your request rate is too high. Reduce the frequency of requests.
 ** retryAfterSeconds **
The number of seconds after which the user can invoke the API again.
HTTP Status Code: 429

 ** ValidationException **
One of the input parameters in your request isn't valid. Check the parameters and try your request again.
HTTP Status Code: 400

## See Also
<a name="API_UpdateResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/UpdateResourcePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/UpdateResourcePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/UpdateResourcePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/UpdateResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/UpdateResourcePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/UpdateResourcePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/UpdateResourcePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/UpdateResourcePolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/UpdateResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/UpdateResourcePolicy)
