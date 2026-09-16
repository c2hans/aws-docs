---
source_url: https://docs.aws.amazon.com/chime/latest/APIReference/API_CreateUser.html
---

**End of support notice**: On February 20, 2026, AWS will end support for the Amazon Chime service. After February 20, 2026, you will no longer be able to access the Amazon Chime console or Amazon Chime application resources. For more information, visit the [blog post](https://aws.amazon.com/blogs/messaging-and-targeting/update-on-support-for-amazon-chime/). **Note:** This does not impact the availability of the [Amazon Chime SDK service](https://aws.amazon.com/chime/chime-sdk/).

# CreateUser
<a name="API_CreateUser"></a>

Creates a user under the specified Amazon Chime account.

## Request Syntax
<a name="API_CreateUser_RequestSyntax"></a>

```
POST /accounts/{{accountId}}/users?operation=create HTTP/1.1
Content-type: application/json

{
   "Email": "{{string}}",
   "Username": "{{string}}",
   "UserType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateUser_RequestParameters"></a>

The request uses the following URI parameters.

 ** [accountId](#API_CreateUser_RequestSyntax) **   <a name="chime-CreateUser-request-uri-AccountId"></a>
The Amazon Chime account ID.
Pattern: `.*\S.*`
Required: Yes

## Request Body
<a name="API_CreateUser_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Email](#API_CreateUser_RequestSyntax) **   <a name="chime-CreateUser-request-Email"></a>
The user's email address.
Type: String
Pattern: `.+@.+\..+`
Required: No

 ** [Username](#API_CreateUser_RequestSyntax) **   <a name="chime-CreateUser-request-Username"></a>
The user name.
Type: String
Required: No

 ** [UserType](#API_CreateUser_RequestSyntax) **   <a name="chime-CreateUser-request-UserType"></a>
The user type.
Type: String
Valid Values: `PrivateUser | SharedDevice`
Required: No

## Response Syntax
<a name="API_CreateUser_ResponseSyntax"></a>

```
HTTP/1.1 201
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
<a name="API_CreateUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [User](#API_CreateUser_ResponseSyntax) **   <a name="chime-CreateUser-response-User"></a>
The user on the Amazon Chime account.
Type: [User](API_User.md) object

## Errors
<a name="API_CreateUser_Errors"></a>

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
<a name="API_CreateUser_Examples"></a>

In the following example or examples, the Authorization header contents( `AUTHPARAMS` ) must be replaced with an AWS Signature Version 4 signature. For more information about creating these signatures, see [Signature Version 4 Signing Process](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) in the *AWS General Reference*.

You only need to learn how to sign HTTP requests if you intend to manually create them. When you use the [AWS Command Line Interface (AWS CLI)](http://aws.amazon.com/cli/) or one of the [AWS SDKs](http://aws.amazon.com/tools/) to make requests to AWS, these tools automatically sign the requests for you with the access key that you specify when you configure the tools. When you use these tools, you don't need to learn how to sign requests yourself.

### Example
<a name="API_CreateUser_Example_1"></a>

This example creates a shared device profile for the specified email address.

#### Sample Request
<a name="API_CreateUser_Example_1_Request"></a>

```
POST /accounts/12a3456b-7c89-012d-3456-78901e23fg45/users?operation=create HTTP/1.1 Host: service.chime.aws.amazon.com Accept-Encoding: identity User-Agent: aws-cli/1.17.3 Python/3.8.0 Windows/10 botocore/1.14.3 X-Amz-Date: 20200115T223809Z AUTHPARAMS {"Email": "roomdevice@example.com", "UserType": "SharedDevice"}
```

#### Sample Response
<a name="API_CreateUser_Example_1_Response"></a>

```
HTTP/1.1 201 Created x-amzn-RequestId: 4225c49a-307a-413b-bc8f-37bb145c1483 Content-Type: application/json Content-Length: 664 Date: Wed, 15 Jan 2020 22:38:09 GMT Connection: keep-alive {"User":{"AccountId":"12a3456b-7c89-012d-3456-78901e23fg45","AlexaForBusinessMetadata":{"AlexaForBusinessRoomArn":null,"IsAlexaForBusinessEnabled":false},"Delegates":null,"Devices":null,"DisplayName":"room device","EmailAlias":[],"FullName":"Room Device","InvitedOn":null,"IsProTrial":false,"LastActiveOn":null,"LicenseType":"Pro","PersonalPIN":null,"PresenceVisibility":null,"PrimaryEmail":"roomdevice@example.com","PrimaryProvisionedNumber":null,"RegisteredOn":"2020-01-15T22:38:09.806Z","UserId":"1ab2345c-67de-8901-f23g-45h678901j2k","UserInvitationStatus":null,"UserLocale":null,"UserRegistrationStatus":"Registered","UserType":"SharedDevice","Vanity":null}}
```

## See Also
<a name="API_CreateUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/chime-2018-05-01/CreateUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/chime-2018-05-01/CreateUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/chime-2018-05-01/CreateUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/chime-2018-05-01/CreateUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/chime-2018-05-01/CreateUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/chime-2018-05-01/CreateUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/chime-2018-05-01/CreateUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/chime-2018-05-01/CreateUser)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/chime-2018-05-01/CreateUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/chime-2018-05-01/CreateUser)
