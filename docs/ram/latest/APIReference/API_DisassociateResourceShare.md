---
source_url: https://docs.aws.amazon.com/ram/latest/APIReference/API_DisassociateResourceShare.html
---

# DisassociateResourceShare
<a name="API_DisassociateResourceShare"></a>

Removes the specified principals, resources, or source constraints from participating in the specified resource share.

## Request Syntax
<a name="API_DisassociateResourceShare_RequestSyntax"></a>

```
POST /disassociateresourceshare HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "principals": [ "{{string}}" ],
   "resourceArns": [ "{{string}}" ],
   "resourceShareArn": "{{string}}",
   "sources": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_DisassociateResourceShare_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DisassociateResourceShare_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [resourceShareArn](#API_DisassociateResourceShare_RequestSyntax) **   <a name="ram-DisassociateResourceShare-request-resourceShareArn"></a>
Specifies [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the resource share that you want to remove resources or principals from.
Type: String
Required: Yes

 ** [clientToken](#API_DisassociateResourceShare_RequestSyntax) **   <a name="ram-DisassociateResourceShare-request-clientToken"></a>
Specifies a unique, case-sensitive identifier that you provide to ensure the idempotency of the request. This lets you safely retry the request without accidentally performing the same operation a second time. Passing the same value to a later call to an operation requires that you also pass the same value for all other parameters. We recommend that you use a [UUID type of value.](https://wikipedia.org/wiki/Universally_unique_identifier).
If you don't provide this value, then AWS generates a random one for you.
If you retry the operation with the same `ClientToken`, but with different parameters, the retry fails with an `IdempotentParameterMismatch` error.
Type: String
Required: No

 ** [principals](#API_DisassociateResourceShare_RequestSyntax) **   <a name="ram-DisassociateResourceShare-request-principals"></a>
Specifies a list of one or more principals that no longer are to have access to the resources in this resource share.
You can include the following values:
+ An AWS account ID, for example: `123456789012`
+ An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of an organization in AWS Organizations, for example: `arn:aws:organizations::123456789012:organization/o-exampleorgid`
+ An ARN of an organizational unit (OU) in AWS Organizations, for example: `arn:aws:organizations::123456789012:ou/o-exampleorgid/ou-examplerootid-exampleouid123`
+ An ARN of an IAM role, for example: `arn:aws:iam::123456789012:role/rolename`
+ An ARN of an IAM user, for example: `arn:aws:iam::123456789012user/username`
+ A service principal name, for example: `service-id.amazonaws.com`
Not all resource types can be shared with IAM roles and users. For more information, see [Sharing with IAM roles and users](https://docs.aws.amazon.com/ram/latest/userguide/permissions.html#permissions-rbp-supported-resource-types) in the * AWS Resource Access Manager User Guide*.
Type: Array of strings
Required: No

 ** [resourceArns](#API_DisassociateResourceShare_RequestSyntax) **   <a name="ram-DisassociateResourceShare-request-resourceArns"></a>
Specifies a list of [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) for one or more resources that you want to remove from the resource share. After the operation runs, these resources are no longer shared with principals associated with the resource share.
Type: Array of strings
Required: No

 ** [sources](#API_DisassociateResourceShare_RequestSyntax) **   <a name="ram-DisassociateResourceShare-request-sources"></a>
Specifies source constraints (accounts, ARNs, organization IDs, or organization paths) to remove from the resource share. This enables granular management of source constraints while maintaining service principal associations. At least one source must remain when service principals are present.
Type: Array of strings
Required: No

## Response Syntax
<a name="API_DisassociateResourceShare_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "clientToken": "string",
   "resourceShareAssociations": [
      {
         "associatedEntity": "string",
         "associationType": "string",
         "creationTime": number,
         "external": boolean,
         "lastUpdatedTime": number,
         "resourceShareArn": "string",
         "resourceShareName": "string",
         "status": "string",
         "statusMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DisassociateResourceShare_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [clientToken](#API_DisassociateResourceShare_ResponseSyntax) **   <a name="ram-DisassociateResourceShare-response-clientToken"></a>
The idempotency identifier associated with this request. If you want to repeat the same operation in an idempotent manner then you must include this value in the `clientToken` request parameter of that later call. All other parameters must also have the same values that you used in the first call.
Type: String

 ** [resourceShareAssociations](#API_DisassociateResourceShare_ResponseSyntax) **   <a name="ram-DisassociateResourceShare-response-resourceShareAssociations"></a>
An array of objects with information about the updated associations for this resource share.
Type: Array of [ResourceShareAssociation](API_ResourceShareAssociation.md) objects

## Errors
<a name="API_DisassociateResourceShare_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** IdempotentParameterMismatchException **
The operation failed because the client token input parameter matched one that was used with a previous call to the operation, but at least one of the other input parameters is different from the previous call.
HTTP Status Code: 400

 ** InvalidClientTokenException **
The operation failed because the specified client token isn't valid.
HTTP Status Code: 400

 ** InvalidParameterException **
The operation failed because a parameter you specified isn't valid.
HTTP Status Code: 400

 ** InvalidStateTransitionException **
The operation failed because the requested operation isn't valid for the resource share in its current state.
HTTP Status Code: 400

 ** MalformedArnException **
The operation failed because the specified [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) has a format that isn't valid.
HTTP Status Code: 400

 ** OperationNotPermittedException **
The operation failed because the requested operation isn't permitted.
HTTP Status Code: 400

 ** ResourceShareLimitExceededException **
The operation failed because it would exceed the limit for resource shares for your account. You can associate up to 100 resources per call. To view the limits for your AWS account, see the [AWS RAM page in the Service Quotas console](https://console.aws.amazon.com/servicequotas/home/services/ram/quotas).
HTTP Status Code: 400

 ** ServerInternalException **
The operation failed because the service could not respond to the request due to an internal problem. Try again later.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The operation failed because the service isn't available. Try again later.
HTTP Status Code: 503

 ** ThrottlingException **
The operation failed because it exceeded the rate at which you are allowed to perform this operation. Please try again later.
HTTP Status Code: 429

 ** UnknownResourceException **
The operation failed because a specified resource couldn't be found.
HTTP Status Code: 400

## See Also
<a name="API_DisassociateResourceShare_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ram-2018-01-04/DisassociateResourceShare)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ram-2018-01-04/DisassociateResourceShare)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ram-2018-01-04/DisassociateResourceShare)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ram-2018-01-04/DisassociateResourceShare)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ram-2018-01-04/DisassociateResourceShare)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ram-2018-01-04/DisassociateResourceShare)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ram-2018-01-04/DisassociateResourceShare)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ram-2018-01-04/DisassociateResourceShare)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ram-2018-01-04/DisassociateResourceShare)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ram-2018-01-04/DisassociateResourceShare)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS RAM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ram` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
