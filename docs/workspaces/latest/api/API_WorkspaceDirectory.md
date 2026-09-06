---
source_url: https://docs.aws.amazon.com/workspaces/latest/api/API_WorkspaceDirectory.html
---

# WorkspaceDirectory
<a name="API_WorkspaceDirectory"></a>

Describes a directory that is used with Amazon WorkSpaces.

## Contents
<a name="API_WorkspaceDirectory_Contents"></a>

 ** ActiveDirectoryConfig **   <a name="WorkSpaces-Type-WorkspaceDirectory-ActiveDirectoryConfig"></a>
Information about the Active Directory config.
Type: [ActiveDirectoryConfig](API_ActiveDirectoryConfig.md) object
Required: No

 ** Alias **   <a name="WorkSpaces-Type-WorkspaceDirectory-Alias"></a>
The directory alias.
Type: String
Required: No

 ** CertificateBasedAuthProperties **   <a name="WorkSpaces-Type-WorkspaceDirectory-CertificateBasedAuthProperties"></a>
The certificate-based authentication properties used to authenticate SAML 2.0 Identity Provider (IdP) user identities to Active Directory for WorkSpaces login.
Type: [CertificateBasedAuthProperties](API_CertificateBasedAuthProperties.md) object
Required: No

 ** CustomerUserName **   <a name="WorkSpaces-Type-WorkspaceDirectory-CustomerUserName"></a>
The user name for the service account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Required: No

 ** DirectoryId **   <a name="WorkSpaces-Type-WorkspaceDirectory-DirectoryId"></a>
The directory identifier.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 65.
Pattern: `^(d-[0-9a-f]{8,63}$)|(wsd-[0-9a-z]{8,63}$)`
Required: No

 ** DirectoryName **   <a name="WorkSpaces-Type-WorkspaceDirectory-DirectoryName"></a>
The name of the directory.
Type: String
Required: No

 ** DirectoryType **   <a name="WorkSpaces-Type-WorkspaceDirectory-DirectoryType"></a>
The directory type.
Type: String
Valid Values: `SIMPLE_AD | AD_CONNECTOR | CUSTOMER_MANAGED | AWS_IAM_IDENTITY_CENTER`
Required: No

 ** DnsIpAddresses **   <a name="WorkSpaces-Type-WorkspaceDirectory-DnsIpAddresses"></a>
The IP addresses of the DNS servers for the directory.
Type: Array of strings
Required: No

 ** DnsIpv6Addresses **   <a name="WorkSpaces-Type-WorkspaceDirectory-DnsIpv6Addresses"></a>
The IPv6 addresses of the DNS servers for the directory.
Type: Array of strings
Pattern: `^(?:[0-9a-fA-F]{1,4}:){7}[0-9a-fA-F]{1,4}|[0-9a-fA-F]{1,4}(?::[0-9a-fA-F]{1,4}){0,6}::[0-9a-fA-F]{1,4}$`
Required: No

 ** EndpointEncryptionMode **   <a name="WorkSpaces-Type-WorkspaceDirectory-EndpointEncryptionMode"></a>
Endpoint encryption mode that allows you to configure the specified directory between Standard TLS and FIPS 140-2 validated mode.
Type: String
Valid Values: `STANDARD_TLS | FIPS_VALIDATED`
Required: No

 ** ErrorMessage **   <a name="WorkSpaces-Type-WorkspaceDirectory-ErrorMessage"></a>
The error message returned.
Type: String
Required: No

 ** IamRoleId **   <a name="WorkSpaces-Type-WorkspaceDirectory-IamRoleId"></a>
The identifier of the IAM role. This is the role that allows Amazon WorkSpaces to make calls to other services, such as Amazon EC2, on your behalf.
Type: String
Pattern: `^arn:aws[a-z-]{0,7}:[A-Za-z0-9][A-za-z0-9_/.-]{0,62}:[A-za-z0-9_/.-]{0,63}:[A-za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: No

 ** IDCConfig **   <a name="WorkSpaces-Type-WorkspaceDirectory-IDCConfig"></a>
Specifies details about identity center configurations.
Type: [IDCConfig](API_IDCConfig.md) object
Required: No

 ** ipGroupIds **   <a name="WorkSpaces-Type-WorkspaceDirectory-ipGroupIds"></a>
The identifiers of the IP access control groups associated with the directory.
Type: Array of strings
Pattern: `wsipg-[0-9a-z]{8,63}$`
Required: No

 ** MicrosoftEntraConfig **   <a name="WorkSpaces-Type-WorkspaceDirectory-MicrosoftEntraConfig"></a>
Specifies details about Microsoft Entra configurations.
Type: [MicrosoftEntraConfig](API_MicrosoftEntraConfig.md) object
Required: No

 ** RegistrationCode **   <a name="WorkSpaces-Type-WorkspaceDirectory-RegistrationCode"></a>
The registration code for the directory. This is the code that users enter in their Amazon WorkSpaces client application to connect to the directory.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Required: No

 ** SamlProperties **   <a name="WorkSpaces-Type-WorkspaceDirectory-SamlProperties"></a>
Describes the enablement status, user access URL, and relay state parameter name that are used for configuring federation with an SAML 2.0 identity provider.
Type: [SamlProperties](API_SamlProperties.md) object
Required: No

 ** SelfservicePermissions **   <a name="WorkSpaces-Type-WorkspaceDirectory-SelfservicePermissions"></a>
The default self-service permissions for WorkSpaces in the directory.
Type: [SelfservicePermissions](API_SelfservicePermissions.md) object
Required: No

 ** State **   <a name="WorkSpaces-Type-WorkspaceDirectory-State"></a>
The state of the directory's registration with Amazon WorkSpaces. After a directory is deregistered, the `DEREGISTERED` state is returned very briefly before the directory metadata is cleaned up, so this state is rarely returned. To confirm that a directory is deregistered, check for the directory ID by using [ DescribeWorkspaceDirectories](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceDirectories.html). If the directory ID isn't returned, then the directory has been successfully deregistered.
Type: String
Valid Values: `REGISTERING | REGISTERED | DEREGISTERING | DEREGISTERED | ERROR`
Required: No

 ** StreamingProperties **   <a name="WorkSpaces-Type-WorkspaceDirectory-StreamingProperties"></a>
The streaming properties to configure.
Type: [StreamingProperties](API_StreamingProperties.md) object
Required: No

 ** SubnetIds **   <a name="WorkSpaces-Type-WorkspaceDirectory-SubnetIds"></a>
The identifiers of the subnets used with the directory.
Type: Array of strings
Array Members: Maximum number of 2 items.
Length Constraints: Minimum length of 15. Maximum length of 24.
Pattern: `^(subnet-([0-9a-f]{8}|[0-9a-f]{17}))$`
Required: No

 ** Tenancy **   <a name="WorkSpaces-Type-WorkspaceDirectory-Tenancy"></a>
Specifies whether the directory is dedicated or shared. To use Bring Your Own License (BYOL), this value must be set to `DEDICATED`. For more information, see [Bring Your Own Windows Desktop Images](https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html).
Type: String
Valid Values: `DEDICATED | SHARED`
Required: No

 ** UserIdentityType **   <a name="WorkSpaces-Type-WorkspaceDirectory-UserIdentityType"></a>
Indicates the identity type of the specifired user.
Type: String
Valid Values: `CUSTOMER_MANAGED | AWS_DIRECTORY_SERVICE | AWS_IAM_IDENTITY_CENTER`
Required: No

 ** WorkspaceAccessProperties **   <a name="WorkSpaces-Type-WorkspaceDirectory-WorkspaceAccessProperties"></a>
The devices and operating systems that users can use to access WorkSpaces.
Type: [WorkspaceAccessProperties](API_WorkspaceAccessProperties.md) object
Required: No

 ** WorkspaceCreationProperties **   <a name="WorkSpaces-Type-WorkspaceDirectory-WorkspaceCreationProperties"></a>
The default creation properties for all WorkSpaces in the directory.
Type: [DefaultWorkspaceCreationProperties](API_DefaultWorkspaceCreationProperties.md) object
Required: No

 ** WorkspaceDirectoryDescription **   <a name="WorkSpaces-Type-WorkspaceDirectory-WorkspaceDirectoryDescription"></a>
The description of the WorkSpace directory
Type: String
Pattern: `^([a-zA-Z0-9_])[\\a-zA-Z0-9_@#%*+=:?./!\s-]{1,255}$`
Required: No

 ** WorkspaceDirectoryName **   <a name="WorkSpaces-Type-WorkspaceDirectory-WorkspaceDirectoryName"></a>
The name fo the WorkSpace directory.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.\s-]{1,64}$`
Required: No

 ** WorkspaceSecurityGroupId **   <a name="WorkSpaces-Type-WorkspaceDirectory-WorkspaceSecurityGroupId"></a>
The identifier of the security group that is assigned to new WorkSpaces.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 20.
Pattern: `^(sg-([0-9a-f]{8}|[0-9a-f]{17}))$`
Required: No

 ** WorkspaceType **   <a name="WorkSpaces-Type-WorkspaceDirectory-WorkspaceType"></a>
Indicates whether the directory's WorkSpace type is personal or pools.
Type: String
Valid Values: `PERSONAL | POOLS`
Required: No

## See Also
<a name="API_WorkspaceDirectory_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workspaces-2015-04-08/WorkspaceDirectory)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workspaces-2015-04-08/WorkspaceDirectory)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workspaces-2015-04-08/WorkspaceDirectory)
