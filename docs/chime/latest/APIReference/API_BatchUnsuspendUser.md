---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_BatchUnsuspendUser.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# BatchUnsuspendUser
<a name="API_BatchUnsuspendUser"></a>

Removes the suspension from up to 50 previously suspended users for the specified Amazon Chime `EnterpriseLWA` account. Only users on `EnterpriseLWA` accounts can be unsuspended using this action. For more information about different account types, see [ Managing Your Amazon Chime Accounts ](https://docs.aws.amazon.com/chime/latest/ag/manage-chime-account.html) in the account types, in the *Amazon Chime Administration Guide*.

Previously suspended users who are unsuspended using this action are returned to `Registered` status. Users who are not previously suspended are ignored.

## Request Syntax
<a name="API_BatchUnsuspendUser_RequestSyntax"></a>

```
POST /accounts/{{accountId}}/users?operation=unsuspend HTTP/1.1
Content-type: application/json

{
   "UserIdList": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchUnsuspendUser_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accountId](#API_BatchUnsuspendUser_RequestSyntax) **   <a name="chime-BatchUnsuspendUser-request-uri-AccountId"></a>
The Amazon Chime account ID.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_BatchUnsuspendUser_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [UserIdList](#API_BatchUnsuspendUser_RequestSyntax) **   <a name="chime-BatchUnsuspendUser-request-UserIdList"></a>
The request containing the user IDs to unsuspend.
Type: Array of strings
Array Members: Maximum number of 50 items.
Pattern: `.*\S.*`
Required: Yes

## Response Syntax
<a name="API_BatchUnsuspendUser_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "UserErrors": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "UserId": "string"
      }
   ]
}
```

## Response Elements
<a name="API_BatchUnsuspendUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [UserErrors](#API_BatchUnsuspendUser_ResponseSyntax) **   <a name="chime-BatchUnsuspendUser-response-UserErrors"></a>
If the [BatchUnsuspendUser](#API_BatchUnsuspendUser) action fails for one or more of the user IDs in the request, a list of the user IDs is returned, along with error codes and error messages.
Type: Array of [UserError](API_UserError.md) objects

## Errors
<a name="API_BatchUnsuspendUser_Errors"></a>

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
<a name="API_BatchUnsuspendUser_Examples"></a>

In the following example or examples, the Authorization header contents( `AUTHPARAMS` ) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_BatchUnsuspendUser_Example_1"></a>

This example removes the previous suspension for the listed users on the specified Amazon Chime account.

#### Sample Request
<a name="API_BatchUnsuspendUser_Example_1_Request"></a>

```
POST /console/accounts/12a3456b-7c89-012d-3456-78901e23fg45/users?operation=unsuspend HTTP/1.1 Host: service.chime.aws.amazon.com Accept-Encoding: identity User-Agent: aws-cli/1.16.83 Python/3.6.6 Windows/10 botocore/1.12.73 X-Amz-Date: 20190108T220526Z Authorization: AUTHPARAMS Content-Length: 96 {"UserIdList": ["1ab2345c-67de-8901-f23g-45h678901j2k", "2ab2345c-67de-8901-f23g-45h678901j2k", "3ab2345c-67de-8901-f23g-45h678901j2k"]}
```

#### Sample Response
<a name="API_BatchUnsuspendUser_Example_1_Response"></a>

```
HTTP/1.1 200 OK x-amzn-RequestId: d97c7380-cb87-40ce-b4c3-c250999a92dc Content-Type: application/json Content-Length: 17 Date: Tue, 08 Jan 2019 22:05:26 GMT Connection: keep-alive {"UserErrors": [] }
```

## See Also
<a name="API_BatchUnsuspendUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-2018-05-01/BatchUnsuspendUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-2018-05-01/BatchUnsuspendUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/BatchUnsuspendUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-2018-05-01/BatchUnsuspendUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/BatchUnsuspendUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-2018-05-01/BatchUnsuspendUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-2018-05-01/BatchUnsuspendUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-2018-05-01/BatchUnsuspendUser)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-2018-05-01/BatchUnsuspendUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/BatchUnsuspendUser)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
