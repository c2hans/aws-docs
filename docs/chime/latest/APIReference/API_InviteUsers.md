---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_InviteUsers.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# InviteUsers
<a name="API_InviteUsers"></a>

Sends email to a maximum of 50 users, inviting them to the specified Amazon Chime `Team` account. Only `Team` account types are currently supported for this action.

## Request Syntax
<a name="API_InviteUsers_RequestSyntax"></a>

```
POST /accounts/{{accountId}}/users?operation=add HTTP/1.1
Content-type: application/json

{
   "UserEmailList": [ "{{string}}" ],
   "UserType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_InviteUsers_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accountId](#API_InviteUsers_RequestSyntax) **   <a name="chime-InviteUsers-request-uri-AccountId"></a>
The Amazon Chime account ID.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_InviteUsers_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [UserEmailList](#API_InviteUsers_RequestSyntax) **   <a name="chime-InviteUsers-request-UserEmailList"></a>
The user email addresses to which to send the email invitation.
Type: Array of strings
Array Members: Maximum number of 50 items.
Pattern: `.+@.+\..+`
Required: Yes

 ** [UserType](#API_InviteUsers_RequestSyntax) **   <a name="chime-InviteUsers-request-UserType"></a>
The user type.
Type: String
Valid Values: `PrivateUser | SharedDevice`
Required: No

## Response Syntax
<a name="API_InviteUsers_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "Invites": [
      {
         "EmailAddress": "string",
         "EmailStatus": "string",
         "InviteId": "string",
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_InviteUsers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Invites](#API_InviteUsers_ResponseSyntax) **   <a name="chime-InviteUsers-response-Invites"></a>
The email invitation details.
Type: Array of [Invite](API_Invite.md) objects

## Errors
<a name="API_InviteUsers_Errors"></a>

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
<a name="API_InviteUsers_Examples"></a>

In the following example or examples, the Authorization header contents( `AUTHPARAMS` ) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_InviteUsers_Example_1"></a>

This example sends an email to invite users to the specified account.

#### Sample Request
<a name="API_InviteUsers_Example_1_Request"></a>

```
POST /console/accounts/12a3456b-7c89-012d-3456-78901e23fg45/users?operation=add HTTP/1.1 Host: service.chime.aws.amazon.com Accept-Encoding: identity User-Agent: aws-cli/1.16.83 Python/3.6.6 Windows/10 botocore/1.12.73 X-Amz-Date: 20190108T180827Z Authorization: AUTHPARAMS Content-Length: 46 {"UserEmailList": ["user1@example.com", "user2@example.com"]}
```

#### Sample Response
<a name="API_InviteUsers_Example_1_Response"></a>

```
HTTP/1.1 201 Created x-amzn-RequestId: e1b2ea98-2934-400d-a5f1-f68d74658ea6 Content-Type: application/json Content-Length: 204 Date: Tue, 08 Jan 2019 18:08:27 GMT Connection: keep-alive {"Invites": [{"EmailAddress": "user1@example.com","EmailStatus": "Sent","InviteId": "a12bc345-6def-78g9-01h2-34jk56789012","Status": "Pending",}{"EmailAddress": "user2@example.com","EmailStatus": "Sent","InviteId": "b12bc345-6def-78g9-01h2-34jk56789012","Status": "Pending",}] }
```

## See Also
<a name="API_InviteUsers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-2018-05-01/InviteUsers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-2018-05-01/InviteUsers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/InviteUsers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-2018-05-01/InviteUsers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/InviteUsers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-2018-05-01/InviteUsers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-2018-05-01/InviteUsers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-2018-05-01/InviteUsers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-2018-05-01/InviteUsers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/InviteUsers)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
