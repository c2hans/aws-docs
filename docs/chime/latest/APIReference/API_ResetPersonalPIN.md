---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_ResetPersonalPIN.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# ResetPersonalPIN
<a name="API_ResetPersonalPIN"></a>

Resets the personal meeting PIN for the specified user on an Amazon Chime account. Returns the [User](API_User.md) object with the updated personal meeting PIN.

## Request Syntax
<a name="API_ResetPersonalPIN_RequestSyntax"></a>

```
POST /accounts/{{accountId}}/users/{userId}?operation=reset-personal-pin HTTP/1.1
```

## URI Request Parameters
<a name="API_ResetPersonalPIN_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accountId](#API_ResetPersonalPIN_RequestSyntax) **   <a name="chime-ResetPersonalPIN-request-uri-AccountId"></a>
The Amazon Chime account ID.
Pattern: `.*\S.*`
Required: Yes

 ** [userId](#API_ResetPersonalPIN_RequestSyntax) **   <a name="chime-ResetPersonalPIN-request-uri-UserId"></a>
The user ID.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_ResetPersonalPIN_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ResetPersonalPIN_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "User": {
      "AccountId": "string",
      "AlexaForBusinessMetadata": {
         "AlexaForBusinessRoomArn": "string",
         "IsAlexaForBusinessEnabled": boolean
      },
      "DisplayName": "string",
      "InvitedOn": "string",
      "LicenseType": "string",
      "PersonalPIN": "string",
      "PrimaryEmail": "string",
      "PrimaryProvisionedNumber": "string",
      "RegisteredOn": "string",
      "UserId": "string",
      "UserInvitationStatus": "string",
      "UserRegistrationStatus": "string",
      "UserType": "string"
   }
}
```

## Response Elements
<a name="API_ResetPersonalPIN_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [User](#API_ResetPersonalPIN_ResponseSyntax) **   <a name="chime-ResetPersonalPIN-response-User"></a>
The user details and new personal meeting PIN.
Type: [User](API_User.md) object

## Errors
<a name="API_ResetPersonalPIN_Errors"></a>

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
<a name="API_ResetPersonalPIN_Examples"></a>

In the following example or examples, the Authorization header contents( `AUTHPARAMS` ) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_ResetPersonalPIN_Example_1"></a>

This example resets the personal meeting PIN for the specified user.

#### Sample Request
<a name="API_ResetPersonalPIN_Example_1_Request"></a>

```
POST /console/accounts/12a3456b-7c89-012d-3456-78901e23fg45/users/1ab2345c-67de-8901-f23g-45h678901j2k?operation=reset-personal-pin HTTP/1.1 Host: service.chime.aws.amazon.com Accept-Encoding: identity User-Agent: aws-cli/1.16.83 Python/3.6.6 Windows/10 botocore/1.12.73 X-Amz-Date: 20190108T181048Z Authorization: AUTHPARAMS Content-Length: 0
```

#### Sample Response
<a name="API_ResetPersonalPIN_Example_1_Response"></a>

```
HTTP/1.1 200 OK x-amzn-RequestId: a0033e1d-41aa-4030-8f52-ded7ebcf34bd Content-Type: application/json Content-Length: 558 Date: Tue, 08 Jan 2019 18:10:48 GMT Connection: keep-alive {"User": {"AccountId": "12a3456b-7c89-012d-3456-78901e23fg45","Delegates": null,"Devices": null,"DisplayName": "user1","EmailAlias": [],"FullName": "user1","InvitedOn": null,"IsProTrial": false,"LastActiveOn": null,"LicenseType": "Pro","PersonalPIN": "XXXXXXXXXX","PresenceVisibility": null,"PrimaryEmail": "user1@example.com","PrimaryProvisionedNumber": null,"RegisteredOn": "2018-12-20T18:45:25.231Z","UserId": "1ab2345c-67de-8901-f23g-45h678901j2k","UserInvitationStatus": null,"UserLocale": null,"UserRegistrationStatus": "Registered","Vanity": null} }
```

## See Also
<a name="API_ResetPersonalPIN_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-2018-05-01/ResetPersonalPIN)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-2018-05-01/ResetPersonalPIN)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/ResetPersonalPIN)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-2018-05-01/ResetPersonalPIN)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/ResetPersonalPIN)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-2018-05-01/ResetPersonalPIN)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-2018-05-01/ResetPersonalPIN)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-2018-05-01/ResetPersonalPIN)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/chime-2018-05-01/ResetPersonalPIN)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/ResetPersonalPIN)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
