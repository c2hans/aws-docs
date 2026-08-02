---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_RemoveRegionsFromReplication.html
---

# RemoveRegionsFromReplication
<a name="API_RemoveRegionsFromReplication"></a>

For a secret that is replicated to other Regions, deletes the secret replicas from the Regions you specify.

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with AWS CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

 **Required permissions: ** `secretsmanager:RemoveRegionsFromReplication`. For more information, see [ IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Request Syntax
<a name="API_RemoveRegionsFromReplication_RequestSyntax"></a>

```
{
   "RemoveReplicaRegions": [ "{{string}}" ],
   "SecretId": "{{string}}"
}
```

## Request Parameters
<a name="API_RemoveRegionsFromReplication_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [RemoveReplicaRegions](#API_RemoveRegionsFromReplication_RequestSyntax) **   <a name="SecretsManager-RemoveRegionsFromReplication-request-RemoveReplicaRegions"></a>
The Regions of the replicas to remove.
Type: Array of strings
Array Members: Minimum number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([a-z]+-)+\d+$`
Required: Yes

 ** [SecretId](#API_RemoveRegionsFromReplication_RequestSyntax) **   <a name="SecretsManager-RemoveRegionsFromReplication-request-SecretId"></a>
The ARN or name of the secret.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_RemoveRegionsFromReplication_ResponseSyntax"></a>

```
{
   "ARN": "string",
   "ReplicationStatus": [
      {
         "KmsKeyId": "string",
         "LastAccessedDate": number,
         "Region": "string",
         "Status": "string",
         "StatusMessage": "string"
      }
   ]
}
```

## Response Elements
<a name="API_RemoveRegionsFromReplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ARN](#API_RemoveRegionsFromReplication_ResponseSyntax) **   <a name="SecretsManager-RemoveRegionsFromReplication-response-ARN"></a>
The ARN of the primary secret.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [ReplicationStatus](#API_RemoveRegionsFromReplication_ResponseSyntax) **   <a name="SecretsManager-RemoveRegionsFromReplication-response-ReplicationStatus"></a>
The status of replicas for this secret after you remove Regions.
Type: Array of [ReplicationStatusType](API_ReplicationStatusType.md) objects

## Errors
<a name="API_RemoveRegionsFromReplication_Errors"></a>

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

 ** ResourceNotFoundException **
Secrets Manager can't find the resource that you asked for.
HTTP Status Code: 400

## Examples
<a name="API_RemoveRegionsFromReplication_Examples"></a>

### Example
<a name="API_RemoveRegionsFromReplication_Example_1"></a>

The following example shows how to remove the replica secrets in Europe (London) and Europe (Paris) The JSON request string input and response output displays formatted code with white space and line breaks for better readability. Submit your input as a single line JSON string.

#### Sample Request
<a name="API_RemoveRegionsFromReplication_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: secretsmanager.region.domain
Accept-Encoding: identity
X-Amz-Target: secretsmanager.RemoveRegionsFromReplication
Content-Type: application/x-amz-json-1.1
User-Agent: <user-agent-string>
X-Amz-Date: <date>
Authorization: AWS4-HMAC-SHA256 Credential=<credentials>,SignedHeaders=<headers>, Signature=<signature>
Content-Length: <payload-size-bytes>

{
  "SecretId": "MyTestDatabaseSecret",
  "RemoveReplicaRegions": "eu-west-2 eu-west-3"
}
```

#### Sample Response
<a name="API_RemoveRegionsFromReplication_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: <date>
Content-Type: application/x-amz-json-1.1
Content-Length: <response-size-bytes>
Connection: keep-alive
x-amzn-RequestId: <request-id-guid>

{
  "ARN":"arn:aws:secretsmanager:us-west-2:123456789012:secret:MyTestDatabaseSecret-a1b2c3",
  "ReplicationStatus":[
      {
          "Region": "eu-west-1",
          "KmsKeyId": "alias/aws/secretsmanager",
          "Status": "InSync",
          "StatusMessage": "Replication succeeded"

      }
  ]
}
```

## See Also
<a name="API_RemoveRegionsFromReplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/secretsmanager-2017-10-17/RemoveRegionsFromReplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/secretsmanager-2017-10-17/RemoveRegionsFromReplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/secretsmanager-2017-10-17/RemoveRegionsFromReplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/secretsmanager-2017-10-17/RemoveRegionsFromReplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/secretsmanager-2017-10-17/RemoveRegionsFromReplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/secretsmanager-2017-10-17/RemoveRegionsFromReplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/secretsmanager-2017-10-17/RemoveRegionsFromReplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/secretsmanager-2017-10-17/RemoveRegionsFromReplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/secretsmanager-2017-10-17/RemoveRegionsFromReplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/secretsmanager-2017-10-17/RemoveRegionsFromReplication)
