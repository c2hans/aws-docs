---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_CreateKxUser.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# CreateKxUser
<a name="API_CreateKxUser"></a>

Creates a user in FinSpace kdb environment with an associated IAM role.

## Request Syntax
<a name="API_CreateKxUser_RequestSyntax"></a>

```
POST /kx/environments/{{environmentId}}/users HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "iamRole": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "userName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateKxUser_RequestParameters"></a>

The request uses the following URI parameters.

 ** [environmentId](#API_CreateKxUser_RequestSyntax) **   <a name="finspace-CreateKxUser-request-uri-environmentId"></a>
A unique identifier for the kdb environment where you want to create a user.
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]{1,26}$`
Required: Yes

## Request Body
<a name="API_CreateKxUser_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [iamRole](#API_CreateKxUser_RequestSyntax) **   <a name="finspace-CreateKxUser-request-iamRole"></a>
The IAM role ARN that will be associated with the user.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`
Required: Yes

 ** [userName](#API_CreateKxUser_RequestSyntax) **   <a name="finspace-CreateKxUser-request-userName"></a>
A unique identifier for the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^[0-9A-Za-z_-]{1,50}$`
Required: Yes

 ** [clientToken](#API_CreateKxUser_RequestSyntax) **   <a name="finspace-CreateKxUser-request-clientToken"></a>
A token that ensures idempotency. This token expires in 10 minutes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `.*\S.*`
Required: No

 ** [tags](#API_CreateKxUser_RequestSyntax) **   <a name="finspace-CreateKxUser-request-tags"></a>
A list of key-value pairs to label the user. You can add up to 50 tags to a user.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Value Pattern: `^[a-zA-Z0-9+-=._:@ ]+$`
Required: No

## Response Syntax
<a name="API_CreateKxUser_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "environmentId": "string",
   "iamRole": "string",
   "userArn": "string",
   "userName": "string"
}
```

## Response Elements
<a name="API_CreateKxUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [environmentId](#API_CreateKxUser_ResponseSyntax) **   <a name="finspace-CreateKxUser-response-environmentId"></a>
A unique identifier for the kdb environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]{1,26}$`

 ** [iamRole](#API_CreateKxUser_ResponseSyntax) **   <a name="finspace-CreateKxUser-response-iamRole"></a>
The IAM role ARN that will be associated with the user.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`

 ** [userArn](#API_CreateKxUser_ResponseSyntax) **   <a name="finspace-CreateKxUser-response-userArn"></a>
 The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs and how to use ARNs in policies, see [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html) in the *IAM User Guide*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws:finspace:[A-Za-z0-9_/.-]{0,63}:\d+:kxEnvironment/[0-9A-Za-z_-]{1,128}/kxUser/[0-9A-Za-z_-]{1,128}$`

 ** [userName](#API_CreateKxUser_ResponseSyntax) **   <a name="finspace-CreateKxUser-response-userName"></a>
A unique identifier for the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^[0-9A-Za-z_-]{1,50}$`

## Errors
<a name="API_CreateKxUser_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There was a conflict with this action, and it could not be completed.
 ** reason **
The reason for the conflict exception.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** LimitExceededException **
A service limit or quota is exceeded.
HTTP Status Code: 400

 ** ResourceAlreadyExistsException **
The specified resource group already exists.
HTTP Status Code: 409

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateKxUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2021-03-12/CreateKxUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2021-03-12/CreateKxUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/CreateKxUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2021-03-12/CreateKxUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/CreateKxUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2021-03-12/CreateKxUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2021-03-12/CreateKxUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2021-03-12/CreateKxUser)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/finspace-2021-03-12/CreateKxUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/CreateKxUser)
