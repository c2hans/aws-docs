---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_AddLayerVersionPermission.html
---

# AddLayerVersionPermission
<a name="API_AddLayerVersionPermission"></a>

Adds permissions to the resource-based policy of a version of an [AWS Lambda layer](https://docs.aws.amazon.com/lambda/latest/dg/configuration-layers.html). Use this action to grant layer usage permission to other accounts. You can grant permission to a single account, all accounts in an organization, or all AWS accounts.

To revoke permission, call [RemoveLayerVersionPermission](API_RemoveLayerVersionPermission.md) with the statement ID that you specified when you added it.

## Request Syntax
<a name="API_AddLayerVersionPermission_RequestSyntax"></a>

```
POST /2018-10-31/layers/{{LayerName}}/versions/{{VersionNumber}}/policy?RevisionId={{RevisionId}} HTTP/1.1
Content-type: application/json

{
   "Action": "{{string}}",
   "OrganizationId": "{{string}}",
   "Principal": "{{string}}",
   "StatementId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AddLayerVersionPermission_RequestParameters"></a>

The request uses the following URI parameters.

 ** [LayerName](#API_AddLayerVersionPermission_RequestSyntax) **   <a name="lambda-AddLayerVersionPermission-request-uri-LayerName"></a>
The name or Amazon Resource Name (ARN) of the layer.
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `(arn:[a-zA-Z0-9-]+:lambda:[a-zA-Z0-9-]+:\d{12}:layer:[a-zA-Z0-9-_]+)|[a-zA-Z0-9-_]+`
Required: Yes

 ** [RevisionId](#API_AddLayerVersionPermission_RequestSyntax) **   <a name="lambda-AddLayerVersionPermission-request-uri-RevisionId"></a>
Only update the policy if the revision ID matches the ID specified. Use this option to avoid modifying a policy that has changed since you last read it.

 ** [VersionNumber](#API_AddLayerVersionPermission_RequestSyntax) **   <a name="lambda-AddLayerVersionPermission-request-uri-VersionNumber"></a>
The version number.
Required: Yes

## Request Body
<a name="API_AddLayerVersionPermission_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Action](#API_AddLayerVersionPermission_RequestSyntax) **   <a name="lambda-AddLayerVersionPermission-request-Action"></a>
The API action that grants access to the layer. For example, `lambda:GetLayerVersion`.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 22.
Pattern: `lambda:GetLayerVersion`
Required: Yes

 ** [OrganizationId](#API_AddLayerVersionPermission_RequestSyntax) **   <a name="lambda-AddLayerVersionPermission-request-OrganizationId"></a>
With the principal set to `*`, grant permission to all accounts in the specified organization.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 34.
Pattern: `o-[a-z0-9]{10,32}`
Required: No

 ** [Principal](#API_AddLayerVersionPermission_RequestSyntax) **   <a name="lambda-AddLayerVersionPermission-request-Principal"></a>
An account ID, or `*` to grant layer usage permission to all accounts in an organization, or all AWS accounts (if `organizationId` is not specified). For the last case, make sure that you really do want all AWS accounts to have usage permission to this layer.
Type: String
Pattern: `\d{12}|\*|arn:(aws[a-zA-Z-]*):iam::\d{12}:root`
Required: Yes

 ** [StatementId](#API_AddLayerVersionPermission_RequestSyntax) **   <a name="lambda-AddLayerVersionPermission-request-StatementId"></a>
An identifier that distinguishes the policy from others on the same layer version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `([a-zA-Z0-9-_]+)`
Required: Yes

## Response Syntax
<a name="API_AddLayerVersionPermission_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "RevisionId": "string",
   "Statement": "string"
}
```

## Response Elements
<a name="API_AddLayerVersionPermission_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [RevisionId](#API_AddLayerVersionPermission_ResponseSyntax) **   <a name="lambda-AddLayerVersionPermission-response-RevisionId"></a>
A unique identifier for the current revision of the policy.
Type: String

 ** [Statement](#API_AddLayerVersionPermission_ResponseSyntax) **   <a name="lambda-AddLayerVersionPermission-response-Statement"></a>
The permission statement.
Type: String

## Errors
<a name="API_AddLayerVersionPermission_Errors"></a>

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
<a name="API_AddLayerVersionPermission_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/AddLayerVersionPermission)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/AddLayerVersionPermission)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/AddLayerVersionPermission)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/AddLayerVersionPermission)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/AddLayerVersionPermission)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/AddLayerVersionPermission)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/AddLayerVersionPermission)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/AddLayerVersionPermission)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/AddLayerVersionPermission)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/AddLayerVersionPermission)
