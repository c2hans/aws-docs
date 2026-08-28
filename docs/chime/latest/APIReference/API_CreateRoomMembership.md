---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateRoomMembership.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# CreateRoomMembership
<a name="API_CreateRoomMembership"></a>

Adds a member to a chat room in an Amazon Chime Enterprise account. A member can be either a user or a bot. The member role designates whether the member is a chat room administrator or a general chat room member.

## Request Syntax
<a name="API_CreateRoomMembership_RequestSyntax"></a>

```
POST /accounts/{{accountId}}/rooms/{{roomId}}/memberships HTTP/1.1
Content-type: application/json

{
   "MemberId": "{{string}}",
   "Role": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateRoomMembership_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accountId](#API_CreateRoomMembership_RequestSyntax) **   <a name="chime-CreateRoomMembership-request-uri-AccountId"></a>
The Amazon Chime account ID.
Pattern: `.*\S.*`
Required: Yes

 ** [roomId](#API_CreateRoomMembership_RequestSyntax) **   <a name="chime-CreateRoomMembership-request-uri-RoomId"></a>
The room ID.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_CreateRoomMembership_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MemberId](#API_CreateRoomMembership_RequestSyntax) **   <a name="chime-CreateRoomMembership-request-MemberId"></a>
The Amazon Chime member ID (user ID or bot ID).
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** [Role](#API_CreateRoomMembership_RequestSyntax) **   <a name="chime-CreateRoomMembership-request-Role"></a>
The role of the member.
Type: String
Valid Values: `Administrator | Member`
Required: No

## Response Syntax
<a name="API_CreateRoomMembership_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "RoomMembership": {
      "InvitedBy": "string",
      "Member": {
         "AccountId": "string",
         "Email": "string",
         "FullName": "string",
         "MemberId": "string",
         "MemberType": "string"
      },
      "Role": "string",
      "RoomId": "string",
      "UpdatedTimestamp": "string"
   }
}
```

## Response Elements
<a name="API_CreateRoomMembership_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [RoomMembership](#API_CreateRoomMembership_ResponseSyntax) **   <a name="chime-CreateRoomMembership-response-RoomMembership"></a>
The room membership details.
Type: [RoomMembership](API_RoomMembership.md) object

## Errors
<a name="API_CreateRoomMembership_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** ConflictException **
The request could not be processed because of conflict in the current state of the resource.
HTTP Status Code: 409

 ** ForbiddenException **
The client is permanently forbidden from making the request.
HTTP Status Code: 403

 ** NotFoundException **
One or more of the resources in the request does not exist in the system.
HTTP Status Code: 404

 ** ResourceLimitExceededException **
The request exceeds the resource limit.
HTTP Status Code: 400

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
<a name="API_CreateRoomMembership_Examples"></a>

In the following example or examples, the Authorization header contents( `AUTHPARAMS` ) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_CreateRoomMembership_Example_1"></a>

This example adds the specified user to the chat room as a chat room member.

#### Sample Request
<a name="API_CreateRoomMembership_Example_1_Request"></a>

```
POST /accounts/12a3456b-7c89-012d-3456-78901e23fg45/rooms/abcd1e2d-3e45-6789-01f2-3g45h67i890j/memberships HTTP/1.1 Host: service.chime.aws.amazon.com Accept-Encoding: identity User-Agent: aws-cli/1.16.293 Python/3.8.0 Windows/10 botocore/1.13.29 X-Amz-Date: 20191202T223641Z Authorization: AUTHPARAMS Content-Length: 52 {"MemberId": "1ab2345c-67de-8901-f23g-45h678901j2k"}
```

#### Sample Response
<a name="API_CreateRoomMembership_Example_1_Response"></a>

```
HTTP/1.1 201 Created x-amzn-RequestId: 899d868f-767e-45f7-b516-7066985c96ff Content-Type: application/json Content-Length: 381 Date: Mon, 02 Dec 2019 22:36:42 GMT Connection: keep-alive {"RoomMembership":{"InvitedBy":"arn:aws:iam::111122223333:user/alejandro","Member":{"AccountId":"12a3456b-7c89-012d-3456-78901e23fg45","Email":"janed@example.com","FullName":"Jane Doe","MemberId":"1ab2345c-67de-8901-f23g-45h678901j2k","MemberType":"User"},"Role":"Member","RoomId":"abcd1e2d-3e45-6789-01f2-3g45h67i890j","UpdatedTimestamp":"2019-12-02T22:36:41.969Z"}}
```

## See Also
<a name="API_CreateRoomMembership_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-2018-05-01/CreateRoomMembership)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-2018-05-01/CreateRoomMembership)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/CreateRoomMembership)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-2018-05-01/CreateRoomMembership)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/CreateRoomMembership)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-2018-05-01/CreateRoomMembership)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-2018-05-01/CreateRoomMembership)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-2018-05-01/CreateRoomMembership)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-2018-05-01/CreateRoomMembership)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/CreateRoomMembership)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
