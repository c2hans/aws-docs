---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ListSecretVersionIds.html
---

# ListSecretVersionIds
<a name="API_ListSecretVersionIds"></a>

Lists the versions of a secret. Secrets Manager uses staging labels to indicate the different versions of a secret. For more information, see [ Secrets Manager concepts: Versions](https://docs.aws.amazon.com/secretsmanager/latest/userguide/getting-started.html#term_version).

To list the secrets in the account, use [ListSecrets](API_ListSecrets.md).

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with AWS CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

 **Required permissions: ** `secretsmanager:ListSecretVersionIds`. For more information, see [ IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Request Syntax
<a name="API_ListSecretVersionIds_RequestSyntax"></a>

```
{
   "IncludeDeprecated": {{boolean}},
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SecretId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListSecretVersionIds_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [IncludeDeprecated](#API_ListSecretVersionIds_RequestSyntax) **   <a name="SecretsManager-ListSecretVersionIds-request-IncludeDeprecated"></a>
Specifies whether to include versions of secrets that don't have any staging labels attached to them. Versions without staging labels are considered deprecated and are subject to deletion by Secrets Manager. By default, versions without staging labels aren't included.
Type: Boolean
Required: No

 ** [MaxResults](#API_ListSecretVersionIds_RequestSyntax) **   <a name="SecretsManager-ListSecretVersionIds-request-MaxResults"></a>
The number of results to include in the response.
If there are more results available, in the response, Secrets Manager includes `NextToken`. To get the next results, call `ListSecretVersionIds` again with the value from `NextToken`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListSecretVersionIds_RequestSyntax) **   <a name="SecretsManager-ListSecretVersionIds-request-NextToken"></a>
A token that indicates where the output should continue from, if a previous call did not show all results. To get the next results, call `ListSecretVersionIds` again with this value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [SecretId](#API_ListSecretVersionIds_RequestSyntax) **   <a name="SecretsManager-ListSecretVersionIds-request-SecretId"></a>
The ARN or name of the secret whose versions you want to list.
For an ARN, we recommend that you specify a complete ARN rather than a partial ARN. See [Finding a secret from a partial ARN](https://docs.aws.amazon.com/secretsmanager/latest/userguide/troubleshoot.html#ARN_secretnamehyphen).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_ListSecretVersionIds_ResponseSyntax"></a>

```
{
   "ARN": "string",
   "Name": "string",
   "NextToken": "string",
   "Versions": [
      {
         "CreatedDate": number,
         "KmsKeyIds": [ "string" ],
         "LastAccessedDate": number,
         "VersionId": "string",
         "VersionStages": [ "string" ]
      }
   ]
}
```

## Response Elements
<a name="API_ListSecretVersionIds_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ARN](#API_ListSecretVersionIds_ResponseSyntax) **   <a name="SecretsManager-ListSecretVersionIds-response-ARN"></a>
The ARN of the secret.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [Name](#API_ListSecretVersionIds_ResponseSyntax) **   <a name="SecretsManager-ListSecretVersionIds-response-Name"></a>
The name of the secret.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [NextToken](#API_ListSecretVersionIds_ResponseSyntax) **   <a name="SecretsManager-ListSecretVersionIds-response-NextToken"></a>
Secrets Manager includes this value if there's more output available than what is included in the current response. This can occur even when the response includes no values at all, such as when you ask for a filtered view of a long list. To get the next results, call `ListSecretVersionIds` again with this value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [Versions](#API_ListSecretVersionIds_ResponseSyntax) **   <a name="SecretsManager-ListSecretVersionIds-response-Versions"></a>
A list of the versions of the secret.
Type: Array of [SecretVersionsListEntry](API_SecretVersionsListEntry.md) objects

## Errors
<a name="API_ListSecretVersionIds_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** InternalServiceError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidNextTokenException **
The `NextToken` value is invalid.
HTTP Status Code: 400

 ** InvalidParameterException **
The parameter name or value is invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Secrets Manager can't find the resource that you asked for.
HTTP Status Code: 400

## Examples
<a name="API_ListSecretVersionIds_Examples"></a>

### Example
<a name="API_ListSecretVersionIds_Example_1"></a>

The following example shows how to retrieve a list of the versions of a secret, including versions which have no staging labels attached. The JSON request string input and response output displays formatted code with white space and line breaks for better readability. Submit your input as a single line JSON string.

#### Sample Request
<a name="API_ListSecretVersionIds_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: secretsmanager.region.domain
Accept-Encoding: identity
X-Amz-Target: secretsmanager.ListSecretVersionIds
Content-Type: application/x-amz-json-1.1
User-Agent: <user-agent-string>
X-Amz-Date: <date>
Authorization: AWS4-HMAC-SHA256 Credential=<credentials>,SignedHeaders=<headers>, Signature=<signature>
Content-Length: <payload-size-bytes>

{
  "SecretId": "MyTestDatabaseSecret",
  "IncludeDeprecated": true
}
```

#### Sample Response
<a name="API_ListSecretVersionIds_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: <date>
Content-Type: application/x-amz-json-1.1
Content-Length: <response-size-bytes>
Connection: keep-alive
x-amzn-RequestId: <request-id-guid>

{
  "ARN":"arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3",
  "Name":"MyTestDatabaseSecret",
  "Versions":[
    {
      "CreatedDate":1.523477145713E9,
      "VersionId":"EXAMPLE1-90ab-cdef-fedc-ba987SECRET1",
      "VersionStages":["AWSPREVIOUS"]
    },
    {
      "CreatedDate":1.523486221391E9,
      "VersionId":"EXAMPLE2-90ab-cdef-fedc-ba987SECRET2",
      "VersionStages":["AWSCURRENT"]
    },
    {
      "CreatedDate": 1.51197446236E9,
      "VersionId": "EXAMPLE3-90ab-cdef-fedc-ba987SECRET3"
    }
  ]
}
```

## See Also
<a name="API_ListSecretVersionIds_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/secretsmanager-2017-10-17/ListSecretVersionIds)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/secretsmanager-2017-10-17/ListSecretVersionIds)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/secretsmanager-2017-10-17/ListSecretVersionIds)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/secretsmanager-2017-10-17/ListSecretVersionIds)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/secretsmanager-2017-10-17/ListSecretVersionIds)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/secretsmanager-2017-10-17/ListSecretVersionIds)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/secretsmanager-2017-10-17/ListSecretVersionIds)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/secretsmanager-2017-10-17/ListSecretVersionIds)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/secretsmanager-2017-10-17/ListSecretVersionIds)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/secretsmanager-2017-10-17/ListSecretVersionIds)
