---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_DescribedConnector.html
---

# DescribedConnector
<a name="API_DescribedConnector"></a>

Describes the parameters for the connector, as identified by the `ConnectorId`.

## Contents
<a name="API_DescribedConnector_Contents"></a>

 ** Arn **   <a name="TransferFamily-Type-DescribedConnector-Arn"></a>
The unique Amazon Resource Name (ARN) for the connector.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1600.
Pattern: `arn:\S+`
Required: Yes

 ** EgressType **   <a name="TransferFamily-Type-DescribedConnector-EgressType"></a>
Type of egress configuration for the connector. SERVICE\_MANAGED uses Transfer Family managed NAT gateways, while VPC\_LATTICE routes traffic through customer VPCs using VPC Lattice.
Type: String
Valid Values: `SERVICE_MANAGED | VPC_LATTICE`
Required: Yes

 ** Status **   <a name="TransferFamily-Type-DescribedConnector-Status"></a>
Current status of the connector. PENDING indicates creation/update in progress, ACTIVE means ready for operations, and ERRORED indicates a failure requiring attention.
Type: String
Valid Values: `ACTIVE | ERRORED | PENDING`
Required: Yes

 ** AccessRole **   <a name="TransferFamily-Type-DescribedConnector-AccessRole"></a>
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

 ** As2Config **   <a name="TransferFamily-Type-DescribedConnector-As2Config"></a>
A structure that contains the parameters for an AS2 connector object.
Type: [As2ConnectorConfig](API_As2ConnectorConfig.md) object
Required: No

 ** ConnectorId **   <a name="TransferFamily-Type-DescribedConnector-ConnectorId"></a>
The unique identifier for the connector.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `c-([0-9a-f]{17})`
Required: No

 ** EgressConfig **   <a name="TransferFamily-Type-DescribedConnector-EgressConfig"></a>
Current egress configuration of the connector, showing how traffic is routed to the SFTP server. Contains VPC Lattice settings when using VPC\_LATTICE egress type.
When using the VPC\_LATTICE egress type, AWS Transfer Family uses a managed Service Network to simplify the resource sharing process.
Type: [DescribedConnectorEgressConfig](API_DescribedConnectorEgressConfig.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** ErrorMessage **   <a name="TransferFamily-Type-DescribedConnector-ErrorMessage"></a>
Error message providing details when the connector is in ERRORED status. Contains information to help troubleshoot connector creation or operation failures.
Type: String
Required: No

 ** IpAddressType **   <a name="TransferFamily-Type-DescribedConnector-IpAddressType"></a>
IP address type for the connector's network connections. When set to `IPV4`, the connector uses IPv4 addresses only. When set to `DUALSTACK`, the connector supports both IPv4 and IPv6 addresses, with IPv6 preferred when available.
Type: String
Valid Values: `IPV4 | DUALSTACK`
Required: No

 ** LoggingRole **   <a name="TransferFamily-Type-DescribedConnector-LoggingRole"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows a connector to turn on CloudWatch logging for Amazon S3 events. When set, you can view connector activity in your CloudWatch logs.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:.*role/\S+`
Required: No

 ** SecurityPolicyName **   <a name="TransferFamily-Type-DescribedConnector-SecurityPolicyName"></a>
The text name of the security policy for the specified connector.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `TransferSFTPConnectorSecurityPolicy-[A-Za-z0-9-]+`
Required: No

 ** ServiceManagedEgressIpAddresses **   <a name="TransferFamily-Type-DescribedConnector-ServiceManagedEgressIpAddresses"></a>
The list of egress IP addresses of this connector. These IP addresses are assigned automatically when you create the connector.
Type: Array of strings
Pattern: `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`
Required: No

 ** SftpConfig **   <a name="TransferFamily-Type-DescribedConnector-SftpConfig"></a>
A structure that contains the parameters for an SFTP connector object.
Type: [SftpConnectorConfig](API_SftpConnectorConfig.md) object
Required: No

 ** Tags **   <a name="TransferFamily-Type-DescribedConnector-Tags"></a>
Key-value pairs that can be used to group and search for connectors.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Required: No

 ** Url **   <a name="TransferFamily-Type-DescribedConnector-Url"></a>
The URL of the partner's AS2 or SFTP endpoint.
When creating AS2 connectors or service-managed SFTP connectors (connectors without egress configuration), you must provide a URL to specify the remote server endpoint. For VPC Lattice type connectors, the URL must be null.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Required: No

## See Also
<a name="API_DescribedConnector_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/DescribedConnector)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/DescribedConnector)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/DescribedConnector)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
