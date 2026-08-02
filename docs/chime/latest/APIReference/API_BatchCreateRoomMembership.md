---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_BatchCreateRoomMembership.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# BatchCreateRoomMembership
<a name="API_BatchCreateRoomMembership"></a>

Adds up to 50 members to a chat room in an Amazon Chime Enterprise account. Members can be users or bots. The member role designates whether the member is a chat room administrator or a general chat room member.

## Request Syntax
<a name="API_BatchCreateRoomMembership_RequestSyntax"></a>

```
POST /accounts/{{accountId}}/rooms/{{roomId}}/memberships?operation=batch-create HTTP/1.1
Content-type: application/json

{
   "MembershipItemList": [
      {
         "MemberId": "{{string}}",
         "Role": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_BatchCreateRoomMembership_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accountId](#API_BatchCreateRoomMembership_RequestSyntax) **   <a name="chime-BatchCreateRoomMembership-request-uri-AccountId"></a>
The Amazon Chime account ID.
Pattern: `.*\S.*`
Required: Yes

 ** [roomId](#API_BatchCreateRoomMembership_RequestSyntax) **   <a name="chime-BatchCreateRoomMembership-request-uri-RoomId"></a>
The room ID.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_BatchCreateRoomMembership_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MembershipItemList](#API_BatchCreateRoomMembership_RequestSyntax) **   <a name="chime-BatchCreateRoomMembership-request-MembershipItemList"></a>
The list of membership items.
Type: Array of [MembershipItem](API_MembershipItem.md) objects
Array Members: Maximum number of 50 items.
Required: Yes

## Response Syntax
<a name="API_BatchCreateRoomMembership_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "Errors": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "MemberId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchCreateRoomMembership_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Errors](#API_BatchCreateRoomMembership_ResponseSyntax) **   <a name="chime-BatchCreateRoomMembership-response-Errors"></a>
If the action fails for one or more of the member IDs in the request, a list of the member IDs is returned, along with error codes and error messages.
Type: Array of [MemberError](API_MemberError.md) objects

## Errors
<a name="API_BatchCreateRoomMembership_Errors"></a>

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
<a name="API_BatchCreateRoomMembership_Examples"></a>

In the following example or examples, the Authorization header contents( `AUTHPARAMS` ) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_BatchCreateRoomMembership_Example_1"></a>

This example adds multiple users to the chat room as chat room members. It also assigns administrator and member roles to the users.

#### Sample Request
<a name="API_BatchCreateRoomMembership_Example_1_Request"></a>

```
POST /accounts/12a3456b-7c89-012d-3456-78901e23fg45/rooms/abcd1e2d-3e45-6789-01f2-3g45h67i890j/memberships?operation=batch-create HTTP/1.1 Host: service.chime.aws.amazon.com Accept-Encoding: identity User-Agent: aws-cli/1.16.293 Python/3.8.0 Windows/10 botocore/1.13.29 X-Amz-Date: 20191202T224658Z Authorization: AUTHPARAMS Content-Length: 175 {"MembershipItemList": [{"MemberId": "1ab2345c-67de-8901-f23g-45h678901j2k", "Role": "Administrator"}, {"MemberId": "2ab2345c-67de-8901-f23g-45h678901j2k", "Role": "Member"}]}
```

#### Sample Response
<a name="API_BatchCreateRoomMembership_Example_1_Response"></a>

```
HTTP/1.1 201 Created x-amzn-RequestId: 169ba401-d886-475f-8b3f-e01eac6fadfb Content-Type: application/json Content-Length: 13 Date: Mon, 02 Dec 2019 22:46:58 GMT Connection: keep-alive {"Errors":[]}
```

## See Also
<a name="API_BatchCreateRoomMembership_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-2018-05-01/BatchCreateRoomMembership)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-2018-05-01/BatchCreateRoomMembership)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/BatchCreateRoomMembership)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-2018-05-01/BatchCreateRoomMembership)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/BatchCreateRoomMembership)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-2018-05-01/BatchCreateRoomMembership)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-2018-05-01/BatchCreateRoomMembership)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-2018-05-01/BatchCreateRoomMembership)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-2018-05-01/BatchCreateRoomMembership)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/BatchCreateRoomMembership)
