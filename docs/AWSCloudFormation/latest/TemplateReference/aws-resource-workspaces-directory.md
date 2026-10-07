---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-workspaces-directory.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpaces::Directory
<a name="aws-resource-workspaces-directory"></a>

<a name="aws-resource-workspaces-directory-description"></a>The `AWS::WorkSpaces::Directory` resource Property description not available. for WorkSpaces.

## Syntax
<a name="aws-resource-workspaces-directory-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-workspaces-directory-syntax.json"></a>

```
{
  "Type" : "AWS::WorkSpaces::Directory",
  "Properties" : {
      "[ActiveDirectoryConfig](#cfn-workspaces-directory-activedirectoryconfig)" : {{ActiveDirectoryConfig}},
      "[CertificateBasedAuthProperties](#cfn-workspaces-directory-certificatebasedauthproperties)" : {{CertificateBasedAuthProperties}},
      "[EnableSelfService](#cfn-workspaces-directory-enableselfservice)" : {{Boolean}},
      "[EndpointEncryptionMode](#cfn-workspaces-directory-endpointencryptionmode)" : {{String}},
      "[IdcInstanceArn](#cfn-workspaces-directory-idcinstancearn)" : {{String}},
      "[IpGroupIds](#cfn-workspaces-directory-ipgroupids)" : {{[ String, ... ]}},
      "[MicrosoftEntraConfig](#cfn-workspaces-directory-microsoftentraconfig)" : {{MicrosoftEntraConfig}},
      "[SamlProperties](#cfn-workspaces-directory-samlproperties)" : {{SamlProperties}},
      "[SelfservicePermissions](#cfn-workspaces-directory-selfservicepermissions)" : {{SelfservicePermissions}},
      "[StreamingProperties](#cfn-workspaces-directory-streamingproperties)" : {{StreamingProperties}},
      "[SubnetIds](#cfn-workspaces-directory-subnetids)" : {{[ String, ... ]}},
      "[Tags](#cfn-workspaces-directory-tags)" : {{[ Tag, ... ]}},
      "[Tenancy](#cfn-workspaces-directory-tenancy)" : {{String}},
      "[UserIdentityType](#cfn-workspaces-directory-useridentitytype)" : {{String}},
      "[WorkspaceAccessProperties](#cfn-workspaces-directory-workspaceaccessproperties)" : {{WorkspaceAccessProperties}},
      "[WorkspaceCreationProperties](#cfn-workspaces-directory-workspacecreationproperties)" : {{DefaultWorkspaceCreationProperties}},
      "[WorkspaceDirectoryDescription](#cfn-workspaces-directory-workspacedirectorydescription)" : {{String}},
      "[WorkspaceDirectoryName](#cfn-workspaces-directory-workspacedirectoryname)" : {{String}},
      "[WorkspaceType](#cfn-workspaces-directory-workspacetype)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-workspaces-directory-syntax.yaml"></a>

```
Type: AWS::WorkSpaces::Directory
Properties:
  [ActiveDirectoryConfig](#cfn-workspaces-directory-activedirectoryconfig): {{
    ActiveDirectoryConfig}}
  [CertificateBasedAuthProperties](#cfn-workspaces-directory-certificatebasedauthproperties): {{
    CertificateBasedAuthProperties}}
  [EnableSelfService](#cfn-workspaces-directory-enableselfservice): {{Boolean}}
  [EndpointEncryptionMode](#cfn-workspaces-directory-endpointencryptionmode): {{String}}
  [IdcInstanceArn](#cfn-workspaces-directory-idcinstancearn): {{String}}
  [IpGroupIds](#cfn-workspaces-directory-ipgroupids): {{
    - String}}
  [MicrosoftEntraConfig](#cfn-workspaces-directory-microsoftentraconfig): {{
    MicrosoftEntraConfig}}
  [SamlProperties](#cfn-workspaces-directory-samlproperties): {{
    SamlProperties}}
  [SelfservicePermissions](#cfn-workspaces-directory-selfservicepermissions): {{
    SelfservicePermissions}}
  [StreamingProperties](#cfn-workspaces-directory-streamingproperties): {{
    StreamingProperties}}
  [SubnetIds](#cfn-workspaces-directory-subnetids): {{
    - String}}
  [Tags](#cfn-workspaces-directory-tags): {{
    - Tag}}
  [Tenancy](#cfn-workspaces-directory-tenancy): {{String}}
  [UserIdentityType](#cfn-workspaces-directory-useridentitytype): {{String}}
  [WorkspaceAccessProperties](#cfn-workspaces-directory-workspaceaccessproperties): {{
    WorkspaceAccessProperties}}
  [WorkspaceCreationProperties](#cfn-workspaces-directory-workspacecreationproperties): {{
    DefaultWorkspaceCreationProperties}}
  [WorkspaceDirectoryDescription](#cfn-workspaces-directory-workspacedirectorydescription): {{String}}
  [WorkspaceDirectoryName](#cfn-workspaces-directory-workspacedirectoryname): {{String}}
  [WorkspaceType](#cfn-workspaces-directory-workspacetype): {{String}}
```

## Properties
<a name="aws-resource-workspaces-directory-properties"></a>

`ActiveDirectoryConfig`  <a name="cfn-workspaces-directory-activedirectoryconfig"></a>
Information about the Active Directory config.
*Required*: No
*Type*: [ActiveDirectoryConfig](aws-properties-workspaces-directory-activedirectoryconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`CertificateBasedAuthProperties`  <a name="cfn-workspaces-directory-certificatebasedauthproperties"></a>
The certificate-based authentication properties used to authenticate SAML 2.0 Identity Provider (IdP) user identities to Active Directory for WorkSpaces login.
*Required*: No
*Type*: [CertificateBasedAuthProperties](aws-properties-workspaces-directory-certificatebasedauthproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableSelfService`  <a name="cfn-workspaces-directory-enableselfservice"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EndpointEncryptionMode`  <a name="cfn-workspaces-directory-endpointencryptionmode"></a>
Endpoint encryption mode that allows you to configure the specified directory between Standard TLS and FIPS 140-2 validated mode.
*Required*: No
*Type*: String
*Allowed values*: `STANDARD_TLS | FIPS_VALIDATED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IdcInstanceArn`  <a name="cfn-workspaces-directory-idcinstancearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws[a-z-]{0,7}:[A-Za-z0-9][A-za-z0-9_/.-]{0,62}:[A-za-z0-9_/.-]{0,63}:[A-za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`IpGroupIds`  <a name="cfn-workspaces-directory-ipgroupids"></a>
The identifiers of the IP access control groups associated with the directory.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MicrosoftEntraConfig`  <a name="cfn-workspaces-directory-microsoftentraconfig"></a>
Specifies details about Microsoft Entra configurations.
*Required*: No
*Type*: [MicrosoftEntraConfig](aws-properties-workspaces-directory-microsoftentraconfig.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SamlProperties`  <a name="cfn-workspaces-directory-samlproperties"></a>
Describes the enablement status, user access URL, and relay state parameter name that are used for configuring federation with an SAML 2.0 identity provider.
*Required*: No
*Type*: [SamlProperties](aws-properties-workspaces-directory-samlproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SelfservicePermissions`  <a name="cfn-workspaces-directory-selfservicepermissions"></a>
The default self-service permissions for WorkSpaces in the directory.
*Required*: No
*Type*: [SelfservicePermissions](aws-properties-workspaces-directory-selfservicepermissions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`StreamingProperties`  <a name="cfn-workspaces-directory-streamingproperties"></a>
The streaming properties to configure.
*Required*: No
*Type*: [StreamingProperties](aws-properties-workspaces-directory-streamingproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SubnetIds`  <a name="cfn-workspaces-directory-subnetids"></a>
The identifiers of the subnets used with the directory.
*Required*: No
*Type*: Array of String
*Minimum*: `15 | 0`
*Maximum*: `24 | 2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-workspaces-directory-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-workspaces-directory-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tenancy`  <a name="cfn-workspaces-directory-tenancy"></a>
Specifies whether the directory is dedicated or shared. To use Bring Your Own License (BYOL), this value must be set to `DEDICATED`. For more information, see [Bring Your Own Windows Desktop Images](https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html).
*Required*: No
*Type*: String
*Allowed values*: `DEDICATED | SHARED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`UserIdentityType`  <a name="cfn-workspaces-directory-useridentitytype"></a>
Indicates the identity type of the specifired user.
*Required*: No
*Type*: String
*Allowed values*: `CUSTOMER_MANAGED | AWS_DIRECTORY_SERVICE | AWS_IAM_IDENTITY_CENTER`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WorkspaceAccessProperties`  <a name="cfn-workspaces-directory-workspaceaccessproperties"></a>
The devices and operating systems that users can use to access WorkSpaces.
*Required*: No
*Type*: [WorkspaceAccessProperties](aws-properties-workspaces-directory-workspaceaccessproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkspaceCreationProperties`  <a name="cfn-workspaces-directory-workspacecreationproperties"></a>
The default creation properties for all WorkSpaces in the directory.
*Required*: No
*Type*: [DefaultWorkspaceCreationProperties](aws-properties-workspaces-directory-defaultworkspacecreationproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`WorkspaceDirectoryDescription`  <a name="cfn-workspaces-directory-workspacedirectorydescription"></a>
The description of the WorkSpace directory
*Required*: No
*Type*: String
*Pattern*: `^([a-zA-Z0-9_])[\\a-zA-Z0-9_@#%*+=:?./!\s-]{1,255}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WorkspaceDirectoryName`  <a name="cfn-workspaces-directory-workspacedirectoryname"></a>
The name fo the WorkSpace directory.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9_.\s-]{1,64}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`WorkspaceType`  <a name="cfn-workspaces-directory-workspacetype"></a>
Indicates whether the directory's WorkSpace type is personal or pools.
*Required*: No
*Type*: String
*Allowed values*: `PERSONAL | POOLS`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-workspaces-directory-return-values"></a>

### Ref
<a name="aws-resource-workspaces-directory-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-workspaces-directory-return-values-fn--getatt"></a>

####
<a name="aws-resource-workspaces-directory-return-values-fn--getatt-fn--getatt"></a>

`Alias`  <a name="Alias-fn::getatt"></a>
The directory alias.

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`CustomerUserName`  <a name="CustomerUserName-fn::getatt"></a>
The user name for the service account.

`DirectoryId`  <a name="DirectoryId-fn::getatt"></a>
The directory identifier.

`DirectoryName`  <a name="DirectoryName-fn::getatt"></a>
The name of the directory.

`DirectoryType`  <a name="DirectoryType-fn::getatt"></a>
The directory type.

`DnsIpAddresses`  <a name="DnsIpAddresses-fn::getatt"></a>
The IP addresses of the DNS servers for the directory.

`DnsIpv6Addresses`  <a name="DnsIpv6Addresses-fn::getatt"></a>
The IPv6 addresses of the DNS servers for the directory.

`IamRoleId`  <a name="IamRoleId-fn::getatt"></a>
The identifier of the IAM role. This is the role that allows Amazon WorkSpaces to make calls to other services, such as Amazon EC2, on your behalf.

`RegistrationCode`  <a name="RegistrationCode-fn::getatt"></a>
The registration code for the directory. This is the code that users enter in their Amazon WorkSpaces client application to connect to the directory.

`State`  <a name="State-fn::getatt"></a>
The state of the directory's registration with Amazon WorkSpaces. After a directory is deregistered, the `DEREGISTERED` state is returned very briefly before the directory metadata is cleaned up, so this state is rarely returned. To confirm that a directory is deregistered, check for the directory ID by using [ DescribeWorkspaceDirectories](https://docs.aws.amazon.com/workspaces/latest/api/API_DescribeWorkspaceDirectories.html). If the directory ID isn't returned, then the directory has been successfully deregistered.

`WorkspaceSecurityGroupId`  <a name="WorkspaceSecurityGroupId-fn::getatt"></a>
The identifier of the security group that is assigned to new WorkSpaces.
