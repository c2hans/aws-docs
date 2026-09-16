---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_ListSecrets.html
---

# ListSecrets
<a name="API_ListSecrets"></a>

Lists the secrets that are stored by Secrets Manager in the AWS account, not including secrets that are marked for deletion. To see secrets marked for deletion, use the Secrets Manager console.

All Secrets Manager operations are eventually consistent. ListSecrets might not reflect changes from the last five minutes. You can get more recent information for a specific secret by calling [DescribeSecret](API_DescribeSecret.md).

To list the versions of a secret, use [ListSecretVersionIds](API_ListSecretVersionIds.md).

To retrieve the values for the secrets, call [BatchGetSecretValue](API_BatchGetSecretValue.md) or [GetSecretValue](API_GetSecretValue.md).

For information about finding secrets in the console, see [Find secrets in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_search-secret.html).

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with AWS CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

 **Required permissions: ** `secretsmanager:ListSecrets`. For more information, see [ IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Request Syntax
<a name="API_ListSecrets_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Key": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "IncludePlannedDeletion": {{boolean}},
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SortBy": "{{string}}",
   "SortOrder": "{{string}}"
}
```

## Request Parameters
<a name="API_ListSecrets_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListSecrets_RequestSyntax) **   <a name="SecretsManager-ListSecrets-request-Filters"></a>
The filters to apply to the list of secrets.
Type: Array of [Filter](API_Filter.md) objects
Array Members: Maximum number of 10 items.
Required: No

 ** [IncludePlannedDeletion](#API_ListSecrets_RequestSyntax) **   <a name="SecretsManager-ListSecrets-request-IncludePlannedDeletion"></a>
Specifies whether to include secrets scheduled for deletion. By default, secrets scheduled for deletion aren't included.
Type: Boolean
Required: No

 ** [MaxResults](#API_ListSecrets_RequestSyntax) **   <a name="SecretsManager-ListSecrets-request-MaxResults"></a>
The number of results to include in the response.
If there are more results available, in the response, Secrets Manager includes `NextToken`. To get the next results, call `ListSecrets` again with the value from `NextToken`.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListSecrets_RequestSyntax) **   <a name="SecretsManager-ListSecrets-request-NextToken"></a>
A token that indicates where the output should continue from, if a previous call did not show all results. To get the next results, call `ListSecrets` again with this value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [SortBy](#API_ListSecrets_RequestSyntax) **   <a name="SecretsManager-ListSecrets-request-SortBy"></a>
If not specified, secrets are listed by `CreatedDate`.
Type: String
Valid Values: `created-date | last-accessed-date | last-changed-date | name`
Required: No

 ** [SortOrder](#API_ListSecrets_RequestSyntax) **   <a name="SecretsManager-ListSecrets-request-SortOrder"></a>
Secrets are listed by `CreatedDate`.
Type: String
Valid Values: `asc | desc`
Required: No

## Response Syntax
<a name="API_ListSecrets_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "SecretList": [
      {
         "ARN": "string",
         "CreatedDate": number,
         "DeletedDate": number,
         "Description": "string",
         "ExternalSecretRotationMetadata": [
            {
               "Key": "string",
               "Value": "string"
            }
         ],
         "ExternalSecretRotationRoleArn": "string",
         "KmsKeyId": "string",
         "LastAccessedDate": number,
         "LastChangedDate": number,
         "LastRotatedDate": number,
         "Name": "string",
         "NextRotationDate": number,
         "OwningService": "string",
         "PrimaryRegion": "string",
         "RotationEnabled": boolean,
         "RotationLambdaARN": "string",
         "RotationRules": {
            "AutomaticallyAfterDays": number,
            "Duration": "string",
            "ScheduleExpression": "string"
         },
         "SecretVersionsToStages": {
            "string" : [ "string" ]
         },
         "Tags": [
            {
               "Key": "string",
               "Value": "string"
            }
         ],
         "Type": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListSecrets_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListSecrets_ResponseSyntax) **   <a name="SecretsManager-ListSecrets-response-NextToken"></a>
Secrets Manager includes this value if there's more output available than what is included in the current response. This can occur even when the response includes no values at all, such as when you ask for a filtered view of a long list. To get the next results, call `ListSecrets` again with this value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [SecretList](#API_ListSecrets_ResponseSyntax) **   <a name="SecretsManager-ListSecrets-response-SecretList"></a>
A list of the secrets in the account.
Type: Array of [SecretListEntry](API_SecretListEntry.md) objects

## Errors
<a name="API_ListSecrets_Errors"></a>

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

 ** InvalidRequestException **
A parameter value is not valid for the current state of the resource.
Possible causes:
+ The secret is scheduled for deletion.
+ You tried to enable rotation on a secret that doesn't already have a Lambda function ARN configured and you didn't include such an ARN as a parameter in this call.
+ The secret is managed by another service, and you must use that service to update it. For more information, see [Secrets managed by other AWS services](https://docs.aws.amazon.com/secretsmanager/latest/userguide/service-linked-secrets.html).
HTTP Status Code: 400

## Examples
<a name="API_ListSecrets_Examples"></a>

### Example
<a name="API_ListSecrets_Example_1"></a>

The following example shows how to list the secrets in the account. The JSON request string input and response output displays formatted code with white space and line breaks for better readability. Submit your input as a single line JSON string.

#### Sample Request
<a name="API_ListSecrets_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: secretsmanager.region.domain
Accept-Encoding: identity
X-Amz-Target: secretsmanager.ListSecrets
Content-Type: application/x-amz-json-1.1
User-Agent: <user-agent-string>
X-Amz-Date: <date>
Authorization: AWS4-HMAC-SHA256 Credential=<credentials>,SignedHeaders=<headers>, Signature=<signature>
Content-Length: <payload-size-bytes>

{}
```

#### Sample Response
<a name="API_ListSecrets_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: <date>
Content-Type: application/x-amz-json-1.1
Content-Length: <response-size-bytes>
Connection: keep-alive
x-amzn-RequestId: <request-id-guid>

{
  "SecretList":[
    {
      "ARN":"arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3",
      "Description":"My test database secret",
      "LastChangedDate":1.523477145729E9,
      "Name":"MyTestDatabaseSecret",
      "SecretVersionsToStages":{
        "EXAMPLE2-90ab-cdef-fedc-ba987EXAMPLE":["AWSCURRENT"]
      }
    },
    {
      "ARN":"arn:aws:secretsmanager:us-west-2:123456789012:secret:AnotherDatabaseSecret-d4e5f6",
      "Description":"Another secret created for a different database",
      "LastChangedDate":1.523482025685E9,
      "Name":"AnotherDatabaseSecret",
      "SecretVersionsToStages":{
        "EXAMPLE3-90ab-cdef-fedc-ba987EXAMPLE":["AWSCURRENT"]
      }
    }
  ]
}
```

### Example
<a name="API_ListSecrets_Example_2"></a>

The following example shows how to list the secrets in the account that are tagged with `costcenter 12345`. The JSON request string input and response output displays formatted code with white space and line breaks for better readability. Submit your input as a single line JSON string.

#### Sample Request
<a name="API_ListSecrets_Example_2_Request"></a>

```
POST / HTTP/1.1
Host: secretsmanager.region.domain
Accept-Encoding: identity
X-Amz-Target: secretsmanager.ListSecrets
&Filter.1.Name=costcenter
&Filter.1.Value.1=12345
Content-Type: application/x-amz-json-1.1
User-Agent: <user-agent-string>
X-Amz-Date: <date>
Authorization: AWS4-HMAC-SHA256 Credential=<credentials>,SignedHeaders=<headers>, Signature=<signature>
Content-Length: <payload-size-bytes>

{}
```

#### Sample Response
<a name="API_ListSecrets_Example_2_Response"></a>

```
HTTP/1.1 200 OK
Date: <date>
Content-Type: application/x-amz-json-1.1
Content-Length: <response-size-bytes>
Connection: keep-alive
x-amzn-RequestId: <request-id-guid>

{
  "SecretList":[
    {
      "ARN":"arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3",
      "Description":"My test database secret",
      "LastChangedDate":1.523477145729E9,
      "Name":"MyTestDatabaseSecret",
      "SecretVersionsToStages":{
        "EXAMPLE2-90ab-cdef-fedc-ba987EXAMPLE":["AWSCURRENT"]
      }
    },
    {
      "ARN":"arn:aws:secretsmanager:us-west-2:123456789012:secret:AnotherDatabaseSecret-d4e5f6",
      "Description":"Another secret created for a different database",
      "LastChangedDate":1.523482025685E9,
      "Name":"AnotherDatabaseSecret",
      "SecretVersionsToStages":{
        "EXAMPLE3-90ab-cdef-fedc-ba987EXAMPLE":["AWSCURRENT"]
      }
    }
  ]
}
```

## See Also
<a name="API_ListSecrets_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/secretsmanager-2017-10-17/ListSecrets)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/secretsmanager-2017-10-17/ListSecrets)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/secretsmanager-2017-10-17/ListSecrets)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/secretsmanager-2017-10-17/ListSecrets)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/secretsmanager-2017-10-17/ListSecrets)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/secretsmanager-2017-10-17/ListSecrets)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/secretsmanager-2017-10-17/ListSecrets)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/secretsmanager-2017-10-17/ListSecrets)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/secretsmanager-2017-10-17/ListSecrets)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/secretsmanager-2017-10-17/ListSecrets)
