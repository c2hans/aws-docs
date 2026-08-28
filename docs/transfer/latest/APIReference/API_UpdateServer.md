---
source_url: https://docs.aws.amazon.com/transfer/latest/APIReference/API_UpdateServer.html
---

# UpdateServer
<a name="API_UpdateServer"></a>

Updates the file transfer protocol-enabled server's properties after that server has been created.

The `UpdateServer` call returns the `ServerId` of the server you updated.

## Request Syntax
<a name="API_UpdateServer_RequestSyntax"></a>

```
{
   "Certificate": "{{string}}",
   "EndpointDetails": {
      "AddressAllocationIds": [ "{{string}}" ],
      "SecurityGroupIds": [ "{{string}}" ],
      "SubnetIds": [ "{{string}}" ],
      "VpcEndpointId": "{{string}}",
      "VpcId": "{{string}}"
   },
   "EndpointType": "{{string}}",
   "HostKey": "{{string}}",
   "IdentityProviderDetails": {
      "DirectoryId": "{{string}}",
      "Function": "{{string}}",
      "InvocationRole": "{{string}}",
      "SftpAuthenticationMethods": "{{string}}",
      "Url": "{{string}}"
   },
   "IdentityProviderType": "{{string}}",
   "IpAddressType": "{{string}}",
   "LoggingRole": "{{string}}",
   "PostAuthenticationLoginBanner": "{{string}}",
   "PreAuthenticationLoginBanner": "{{string}}",
   "ProtocolDetails": {
      "As2Transports": [ "{{string}}" ],
      "PassiveIp": "{{string}}",
      "SetStatOption": "{{string}}",
      "TlsSessionResumptionMode": "{{string}}"
   },
   "Protocols": [ "{{string}}" ],
   "S3StorageOptions": {
      "DirectoryListingOptimization": "{{string}}"
   },
   "SecurityPolicyName": "{{string}}",
   "ServerId": "{{string}}",
   "StructuredLogDestinations": [ "{{string}}" ],
   "WorkflowDetails": {
      "OnPartialUpload": [
         {
            "ExecutionRole": "{{string}}",
            "WorkflowId": "{{string}}"
         }
      ],
      "OnUpload": [
         {
            "ExecutionRole": "{{string}}",
            "WorkflowId": "{{string}}"
         }
      ]
   }
}
```

## Request Parameters
<a name="API_UpdateServer_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Certificate](#API_UpdateServer_RequestSyntax) **   <a name="TransferFamily-UpdateServer-request-Certificate"></a>
The Amazon Resource Name (ARN) of the AWSCertificate Manager (ACM) certificate. Required when `Protocols` is set to `FTPS`.
To request a new public certificate, see [Request a public certificate](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-public.html) in the * AWSCertificate Manager User Guide*.
To import an existing certificate into ACM, see [Importing certificates into ACM](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate.html) in the * AWSCertificate Manager User Guide*.
To request a private certificate to use FTPS through private IP addresses, see [Request a private certificate](https://docs.aws.amazon.com/acm/latest/userguide/gs-acm-request-private.html) in the * AWSCertificate Manager User Guide*.
Certificates with the following cryptographic algorithms and key sizes are supported:
+ 2048-bit RSA (RSA\_2048)
+ 4096-bit RSA (RSA\_4096)
+ Elliptic Prime Curve 256 bit (EC\_prime256v1)
+ Elliptic Prime Curve 384 bit (EC\_secp384r1)
+ Elliptic Prime Curve 521 bit (EC\_secp521r1)
The certificate must be a valid SSL/TLS X.509 version 3 certificate with FQDN or IP address specified and information about the issuer.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1600.
Required: No

 ** [EndpointDetails](#API_UpdateServer_RequestSyntax) **   <a name="TransferFamily-UpdateServer-request-EndpointDetails"></a>
The virtual private cloud (VPC) endpoint settings that are configured for your server. When you host your endpoint within your VPC, you can make your endpoint accessible only to resources within your VPC, or you can attach Elastic IP addresses and make your endpoint accessible to clients over the internet. Your VPC's default security groups are automatically assigned to your endpoint.
Type: [EndpointDetails](API_EndpointDetails.md) object
Required: No

 ** [EndpointType](#API_UpdateServer_RequestSyntax) **   <a name="TransferFamily-UpdateServer-request-EndpointType"></a>
The type of endpoint that you want your server to use. You can choose to make your server's endpoint publicly accessible (PUBLIC) or host it inside your VPC. With an endpoint that is hosted in a VPC, you can restrict access to your server and resources only within your VPC or choose to make it internet facing by attaching Elastic IP addresses directly to it.
 After May 19, 2021, you won't be able to create a server using `EndpointType=VPC_ENDPOINT` in your AWS account if your account hasn't already done so before May 19, 2021. If you have already created servers with `EndpointType=VPC_ENDPOINT` in your AWS account on or before May 19, 2021, you will not be affected. After this date, use `EndpointType`=`VPC`.
For more information, see [Discontinuing the use of VPC\_ENDPOINT](https://docs.aws.amazon.com/transfer/latest/userguide/create-server-in-vpc.html#deprecate-vpc-endpoint).
It is recommended that you use `VPC` as the `EndpointType`. With this endpoint type, you have the option to directly associate up to three Elastic IPv4 addresses (BYO IP included) with your server's endpoint and use VPC security groups to restrict traffic by the client's public IP address. This is not possible with `EndpointType` set to `VPC_ENDPOINT`.
Type: String
Valid Values: `PUBLIC | VPC | VPC_ENDPOINT`
Required: No

 ** [HostKey](#API_UpdateServer_RequestSyntax) **   <a name="TransferFamily-UpdateServer-request-HostKey"></a>
The RSA, ECDSA, or ED25519 private key to use for your SFTP-enabled server. You can add multiple host keys, in case you want to rotate keys, or have a set of active keys that use different algorithms.
Use the following command to generate an RSA 2048 bit key with no passphrase:
 `ssh-keygen -t rsa -b 2048 -N "" -m PEM -f my-new-server-key`.
Use a minimum value of 2048 for the `-b` option. You can create a stronger key by using 3072 or 4096.
Use the following command to generate an ECDSA 256 bit key with no passphrase:
 `ssh-keygen -t ecdsa -b 256 -N "" -m PEM -f my-new-server-key`.
Valid values for the `-b` option for ECDSA are 256, 384, and 521.
Use the following command to generate an ED25519 key with no passphrase:
 `ssh-keygen -t ed25519 -N "" -f my-new-server-key`.
For all of these commands, you can replace *my-new-server-key* with a string of your choice.
If you aren't planning to migrate existing users from an existing SFTP-enabled server to a new server, don't update the host key. Accidentally changing a server's host key can be disruptive.
For more information, see [Update host keys for your SFTP-enabled server](https://docs.aws.amazon.com/transfer/latest/userguide/edit-server-config.html#configuring-servers-change-host-key) in the * AWS Transfer Family User Guide*.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

 ** [IdentityProviderDetails](#API_UpdateServer_RequestSyntax) **   <a name="TransferFamily-UpdateServer-request-IdentityProviderDetails"></a>
An array containing all of the information required to call a customer's authentication API method.
Type: [IdentityProviderDetails](API_IdentityProviderDetails.md) object
Required: No

 ** [IdentityProviderType](#API_UpdateServer_RequestSyntax) **   <a name="TransferFamily-UpdateServer-request-IdentityProviderType"></a>
The mode of authentication for a server. The default value is `SERVICE_MANAGED`, which allows you to store and access user credentials within the AWS Transfer Family service.
Use `AWS_DIRECTORY_SERVICE` to provide access to Active Directory groups in AWS Directory Service for Microsoft Active Directory or Microsoft Active Directory in your on-premises environment or in AWS using AD Connector. This option also requires you to provide a Directory ID by using the `IdentityProviderDetails` parameter.
Use the `API_GATEWAY` value to integrate with an identity provider of your choosing. The `API_GATEWAY` setting requires you to provide an Amazon API Gateway endpoint URL to call for authentication by using the `IdentityProviderDetails` parameter.
Use the `AWS_LAMBDA` value to directly use an AWS Lambda function as your identity provider. If you choose this value, you must specify the ARN for the Lambda function in the `Function` parameter for the `IdentityProviderDetails` data type.
Type: String
Valid Values: `SERVICE_MANAGED | API_GATEWAY | AWS_DIRECTORY_SERVICE | AWS_LAMBDA`
Required: No

 ** [IpAddressType](#API_UpdateServer_RequestSyntax) **   <a name="TransferFamily-UpdateServer-request-IpAddressType"></a>
Specifies whether to use IPv4 only, or to use dual-stack (IPv4 and IPv6) for your AWS Transfer Family endpoint. The default value is `IPV4`.
The `IpAddressType` parameter has the following limitations:
+ It cannot be changed while the server is online. You must stop the server before modifying this parameter.
+ It cannot be updated to `DUALSTACK` if the server has `AddressAllocationIds` specified.
When using `DUALSTACK` as the `IpAddressType`, you cannot set the `AddressAllocationIds` parameter for the [EndpointDetails](https://docs.aws.amazon.com/transfer/latest/APIReference/API_EndpointDetails.html) for the server.
Type: String
Valid Values: `IPV4 | DUALSTACK`
Required: No

 ** [LoggingRole](#API_UpdateServer_RequestSyntax) **   <a name="TransferFamily-UpdateServer-request-LoggingRole"></a>
The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows a server to turn on Amazon CloudWatch logging for Amazon S3 or Amazon EFS events. When set, you can view user activity in your CloudWatch logs.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `(|arn:.*role/\S+)`
Required: No

 ** [PostAuthenticationLoginBanner](#API_UpdateServer_RequestSyntax) **   <a name="TransferFamily-UpdateServer-request-PostAuthenticationLoginBanner"></a>
Specifies a string to display when users connect to a server. This string is displayed after the user authenticates.
The SFTP protocol does not support post-authentication display banners.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Pattern: `[\x09-\x0D\x20-\x7E]*`
Required: No

 ** [PreAuthenticationLoginBanner](#API_UpdateServer_RequestSyntax) **   <a name="TransferFamily-UpdateServer-request-PreAuthenticationLoginBanner"></a>
Specifies a string to display when users connect to a server. This string is displayed before the user authenticates. For example, the following banner displays details about using the system:
 `This system is for the use of authorized users only. Individuals using this computer system without authority, or in excess of their authority, are subject to having all of their activities on this system monitored and recorded by system personnel.`
Type: String
Length Constraints: Minimum length of 0. Maximum length of 4096.
Pattern: `[\x09-\x0D\x20-\x7E]*`
Required: No

 ** [ProtocolDetails](#API_UpdateServer_RequestSyntax) **   <a name="TransferFamily-UpdateServer-request-ProtocolDetails"></a>
The protocol settings that are configured for your server.
Avoid placing Network Load Balancers (NLBs) or NAT gateways in front of AWS Transfer Family servers, as this increases costs and can cause performance issues, including reduced connection limits for FTPS. For more details, see [ Avoid placing NLBs and NATs in front of AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/infrastructure-security.html#nlb-considerations).
+  To indicate passive mode (for FTP and FTPS protocols), use the `PassiveIp` parameter. Enter a single dotted-quad IPv4 address, such as the external IP address of a firewall, router, or load balancer.
+ To ignore the error that is generated when the client attempts to use the `SETSTAT` command on a file that you are uploading to an Amazon S3 bucket, use the `SetStatOption` parameter. To have the AWS Transfer Family server ignore the `SETSTAT` command and upload files without needing to make any changes to your SFTP client, set the value to `ENABLE_NO_OP`. If you set the `SetStatOption` parameter to `ENABLE_NO_OP`, Transfer Family generates a log entry to Amazon CloudWatch Logs, so that you can determine when the client is making a `SETSTAT` call.
+ To determine whether your AWS Transfer Family server resumes recent, negotiated sessions through a unique session ID, use the `TlsSessionResumptionMode` parameter.
+  `As2Transports` indicates the transport method for the AS2 messages. Currently, only HTTP is supported.
Type: [ProtocolDetails](API_ProtocolDetails.md) object
Required: No

 ** [Protocols](#API_UpdateServer_RequestSyntax) **   <a name="TransferFamily-UpdateServer-request-Protocols"></a>
Specifies the file transfer protocol or protocols over which your file transfer protocol client can connect to your server's endpoint. The available protocols are:
+  `SFTP` (Secure Shell (SSH) File Transfer Protocol): File transfer over SSH
+  `FTPS` (File Transfer Protocol Secure): File transfer with TLS encryption
+  `FTP` (File Transfer Protocol): Unencrypted file transfer
+  `AS2` (Applicability Statement 2): used for transporting structured business-to-business data
+ If you select `FTPS`, you must choose a certificate stored in AWS Certificate Manager (ACM) which is used to identify your server when clients connect to it over FTPS.
+ If `Protocol` includes either `FTP` or `FTPS`, then the `EndpointType` must be `VPC` and the `IdentityProviderType` must be either `AWS_DIRECTORY_SERVICE`, `AWS_LAMBDA`, or `API_GATEWAY`.
+ If `Protocol` includes `FTP`, then `AddressAllocationIds` cannot be associated.
+ If `Protocol` is set only to `SFTP`, the `EndpointType` can be set to `PUBLIC` and the `IdentityProviderType` can be set any of the supported identity types: `SERVICE_MANAGED`, `AWS_DIRECTORY_SERVICE`, `AWS_LAMBDA`, or `API_GATEWAY`.
+ If `Protocol` includes `AS2`, then the `EndpointType` must be `VPC`, and domain must be Amazon S3.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Valid Values: `SFTP | FTP | FTPS | AS2`
Required: No

 ** [S3StorageOptions](#API_UpdateServer_RequestSyntax) **   <a name="TransferFamily-UpdateServer-request-S3StorageOptions"></a>
Specifies whether or not performance for your Amazon S3 directories is optimized.
+ If using the console, this is enabled by default.
+ If using the API or CLI, this is disabled by default.
By default, home directory mappings have a `TYPE` of `DIRECTORY`. If you enable this option, you would then need to explicitly set the `HomeDirectoryMapEntry` `Type` to `FILE` if you want a mapping to have a file target.
Type: [S3StorageOptions](API_S3StorageOptions.md) object
Required: No

 ** [SecurityPolicyName](#API_UpdateServer_RequestSyntax) **   <a name="TransferFamily-UpdateServer-request-SecurityPolicyName"></a>
Specifies the name of the security policy for the server.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `Transfer[A-Za-z0-9]*SecurityPolicy-[A-Za-z0-9-]+`
Required: No

 ** [ServerId](#API_UpdateServer_RequestSyntax) **   <a name="TransferFamily-UpdateServer-request-ServerId"></a>
A system-assigned unique identifier for a server instance that the Transfer Family user is assigned to.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-([0-9a-f]{17})`
Required: Yes

 ** [StructuredLogDestinations](#API_UpdateServer_RequestSyntax) **   <a name="TransferFamily-UpdateServer-request-StructuredLogDestinations"></a>
Specifies the log groups to which your server logs are sent.
To specify a log group, you must provide the ARN for an existing log group. In this case, the format of the log group is as follows:
 `arn:aws:logs:region-name:amazon-account-id:log-group:log-group-name:*`
For example, `arn:aws:logs:us-east-1:111122223333:log-group:mytestgroup:*`
If you have previously specified a log group for a server, you can clear it, and in effect turn off structured logging, by providing an empty value for this parameter in an `update-server` call. For example:
 `update-server --server-id s-1234567890abcdef0 --structured-log-destinations`
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Length Constraints: Minimum length of 20. Maximum length of 1600.
Pattern: `arn:\S+`
Required: No

 ** [WorkflowDetails](#API_UpdateServer_RequestSyntax) **   <a name="TransferFamily-UpdateServer-request-WorkflowDetails"></a>
Specifies the workflow ID for the workflow to assign and the execution role that's used for executing the workflow.
In addition to a workflow to execute when a file is uploaded completely, `WorkflowDetails` can also contain a workflow ID (and execution role) for a workflow to execute on partial upload. A partial upload occurs when the server session disconnects while the file is still being uploaded.
To remove an associated workflow from a server, you can provide an empty `OnUpload` object, as in the following example.
 `aws transfer update-server --server-id s-01234567890abcdef --workflow-details '{"OnUpload":[]}'`
Type: [WorkflowDetails](API_WorkflowDetails.md) object
Required: No

## Response Syntax
<a name="API_UpdateServer_ResponseSyntax"></a>

```
{
   "ServerId": "string"
}
```

## Response Elements
<a name="API_UpdateServer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ServerId](#API_UpdateServer_ResponseSyntax) **   <a name="TransferFamily-UpdateServer-response-ServerId"></a>
A system-assigned unique identifier for a server that the Transfer Family user is assigned to.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-([0-9a-f]{17})`

## Errors
<a name="API_UpdateServer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConflictException **
This exception is thrown when the `UpdateServer` is called for a file transfer protocol-enabled server that has VPC as the endpoint type and the server's `VpcEndpointID` is not in the available state.
HTTP Status Code: 400

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

## Examples
<a name="API_UpdateServer_Examples"></a>

### Example
<a name="API_UpdateServer_Example_1"></a>

The following example updates the role of a server.

#### Sample Request
<a name="API_UpdateServer_Example_1_Request"></a>

```
{
   "EndpointDetails": {
   "VpcEndpointId": "vpce-01234f056f3g13",
   "LoggingRole": "CloudWatchS3Events",
   "ServerId": "s-01234567890abcdef"
   }
}
```

### Example
<a name="API_UpdateServer_Example_2"></a>

The following example removes any associated workflows from the server.

#### Sample Request
<a name="API_UpdateServer_Example_2_Request"></a>

```
aws transfer update-server --server-id s-01234567890abcdef --workflow-details '{"OnUpload":[]}'
```

### Example
<a name="API_UpdateServer_Example_3"></a>

This is a sample response for this API call.

#### Sample Response
<a name="API_UpdateServer_Example_3_Response"></a>

```
{
   "ServerId": "s-01234567890abcdef"
}
```

## See Also
<a name="API_UpdateServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/transfer-2018-11-05/UpdateServer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/transfer-2018-11-05/UpdateServer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/transfer-2018-11-05/UpdateServer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/transfer-2018-11-05/UpdateServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/transfer-2018-11-05/UpdateServer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/transfer-2018-11-05/UpdateServer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/transfer-2018-11-05/UpdateServer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/transfer-2018-11-05/UpdateServer)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/transfer-2018-11-05/UpdateServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/transfer-2018-11-05/UpdateServer)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Transfer Family. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query transfer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
