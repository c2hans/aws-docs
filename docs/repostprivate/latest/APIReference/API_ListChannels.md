---
source_url: https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_ListChannels.html
---

# ListChannels
<a name="API_ListChannels"></a>

**Note**
End of support notice: On June 30, 2027, AWS will end support for AWS re:Post Private. After June 30, 2027, you will no longer be able to access the re:Post Private console or re:Post Private resources. For more information, see [AWS re:Post Private end of support](https://docs.aws.amazon.com/repostprivate/latest/userguide/repost-private-end-of-support.html).

Returns the list of channel within a private re:Post with some information about each channel.

## Request Syntax
<a name="API_ListChannels_RequestSyntax"></a>

```
GET /spaces/{{spaceId}}/channels?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListChannels_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListChannels_RequestSyntax) **   <a name="repostprivate-ListChannels-request-uri-maxResults"></a>
The maximum number of channels to include in the results.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListChannels_RequestSyntax) **   <a name="repostprivate-ListChannels-request-uri-nextToken"></a>
The token for the next set of channel to return. You receive this token from a previous ListChannels operation.

 ** [spaceId](#API_ListChannels_RequestSyntax) **   <a name="repostprivate-ListChannels-request-uri-spaceId"></a>
The unique ID of the private re:Post.
Required: Yes

## Request Body
<a name="API_ListChannels_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListChannels_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "channels": [
      {
         "channelDescription": "string",
         "channelId": "string",
         "channelName": "string",
         "channelStatus": "string",
         "createDateTime": "string",
         "deleteDateTime": "string",
         "groupCount": number,
         "spaceId": "string",
         "userCount": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListChannels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [channels](#API_ListChannels_ResponseSyntax) **   <a name="repostprivate-ListChannels-response-channels"></a>
An array of structures that contain some information about the channels in the private re:Post.
Type: Array of [ChannelData](API_ChannelData.md) objects

 ** [nextToken](#API_ListChannels_ResponseSyntax) **   <a name="repostprivate-ListChannels-response-nextToken"></a>
The token that you use when you request the next set of channels.
Type: String

## Errors
<a name="API_ListChannels_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of request.
 ** retryAfterSeconds **
Advice to clients on when the call can be safely retried.
HTTP Status Code: 500

 ** ThrottlingException **
Request was denied due to request throttling.
 ** quotaCode **
The code to identify the quota.
 ** retryAfterSeconds **
 Advice to clients on when the call can be safely retried.
 ** serviceCode **
The code to identify the service.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The field that caused the error, if applicable.
 ** reason **
The reason why the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_ListChannels_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/repostspace-2022-05-13/ListChannels)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/repostspace-2022-05-13/ListChannels)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/repostspace-2022-05-13/ListChannels)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/repostspace-2022-05-13/ListChannels)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/repostspace-2022-05-13/ListChannels)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/repostspace-2022-05-13/ListChannels)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/repostspace-2022-05-13/ListChannels)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/repostspace-2022-05-13/ListChannels)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/repostspace-2022-05-13/ListChannels)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/repostspace-2022-05-13/ListChannels)
