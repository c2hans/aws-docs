---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_AddPermission.html
---

# AddPermission
<a name="API_AddPermission"></a>

Grants a [principal](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_policies_elements_principal.html#Principal_specifying) permission to use a function. You can apply the policy at the function level, or specify a qualifier to restrict access to a single version or alias. If you use a qualifier, the invoker must use the full Amazon Resource Name (ARN) of that version or alias to invoke the function. Note: Lambda does not support adding policies to version $LATEST.

To grant permission to another account, specify the account ID as the `Principal`. To grant permission to an organization defined in AWS Organizations, specify the organization ID as the `PrincipalOrgID`. For AWS services, the principal is a domain-style identifier that the service defines, such as `s3.amazonaws.com` or `sns.amazonaws.com`. For AWS services, you can also specify the ARN of the associated resource as the `SourceArn`. If you grant permission to a service principal without specifying the source, other accounts could potentially configure resources in their account to invoke your Lambda function.

This operation adds a statement to a resource-based permissions policy for the function. For more information about function policies, see [Using resource-based policies for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/access-control-resource-based.html).

## Request Syntax
<a name="API_AddPermission_RequestSyntax"></a>

```
POST /2015-03-31/functions/{{FunctionName}}/policy?Qualifier={{Qualifier}} HTTP/1.1
Content-type: application/json

{
   "Action": "{{string}}",
   "EventSourceToken": "{{string}}",
   "FunctionUrlAuthType": "{{string}}",
   "InvokedViaFunctionUrl": {{boolean}},
   "Principal": "{{string}}",
   "PrincipalOrgID": "{{string}}",
   "RevisionId": "{{string}}",
   "SourceAccount": "{{string}}",
   "SourceArn": "{{string}}",
   "StatementId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AddPermission_RequestParameters"></a>

The request uses the following URI parameters.

 ** [FunctionName](#API_AddPermission_RequestSyntax) **   <a name="lambda-AddPermission-request-uri-FunctionName"></a>
The name or ARN of the Lambda function, version, or alias.

**Name formats**
+  **Function name** – `my-function` (name-only), `my-function:v1` (with alias).
+  **Function ARN** – `arn:aws:lambda:us-west-2:123456789012:function:my-function`.
+  **Partial ARN** – `123456789012:function:my-function`.
You can append a version number or alias to any of the formats. The length constraint applies only to the full ARN. If you specify only the function name, it is limited to 64 characters in length.
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:(aws[a-zA-Z-]*)?:lambda:)?([a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:)?(\d{12}:)?(function:)?([a-zA-Z0-9-_\.]+)(:(\$LATEST(\.PUBLISHED)?|[a-zA-Z0-9-_]+))?`
Required: Yes

 ** [Qualifier](#API_AddPermission_RequestSyntax) **   <a name="lambda-AddPermission-request-uri-Qualifier"></a>
Specify a version or alias to add permissions to a published version of the function.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `\$(LATEST(\.PUBLISHED)?)|[a-zA-Z0-9-_$]+`

## Request Body
<a name="API_AddPermission_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Action](#API_AddPermission_RequestSyntax) **   <a name="lambda-AddPermission-request-Action"></a>
The action that the principal can use on the function. For example, `lambda:InvokeFunction` or `lambda:GetFunction`.
Type: String
Pattern: `(lambda:[*]|lambda:[a-zA-Z]+|[*])`
Required: Yes

 ** [EventSourceToken](#API_AddPermission_RequestSyntax) **   <a name="lambda-AddPermission-request-EventSourceToken"></a>
For Alexa Smart Home functions, a token that the invoker must supply.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[a-zA-Z0-9._\-]+`
Required: No

 ** [FunctionUrlAuthType](#API_AddPermission_RequestSyntax) **   <a name="lambda-AddPermission-request-FunctionUrlAuthType"></a>
The type of authentication that your function URL uses. Set to `AWS_IAM` if you want to restrict access to authenticated users only. Set to `NONE` if you want to bypass IAM authentication to create a public endpoint. For more information, see [Control access to Lambda function URLs](https://docs.aws.amazon.com/lambda/latest/dg/urls-auth.html).
Type: String
Valid Values: `NONE | AWS_IAM`
Required: No

 ** [InvokedViaFunctionUrl](#API_AddPermission_RequestSyntax) **   <a name="lambda-AddPermission-request-InvokedViaFunctionUrl"></a>
Indicates whether the permission applies when the function is invoked through a function URL.
Type: Boolean
Required: No

 ** [Principal](#API_AddPermission_RequestSyntax) **   <a name="lambda-AddPermission-request-Principal"></a>
The AWS service, AWS account, IAM user, or IAM role that invokes the function. If you specify a service, use `SourceArn` or `SourceAccount` to limit who can invoke the function through that service.
Type: String
Pattern: `[^\s]+`
Required: Yes

 ** [PrincipalOrgID](#API_AddPermission_RequestSyntax) **   <a name="lambda-AddPermission-request-PrincipalOrgID"></a>
The identifier for your organization in AWS Organizations. Use this to grant permissions to all the AWS accounts under this organization.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 34.
Pattern: `o-[a-z0-9]{10,32}`
Required: No

 ** [RevisionId](#API_AddPermission_RequestSyntax) **   <a name="lambda-AddPermission-request-RevisionId"></a>
Update the policy only if the revision ID matches the ID that's specified. Use this option to avoid modifying a policy that has changed since you last read it.
Type: String
Required: No

 ** [SourceAccount](#API_AddPermission_RequestSyntax) **   <a name="lambda-AddPermission-request-SourceAccount"></a>
For AWS service, the ID of the AWS account that owns the resource. Use this together with `SourceArn` to ensure that the specified account owns the resource. It is possible for an Amazon S3 bucket to be deleted by its owner and recreated by another account.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 12.
Pattern: `\d{12}`
Required: No

 ** [SourceArn](#API_AddPermission_RequestSyntax) **   <a name="lambda-AddPermission-request-SourceArn"></a>
For AWS services, the ARN of the AWS resource that invokes the function. For example, an Amazon S3 bucket or Amazon SNS topic.
Note that Lambda configures the comparison using the `StringLike` operator.
Type: String
Pattern: `arn:(aws[a-zA-Z0-9-]*):([a-zA-Z0-9\-])+:([a-z]{2}(-gov)?-[a-z]+-\d{1})?:(\d{12})?:(.*)`
Required: No

 ** [StatementId](#API_AddPermission_RequestSyntax) **   <a name="lambda-AddPermission-request-StatementId"></a>
A statement identifier that differentiates the statement from others in the same policy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `([a-zA-Z0-9-_]+)`
Required: Yes

## Response Syntax
<a name="API_AddPermission_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "Statement": "string"
}
```

## Response Elements
<a name="API_AddPermission_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Statement](#API_AddPermission_ResponseSyntax) **   <a name="lambda-AddPermission-response-Statement"></a>
The permission statement that's added to the function policy.
Type: String

## Errors
<a name="API_AddPermission_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
One of the parameters in the request is not valid.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 400

 ** PolicyLengthExceededException **
The permissions policy for the resource is too large. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html).
HTTP Status Code: 400

 ** PreconditionFailedException **
The RevisionId provided does not match the latest RevisionId for the Lambda function or alias.
+  **For AddPermission and RemovePermission API operations:** Call `GetPolicy` to retrieve the latest RevisionId for your resource.
+  **For all other API operations:** Call `GetFunction` or `GetAlias` to retrieve the latest RevisionId for your resource.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 412

 ** PublicPolicyException **
The resource-based policy you tried to add to the Lambda resource would grant public access to it, which isn't allowed.
 ** Message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 400

 ** ResourceConflictException **
The resource already exists, or another operation is in progress.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The resource specified in the request does not exist.
HTTP Status Code: 404

 ** ServiceException **
The AWS Lambda service encountered an internal error.
HTTP Status Code: 500

 ** TooManyRequestsException **
The request throughput limit was exceeded. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests).
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
HTTP Status Code: 429

## See Also
<a name="API_AddPermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/AddPermission)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/AddPermission)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/AddPermission)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/AddPermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/AddPermission)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/AddPermission)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/AddPermission)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/AddPermission)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/AddPermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/AddPermission)
