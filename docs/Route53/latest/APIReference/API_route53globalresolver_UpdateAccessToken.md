---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_UpdateAccessToken.html
---

# UpdateAccessToken
<a name="API_route53globalresolver_UpdateAccessToken"></a>

Updates the configuration of an access token.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Request Syntax
<a name="API_route53globalresolver_UpdateAccessToken_RequestSyntax"></a>

```
PATCH /tokens/{{accessTokenId}} HTTP/1.1
Content-type: application/json

{
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_route53globalresolver_UpdateAccessToken_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accessTokenId](#API_route53globalresolver_UpdateAccessToken_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateAccessToken-request-uri-accessTokenId"></a>
The ID of the token.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_route53globalresolver_UpdateAccessToken_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [name](#API_route53globalresolver_UpdateAccessToken_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateAccessToken-request-name"></a>
The new name of the token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`
Required: Yes

## Response Syntax
<a name="API_route53globalresolver_UpdateAccessToken_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "id": "string",
   "name": "string"
}
```

## Response Elements
<a name="API_route53globalresolver_UpdateAccessToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [id](#API_route53globalresolver_UpdateAccessToken_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateAccessToken-response-id"></a>
The ID of the token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [name](#API_route53globalresolver_UpdateAccessToken_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_UpdateAccessToken-response-name"></a>
The name of the token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`

## Errors
<a name="API_route53globalresolver_UpdateAccessToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform this operation. Check your IAM permissions and try again.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with the current state of the resource. This can occur when trying to modify a resource that is not in a valid state for the requested operation.
 ** resourceId **
The ID of the conflicting resource.
 ** resourceType **
The type of the conflicting resource.
HTTP Status Code: 409

 ** InternalServerException **
An internal server error occurred. Try again later.
 ** retryAfterSeconds **
Number of seconds in which the caller can retry the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found. Verify the resource ID and try again.
 ** resourceId **
The unique ID of the resource referenced in the failed request.
 ** resourceType **
The resource type of the resource referenced in the failed request.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request would exceed one or more service quotas. Check your current usage and quotas, then try again.
 ** quotaCode **
The quota code recognized by the AWS Service Quotas service.
 ** resourceId **
The unique ID of the resource referenced in the failed request.
 ** resourceType **
The resource type of the resource referenced in the failed request.
 ** serviceCode **
The code for the AWS service that owns the quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was throttled due to too many requests. Wait a moment and try again.
 ** quotaCode **
The quota code recognized by the AWS Service Quotas service.
 ** retryAfterSeconds **
Number of seconds in which the caller can retry the request.
 ** serviceCode **
The code for the AWS service that owns the quota.
HTTP Status Code: 429

 ** ValidationException **
The input parameters are invalid. Check the parameter values and try again.
 ** fieldList **
The list of fields that aren't valid.
 ** reason **
Reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_route53globalresolver_UpdateAccessToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53globalresolver-2022-09-27/UpdateAccessToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53globalresolver-2022-09-27/UpdateAccessToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/UpdateAccessToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53globalresolver-2022-09-27/UpdateAccessToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/UpdateAccessToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53globalresolver-2022-09-27/UpdateAccessToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53globalresolver-2022-09-27/UpdateAccessToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53globalresolver-2022-09-27/UpdateAccessToken)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53globalresolver-2022-09-27/UpdateAccessToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/UpdateAccessToken)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Route 53. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query Route53` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
