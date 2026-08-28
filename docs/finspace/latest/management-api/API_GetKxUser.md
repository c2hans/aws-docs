---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_GetKxUser.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# GetKxUser
<a name="API_GetKxUser"></a>

Retrieves information about the specified kdb user.

## Request Syntax
<a name="API_GetKxUser_RequestSyntax"></a>

```
GET /kx/environments/{{environmentId}}/users/{{userName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetKxUser_RequestParameters"></a>

The request uses the following URI parameters.

 ** [environmentId](#API_GetKxUser_RequestSyntax) **   <a name="finspace-GetKxUser-request-uri-environmentId"></a>
A unique identifier for the kdb environment.
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]{1,26}$`
Required: Yes

 ** [userName](#API_GetKxUser_RequestSyntax) **   <a name="finspace-GetKxUser-request-uri-userName"></a>
A unique identifier for the user.
Length Constraints: Minimum length of 1. Maximum length of 50.
Pattern: `^[0-9A-Za-z_-]{1,50}$`
Required: Yes

## Request Body
<a name="API_GetKxUser_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetKxUser_ResponseSyntax"></a>

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
<a name="API_GetKxUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [environmentId](#API_GetKxUser_ResponseSyntax) **   <a name="finspace-GetKxUser-response-environmentId"></a>
A unique identifier for the kdb environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]{1,26}$`

 ** [iamRole](#API_GetKxUser_ResponseSyntax) **   <a name="finspace-GetKxUser-response-iamRole"></a>
The IAM role ARN that is associated with the user.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws[a-z\-]*:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+$`

 ** [userArn](#API_GetKxUser_ResponseSyntax) **   <a name="finspace-GetKxUser-response-userArn"></a>
 The Amazon Resource Name (ARN) that identifies the user. For more information about ARNs and how to use ARNs in policies, see [IAM Identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html) in the *IAM User Guide*.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws:finspace:[A-Za-z0-9_/.-]{0,63}:\d+:kxEnvironment/[0-9A-Za-z_-]{1,128}/kxUser/[0-9A-Za-z_-]{1,128}$`

 ** [userName](#API_GetKxUser_ResponseSyntax) **   <a name="finspace-GetKxUser-response-userName"></a>
A unique identifier for the user.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]{1,26}$`

## Errors
<a name="API_GetKxUser_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

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
<a name="API_GetKxUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2021-03-12/GetKxUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2021-03-12/GetKxUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/GetKxUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2021-03-12/GetKxUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/GetKxUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2021-03-12/GetKxUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2021-03-12/GetKxUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2021-03-12/GetKxUser)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/finspace-2021-03-12/GetKxUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/GetKxUser)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
