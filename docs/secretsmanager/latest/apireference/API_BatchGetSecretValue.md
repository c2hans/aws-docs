---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_BatchGetSecretValue.html
---

# BatchGetSecretValue
<a name="API_BatchGetSecretValue"></a>

Retrieves the contents of the encrypted fields `SecretString` or `SecretBinary` for up to 20 secrets. To retrieve a single secret, call [GetSecretValue](API_GetSecretValue.md).

To choose which secrets to retrieve, you can specify a list of secrets by name or ARN, or you can use filters. If Secrets Manager encounters errors such as `AccessDeniedException` while attempting to retrieve any of the secrets, you can see the errors in `Errors` in the response.

Secrets Manager generates CloudTrail `GetSecretValue` log entries for each secret you request when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with AWS CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

 **Required permissions: ** `secretsmanager:BatchGetSecretValue`, and you must have `secretsmanager:GetSecretValue` for each secret. If you use filters, you must also have `secretsmanager:ListSecrets`. If the secrets are encrypted using customer-managed keys instead of the AWS managed key `aws/secretsmanager`, then you also need `kms:Decrypt` permissions for the keys. For more information, see [ IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Request Syntax
<a name="API_BatchGetSecretValue_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Key": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SecretIdList": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_BatchGetSecretValue_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_BatchGetSecretValue_RequestSyntax) **   <a name="SecretsManager-BatchGetSecretValue-request-Filters"></a>
The filters to choose which secrets to retrieve. You must include `Filters` or `SecretIdList`, but not both.
Type: Array of [Filter](API_Filter.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** [MaxResults](#API_BatchGetSecretValue_RequestSyntax) **   <a name="SecretsManager-BatchGetSecretValue-request-MaxResults"></a>
The number of results to include in the response.
If there are more results available, in the response, Secrets Manager includes `NextToken`. To get the next results, call `BatchGetSecretValue` again with the value from `NextToken`. To use this parameter, you must also use the `Filters` parameter.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 20.
Required: No

 ** [NextToken](#API_BatchGetSecretValue_RequestSyntax) **   <a name="SecretsManager-BatchGetSecretValue-request-NextToken"></a>
A token that indicates where the output should continue from, if a previous call did not show all results. To get the next results, call `BatchGetSecretValue` again with this value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [SecretIdList](#API_BatchGetSecretValue_RequestSyntax) **   <a name="SecretsManager-BatchGetSecretValue-request-SecretIdList"></a>
The ARN or names of the secrets to retrieve. You must include `Filters` or `SecretIdList`, but not both.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 20 items.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_BatchGetSecretValue_ResponseSyntax"></a>

```
{
   "Errors": [
      {
         "ErrorCode": "string",
         "Message": "string",
         "SecretId": "string"
      }
   ],
   "NextToken": "string",
   "SecretValues": [
      {
         "ARN": "string",
         "CreatedDate": number,
         "Name": "string",
         "SecretBinary": blob,
         "SecretString": "string",
         "VersionId": "string",
         "VersionStages": [ "string" ]
      }
   ]
}
```

## Response Elements
<a name="API_BatchGetSecretValue_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Errors](#API_BatchGetSecretValue_ResponseSyntax) **   <a name="SecretsManager-BatchGetSecretValue-response-Errors"></a>
A list of errors Secrets Manager encountered while attempting to retrieve individual secrets.
Type: Array of [APIErrorType](API_APIErrorType.md) objects

 ** [NextToken](#API_BatchGetSecretValue_ResponseSyntax) **   <a name="SecretsManager-BatchGetSecretValue-response-NextToken"></a>
Secrets Manager includes this value if there's more output available than what is included in the current response. This can occur even when the response includes no values at all, such as when you ask for a filtered view of a long list. To get the next results, call `BatchGetSecretValue` again with this value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [SecretValues](#API_BatchGetSecretValue_ResponseSyntax) **   <a name="SecretsManager-BatchGetSecretValue-response-SecretValues"></a>
A list of secret values.
Type: Array of [SecretValueEntry](API_SecretValueEntry.md) objects

## Errors
<a name="API_BatchGetSecretValue_Errors"></a>

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md).

 ** DecryptionFailure **
Secrets Manager can't decrypt the protected secret text using the provided KMS key.
HTTP Status Code: 400

 ** InternalServiceError **
An error occurred on the server side.
HTTP Status Code: 500

 ** InvalidNextTokenException **
The `NextToken` value is invalid.
HTTP Status Code: 400

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

 ** ResourceNotFoundException **
Secrets Manager can't find the resource that you asked for.
HTTP Status Code: 400

## Examples
<a name="API_BatchGetSecretValue_Examples"></a>

### Example
<a name="API_BatchGetSecretValue_Example_1"></a>

The following example shows how to retrieve the secret values for a group of secrets listed by name. The JSON request string input and response output displays formatted code with white space and line breaks for better readability. Submit your input as a single line JSON string.

#### Sample Request
<a name="API_BatchGetSecretValue_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: secretsmanager.region.domain
Accept-Encoding: identity
X-Amz-Target: secretsmanager.BatchGetSecretValue
Content-Type: application/x-amz-json-1.1
User-Agent: <user-agent-string>
X-Amz-Date: <date>
Authorization: AWS4-HMAC-SHA256 Credential=<credentials>,SignedHeaders=<headers>, Signature=<signature>
Content-Length: <payload-size-bytes>

{
  "SecretIdList": ["MySecret1", "MySecret2", "MySecret3"]
}
```

#### Sample Response
<a name="API_BatchGetSecretValue_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: <date>
Content-Type: application/x-amz-json-1.1
Content-Length: <response-size-bytes>
Connection: keep-alive
x-amzn-RequestId: <request-id-guid>

  {
    "Errors":[],
    "SecretValues":
      [
        {
          "ARN":"arn:aws:secretsmanager:us-west-2:123456789012:secret:MySecret1-a1b2c3",
          "CreatedDate":1.700591229801E9,
          "Name":"MySecret1",
          "SecretString":"{\"username\":\"diego_ramirez\",\"password\":\"EXAMPLE-PASSWORD\",\"engine\":\"mysql\",\"host\":\"secretsmanagertutorial.cluster.us-west-2.rds.amazonaws.com\",\"port\":3306,\"dbClusterIdentifier\":\"secretsmanagertutorial\"}",
          "VersionId":"a1b2c3d4-5678-90ab-cdef-EXAMPLEaaaaa",
          "VersionStages": ["AWSCURRENT"]
        },
        {
          "ARN":"arn:aws:secretsmanager:us-west-2:123456789012:secret:MySecret2-a1b2c3",
          "CreatedDate":1.699911394105E9,
          "Name":"MySecret2",
          "SecretString":"{\"username\":\"akua_mansa\",\"password\":\"EXAMPLE-PASSWORD\"",
          "VersionId":"a1b2c3d4-5678-90ab-cdef-EXAMPLEbbbbb",
          "VersionStages":["AWSCURRENT"]
        },
        {
          "ARN":"arn:aws:secretsmanager:us-west-2:123456789012:secret:MySecret3-a1b2c3",
          "CreatedDate":1.699911394105E9,
          "Name":"MySecret3",
          "SecretString":"{\"username\":\"jie_liu\",\"password\":\"EXAMPLE-PASSWORD\"",
          "VersionId":"a1b2c3d4-5678-90ab-cdef-EXAMPLEccccc",
          "VersionStages":["AWSCURRENT"]
        }
      ]
    }
```

## See Also
<a name="API_BatchGetSecretValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/secretsmanager-2017-10-17/BatchGetSecretValue)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/secretsmanager-2017-10-17/BatchGetSecretValue)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/secretsmanager-2017-10-17/BatchGetSecretValue)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/secretsmanager-2017-10-17/BatchGetSecretValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/secretsmanager-2017-10-17/BatchGetSecretValue)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/secretsmanager-2017-10-17/BatchGetSecretValue)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/secretsmanager-2017-10-17/BatchGetSecretValue)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/secretsmanager-2017-10-17/BatchGetSecretValue)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/secretsmanager-2017-10-17/BatchGetSecretValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/secretsmanager-2017-10-17/BatchGetSecretValue)
