---
source_url: https://docs.aws.amazon.com/Route53/latest/APIReference/API_route53globalresolver_GetAccessToken.html
---

# GetAccessToken
<a name="API_route53globalresolver_GetAccessToken"></a>

Retrieves information about an access token.

**Important**
Route 53 Global Resolver is a global service that supports resolvers in multiple AWS Regions but you must specify the US East (Ohio) Region to create, update, or otherwise work with Route 53 Global Resolver resources. That is, for example, specify `--region us-east-2` on AWS CLI commands.

## Request Syntax
<a name="API_route53globalresolver_GetAccessToken_RequestSyntax"></a>

```
GET /tokens/{{accessTokenId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_route53globalresolver_GetAccessToken_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accessTokenId](#API_route53globalresolver_GetAccessToken_RequestSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetAccessToken-request-uri-accessTokenId"></a>
ID of the token.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`
Required: Yes

## Request Body
<a name="API_route53globalresolver_GetAccessToken_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_route53globalresolver_GetAccessToken_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "arn": "string",
   "clientToken": "string",
   "createdAt": "string",
   "dnsViewId": "string",
   "expiresAt": "string",
   "globalResolverId": "string",
   "id": "string",
   "name": "string",
   "status": "string",
   "updatedAt": "string",
   "value": "string"
}
```

## Response Elements
<a name="API_route53globalresolver_GetAccessToken_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_route53globalresolver_GetAccessToken_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetAccessToken-response-arn"></a>
The Amazon Resource Name (ARN) of the token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:[-.a-z0-9]{1,63}:[-.a-z0-9]{1,63}:[-.a-z0-9]{0,63}:[-.a-z0-9]{0,63}:[^/].{0,1023}`

 ** [clientToken](#API_route53globalresolver_GetAccessToken_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetAccessToken-response-clientToken"></a>
A unique, case-sensitive identifier to ensure idempotency. This means that making the same request multiple times with the same `clientToken` has the same result every time.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [createdAt](#API_route53globalresolver_GetAccessToken_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetAccessToken-response-createdAt"></a>
The time and date the token was created.
Type: Timestamp

 ** [dnsViewId](#API_route53globalresolver_GetAccessToken_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetAccessToken-response-dnsViewId"></a>
ID of the DNS view the token is associated to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [expiresAt](#API_route53globalresolver_GetAccessToken_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetAccessToken-response-expiresAt"></a>
The token's expiration time and date.
Type: Timestamp

 ** [globalResolverId](#API_route53globalresolver_GetAccessToken_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetAccessToken-response-globalResolverId"></a>
ID of the Global Resolver.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [id](#API_route53globalresolver_GetAccessToken_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetAccessToken-response-id"></a>
ID of the token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[-.a-zA-Z0-9]+`

 ** [name](#API_route53globalresolver_GetAccessToken_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetAccessToken-response-name"></a>
Name of the token.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `(?!^[0-9]+$)([a-zA-Z0-9-_/' ']+)`

 ** [status](#API_route53globalresolver_GetAccessToken_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetAccessToken-response-status"></a>
The operational status of the token.
Type: String
Valid Values: `CREATING | OPERATIONAL | DELETING`

 ** [updatedAt](#API_route53globalresolver_GetAccessToken_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetAccessToken-response-updatedAt"></a>
The time and date the token was created.
Type: Timestamp

 ** [value](#API_route53globalresolver_GetAccessToken_ResponseSyntax) **   <a name="Route53GlobalResolver-route53globalresolver_GetAccessToken-response-value"></a>
The value of the token.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.

## Errors
<a name="API_route53globalresolver_GetAccessToken_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform this operation. Check your IAM permissions and try again.
HTTP Status Code: 403

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
<a name="API_route53globalresolver_GetAccessToken_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/route53globalresolver-2022-09-27/GetAccessToken)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/route53globalresolver-2022-09-27/GetAccessToken)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/route53globalresolver-2022-09-27/GetAccessToken)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/route53globalresolver-2022-09-27/GetAccessToken)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/route53globalresolver-2022-09-27/GetAccessToken)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/route53globalresolver-2022-09-27/GetAccessToken)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/route53globalresolver-2022-09-27/GetAccessToken)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/route53globalresolver-2022-09-27/GetAccessToken)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/route53globalresolver-2022-09-27/GetAccessToken)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/route53globalresolver-2022-09-27/GetAccessToken)
