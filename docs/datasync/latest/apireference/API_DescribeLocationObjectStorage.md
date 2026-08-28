---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_DescribeLocationObjectStorage.html
---

# DescribeLocationObjectStorage
<a name="API_DescribeLocationObjectStorage"></a>

Provides details about how an AWS DataSync transfer location for an object storage system is configured.

## Request Syntax
<a name="API_DescribeLocationObjectStorage_RequestSyntax"></a>

```
{
   "LocationArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeLocationObjectStorage_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [LocationArn](#API_DescribeLocationObjectStorage_RequestSyntax) **   <a name="DataSync-DescribeLocationObjectStorage-request-LocationArn"></a>
Specifies the Amazon Resource Name (ARN) of the object storage system location.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`
Required: Yes

## Response Syntax
<a name="API_DescribeLocationObjectStorage_ResponseSyntax"></a>

```
{
   "AccessKey": "string",
   "AgentArns": [ "string" ],
   "CmkSecretConfig": {
      "KmsKeyArn": "string",
      "SecretArn": "string"
   },
   "CreationTime": number,
   "CustomSecretConfig": {
      "SecretAccessRoleArn": "string",
      "SecretArn": "string"
   },
   "LocationArn": "string",
   "LocationUri": "string",
   "ManagedSecretConfig": {
      "SecretArn": "string"
   },
   "ServerCertificate": blob,
   "ServerPort": number,
   "ServerProtocol": "string"
}
```

## Response Elements
<a name="API_DescribeLocationObjectStorage_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AccessKey](#API_DescribeLocationObjectStorage_ResponseSyntax) **   <a name="DataSync-DescribeLocationObjectStorage-response-AccessKey"></a>
The access key (for example, a user name) required to authenticate with the object storage system.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 200.
Pattern: `^.*$`

 ** [AgentArns](#API_DescribeLocationObjectStorage_ResponseSyntax) **   <a name="DataSync-DescribeLocationObjectStorage-response-AgentArns"></a>
The ARNs of the DataSync agents that can connect with your object storage system.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 8 items.
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$`

 ** [CmkSecretConfig](#API_DescribeLocationObjectStorage_ResponseSyntax) **   <a name="DataSync-DescribeLocationObjectStorage-response-CmkSecretConfig"></a>
Describes configuration information for a DataSync-managed secret, such as an authentication token or set of credentials that DataSync uses to access a specific transfer location, and a customer-managed AWS KMS key.
Type: [CmkSecretConfig](API_CmkSecretConfig.md) object

 ** [CreationTime](#API_DescribeLocationObjectStorage_ResponseSyntax) **   <a name="DataSync-DescribeLocationObjectStorage-response-CreationTime"></a>
The time that the location was created.
Type: Timestamp

 ** [CustomSecretConfig](#API_DescribeLocationObjectStorage_ResponseSyntax) **   <a name="DataSync-DescribeLocationObjectStorage-response-CustomSecretConfig"></a>
Describes configuration information for a customer-managed secret, such as an authentication token or set of credentials that DataSync uses to access a specific transfer location, and a customer-managed AWS Identity and Access Management (IAM) role that provides access to the secret.
Type: [CustomSecretConfig](API_CustomSecretConfig.md) object

 ** [LocationArn](#API_DescribeLocationObjectStorage_ResponseSyntax) **   <a name="DataSync-DescribeLocationObjectStorage-response-LocationArn"></a>
The ARN of the object storage system location.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`

 ** [LocationUri](#API_DescribeLocationObjectStorage_ResponseSyntax) **   <a name="DataSync-DescribeLocationObjectStorage-response-LocationUri"></a>
The URI of the object storage system location.
Type: String
Length Constraints: Maximum length of 4360.
Pattern: `^(efs|nfs|s3|smb|hdfs|fsx[a-z0-9-]+)://[a-zA-Z0-9.:/\-]+$`

 ** [ManagedSecretConfig](#API_DescribeLocationObjectStorage_ResponseSyntax) **   <a name="DataSync-DescribeLocationObjectStorage-response-ManagedSecretConfig"></a>
Describes configuration information for a DataSync-managed secret, such as an authentication token or set of credentials that DataSync uses to access a specific transfer location. DataSync uses the default AWS-managed KMS key to encrypt this secret in AWS Secrets Manager.
Type: [ManagedSecretConfig](API_ManagedSecretConfig.md) object

 ** [ServerCertificate](#API_DescribeLocationObjectStorage_ResponseSyntax) **   <a name="DataSync-DescribeLocationObjectStorage-response-ServerCertificate"></a>
The certificate chain for DataSync to authenticate with your object storage system if the system uses a private or self-signed certificate authority (CA).
Type: Base64-encoded binary data object
Length Constraints: Maximum length of 32768.

 ** [ServerPort](#API_DescribeLocationObjectStorage_ResponseSyntax) **   <a name="DataSync-DescribeLocationObjectStorage-response-ServerPort"></a>
The port that your object storage server accepts inbound network traffic on (for example, port 443).
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65536.

 ** [ServerProtocol](#API_DescribeLocationObjectStorage_ResponseSyntax) **   <a name="DataSync-DescribeLocationObjectStorage-response-ServerProtocol"></a>
The protocol that your object storage system uses to communicate.
Type: String
Valid Values: `HTTPS | HTTP`

## Errors
<a name="API_DescribeLocationObjectStorage_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception is thrown when an error occurs in the AWS DataSync service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

## See Also
<a name="API_DescribeLocationObjectStorage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datasync-2018-11-09/DescribeLocationObjectStorage)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datasync-2018-11-09/DescribeLocationObjectStorage)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/DescribeLocationObjectStorage)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datasync-2018-11-09/DescribeLocationObjectStorage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/DescribeLocationObjectStorage)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datasync-2018-11-09/DescribeLocationObjectStorage)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datasync-2018-11-09/DescribeLocationObjectStorage)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datasync-2018-11-09/DescribeLocationObjectStorage)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datasync-2018-11-09/DescribeLocationObjectStorage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/DescribeLocationObjectStorage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
