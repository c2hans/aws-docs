---
source_url: https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_CreateSpace.html
---

# CreateSpace
<a name="API_CreateSpace"></a>

**Note**
End of support notice: On June 30, 2027, AWS will end support for AWS re:Post Private. After June 30, 2027, you will no longer be able to access the re:Post Private console or re:Post Private resources. For more information, see [AWS re:Post Private end of support](https://docs.aws.amazon.com/repostprivate/latest/userguide/repost-private-end-of-support.html).

Creates an AWS re:Post Private private re:Post.

## Request Syntax
<a name="API_CreateSpace_RequestSyntax"></a>

```
POST /spaces HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "name": "{{string}}",
   "roleArn": "{{string}}",
   "subdomain": "{{string}}",
   "supportedEmailDomains": {
      "allowedDomains": [ "{{string}}" ],
      "enabled": "{{string}}"
   },
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "tier": "{{string}}",
   "userKMSKey": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateSpace_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateSpace_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_CreateSpace_RequestSyntax) **   <a name="repostprivate-CreateSpace-request-description"></a>
A description for the private re:Post. This is used only to help you identify this private re:Post.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [name](#API_CreateSpace_RequestSyntax) **   <a name="repostprivate-CreateSpace-request-name"></a>
The name for the private re:Post. This must be unique in your account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 30.
Required: Yes

 ** [roleArn](#API_CreateSpace_RequestSyntax) **   <a name="repostprivate-CreateSpace-request-roleArn"></a>
The IAM role that grants permissions to the private re:Post to convert unanswered questions into AWS support tickets.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** [subdomain](#API_CreateSpace_RequestSyntax) **   <a name="repostprivate-CreateSpace-request-subdomain"></a>
The subdomain that you use to access your AWS re:Post Private private re:Post. All custom subdomains must be approved by AWS before use. In addition to your custom subdomain, all private re:Posts are issued an AWS generated subdomain for immediate use.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Required: Yes

 ** [supportedEmailDomains](#API_CreateSpace_RequestSyntax) **   <a name="repostprivate-CreateSpace-request-supportedEmailDomains"></a>

Type: [SupportedEmailDomainsParameters](API_SupportedEmailDomainsParameters.md) object
Required: No

 ** [tags](#API_CreateSpace_RequestSyntax) **   <a name="repostprivate-CreateSpace-request-tags"></a>
The list of tags associated with the private re:Post.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [tier](#API_CreateSpace_RequestSyntax) **   <a name="repostprivate-CreateSpace-request-tier"></a>
The pricing tier for the private re:Post.
Type: String
Valid Values: `BASIC | STANDARD`
Required: Yes

 ** [userKMSKey](#API_CreateSpace_RequestSyntax) **   <a name="repostprivate-CreateSpace-request-userKMSKey"></a>
The AWS KMS key ARN that’s used for the AWS KMS encryption. If you don't provide a key, your data is encrypted by default with a key that AWS owns and manages for you.
Type: String
Required: No

## Response Syntax
<a name="API_CreateSpace_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "spaceId": "string"
}
```

## Response Elements
<a name="API_CreateSpace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [spaceId](#API_CreateSpace_ResponseSyntax) **   <a name="repostprivate-CreateSpace-response-spaceId"></a>
The unique ID of the private re:Post.
Type: String

## Errors
<a name="API_CreateSpace_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 409

 ** InternalServerException **
Unexpected error during processing of request.
 ** retryAfterSeconds **
Advice to clients on when the call can be safely retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
Request would cause a service quota to be exceeded.
 ** quotaCode **
The code to identify the quota.
 ** resourceId **
The id of the resource.
 ** resourceType **
The type of the resource.
 ** serviceCode **
The code to identify the service.
HTTP Status Code: 402

 ** ThrottlingException **
Request was denied due to request throttling.
 ** quotaCode **
The code to identify the quota.
 ** retryAfterSeconds **
 Advice to clients on when the call can be safely retried.
 ** serviceCode **
The code to identify the service.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The field that caused the error, if applicable.
 ** reason **
The reason why the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_CreateSpace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/repostspace-2022-05-13/CreateSpace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/repostspace-2022-05-13/CreateSpace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/repostspace-2022-05-13/CreateSpace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/repostspace-2022-05-13/CreateSpace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/repostspace-2022-05-13/CreateSpace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/repostspace-2022-05-13/CreateSpace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/repostspace-2022-05-13/CreateSpace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/repostspace-2022-05-13/CreateSpace)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/repostspace-2022-05-13/CreateSpace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/repostspace-2022-05-13/CreateSpace)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS re:Post Private. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query repostprivate` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
