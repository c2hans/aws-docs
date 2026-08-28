---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_UpdateConnector.html
---

# UpdateConnector
<a name="API_UpdateConnector"></a>

Updates some of the parameters for an existing connector. Provide the `ConnectorId` for the connector that you want to update, along with the new values for the parameters to update.

## Request Syntax
<a name="API_UpdateConnector_RequestSyntax"></a>

```
{
   "AccessRole": "{{string}}",
   "As2Config": {
      "AsyncMdnConfig": {
         "ServerIds": [ "{{string}}" ],
         "Url": "{{string}}"
      },
      "BasicAuthSecretId": "{{string}}",
      "Compression": "{{string}}",
      "EncryptionAlgorithm": "{{string}}",
      "LocalProfileId": "{{string}}",
      "MdnResponse": "{{string}}",
      "MdnSigningAlgorithm": "{{string}}",
      "MessageSubject": "{{string}}",
      "PartnerProfileId": "{{string}}",
      "PreserveContentType": "{{string}}",
      "SigningAlgorithm": "{{string}}"
   },
   "ConnectorId": "{{string}}",
   "EgressConfig": { ... },
   "IpAddressType": "{{string}}",
   "LoggingRole": "{{string}}",
   "SecurityPolicyName": "{{string}}",
   "SftpConfig": {
      "MaxConcurrentConnections": {{number}},
      "TrustedHostKeys": [ "{{string}}" ],
      "UserSecretId": "{{string}}"
   },
   "Url": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateConnector_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AccessRole](#API_UpdateConnector_RequestSyntax) **   <a name="TransferFamily-UpdateConnector-request-AccessRole"></a>
Connectors are used to send files using either the AS2 or SFTP protocol. For the access role, provide the Amazon Resource Name (ARN) of the AWS Identity and Access Management role to use.
 **For AS2 connectors**
With AS2, you can send files by calling `StartFileTransfer` and specifying the file paths in the request parameter, `SendFilePaths`. We use the file’s parent directory (for example, for `--send-file-paths /bucket/dir/file.txt`, parent directory is `/bucket/dir/`) to temporarily store a processed AS2 message file, store the MDN when we receive them from the partner, and write a final JSON file containing relevant metadata of the transmission. So, the `AccessRole` needs to provide read and write access to the parent directory of the file location used in the `StartFileTransfer` request. Additionally, you need to provide read and write access to the parent directory of the files that you intend to send with `StartFileTransfer`.
If you are using Basic authentication for your AS2 connector, the access role requires the `secretsmanager:GetSecretValue` permission for the secret. If the secret is encrypted using a customer-managed key instead of the AWS managed key in Secrets Manager, then the role also needs the `kms:Decrypt` permission for that key.
 **For SFTP connectors**
Make sure that the access role provides read and write access to the parent directory of the file location that's used in the `StartFileTransfer` request. Additionally, make sure that the role provides `secretsmanager:GetSecretValue` permission to AWS Secrets Manager.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*role/\S+`
Required: No

 ** [As2Config](#API_UpdateConnector_RequestSyntax) **   <a name="TransferFamily-UpdateConnector-request-As2Config"></a>
A structure that contains the parameters for an AS2 connector object.
Type: [As2ConnectorConfig](API_As2ConnectorConfig.md) object
Required: No

 ** [ConnectorId](#API_UpdateConnector_RequestSyntax) **   <a name="TransferFamily-UpdateConnector-request-ConnectorId"></a>
The unique identifier for the connector.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `c-([0-9a-f]{17})`
Required: Yes

 ** [EgressConfig](#API_UpdateConnector_RequestSyntax) **   <a name="TransferFamily-UpdateConnector-request-EgressConfig"></a>
Updates the egress configuration for the connector, allowing you to modify how traffic is routed from the connector to the SFTP server. Changes to VPC configuration may require connector restart.
Type: [UpdateConnectorEgressConfig](API_UpdateConnectorEgressConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [IpAddressType](#API_UpdateConnector_RequestSyntax) **   <a name="TransferFamily-UpdateConnector-request-IpAddressType"></a>
Specifies the IP address type for the connector's network connections. When set to `IPV4`, the connector uses IPv4 addresses only. When set to `DUALSTACK`, the connector supports both IPv4 and IPv6 addresses, with IPv6 preferred when available.
Type: String
Valid Values: `IPV4 | DUALSTACK`
Required: No

 ** [LoggingRole](#API_UpdateConnector_RequestSyntax) **   <a name="TransferFamily-UpdateConnector-request-LoggingRole"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows a connector to turn on CloudWatch logging for Amazon S3 events. When set, you can view connector activity in your CloudWatch logs.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*role/\S+`
Required: No

 ** [SecurityPolicyName](#API_UpdateConnector_RequestSyntax) **   <a name="TransferFamily-UpdateConnector-request-SecurityPolicyName"></a>
Specifies the name of the security policy for the connector.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `TransferSFTPConnectorSecurityPolicy-[A-Za-z0-9-]+`
Required: No

 ** [SftpConfig](#API_UpdateConnector_RequestSyntax) **   <a name="TransferFamily-UpdateConnector-request-SftpConfig"></a>
A structure that contains the parameters for an SFTP connector object.
Type: [SftpConnectorConfig](API_SftpConnectorConfig.md) object
Required: No

 ** [Url](#API_UpdateConnector_RequestSyntax) **   <a name="TransferFamily-UpdateConnector-request-Url"></a>
The URL of the partner's AS2 or SFTP endpoint.
When creating AS2 connectors or service-managed SFTP connectors (connectors without egress configuration), you must provide a URL to specify the remote server endpoint. For VPC Lattice type connectors, the URL must be null.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

## Response Syntax
<a name="API_UpdateConnector_ResponseSyntax"></a>

```
{
   "ConnectorId": "string"
}
```

## Response Elements
<a name="API_UpdateConnector_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConnectorId](#API_UpdateConnector_ResponseSyntax) **   <a name="TransferFamily-UpdateConnector-response-ConnectorId"></a>
Returns the identifier of the connector object that you are updating.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `c-([0-9a-f]{17})`

## Errors
<a name="API_UpdateConnector_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceError **
This exception is thrown when an error occurs in the AWS Transfer Family service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

 ** ResourceExistsException **
The requested resource does not exist, or exists in a region other than the one specified for the command.
HTTP Status Code: 400

 ** ResourceNotFoundException **
This exception is thrown when a resource is not found by the AWSTransfer Family service.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The request has failed because the AWSTransfer Family service is not available.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

## See Also
<a name="API_UpdateConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transfer-2018-11-05/UpdateConnector)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transfer-2018-11-05/UpdateConnector)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/UpdateConnector)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transfer-2018-11-05/UpdateConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/UpdateConnector)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transfer-2018-11-05/UpdateConnector)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transfer-2018-11-05/UpdateConnector)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transfer-2018-11-05/UpdateConnector)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transfer-2018-11-05/UpdateConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/UpdateConnector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
