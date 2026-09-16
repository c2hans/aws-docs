---
source_url: https://docs.aws.amazon.com/signin/latest/APIReference/API_PutResourcePermissionStatement.html
---

# PutResourcePermissionStatement
<a name="API_PutResourcePermissionStatement"></a>

Creates a permission statement in the account's AWS Sign-In resource-based policy that specifies under what conditions principals can access AWS resources. Conditions can scope access by source VPC, source VPC endpoint, source IP, or excluded principal.

## Request Syntax
<a name="API_PutResourcePermissionStatement_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "consoleSourceVpce": "{{string}}",
   "excludedPrincipal": "{{string}}",
   "requestedRegion": "{{string}}",
   "signinSourceVpce": "{{string}}",
   "sourceIp": "{{string}}",
   "sourceVpc": "{{string}}",
   "vpcSourceIp": "{{string}}"
}
```

## Request Parameters
<a name="API_PutResourcePermissionStatement_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_PutResourcePermissionStatement_RequestSyntax) **   <a name="signin-PutResourcePermissionStatement-request-clientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. If not provided, the AWS SDK will automatically generate one for you.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[!-~]+`
Required: No

 ** [consoleSourceVpce](#API_PutResourcePermissionStatement_RequestSyntax) **   <a name="signin-PutResourcePermissionStatement-request-consoleSourceVpce"></a>
The AWS Management Console VPC endpoint identifier from which access is allowed. See `aws:SourceVpce` for more details.
Type: String
Pattern: `vpce-[a-z0-9]{8,20}`
Required: No

 ** [excludedPrincipal](#API_PutResourcePermissionStatement_RequestSyntax) **   <a name="signin-PutResourcePermissionStatement-request-excludedPrincipal"></a>
The principal ARN that is excluded from policy evaluation. When a principal matching this ARN attempts to access an AWS resource, the resource-based policy is not evaluated.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:((iam::[0-9]{12}:role/[a-zA-Z0-9_+=,.@-]{1,64})|(iam::[0-9]{12}:user/[a-zA-Z0-9_+=,.@-]{1,64})|(sts::[0-9]{12}:federated-user/[a-zA-Z0-9_+=,.@-]{2,193})|(iam::[0-9]{12}:root))`
Required: No

 ** [requestedRegion](#API_PutResourcePermissionStatement_RequestSyntax) **   <a name="signin-PutResourcePermissionStatement-request-requestedRegion"></a>
The AWS Region where the VPC resides. Required when `sourceVpc` is provided.
Type: String
Pattern: `[a-z]{2}(-[a-z]+)+-\d+`
Required: No

 ** [signinSourceVpce](#API_PutResourcePermissionStatement_RequestSyntax) **   <a name="signin-PutResourcePermissionStatement-request-signinSourceVpce"></a>
The AWS Sign-In VPC endpoint identifier from which access is allowed. See `aws:SourceVpce` for more details.
Type: String
Pattern: `vpce-[a-z0-9]{8,20}`
Required: No

 ** [sourceIp](#API_PutResourcePermissionStatement_RequestSyntax) **   <a name="signin-PutResourcePermissionStatement-request-sourceIp"></a>
The IP address outside a VPC from which access is allowed. See `aws:SourceIp` for more details.
Type: String
Required: No

 ** [sourceVpc](#API_PutResourcePermissionStatement_RequestSyntax) **   <a name="signin-PutResourcePermissionStatement-request-sourceVpc"></a>
The VPC identifier from which access is allowed. See `aws:SourceVpc` for more details.
Type: String
Pattern: `vpc-([0-9a-f]{8}|[0-9a-f]{17})`
Required: No

 ** [vpcSourceIp](#API_PutResourcePermissionStatement_RequestSyntax) **   <a name="signin-PutResourcePermissionStatement-request-vpcSourceIp"></a>
The IP address in a VPC from which access is allowed. See `aws:VpcSourceIp` for more details.
Type: String
Required: No

## Response Syntax
<a name="API_PutResourcePermissionStatement_ResponseSyntax"></a>

```
{
   "statementId": "string"
}
```

## Response Elements
<a name="API_PutResourcePermissionStatement_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [statementId](#API_PutResourcePermissionStatement_ResponseSyntax) **   <a name="signin-PutResourcePermissionStatement-response-statementId"></a>
The unique identifier of the created permission statement.
Type: String
Pattern: `[A-Za-z0-9+/]{64}=?`

## Errors
<a name="API_PutResourcePermissionStatement_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConflictException **
The request conflicts with the current state of the resource. For example, this exception is thrown when a client provides the same `ClientToken` for requests with differing parameter values, or the same parameter values with different `ClientToken` within the expiration window.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure with an internal server.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The request would cause a service quota to be exceeded.
HTTP Status Code: 400

 ** TooManyRequestsError **
The request was denied due to rate limiting.
HTTP Status Code: 400

 ** ValidationException **
The request failed because it contains a syntax error.
HTTP Status Code: 400

## See Also
<a name="API_PutResourcePermissionStatement_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/signincontrolplane-2022-07-26/PutResourcePermissionStatement)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/signincontrolplane-2022-07-26/PutResourcePermissionStatement)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/signincontrolplane-2022-07-26/PutResourcePermissionStatement)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/signincontrolplane-2022-07-26/PutResourcePermissionStatement)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/signincontrolplane-2022-07-26/PutResourcePermissionStatement)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/signincontrolplane-2022-07-26/PutResourcePermissionStatement)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/signincontrolplane-2022-07-26/PutResourcePermissionStatement)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/signincontrolplane-2022-07-26/PutResourcePermissionStatement)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/signincontrolplane-2022-07-26/PutResourcePermissionStatement)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/signincontrolplane-2022-07-26/PutResourcePermissionStatement)
