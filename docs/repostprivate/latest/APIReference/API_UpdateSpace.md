---
source_url: https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_UpdateSpace.html
---

# UpdateSpace
<a name="API_UpdateSpace"></a>

**Note**
End of support notice: On June 30, 2027, AWS will end support for AWS re:Post Private. After June 30, 2027, you will no longer be able to access the re:Post Private console or re:Post Private resources. For more information, see [AWS re:Post Private end of support](https://docs.aws.amazon.com/repostprivate/latest/userguide/repost-private-end-of-support.html).

Modifies an existing AWS re:Post Private private re:Post.

## Request Syntax
<a name="API_UpdateSpace_RequestSyntax"></a>

```
PUT /spaces/{{spaceId}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "roleArn": "{{string}}",
   "supportedEmailDomains": {
      "allowedDomains": [ "{{string}}" ],
      "enabled": "{{string}}"
   },
   "tier": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateSpace_RequestParameters"></a>

The request uses the following URI parameters.

 ** [spaceId](#API_UpdateSpace_RequestSyntax) **   <a name="repostprivate-UpdateSpace-request-uri-spaceId"></a>
The unique ID of this private re:Post.
Required: Yes

## Request Body
<a name="API_UpdateSpace_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateSpace_RequestSyntax) **   <a name="repostprivate-UpdateSpace-request-description"></a>
A description for the private re:Post. This is used only to help you identify this private re:Post.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** [roleArn](#API_UpdateSpace_RequestSyntax) **   <a name="repostprivate-UpdateSpace-request-roleArn"></a>
The IAM role that grants permissions to the private re:Post to convert unanswered questions into AWS support tickets.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** [supportedEmailDomains](#API_UpdateSpace_RequestSyntax) **   <a name="repostprivate-UpdateSpace-request-supportedEmailDomains"></a>

Type: [SupportedEmailDomainsParameters](API_SupportedEmailDomainsParameters.md) object
Required: No

 ** [tier](#API_UpdateSpace_RequestSyntax) **   <a name="repostprivate-UpdateSpace-request-tier"></a>
The pricing tier of this private re:Post.
Type: String
Valid Values: `BASIC | STANDARD`
Required: No

## Response Syntax
<a name="API_UpdateSpace_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateSpace_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateSpace_Errors"></a>

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
<a name="API_UpdateSpace_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/repostspace-2022-05-13/UpdateSpace)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/repostspace-2022-05-13/UpdateSpace)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/repostspace-2022-05-13/UpdateSpace)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/repostspace-2022-05-13/UpdateSpace)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/repostspace-2022-05-13/UpdateSpace)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/repostspace-2022-05-13/UpdateSpace)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/repostspace-2022-05-13/UpdateSpace)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/repostspace-2022-05-13/UpdateSpace)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/repostspace-2022-05-13/UpdateSpace)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/repostspace-2022-05-13/UpdateSpace)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS re:Post Private. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query repostprivate` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
