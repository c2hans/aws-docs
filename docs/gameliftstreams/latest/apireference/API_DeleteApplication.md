---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_DeleteApplication.html
---

# DeleteApplication
<a name="API_DeleteApplication"></a>

Permanently deletes an Amazon GameLift Streams application resource. This also deletes the application content files stored with Amazon GameLift Streams. However, this does not delete the original files that you uploaded to your Amazon S3 bucket; you can delete these any time after Amazon GameLift Streams creates an application, which is the only time Amazon GameLift Streams accesses your Amazon S3 bucket.

 You can only delete an application that meets the following conditions:
+ The application is in `READY` or `ERROR` status. You cannot delete an application that's in `PROCESSING` or `INITIALIZED` status.
+ The application is not the default application of any stream groups. You must first delete the stream group by using [DeleteStreamGroup](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_DeleteStreamGroup.html).
+ The application is not linked to any stream groups. You must first unlink the stream group by using [DisassociateApplications](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_DisassociateApplications.html).
+  An application is not streaming in any ongoing stream session. You must wait until the client ends the stream session or call [TerminateStreamSession](https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_TerminateStreamSession.html) to end the stream.

If any active stream groups exist for this application, this request returns a `ValidationException`.

## Request Syntax
<a name="API_DeleteApplication_RequestSyntax"></a>

```
DELETE /applications/{{Identifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteApplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_DeleteApplication_RequestSyntax) **   <a name="gameliftstreams-DeleteApplication-request-uri-Identifier"></a>
An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the application resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6`. Example ID: `a-9ZY8X7Wv6`.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: Yes

## Request Body
<a name="API_DeleteApplication_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteApplication_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 [AccessDeniedException](API_AccessDeniedException.md)
You don't have the required permissions to access this Amazon GameLift Streams resource. Correct the permissions before you try again.
 ** Message **
Description of the error.
HTTP Status Code: 403

 [ConflictException](API_ConflictException.md)
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request.
 ** Message **
Description of the error.
HTTP Status Code: 409

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
<a name="API_DeleteApplication_Examples"></a>

### CLI Example
<a name="API_DeleteApplication_Example_1"></a>

The following example shows how to use the AWS CLI to delete a Amazon GameLift Streams application.

#### Sample Request
<a name="API_DeleteApplication_Example_1_Request"></a>

```
aws gameliftstreams delete-application \
  --identifier arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6
```

## See Also
<a name="API_DeleteApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gameliftstreams-2018-05-10/DeleteApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gameliftstreams-2018-05-10/DeleteApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/DeleteApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gameliftstreams-2018-05-10/DeleteApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/DeleteApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gameliftstreams-2018-05-10/DeleteApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gameliftstreams-2018-05-10/DeleteApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gameliftstreams-2018-05-10/DeleteApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gameliftstreams-2018-05-10/DeleteApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/DeleteApplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftstreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
