---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/apireference/API_RemoveStreamGroupLocations.html
---

# RemoveStreamGroupLocations
<a name="API_RemoveStreamGroupLocations"></a>

 Removes a set of remote locations from this stream group. To remove a location, the stream group must be in `ACTIVE` status. When you remove a location, Amazon GameLift Streams releases allocated compute resources in that location. Stream sessions can no longer start from removed locations in a stream group. Amazon GameLift Streams also deletes the content files of all associated applications that were in Amazon GameLift Streams's internal Amazon S3 bucket at this location.

 You cannot remove the AWS Region location where you initially created this stream group, known as the primary location. However, you can set the stream capacity to zero to avoid incurring costs for allocated compute resources in that location.

## Request Syntax
<a name="API_RemoveStreamGroupLocations_RequestSyntax"></a>

```
DELETE /streamgroups/{{Identifier}}/locations?locations={{Locations}} HTTP/1.1
```

## URI Request Parameters
<a name="API_RemoveStreamGroupLocations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Identifier](#API_RemoveStreamGroupLocations_RequestSyntax) **   <a name="gameliftstreams-RemoveStreamGroupLocations-request-uri-Identifier"></a>
 A stream group to remove the specified locations from.
 This value is an [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) or ID that uniquely identifies the stream group resource. Example ARN: `arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4`. Example ID: `sg-1AB2C3De4`.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[a-zA-Z0-9-]+$)|(^arn:aws:gameliftstreams:([^: ]*):([0-9]{12}):([^: ]*)$)`
Required: Yes

 ** [Locations](#API_RemoveStreamGroupLocations_RequestSyntax) **   <a name="gameliftstreams-RemoveStreamGroupLocations-request-uri-Locations"></a>
 A set of locations to remove this stream group. For example, `us-east-1`.
 For a complete list of locations that Amazon GameLift Streams supports, refer to [Regions, quotas, and limitations](https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/regions-quotas.html) in the *Amazon GameLift Streams Developer Guide*.
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Required: Yes

## Request Body
<a name="API_RemoveStreamGroupLocations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_RemoveStreamGroupLocations_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_RemoveStreamGroupLocations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_RemoveStreamGroupLocations_Errors"></a>

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
<a name="API_RemoveStreamGroupLocations_Examples"></a>

### CLI Example
<a name="API_RemoveStreamGroupLocations_Example_1"></a>

The following example shows how to remove multiple locations from the stream group.

#### Sample Request
<a name="API_RemoveStreamGroupLocations_Example_1_Request"></a>

```
aws gameliftstreams remove-stream-group-locations \
    --identifier arn:aws:gameliftstreams:us-west-2:111122223333:streamgroup/sg-1AB2C3De4 \
    --locations us-east-1 ap-northeast-1
```

## See Also
<a name="API_RemoveStreamGroupLocations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/gameliftstreams-2018-05-10/RemoveStreamGroupLocations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/gameliftstreams-2018-05-10/RemoveStreamGroupLocations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gameliftstreams-2018-05-10/RemoveStreamGroupLocations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/gameliftstreams-2018-05-10/RemoveStreamGroupLocations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gameliftstreams-2018-05-10/RemoveStreamGroupLocations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/gameliftstreams-2018-05-10/RemoveStreamGroupLocations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/gameliftstreams-2018-05-10/RemoveStreamGroupLocations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/gameliftstreams-2018-05-10/RemoveStreamGroupLocations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/gameliftstreams-2018-05-10/RemoveStreamGroupLocations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gameliftstreams-2018-05-10/RemoveStreamGroupLocations)
