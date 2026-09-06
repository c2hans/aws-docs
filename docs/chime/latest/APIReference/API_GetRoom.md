---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_GetRoom.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# GetRoom
<a name="API_GetRoom"></a>

Retrieves room details, such as the room name, for a room in an Amazon Chime Enterprise account.

## Request Syntax
<a name="API_GetRoom_RequestSyntax"></a>

```
GET /accounts/{{accountId}}/rooms/{{roomId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetRoom_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accountId](#API_GetRoom_RequestSyntax) **   <a name="chime-GetRoom-request-uri-AccountId"></a>
The Amazon Chime account ID.
Pattern: `.*\S.*`
Required: Yes

 ** [roomId](#API_GetRoom_RequestSyntax) **   <a name="chime-GetRoom-request-uri-RoomId"></a>
The room ID.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_GetRoom_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetRoom_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Room": {
      "AccountId": "string",
      "CreatedBy": "string",
      "CreatedTimestamp": "string",
      "Name": "string",
      "RoomId": "string",
      "UpdatedTimestamp": "string"
   }
}
```

## Response Elements
<a name="API_GetRoom_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Room](#API_GetRoom_ResponseSyntax) **   <a name="chime-GetRoom-response-Room"></a>
The room details.
Type: [Room](API_Room.md) object

## Errors
<a name="API_GetRoom_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** NotFoundException **
One or more of the resources in the request does not exist in the system.
HTTP Status Code: 404

 ** ServiceFailureException **
The service encountered an unexpected error.
HTTP Status Code: 500

 ** ServiceUnavailableException **
The service is currently unavailable.
HTTP Status Code: 503

 ** ThrottledClientException **
The client exceeded its request rate limit.
HTTP Status Code: 429

 ** UnauthorizedClientException **
The client is not currently authorized to make the request.
HTTP Status Code: 401

## Examples
<a name="API_GetRoom_Examples"></a>

In the following example or examples, the Authorization header contents( `AUTHPARAMS` ) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_GetRoom_Example_1"></a>

This example gets the details about the specified chat room, including the name.

#### Sample Request
<a name="API_GetRoom_Example_1_Request"></a>

```
GET /accounts/12a3456b-7c89-012d-3456-78901e23fg45/rooms/abcd1e2d-3e45-6789-01f2-3g45h67i890j HTTP/1.1 Host: service.chime.aws.amazon.com Accept-Encoding: identity User-Agent: aws-cli/1.16.293 Python/3.8.0 Windows/10 botocore/1.13.29 X-Amz-Date: 20191202T223145Z Authorization: AUTHPARAMS
```

#### Sample Response
<a name="API_GetRoom_Example_1_Response"></a>

```
HTTP/1.1 200 OK x-amzn-RequestId: 6b2786c6-e616-4e0d-a991-f635fa827583 Content-Type: application/json Content-Length: 273 Date: Mon, 02 Dec 2019 22:31:45 GMT Connection: keep-alive {"Room":{"AccountId":"12a3456b-7c89-012d-3456-78901e23fg45","CreatedBy":"arn:aws:iam::111122223333:user/alejandro","CreatedTimestamp":"2019-12-02T22:29:31.549Z","Name":"chatRoom","RoomId":"abcd1e2d-3e45-6789-01f2-3g45h67i890j","UpdatedTimestamp":"2019-12-02T22:29:31.549Z"}}
```

## See Also
<a name="API_GetRoom_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-2018-05-01/GetRoom)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-2018-05-01/GetRoom)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/GetRoom)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-2018-05-01/GetRoom)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/GetRoom)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-2018-05-01/GetRoom)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-2018-05-01/GetRoom)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-2018-05-01/GetRoom)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-2018-05-01/GetRoom)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/GetRoom)
