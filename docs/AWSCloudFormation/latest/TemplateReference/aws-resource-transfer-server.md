---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-transfer-server.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Transfer::Server
<a name="aws-resource-transfer-server"></a>

Instantiates an auto-scaling virtual server based on the selected file transfer protocol in AWS. When you make updates to your file transfer protocol-enabled server or when you work with users, use the service-generated `ServerId` property that is assigned to the newly created server.

## Syntax
<a name="aws-resource-transfer-server-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-transfer-server-syntax.json"></a>

```
{
  "Type" : "AWS::Transfer::Server",
  "Properties" : {
      "[Certificate](#cfn-transfer-server-certificate)" : {{String}},
      "[Domain](#cfn-transfer-server-domain)" : {{String}},
      "[EndpointDetails](#cfn-transfer-server-endpointdetails)" : {{EndpointDetails}},
      "[EndpointType](#cfn-transfer-server-endpointtype)" : {{String}},
      "[IdentityProviderDetails](#cfn-transfer-server-identityproviderdetails)" : {{IdentityProviderDetails}},
      "[IdentityProviderType](#cfn-transfer-server-identityprovidertype)" : {{String}},
      "[IpAddressType](#cfn-transfer-server-ipaddresstype)" : {{String}},
      "[LoggingRole](#cfn-transfer-server-loggingrole)" : {{String}},
      "[PostAuthenticationLoginBanner](#cfn-transfer-server-postauthenticationloginbanner)" : {{String}},
      "[PreAuthenticationLoginBanner](#cfn-transfer-server-preauthenticationloginbanner)" : {{String}},
      "[ProtocolDetails](#cfn-transfer-server-protocoldetails)" : {{ProtocolDetails}},
      "[Protocols](#cfn-transfer-server-protocols)" : {{[ String, ... ]}},
      "[S3StorageOptions](#cfn-transfer-server-s3storageoptions)" : {{S3StorageOptions}},
      "[SecurityPolicyName](#cfn-transfer-server-securitypolicyname)" : {{String}},
      "[StructuredLogDestinations](#cfn-transfer-server-structuredlogdestinations)" : {{[ String, ... ]}},
      "[Tags](#cfn-transfer-server-tags)" : {{[ Tag, ... ]}},
      "[WorkflowDetails](#cfn-transfer-server-workflowdetails)" : {{WorkflowDetails}}
    }
}
```

### YAML
<a name="aws-resource-transfer-server-syntax.yaml"></a>

```
Type: AWS::Transfer::Server
Properties:
  [Certificate](#cfn-transfer-server-certificate): {{String}}
  [Domain](#cfn-transfer-server-domain): {{String}}
  [EndpointDetails](#cfn-transfer-server-endpointdetails): {{
    EndpointDetails}}
  [EndpointType](#cfn-transfer-server-endpointtype): {{String}}
  [IdentityProviderDetails](#cfn-transfer-server-identityproviderdetails): {{
    IdentityProviderDetails}}
  [IdentityProviderType](#cfn-transfer-server-identityprovidertype): {{String}}
  [IpAddressType](#cfn-transfer-server-ipaddresstype): {{String}}
  [LoggingRole](#cfn-transfer-server-loggingrole): {{String}}
  [PostAuthenticationLoginBanner](#cfn-transfer-server-postauthenticationloginbanner): {{String}}
  [PreAuthenticationLoginBanner](#cfn-transfer-server-preauthenticationloginbanner): {{String}}
  [ProtocolDetails](#cfn-transfer-server-protocoldetails): {{
    ProtocolDetails}}
  [Protocols](#cfn-transfer-server-protocols): {{
    - String}}
  [S3StorageOptions](#cfn-transfer-server-s3storageoptions): {{
    S3StorageOptions}}
  [SecurityPolicyName](#cfn-transfer-server-securitypolicyname): {{String}}
  [StructuredLogDestinations](#cfn-transfer-server-structuredlogdestinations): {{
    - String}}
  [Tags](#cfn-transfer-server-tags): {{
    - Tag}}
  [WorkflowDetails](#cfn-transfer-server-workflowdetails): {{
    WorkflowDetails}}
```

## Properties
<a name="aws-resource-transfer-server-properties"></a>

`Certificate`  <a name="cfn-transfer-server-certificate"></a>
The Amazon Resource Name (ARN) of the AWS Certificate Manager (ACM) certificate. Required when `Protocols` is set to `FTPS`.
To request a new public certificate, see [Request a public certificate](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html) in the *AWS Certificate Manager User Guide*.
To import an existing certificate into ACM, see [Importing certificates into ACM](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the *AWS Certificate Manager User Guide*.
To request a private certificate to use FTPS through private IP addresses, see [Request a private certificate](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-private.html) in the *AWS Certificate Manager User Guide*.
Certificates with the following cryptographic algorithms and key sizes are supported:
+ 2048-bit RSA (RSA\_2048)
+ 4096-bit RSA (RSA\_4096)
+ Elliptic Prime Curve 256 bit (EC\_prime256v1)
+ Elliptic Prime Curve 384 bit (EC\_secp384r1)
+ Elliptic Prime Curve 521 bit (EC\_secp521r1)
The certificate must be a valid SSL/TLS X.509 version 3 certificate with FQDN or IP address specified and information about the issuer.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1600`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Domain`  <a name="cfn-transfer-server-domain"></a>
Specifies the domain of the storage system that is used for file transfers. There are two domains available: Amazon Simple Storage Service (Amazon S3) and Amazon Elastic File System (Amazon EFS). The default value is S3.
*Required*: No
*Type*: String
*Allowed values*: `S3 | EFS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EndpointDetails`  <a name="cfn-transfer-server-endpointdetails"></a>
The virtual private cloud (VPC) endpoint settings that are configured for your server. When you host your endpoint within your VPC, you can make your endpoint accessible only to resources within your VPC, or you can attach Elastic IP addresses and make your endpoint accessible to clients over the internet. Your VPC's default security groups are automatically assigned to your endpoint.
*Required*: No
*Type*: [EndpointDetails](aws-properties-transfer-server-endpointdetails.md)
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`EndpointType`  <a name="cfn-transfer-server-endpointtype"></a>
The type of endpoint that you want your server to use. You can choose to make your server's endpoint publicly accessible (PUBLIC) or host it inside your VPC. With an endpoint that is hosted in a VPC, you can restrict access to your server and resources only within your VPC or choose to make it internet facing by attaching Elastic IP addresses directly to it.
 After May 19, 2021, you won't be able to create a server using `EndpointType=VPC_ENDPOINT` in your AWS account if your account hasn't already done so before May 19, 2021. If you have already created servers with `EndpointType=VPC_ENDPOINT` in your AWS account on or before May 19, 2021, you will not be affected. After this date, use `EndpointType` = `VPC` .
 For more information, see [Discontinuing the use of VPC\_ENDPOINT](https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html#deprecate-vpc-endpoint) .
 It is recommended that you use `VPC` as the `EndpointType` . With this endpoint type, you have the option to directly associate up to three Elastic IPv4 addresses (BYO IP included) with your server's endpoint and use VPC security groups to restrict traffic by the client's public IP address. This is not possible with `EndpointType` set to `VPC_ENDPOINT` .
*Required*: No
*Type*: String
*Allowed values*: `PUBLIC | VPC | VPC_ENDPOINT`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdentityProviderDetails`  <a name="cfn-transfer-server-identityproviderdetails"></a>
Required when `IdentityProviderType` is set to `AWS_DIRECTORY_SERVICE`, `AWS_LAMBDA` or `API_GATEWAY`. Accepts an array containing all of the information required to use a directory in `AWS_DIRECTORY_SERVICE` or invoke a customer-supplied authentication API, including the API Gateway URL. Cannot be specified when `IdentityProviderType` is set to `SERVICE_MANAGED`.
*Required*: No
*Type*: [IdentityProviderDetails](aws-properties-transfer-server-identityproviderdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdentityProviderType`  <a name="cfn-transfer-server-identityprovidertype"></a>
The mode of authentication for a server. The default value is `SERVICE_MANAGED`, which allows you to store and access user credentials within the AWS Transfer Family service.
Use `AWS_DIRECTORY_SERVICE` to provide access to Active Directory groups in AWS Directory Service for Microsoft Active Directory or Microsoft Active Directory in your on-premises environment or in AWS using AD Connector. This option also requires you to provide a Directory ID by using the `IdentityProviderDetails` parameter.
Use the `API_GATEWAY` value to integrate with an identity provider of your choosing. The `API_GATEWAY` setting requires you to provide an Amazon API Gateway endpoint URL to call for authentication by using the `IdentityProviderDetails` parameter.
Use the `AWS_LAMBDA` value to directly use an AWS Lambda function as your identity provider. If you choose this value, you must specify the ARN for the Lambda function in the `Function` parameter for the `IdentityProviderDetails` data type.
*Required*: No
*Type*: String
*Allowed values*: `SERVICE_MANAGED | API_GATEWAY | AWS_DIRECTORY_SERVICE | AWS_LAMBDA`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IpAddressType`  <a name="cfn-transfer-server-ipaddresstype"></a>
Specifies whether to use IPv4 only, or to use dual-stack (IPv4 and IPv6) for your AWS Transfer Family endpoint. The default value is `IPV4`.
The `IpAddressType` parameter has the following limitations:
+ It cannot be changed while the server is online. You must stop the server before modifying this parameter.
+ It cannot be updated to `DUALSTACK` if the server has `AddressAllocationIds` specified.
When using `DUALSTACK` as the `IpAddressType`, you cannot set the `AddressAllocationIds` parameter for the [EndpointDetails](https://docs.aws.amazon.com/transfer/latest/APIReference/API_EndpointDetails.html) for the server.
*Required*: No
*Type*: String
*Allowed values*: `IPV4 | DUALSTACK`
*Update requires*: [Some interruptions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-some-interrupt)

`LoggingRole`  <a name="cfn-transfer-server-loggingrole"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows a server to turn on Amazon CloudWatch logging for Amazon S3 or Amazon EFS events. When set, you can view user activity in your CloudWatch logs.
*Required*: No
*Type*: String
*Pattern*: `^(|arn:.*role/\S+)$`
*Minimum*: `0`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PostAuthenticationLoginBanner`  <a name="cfn-transfer-server-postauthenticationloginbanner"></a>
Specifies a string to display when users connect to a server. This string is displayed after the user authenticates.
The SFTP protocol does not support post-authentication display banners.
*Required*: No
*Type*: String
*Pattern*: `^[\x09-\x0D\x20-\x7E]*$`
*Minimum*: `0`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PreAuthenticationLoginBanner`  <a name="cfn-transfer-server-preauthenticationloginbanner"></a>
Specifies a string to display when users connect to a server. This string is displayed before the user authenticates. For example, the following banner displays details about using the system:
 `This system is for the use of authorized users only. Individuals using this computer system without authority, or in excess of their authority, are subject to having all of their activities on this system monitored and recorded by system personnel.`
*Required*: No
*Type*: String
*Pattern*: `^[\x09-\x0D\x20-\x7E]*$`
*Minimum*: `0`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProtocolDetails`  <a name="cfn-transfer-server-protocoldetails"></a>
The protocol settings that are configured for your server.
+  To indicate passive mode (for FTP and FTPS protocols), use the `PassiveIp` parameter. Enter a single dotted-quad IPv4 address, such as the external IP address of a firewall, router, or load balancer.
+  To ignore the error that is generated when the client attempts to use the `SETSTAT` command on a file that you are uploading to an Amazon S3 bucket, use the `SetStatOption` parameter. To have the AWS Transfer Family server ignore the `SETSTAT` command and upload files without needing to make any changes to your SFTP client, set the value to `ENABLE_NO_OP` . If you set the `SetStatOption` parameter to `ENABLE_NO_OP` , Transfer Family generates a log entry to Amazon CloudWatch Logs, so that you can determine when the client is making a `SETSTAT` call.
+  To determine whether your AWS Transfer Family server resumes recent, negotiated sessions through a unique session ID, use the `TlsSessionResumptionMode` parameter.
+ `As2Transports` indicates the transport method for the AS2 messages. Currently, only HTTP is supported.

   The `Protocols` parameter is an array of strings.

  *Allowed values* : One or more of `SFTP` , `FTPS` , `FTP` , `AS2`
*Required*: No
*Type*: [ProtocolDetails](aws-properties-transfer-server-protocoldetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Protocols`  <a name="cfn-transfer-server-protocols"></a>
Specifies the file transfer protocol or protocols over which your file transfer protocol client can connect to your server's endpoint. The available protocols are:
+ `SFTP` (Secure Shell (SSH) File Transfer Protocol): File transfer over SSH
+ `FTPS` (File Transfer Protocol Secure): File transfer with TLS encryption
+ `FTP` (File Transfer Protocol): Unencrypted file transfer
+ `AS2` (Applicability Statement 2): used for transporting structured business-to-business data
+  If you select `FTPS` , you must choose a certificate stored in AWS Certificate Manager (ACM) which is used to identify your server when clients connect to it over FTPS.
+  If `Protocol` includes either `FTP` or `FTPS` , then the `EndpointType` must be `VPC` and the `IdentityProviderType` must be either `AWS_DIRECTORY_SERVICE` , `AWS_LAMBDA` , or `API_GATEWAY` .
+  If `Protocol` includes `FTP` , then `AddressAllocationIds` cannot be associated.
+  If `Protocol` is set only to `SFTP` , the `EndpointType` can be set to `PUBLIC` and the `IdentityProviderType` can be set any of the supported identity types: `SERVICE_MANAGED` , `AWS_DIRECTORY_SERVICE` , `AWS_LAMBDA` , or `API_GATEWAY` .
+  If `Protocol` includes `AS2` , then the `EndpointType` must be `VPC` , and domain must be Amazon S3.
 The `Protocols` parameter is an array of strings.
*Allowed values* : One or more of `SFTP` , `FTPS` , `FTP` , `AS2`
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`S3StorageOptions`  <a name="cfn-transfer-server-s3storageoptions"></a>
Specifies whether or not performance for your Amazon S3 directories is optimized.
+ If using the console, this is enabled by default.
+ If using the API or CLI, this is disabled by default.
By default, home directory mappings have a `TYPE` of `DIRECTORY`. If you enable this option, you would then need to explicitly set the `HomeDirectoryMapEntry``Type` to `FILE` if you want a mapping to have a file target.
*Required*: No
*Type*: [S3StorageOptions](aws-properties-transfer-server-s3storageoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SecurityPolicyName`  <a name="cfn-transfer-server-securitypolicyname"></a>
Specifies the name of the security policy for the server.
*Required*: No
*Type*: String
*Pattern*: `^TransferSecurityPolicy-.+$`
*Minimum*: `0`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StructuredLogDestinations`  <a name="cfn-transfer-server-structuredlogdestinations"></a>
Specifies the log groups to which your server logs are sent.
To specify a log group, you must provide the ARN for an existing log group. In this case, the format of the log group is as follows:
 `arn:aws:logs:region-name:amazon-account-id:log-group:log-group-name:*`
For example, `arn:aws:logs:us-east-1:111122223333:log-group:mytestgroup:*`
If you have previously specified a log group for a server, you can clear it, and in effect turn off structured logging, by providing an empty value for this parameter in an `update-server` call. For example:
 `update-server --server-id s-1234567890abcdef0 --structured-log-destinations`
*Required*: No
*Type*: Array of String
*Minimum*: `20 | 0`
*Maximum*: `1600 | 1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-transfer-server-tags"></a>
Key-value pairs that can be used to group and search for servers.
*Required*: No
*Type*: Array of [Tag](aws-properties-transfer-server-tag.md)
*Minimum*: `1`
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkflowDetails`  <a name="cfn-transfer-server-workflowdetails"></a>
Specifies the workflow ID for the workflow to assign and the execution role that's used for executing the workflow.
 In addition to a workflow to execute when a file is uploaded completely, `WorkflowDetails` can also contain a workflow ID (and execution role) for a workflow to execute on partial upload. A partial upload occurs when a file is open when the session disconnects.
*Required*: No
*Type*: [WorkflowDetails](aws-properties-transfer-server-workflowdetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-transfer-server-return-values"></a>

### Ref
<a name="aws-resource-transfer-server-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the server ARN, such as `arn:aws:transfer:us-east-1:123456789012:server/s-01234567890abcdef` .

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-transfer-server-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-transfer-server-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Specifies the unique Amazon Resource Name (ARN) of the server.

`As2ServiceManagedEgressIpAddresses`  <a name="As2ServiceManagedEgressIpAddresses-fn::getatt"></a>
The list of egress IP addresses of this server. These IP addresses are only relevant for servers that use the AS2 protocol. They are used for sending asynchronous MDNs.
These IP addresses are assigned automatically when you create an AS2 server. Additionally, if you update an existing server and add the AS2 protocol, static IP addresses are assigned as well.

`ServerId`  <a name="ServerId-fn::getatt"></a>
Specifies the unique system-assigned identifier for a server that you instantiate.

`State`  <a name="State-fn::getatt"></a>
The condition of the server that was described. A value of `ONLINE` indicates that the server can accept jobs and transfer files. A `State` value of `OFFLINE` means that the server cannot perform file transfer operations.
The states of `STARTING` and `STOPPING` indicate that the server is in an intermediate state, either not fully able to respond, or not fully offline. The values of `START_FAILED` or `STOP_FAILED` can indicate an error condition.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
