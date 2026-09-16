---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_ListApplicationShaderCaches.html
---

# ListApplicationShaderCaches
<a name="API_ListApplicationShaderCaches"></a>

Lists the shader caches associated with an Amazon GameLift Streams application. Each shader cache entry includes its status, associated stream groups, and size in bytes.

Returns shader caches associated with the specified Amazon GameLift Streams application in all statuses.

## Request Syntax
<a name="API_ListApplicationShaderCaches_RequestSyntax"></a>

```
GET /applications/{{Identifier}}/shadercaches HTTP/1.1
```

## URI Request Parameters
<a name="API_ListApplicationShaderCaches_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_ListApplicationShaderCaches_RequestSyntax) **   <a name="gameliftstreams-ListApplicationShaderCaches-request-uri-Identifier"></a>
An [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the application resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6`. Example ID: `a-9ZY8X7Wv6`.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: Yes

## Request Body
<a name="API_ListApplicationShaderCaches_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListApplicationShaderCaches_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Items": [
      {
         "ApplicationArn": "string",
         "AssociatedStreamGroups": [ "string" ],
         "Identifier": "string",
         "LastUpdatedAt": number,
         "Status": "string",
         "StorageBytes": number
      }
   ]
}
```

## Response Elements
<a name="API_ListApplicationShaderCaches_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Items](#API_ListApplicationShaderCaches_ResponseSyntax) **   <a name="gameliftstreams-ListApplicationShaderCaches-response-Items"></a>
A collection of shader cache metadata for the specified Amazon GameLift Streams application. Each item includes the shader cache status, associated stream groups, and storage size.
Type: Array of [ShaderCacheSummary](API_ShaderCacheSummary.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1000 items.

## Errors
<a name="API_ListApplicationShaderCaches_Errors"></a>

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
<a name="API_ListApplicationShaderCaches_Examples"></a>

### CLI Example
<a name="API_ListApplicationShaderCaches_Example_1"></a>

The following example shows how to use the AWS CLI to list shader caches for a Amazon GameLift Streams application.

#### Sample Request
<a name="API_ListApplicationShaderCaches_Example_1_Request"></a>

```
aws gameliftstreams list-application-shader-caches \
  --identifier arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6
```

## See Also
<a name="API_ListApplicationShaderCaches_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gameliftstreams-2018-05-10/ListApplicationShaderCaches)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gameliftstreams-2018-05-10/ListApplicationShaderCaches)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/ListApplicationShaderCaches)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gameliftstreams-2018-05-10/ListApplicationShaderCaches)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/ListApplicationShaderCaches)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gameliftstreams-2018-05-10/ListApplicationShaderCaches)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gameliftstreams-2018-05-10/ListApplicationShaderCaches)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gameliftstreams-2018-05-10/ListApplicationShaderCaches)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/gameliftstreams-2018-05-10/ListApplicationShaderCaches)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/ListApplicationShaderCaches)
