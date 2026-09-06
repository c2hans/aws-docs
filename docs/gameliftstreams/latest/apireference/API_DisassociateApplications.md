---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_DisassociateApplications.html
---

# DisassociateApplications
<a name="API_DisassociateApplications"></a>

 When you disassociate, or unlink, an application from a stream group, you can no longer stream this application by using that stream group's allocated compute resources. Any streams in process will continue until they terminate, which helps avoid interrupting an end-user's stream. Amazon GameLift Streams will not initiate new streams in the stream group using the disassociated application. The disassociate action does not affect the stream capacity of a stream group. To disassociate an application, the stream group must be in `ACTIVE` status.

 If you disassociate the default application, Amazon GameLift Streams will automatically choose a new default application from the remaining associated applications. To change which application is the default application, call [UpdateStreamGroup](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_UpdateStreamGroup.html) and specify a new `DefaultApplicationIdentifier`.

## Request Syntax
<a name="API_DisassociateApplications_RequestSyntax"></a>

```
POST /streamgroups/{{Identifier}}/disassociations HTTP/1.1
Content-type: application/json

{
   "ApplicationIdentifiers": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_DisassociateApplications_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_DisassociateApplications_RequestSyntax) **   <a name="gameliftstreams-DisassociateApplications-request-uri-Identifier"></a>
A stream group to disassociate these applications from.
This value is an [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the stream group resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4`. Example ID: `sg-1AB2C3De4`.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: Yes

## Request Body
<a name="API_DisassociateApplications_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ApplicationIdentifiers](#API_DisassociateApplications_RequestSyntax) **   <a name="gameliftstreams-DisassociateApplications-request-ApplicationIdentifiers"></a>
A set of applications that you want to disassociate from the stream group.
This value is a set of either [Amazon Resource Names (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or IDs that uniquely identify application resources. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6`. Example ID: `a-9ZY8X7Wv6`.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: Yes

## Response Syntax
<a name="API_DisassociateApplications_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApplicationArns": [ "string" ],
   "Arn": "string"
}
```

## Response Elements
<a name="API_DisassociateApplications_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationArns](#API_DisassociateApplications_ResponseSyntax) **   <a name="gameliftstreams-DisassociateApplications-response-ApplicationArns"></a>
A set of applications that are disassociated from this stream group.
This value is a set of [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identify application resources. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6`.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)`

 ** [Arn](#API_DisassociateApplications_ResponseSyntax) **   <a name="gameliftstreams-DisassociateApplications-response-Arn"></a>
An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) that uniquely identifies the stream group resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)`

## Errors
<a name="API_DisassociateApplications_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.
 ** Message **
Description of the error.
HTTP Status Code: 403

 [InternalServerException](API_InternalServerException.md)
The service encountered an internal error and is unable to complete the request.
 ** Message **
Description of the error.
HTTP Status Code: 500

 [ResourceNotFoundException](API_ResourceNotFoundException.md)
The resource specified in the request was not found. Correct the request before you try again.
 ** Message **
Description of the error.
HTTP Status Code: 404

 [ThrottlingException](API_ThrottlingException.md)
The request was denied due to request throttling. Retry the request after the suggested wait time.
 ** Message **
Description of the error.
HTTP Status Code: 429

 [ValidationException](API_ValidationException.md)
One or more parameter values in the request fail to satisfy the specified constraints. Correct the invalid parameter values before retrying the request.
 ** Message **
Description of the error.
HTTP Status Code: 400

## Examples
<a name="API_DisassociateApplications_Examples"></a>

### CLI Example
<a name="API_DisassociateApplications_Example_1"></a>

The following example shows how to use the AWS CLI to disassociate, or unlink, multiple applications from a stream group.

#### Sample Request
<a name="API_DisassociateApplications_Example_1_Request"></a>

```
aws gameliftstreams disassociate-applications \
    --identifier arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4 \
    --application-identifiers a-9ZY8X7Wv6 a-1Z78C7Wv6
```

## See Also
<a name="API_DisassociateApplications_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gameliftstreams-2018-05-10/DisassociateApplications)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gameliftstreams-2018-05-10/DisassociateApplications)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/DisassociateApplications)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gameliftstreams-2018-05-10/DisassociateApplications)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/DisassociateApplications)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gameliftstreams-2018-05-10/DisassociateApplications)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gameliftstreams-2018-05-10/DisassociateApplications)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gameliftstreams-2018-05-10/DisassociateApplications)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gameliftstreams-2018-05-10/DisassociateApplications)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/DisassociateApplications)
