---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_FsxProtocolSmb.html
---

# FsxProtocolSmb
<a name="API_FsxProtocolSmb"></a>

Specifies the Server Message Block (SMB) protocol configuration that AWS DataSync uses to access your Amazon FSx for NetApp ONTAP file system's storage virtual machine (SVM). For more information, see [Providing DataSync access to FSx for ONTAP file systems](https://docs.aws.amazon.com/datasync/latest/userguide/create-ontap-location.html#create-ontap-location-access).

## Contents
<a name="API_FsxProtocolSmb_Contents"></a>

 ** User **   <a name="DataSync-Type-FsxProtocolSmb-User"></a>
Specifies a user that can mount and access the files, folders, and metadata in your SVM.
For information about choosing a user with the right level of access for your transfer, see [Using the SMB protocol](https://docs.aws.amazon.com/datasync/latest/userguide/create-ontap-location.html#create-ontap-location-smb).
Type: String
Length Constraints: Maximum length of 104.
Pattern: `^[^\x22\x5B\x5D/\\:;|=,+*?\x3C\x3E]{1,104}$`
Required: Yes

 ** CmkSecretConfig **   <a name="DataSync-Type-FsxProtocolSmb-CmkSecretConfig"></a>
Specifies configuration information for a DataSync-managed secret, which includes the password that DataSync uses to access a specific FSx for ONTAP storage location (using SMB), with a customer-managed AWS KMS key.
When you include this parameter as part of a `CreateLocationFsxOntap` request, you provide only the KMS key ARN. DataSync uses this KMS key together with the `Password` you specify for to create a DataSync-managed secret to store the location access credentials.
Make sure that DataSync has permission to access the KMS key that you specify. For more information, see [ Using a service-managed secret encrypted with a custom AWS KMS key](https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html#service-secret-custom-key).
You can use either `CmkSecretConfig` (with `Password`) or `CustomSecretConfig` (without `Password`) to provide credentials for a `CreateLocationFsxOntap` request. Do not provide both parameters for the same request.
Type: [CmkSecretConfig](API_CmkSecretConfig.md) object
Required: No

 ** CustomSecretConfig **   <a name="DataSync-Type-FsxProtocolSmb-CustomSecretConfig"></a>
Specifies configuration information for a customer-managed Secrets Manager secret where the password for an FSx for ONTAP storage location (using SMB) is stored in plain text, in Secrets Manager. This configuration includes the secret ARN, and the ARN for an IAM role that provides access to the secret. For more information, see [ Using a secret that you manage](https://docs.aws.amazon.com/datasync/latest/userguide/location-credentials.html#custom-secret-custom-key).
You can use either `CmkSecretConfig` (with `Password`) or `CustomSecretConfig` (without `Password`) to provide credentials for a `CreateLocationFsxOntap` request. Do not provide both parameters for the same request.
Type: [CustomSecretConfig](API_CustomSecretConfig.md) object
Required: No

 ** Domain **   <a name="DataSync-Type-FsxProtocolSmb-Domain"></a>
Specifies the name of the Windows domain that your storage virtual machine (SVM) belongs to.
If you have multiple domains in your environment, configuring this setting makes sure that DataSync connects to the right SVM.
If you have multiple Active Directory domains in your environment, configuring this parameter makes sure that DataSync connects to the right SVM.
Type: String
Length Constraints: Maximum length of 253.
Pattern: `^[A-Za-z0-9]((\.|-+)?[A-Za-z0-9]){0,252}$`
Required: No

 ** ManagedSecretConfig **   <a name="DataSync-Type-FsxProtocolSmb-ManagedSecretConfig"></a>
Describes configuration information for a DataSync-managed secret, such as a `Password` that DataSync uses to access a specific storage location. DataSync uses the default AWS-managed KMS key to encrypt this secret in AWS Secrets Manager.
Do not provide this for a `CreateLocation` request. `ManagedSecretConfig` is a ReadOnly property and is only be populated in the `DescribeLocation` response.
Type: [ManagedSecretConfig](API_ManagedSecretConfig.md) object
Required: No

 ** MountOptions **   <a name="DataSync-Type-FsxProtocolSmb-MountOptions"></a>
Specifies the version of the Server Message Block (SMB) protocol that AWS DataSync uses to access an SMB file server.
Type: [SmbMountOptions](API_SmbMountOptions.md) object
Required: No

 ** Password **   <a name="DataSync-Type-FsxProtocolSmb-Password"></a>
Specifies the password of a user who has permission to access your SVM.
Type: String
Length Constraints: Maximum length of 104.
Pattern: `^.{0,104}$`
Required: No

## See Also
<a name="API_FsxProtocolSmb_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/FsxProtocolSmb)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/FsxProtocolSmb)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/FsxProtocolSmb)
