---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_UpdateRoom.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# UpdateRoom
<a name="API_UpdateRoom"></a>

Updates room details, such as the room name, for a room in an Amazon Chime Enterprise account.

## Request Syntax
<a name="API_UpdateRoom_RequestSyntax"></a>

```
POST /accounts/{{accountId}}/rooms/{{roomId}} HTTP/1.1
Content-type: application/json

{
   "Name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateRoom_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accountId](#API_UpdateRoom_RequestSyntax) **   <a name="chime-UpdateRoom-request-uri-AccountId"></a>
The Amazon Chime account ID.
Pattern: `.*\S.*`
Required: Yes

 ** [roomId](#API_UpdateRoom_RequestSyntax) **   <a name="chime-UpdateRoom-request-uri-RoomId"></a>
The room ID.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_UpdateRoom_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Name](#API_UpdateRoom_RequestSyntax) **   <a name="chime-UpdateRoom-request-Name"></a>
The room name.
Type: String
Required: No

## Response Syntax
<a name="API_UpdateRoom_ResponseSyntax"></a>

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
<a name="API_UpdateRoom_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Room](#API_UpdateRoom_ResponseSyntax) **   <a name="chime-UpdateRoom-response-Room"></a>
The room details.
Type: [Room](API_Room.md) object

## Errors
<a name="API_UpdateRoom_Errors"></a>

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
<a name="API_UpdateRoom_Examples"></a>

In the following example or examples, the Authorization header contents( `AUTHPARAMS` ) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_UpdateRoom_Example_1"></a>

 This example updates the specified chat room name to `teamRoom` .

#### Sample Request
<a name="API_UpdateRoom_Example_1_Request"></a>

```
POST /accounts/12a3456b-7c89-012d-3456-78901e23fg45/rooms/abcd1e2d-3e45-6789-01f2-3g45h67i890j HTTP/1.1 Host: service.chime.aws.amazon.com Accept-Encoding: identity User-Agent: aws-cli/1.16.293 Python/3.8.0 Windows/10 botocore/1.13.29 X-Amz-Date: 20191202T223318Z Authorization: AUTHPARAMS Content-Length: 21
```

#### Sample Response
<a name="API_UpdateRoom_Example_1_Response"></a>

```
HTTP/1.1 200 OK x-amzn-RequestId: e48fe3de-9a18-4ea2-b656-a00690a91f46 Content-Type: application/json Content-Length: 274 Date: Mon, 02 Dec 2019 22:33:19 GMT Connection: keep-alive {"Room":{"AccountId":"12a3456b-7c89-012d-3456-78901e23fg45","CreatedBy":"arn:aws:iam::111122223333:user/alejandro","CreatedTimestamp":"2019-12-02T22:29:31.549Z","Name":"teamRoom","RoomId":"abcd1e2d-3e45-6789-01f2-3g45h67i890j","UpdatedTimestamp":"2019-12-02T22:33:19.310Z"}}
```

## See Also
<a name="API_UpdateRoom_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-2018-05-01/UpdateRoom)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-2018-05-01/UpdateRoom)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/UpdateRoom)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-2018-05-01/UpdateRoom)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/UpdateRoom)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-2018-05-01/UpdateRoom)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-2018-05-01/UpdateRoom)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-2018-05-01/UpdateRoom)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-2018-05-01/UpdateRoom)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/UpdateRoom)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
