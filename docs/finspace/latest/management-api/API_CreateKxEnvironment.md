---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_CreateKxEnvironment.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# CreateKxEnvironment
<a name="API_CreateKxEnvironment"></a>

Creates a managed kdb environment for the account.

## Request Syntax
<a name="API_CreateKxEnvironment_RequestSyntax"></a>

```
POST /kx/environments HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "description": "{{string}}",
   "kmsKeyId": "{{string}}",
   "name": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateKxEnvironment_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateKxEnvironment_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [kmsKeyId](#API_CreateKxEnvironment_RequestSyntax) **   <a name="finspace-CreateKxEnvironment-request-kmsKeyId"></a>
The KMS key ID to encrypt your data in the FinSpace environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^arn:aws:kms:.*:\d+:.*$`
Required: Yes

 ** [name](#API_CreateKxEnvironment_RequestSyntax) **   <a name="finspace-CreateKxEnvironment-request-name"></a>
The name of the kdb environment that you want to create.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: Yes

 ** [clientToken](#API_CreateKxEnvironment_RequestSyntax) **   <a name="finspace-CreateKxEnvironment-request-clientToken"></a>
A token that ensures idempotency. This token expires in 10 minutes.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `.*\S.*`
Required: No

 ** [description](#API_CreateKxEnvironment_RequestSyntax) **   <a name="finspace-CreateKxEnvironment-request-description"></a>
A description for the kdb environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[a-zA-Z0-9. ]{1,1000}$`
Required: No

 ** [tags](#API_CreateKxEnvironment_RequestSyntax) **   <a name="finspace-CreateKxEnvironment-request-tags"></a>
A list of key-value pairs to label the kdb environment. You can add up to 50 tags to your kdb environment.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Value Pattern: `^[a-zA-Z0-9+-=._:@ ]+$`
Required: No

## Response Syntax
<a name="API_CreateKxEnvironment_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationTimestamp": number,
   "description": "string",
   "environmentArn": "string",
   "environmentId": "string",
   "kmsKeyId": "string",
   "name": "string",
   "status": "string"
}
```

## Response Elements
<a name="API_CreateKxEnvironment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTimestamp](#API_CreateKxEnvironment_ResponseSyntax) **   <a name="finspace-CreateKxEnvironment-response-creationTimestamp"></a>
The timestamp at which the kdb environment was created in FinSpace.
Type: Timestamp

 ** [description](#API_CreateKxEnvironment_ResponseSyntax) **   <a name="finspace-CreateKxEnvironment-response-description"></a>
A description for the kdb environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[a-zA-Z0-9. ]{1,1000}$`

 ** [environmentArn](#API_CreateKxEnvironment_ResponseSyntax) **   <a name="finspace-CreateKxEnvironment-response-environmentArn"></a>
The ARN identifier of the environment.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `^arn:aws:finspace:[A-Za-z0-9_/.-]{0,63}:\d+:environment/[0-9A-Za-z_-]{1,128}$`

 ** [environmentId](#API_CreateKxEnvironment_ResponseSyntax) **   <a name="finspace-CreateKxEnvironment-response-environmentId"></a>
A unique identifier for the kdb environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.
Pattern: `^[a-zA-Z0-9]{1,26}$`

 ** [kmsKeyId](#API_CreateKxEnvironment_ResponseSyntax) **   <a name="finspace-CreateKxEnvironment-response-kmsKeyId"></a>
The KMS key ID to encrypt your data in the FinSpace environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[a-zA-Z-0-9-:\/]*$`

 ** [name](#API_CreateKxEnvironment_ResponseSyntax) **   <a name="finspace-CreateKxEnvironment-response-name"></a>
The name of the kdb environment.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`

 ** [status](#API_CreateKxEnvironment_ResponseSyntax) **   <a name="finspace-CreateKxEnvironment-response-status"></a>
The status of the kdb environment.
Type: String
Valid Values: `CREATE_REQUESTED | CREATING | CREATED | DELETE_REQUESTED | DELETING | DELETED | FAILED_CREATION | RETRY_DELETION | FAILED_DELETION | UPDATE_NETWORK_REQUESTED | UPDATING_NETWORK | FAILED_UPDATING_NETWORK | SUSPENDED`

## Errors
<a name="API_CreateKxEnvironment_Errors"></a>

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

 ** ServiceQuotaExceededException **
 You have exceeded your service quota. To perform the requested action, remove some of the relevant resources, or use Service Quotas to request a service quota increase.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateKxEnvironment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2021-03-12/CreateKxEnvironment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2021-03-12/CreateKxEnvironment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/CreateKxEnvironment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2021-03-12/CreateKxEnvironment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/CreateKxEnvironment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2021-03-12/CreateKxEnvironment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2021-03-12/CreateKxEnvironment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2021-03-12/CreateKxEnvironment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/finspace-2021-03-12/CreateKxEnvironment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/CreateKxEnvironment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
