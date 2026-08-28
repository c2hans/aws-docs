---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_UpdateLocationSmb.html
---

# UpdateLocationSmb
<a name="API_UpdateLocationSmb"></a>

Modifies the following configuration parameters of the Server Message Block (SMB) transfer location that you're using with AWS DataSync.

For more information, see [Configuring DataSync transfers with an SMB file server](https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html).

## Request Syntax
<a name="API_UpdateLocationSmb_RequestSyntax"></a>

```
{
   "AgentArns": [ "{{string}}" ],
   "AuthenticationType": "{{string}}",
   "CmkSecretConfig": {
      "KmsKeyArn": "{{string}}",
      "SecretArn": "{{string}}"
   },
   "CustomSecretConfig": {
      "SecretAccessRoleArn": "{{string}}",
      "SecretArn": "{{string}}"
   },
   "DnsIpAddresses": [ "{{string}}" ],
   "Domain": "{{string}}",
   "KerberosKeytab": {{blob}},
   "KerberosKrb5Conf": {{blob}},
   "KerberosPrincipal": "{{string}}",
   "LocationArn": "{{string}}",
   "MountOptions": {
      "Version": "{{string}}"
   },
   "Password": "{{string}}",
   "ServerHostname": "{{string}}",
   "Subdirectory": "{{string}}",
   "User": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateLocationSmb_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AgentArns](#API_UpdateLocationSmb_RequestSyntax) **   <a name="DataSync-UpdateLocationSmb-request-AgentArns"></a>
Specifies the DataSync agent (or agents) that can connect to your SMB file server. You specify an agent by using its Amazon Resource Name (ARN).
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 8 items.
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:agent/agent-[0-9a-z]{17}$`
Required: No

 ** [AuthenticationType](#API_UpdateLocationSmb_RequestSyntax) **   <a name="DataSync-UpdateLocationSmb-request-AuthenticationType"></a>
Specifies the authentication protocol that DataSync uses to connect to your SMB file server. DataSync supports `NTLM` (default) and `KERBEROS` authentication.
For more information, see [Providing DataSync access to SMB file servers](https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html#configuring-smb-permissions).
Type: String
Valid Values: `NTLM | KERBEROS`
Required: No

 ** [CmkSecretConfig](#API_UpdateLocationSmb_RequestSyntax) **   <a name="DataSync-UpdateLocationSmb-request-CmkSecretConfig"></a>
Specifies configuration information for a DataSync-managed secret, such as a `Password` or `KerberosKeytab` or set of credentials that DataSync uses to access a specific transfer location, and a customer-managed AWS KMS key.
Type: [CmkSecretConfig](API_CmkSecretConfig.md) object
Required: No

 ** [CustomSecretConfig](#API_UpdateLocationSmb_RequestSyntax) **   <a name="DataSync-UpdateLocationSmb-request-CustomSecretConfig"></a>
Specifies configuration information for a customer-managed secret, such as a `Password` or `KerberosKeytab` or set of credentials that DataSync uses to access a specific transfer location, and a customer-managed AWS Identity and Access Management (IAM) role that provides access to the secret.
Type: [CustomSecretConfig](API_CustomSecretConfig.md) object
Required: No

 ** [DnsIpAddresses](#API_UpdateLocationSmb_RequestSyntax) **   <a name="DataSync-UpdateLocationSmb-request-DnsIpAddresses"></a>
Specifies the IP addresses (IPv4 or IPv6) for the DNS servers that your SMB file server belongs to. This parameter applies only if `AuthenticationType` is set to `KERBEROS`.
If you have multiple domains in your environment, configuring this parameter makes sure that DataSync connects to the right SMB file server.
Type: Array of strings
Array Members: Maximum number of 2 items.
Length Constraints: Minimum length of 7. Maximum length of 39.
Pattern: `\A((25[0-5]|2[0-4]\d|[0-1]?\d?\d)(\.(25[0-5]|2[0-4]\d|[0-1]?\d?\d)){3}|([0-9a-fA-F]{1,4}:){7,7}[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,7}:|([0-9a-fA-F]{1,4}:){1,6}:[0-9a-fA-F]{1,4}|([0-9a-fA-F]{1,4}:){1,5}(:[0-9a-fA-F]{1,4}){1,2}|([0-9a-fA-F]{1,4}:){1,4}(:[0-9a-fA-F]{1,4}){1,3}|([0-9a-fA-F]{1,4}:){1,3}(:[0-9a-fA-F]{1,4}){1,4}|([0-9a-fA-F]{1,4}:){1,2}(:[0-9a-fA-F]{1,4}){1,5}|[0-9a-fA-F]{1,4}:((:[0-9a-fA-F]{1,4}){1,6}))\z`
Required: No

 ** [Domain](#API_UpdateLocationSmb_RequestSyntax) **   <a name="DataSync-UpdateLocationSmb-request-Domain"></a>
Specifies the Windows domain name that your SMB file server belongs to. This parameter applies only if `AuthenticationType` is set to `NTLM`.
If you have multiple domains in your environment, configuring this parameter makes sure that DataSync connects to the right file server.
Type: String
Length Constraints: Maximum length of 253.
Pattern: `^[A-Za-z0-9]((\.|-+)?[A-Za-z0-9]){0,252}$`
Required: No

 ** [KerberosKeytab](#API_UpdateLocationSmb_RequestSyntax) **   <a name="DataSync-UpdateLocationSmb-request-KerberosKeytab"></a>
Specifies your Kerberos key table (keytab) file, which includes mappings between your Kerberos principal and encryption keys.
To avoid task execution errors, make sure that the Kerberos principal that you use to create the keytab file matches exactly what you specify for `KerberosPrincipal`.
Type: Base64-encoded binary data object
Length Constraints: Maximum length of 65536.
Required: No

 ** [KerberosKrb5Conf](#API_UpdateLocationSmb_RequestSyntax) **   <a name="DataSync-UpdateLocationSmb-request-KerberosKrb5Conf"></a>
Specifies a Kerberos configuration file (`krb5.conf`) that defines your Kerberos realm configuration.
The file must be base64 encoded. If you're using the AWS CLI, the encoding is done for you.
Type: Base64-encoded binary data object
Length Constraints: Maximum length of 131072.
Required: No

 ** [KerberosPrincipal](#API_UpdateLocationSmb_RequestSyntax) **   <a name="DataSync-UpdateLocationSmb-request-KerberosPrincipal"></a>
Specifies a Kerberos prinicpal, which is an identity in your Kerberos realm that has permission to access the files, folders, and file metadata in your SMB file server.
A Kerberos principal might look like `HOST/kerberosuser@MYDOMAIN.ORG`.
Principal names are case sensitive. Your DataSync task execution will fail if the principal that you specify for this parameter doesn’t exactly match the principal that you use to create the keytab file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^.+$`
Required: No

 ** [LocationArn](#API_UpdateLocationSmb_RequestSyntax) **   <a name="DataSync-UpdateLocationSmb-request-LocationArn"></a>
Specifies the ARN of the SMB location that you want to update.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `^arn:(aws|aws-cn|aws-us-gov|aws-eusc|aws-iso|aws-iso-b):datasync:[a-z\-0-9]+:[0-9]{12}:location/loc-[0-9a-z]{17}$`
Required: Yes

 ** [MountOptions](#API_UpdateLocationSmb_RequestSyntax) **   <a name="DataSync-UpdateLocationSmb-request-MountOptions"></a>
Specifies the version of the Server Message Block (SMB) protocol that AWS DataSync uses to access an SMB file server.
Type: [SmbMountOptions](API_SmbMountOptions.md) object
Required: No

 ** [Password](#API_UpdateLocationSmb_RequestSyntax) **   <a name="DataSync-UpdateLocationSmb-request-Password"></a>
Specifies the password of the user who can mount your SMB file server and has permission to access the files and folders involved in your transfer. This parameter applies only if `AuthenticationType` is set to `NTLM`.
Type: String
Length Constraints: Maximum length of 104.
Pattern: `^.{0,104}$`
Required: No

 ** [ServerHostname](#API_UpdateLocationSmb_RequestSyntax) **   <a name="DataSync-UpdateLocationSmb-request-ServerHostname"></a>
Specifies the domain name or IP address (IPv4 or IPv6) of the SMB file server that your DataSync agent connects to.
If you're using Kerberos authentication, you must specify a domain name.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-:]*[A-Za-z0-9])$`
Required: No

 ** [Subdirectory](#API_UpdateLocationSmb_RequestSyntax) **   <a name="DataSync-UpdateLocationSmb-request-Subdirectory"></a>
Specifies the name of the share exported by your SMB file server where DataSync will read or write data. You can include a subdirectory in the share path (for example, `/path/to/subdirectory`). Make sure that other SMB clients in your network can also mount this path.
To copy all data in the specified subdirectory, DataSync must be able to mount the SMB share and access all of its data. For more information, see [Providing DataSync access to SMB file servers](https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html#configuring-smb-permissions).
Type: String
Length Constraints: Maximum length of 4096.
Pattern: `^[a-zA-Z0-9_\-\+\./\(\)\$\p{Zs}]+$`
Required: No

 ** [User](#API_UpdateLocationSmb_RequestSyntax) **   <a name="DataSync-UpdateLocationSmb-request-User"></a>
Specifies the user name that can mount your SMB file server and has permission to access the files and folders involved in your transfer. This parameter applies only if `AuthenticationType` is set to `NTLM`.
For information about choosing a user with the right level of access for your transfer, see [Providing DataSync access to SMB file servers](https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html#configuring-smb-permissions).
Type: String
Length Constraints: Maximum length of 104.
Pattern: `^[^\x22\x5B\x5D/\\:;|=,+*?\x3C\x3E]{1,104}$`
Required: No

## Response Elements
<a name="API_UpdateLocationSmb_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateLocationSmb_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception is thrown when an error occurs in the AWS DataSync service.
HTTP Status Code: 500

 ** InvalidRequestException **
This exception is thrown when the client submits a malformed request.
HTTP Status Code: 400

## See Also
<a name="API_UpdateLocationSmb_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datasync-2018-11-09/UpdateLocationSmb)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datasync-2018-11-09/UpdateLocationSmb)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/UpdateLocationSmb)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datasync-2018-11-09/UpdateLocationSmb)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/UpdateLocationSmb)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datasync-2018-11-09/UpdateLocationSmb)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datasync-2018-11-09/UpdateLocationSmb)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datasync-2018-11-09/UpdateLocationSmb)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datasync-2018-11-09/UpdateLocationSmb)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/UpdateLocationSmb)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
