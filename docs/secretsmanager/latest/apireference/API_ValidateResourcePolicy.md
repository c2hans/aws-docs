---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ValidateResourcePolicy.html
---

# ValidateResourcePolicy
<a name="API_ValidateResourcePolicy"></a>

Validates that a resource policy does not grant a wide range of principals access to your secret. A resource-based policy is optional for secrets.

The API performs three checks when validating the policy:
+ Sends a call to [Zelkova](https://aws.amazon.com/blogs/security/protect-sensitive-data-in-the-cloud-with-automated-reasoning-zelkova/), an automated reasoning engine, to ensure your resource policy does not allow broad access to your secret, for example policies that use a wildcard for the principal.
+ Checks for correct syntax in a policy.
+ Verifies the policy does not lock out a caller.

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with AWS CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

 **Required permissions: ** `secretsmanager:ValidateResourcePolicy` and `secretsmanager:PutResourcePolicy`. For more information, see [ IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Request Syntax
<a name="API_ValidateResourcePolicy_RequestSyntax"></a>

```
{
   "ResourcePolicy": "{{string}}",
   "SecretId": "{{string}}"
}
```

## Request Parameters
<a name="API_ValidateResourcePolicy_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourcePolicy](#API_ValidateResourcePolicy_RequestSyntax) **   <a name="SecretsManager-ValidateResourcePolicy-request-ResourcePolicy"></a>
A JSON-formatted string that contains an AWS resource-based policy. The policy in the string identifies who can access or manage this secret and its versions. For example policies, see [Permissions policy examples](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access_examples.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20480.
Required: Yes

 ** [SecretId](#API_ValidateResourcePolicy_RequestSyntax) **   <a name="SecretsManager-ValidateResourcePolicy-request-SecretId"></a>
The ARN or name of the secret with the resource-based policy you want to validate.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_ValidateResourcePolicy_ResponseSyntax"></a>

```
{
   "PolicyValidationPassed": boolean,
   "ValidationErrors": [
      {
         "CheckName": "string",
         "ErrorMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ValidateResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [PolicyValidationPassed](#API_ValidateResourcePolicy_ResponseSyntax) **   <a name="SecretsManager-ValidateResourcePolicy-response-PolicyValidationPassed"></a>
True if your policy passes validation, otherwise false.
Type: Boolean

 ** [ValidationErrors](#API_ValidateResourcePolicy_ResponseSyntax) **   <a name="SecretsManager-ValidateResourcePolicy-response-ValidationErrors"></a>
Validation errors if your policy didn't pass validation.
Type: Array of [ValidationErrorsEntry](API_ValidationErrorsEntry.md) objects

## Errors
<a name="API_ValidateResourcePolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** InternalServiceError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidParameterException **
The parameter name or value is invalid.
HTTP Status Code: 400

 ** InvalidRequestException **
A parameter value is not valid for the current state of the resource.
Possible causes:
+ The secret is scheduled for deletion.
+ You tried to enable rotation on a secret that doesn't already have a Lambda function ARN configured and you didn't include such an ARN as a parameter in this call.
+ The secret is managed by another service, and you must use that service to update it. For more information, see [Secrets managed by other AWS services](https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html).
HTTP Status Code: 400

 ** MalformedPolicyDocumentException **
The resource policy has syntax errors.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Secrets Manager can't find the resource that you asked for.
HTTP Status Code: 400

## Examples
<a name="API_ValidateResourcePolicy_Examples"></a>

### Example
<a name="API_ValidateResourcePolicy_Example_1"></a>

The following example shows how to validate a JSON policy.

#### Sample Request
<a name="API_ValidateResourcePolicy_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: secretsmanager.region.domain
Accept-Encoding: identity
X-Amz-Target: secretsmanager.ValidateResourcePolicy
Content-Type: application/x-amz-json-1.1
User-Agent: <user-agent-string>
X-Amz-Date: <date>
Authorization: AWS4-HMAC-SHA256 Credential=<credentials>,SignedHeaders=<headers>, Signature=<signature>
Content-Length: <payload-size-bytes>

    {
      "SecretId": "MyTestDatabaseSecret",
      "ResourcePolicy": "{\n\"Version\":\"2012-10-17\",\n\"Statement\":[{\n\"Effect\":\"Allow\",\n\"Principal\":{\n\"AWS\":\"arn:aws:iam::123456789012:root\"\n},\n\"Action\":\"secretsmanager:GetSecretValue\",\n\"Resource\":\"*\"\n}]\n}"
  }
```

## See Also
<a name="API_ValidateResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/secretsmanager-2017-10-17/ValidateResourcePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/secretsmanager-2017-10-17/ValidateResourcePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/secretsmanager-2017-10-17/ValidateResourcePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/secretsmanager-2017-10-17/ValidateResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/secretsmanager-2017-10-17/ValidateResourcePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/secretsmanager-2017-10-17/ValidateResourcePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/secretsmanager-2017-10-17/ValidateResourcePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/secretsmanager-2017-10-17/ValidateResourcePolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/secretsmanager-2017-10-17/ValidateResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/secretsmanager-2017-10-17/ValidateResourcePolicy)
