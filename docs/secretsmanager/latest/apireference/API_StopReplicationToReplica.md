---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_StopReplicationToReplica.html
---

# StopReplicationToReplica
<a name="API_StopReplicationToReplica"></a>

Removes the link between the replica secret and the primary secret and promotes the replica to a primary secret in the replica Region.

You must call this operation from the Region in which you want to promote the replica to a primary secret.

Secrets Manager generates a CloudTrail log entry when you call this action. Do not include sensitive information in request parameters because it might be logged. For more information, see [Logging Secrets Manager events with AWS CloudTrail](https://docs.aws.amazon.com/secretsmanager/latest/userguide/retrieve-ct-entries.html).

 **Required permissions: ** `secretsmanager:StopReplicationToReplica`. For more information, see [ IAM policy actions for Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/reference_iam-permissions.html#reference_iam-permissions_actions) and [Authentication and access control in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/auth-and-access.html).

## Request Syntax
<a name="API_StopReplicationToReplica_RequestSyntax"></a>

```
{
   "SecretId": "{{string}}"
}
```

## Request Parameters
<a name="API_StopReplicationToReplica_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [SecretId](#API_StopReplicationToReplica_RequestSyntax) **   <a name="SecretsManager-StopReplicationToReplica-request-SecretId"></a>
The name of the secret or the replica ARN. The replica ARN is the same as the original primary secret ARN expect the Region is changed to the replica Region.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: Yes

## Response Syntax
<a name="API_StopReplicationToReplica_ResponseSyntax"></a>

```
{
   "ARN": "string"
}
```

## Response Elements
<a name="API_StopReplicationToReplica_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ARN](#API_StopReplicationToReplica_ResponseSyntax) **   <a name="SecretsManager-StopReplicationToReplica-response-ARN"></a>
The ARN of the promoted secret. The ARN is the same as the original primary secret except the Region is changed.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

## Errors
<a name="API_StopReplicationToReplica_Errors"></a>

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
<a name="API_StopReplicationToReplica_Examples"></a>

### Example
<a name="API_StopReplicationToReplica_Example_1"></a>

The following example is intended for a primary secret in `us-west-2` that has a replica in `ap-south-1`. The example removes the replica from the primary secret and promotes it to a primary secret in `ap-south-1`.

#### Sample Request
<a name="API_StopReplicationToReplica_Example_1_Request"></a>

```
POST / HTTP/1.1
Host: secretsmanager.region.domain
Accept-Encoding: identity
X-Amz-Target: secretsmanager.StopReplicationToReplica
Content-Type: application/x-amz-json-1.1
User-Agent: <user-agent-string>
X-Amz-Date: <date>
Authorization: AWS4-HMAC-SHA256 Credential=<credentials>,SignedHeaders=<headers>, Signature=<signature>
Content-Length: <payload-size-bytes>

        {
        "SecretId": "arn:aws:secretsmanager:us-west-2:123456789012:secret:MyExampleSecret-a1b2c3"
        }
```

#### Sample Response
<a name="API_StopReplicationToReplica_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Date: <date>
Content-Type: application/x-amz-json-1.1
Content-Length: <response-size-bytes>
Connection: keep-alive
x-amzn-RequestId: <request-id-guid>

       {
{
  "ARN":"arn:aws:secretsmanager:ap-south-1:123456789012:secret:MyExampleSecret-a1b2c3",
}
```

## See Also
<a name="API_StopReplicationToReplica_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/secretsmanager-2017-10-17/StopReplicationToReplica)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/secretsmanager-2017-10-17/StopReplicationToReplica)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/secretsmanager-2017-10-17/StopReplicationToReplica)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/secretsmanager-2017-10-17/StopReplicationToReplica)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/secretsmanager-2017-10-17/StopReplicationToReplica)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/secretsmanager-2017-10-17/StopReplicationToReplica)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/secretsmanager-2017-10-17/StopReplicationToReplica)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/secretsmanager-2017-10-17/StopReplicationToReplica)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/secretsmanager-2017-10-17/StopReplicationToReplica)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/secretsmanager-2017-10-17/StopReplicationToReplica)
