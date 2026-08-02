---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-datasync-locationsmb.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationSMB
<a name="aws-resource-datasync-locationsmb"></a>

The `AWS::DataSync::LocationSMB` resource specifies a Server Message Block (SMB) location that AWS DataSync can use as a transfer source or destination.

## Syntax
<a name="aws-resource-datasync-locationsmb-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-datasync-locationsmb-syntax.json"></a>

```
{
  "Type" : "AWS::DataSync::LocationSMB",
  "Properties" : {
      "[AgentArns](#cfn-datasync-locationsmb-agentarns)" : {{[ String, ... ]}},
      "[AuthenticationType](#cfn-datasync-locationsmb-authenticationtype)" : {{String}},
      "[CmkSecretConfig](#cfn-datasync-locationsmb-cmksecretconfig)" : {{CmkSecretConfig}},
      "[CustomSecretConfig](#cfn-datasync-locationsmb-customsecretconfig)" : {{CustomSecretConfig}},
      "[DnsIpAddresses](#cfn-datasync-locationsmb-dnsipaddresses)" : {{[ String, ... ]}},
      "[Domain](#cfn-datasync-locationsmb-domain)" : {{String}},
      "[KerberosKeytab](#cfn-datasync-locationsmb-kerberoskeytab)" : {{String}},
      "[KerberosKrb5Conf](#cfn-datasync-locationsmb-kerberoskrb5conf)" : {{String}},
      "[KerberosPrincipal](#cfn-datasync-locationsmb-kerberosprincipal)" : {{String}},
      "[MountOptions](#cfn-datasync-locationsmb-mountoptions)" : {{MountOptions}},
      "[Password](#cfn-datasync-locationsmb-password)" : {{String}},
      "[ServerHostname](#cfn-datasync-locationsmb-serverhostname)" : {{String}},
      "[Subdirectory](#cfn-datasync-locationsmb-subdirectory)" : {{String}},
      "[Tags](#cfn-datasync-locationsmb-tags)" : {{[ Tag, ... ]}},
      "[User](#cfn-datasync-locationsmb-user)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-datasync-locationsmb-syntax.yaml"></a>

```
Type: AWS::DataSync::LocationSMB
Properties:
  [AgentArns](#cfn-datasync-locationsmb-agentarns): {{
    - String}}
  [AuthenticationType](#cfn-datasync-locationsmb-authenticationtype): {{String}}
  [CmkSecretConfig](#cfn-datasync-locationsmb-cmksecretconfig): {{
    CmkSecretConfig}}
  [CustomSecretConfig](#cfn-datasync-locationsmb-customsecretconfig): {{
    CustomSecretConfig}}
  [DnsIpAddresses](#cfn-datasync-locationsmb-dnsipaddresses): {{
    - String}}
  [Domain](#cfn-datasync-locationsmb-domain): {{String}}
  [KerberosKeytab](#cfn-datasync-locationsmb-kerberoskeytab): {{String}}
  [KerberosKrb5Conf](#cfn-datasync-locationsmb-kerberoskrb5conf): {{String}}
  [KerberosPrincipal](#cfn-datasync-locationsmb-kerberosprincipal): {{String}}
  [MountOptions](#cfn-datasync-locationsmb-mountoptions): {{
    MountOptions}}
  [Password](#cfn-datasync-locationsmb-password): {{String}}
  [ServerHostname](#cfn-datasync-locationsmb-serverhostname): {{String}}
  [Subdirectory](#cfn-datasync-locationsmb-subdirectory): {{String}}
  [Tags](#cfn-datasync-locationsmb-tags): {{
    - Tag}}
  [User](#cfn-datasync-locationsmb-user): {{String}}
```

## Properties
<a name="aws-resource-datasync-locationsmb-properties"></a>

`AgentArns`  <a name="cfn-datasync-locationsmb-agentarns"></a>
Specifies the DataSync agent (or agents) that can connect to your SMB file server. You specify an agent by using its Amazon Resource Name (ARN).
*Required*: Yes
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `128 | 8`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AuthenticationType`  <a name="cfn-datasync-locationsmb-authenticationtype"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `NTLM | KERBEROS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CmkSecretConfig`  <a name="cfn-datasync-locationsmb-cmksecretconfig"></a>
Specifies configuration information for a DataSync-managed secret, such as an authentication token, secret key, password, or Kerberos keytab that DataSync uses to access a specific storage location, with a customer-managed AWS KMS key.
You can use either `CmkSecretConfig` or `CustomSecretConfig` to provide credentials for a `CreateLocation` request. Do not provide both parameters for the same request.
*Required*: No
*Type*: [CmkSecretConfig](aws-properties-datasync-locationsmb-cmksecretconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CustomSecretConfig`  <a name="cfn-datasync-locationsmb-customsecretconfig"></a>
Specifies configuration information for a customer-managed Secrets Manager secret where a storage location credentials is stored in Secrets Manager as plain text (for authentication token, secret key, or password) or as binary (for Kerberos keytab). This configuration includes the secret ARN, and the ARN for an IAM role that provides access to the secret.
You can use either `CmkSecretConfig` or `CustomSecretConfig` to provide credentials for a `CreateLocation` request. Do not provide both parameters for the same request.
*Required*: No
*Type*: [CustomSecretConfig](aws-properties-datasync-locationsmb-customsecretconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DnsIpAddresses`  <a name="cfn-datasync-locationsmb-dnsipaddresses"></a>
Property description not available.
*Required*: No
*Type*: Array of String
*Minimum*: `7`
*Maximum*: `15 | 2`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Domain`  <a name="cfn-datasync-locationsmb-domain"></a>
Specifies the Windows domain name that your SMB file server belongs to. This parameter applies only if `AuthenticationType` is set to `NTLM`.
If you have multiple domains in your environment, configuring this parameter makes sure that DataSync connects to the right file server.
*Required*: No
*Type*: String
*Pattern*: `^([A-Za-z0-9]+[A-Za-z0-9-.]*)*[A-Za-z0-9-]*[A-Za-z0-9]$`
*Maximum*: `253`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KerberosKeytab`  <a name="cfn-datasync-locationsmb-kerberoskeytab"></a>
Property description not available.
*Required*: No
*Type*: String
*Maximum*: `87384`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KerberosKrb5Conf`  <a name="cfn-datasync-locationsmb-kerberoskrb5conf"></a>
Property description not available.
*Required*: No
*Type*: String
*Maximum*: `174764`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KerberosPrincipal`  <a name="cfn-datasync-locationsmb-kerberosprincipal"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^.+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MountOptions`  <a name="cfn-datasync-locationsmb-mountoptions"></a>
Specifies the version of the SMB protocol that DataSync uses to access your SMB file server.
*Required*: No
*Type*: [MountOptions](aws-properties-datasync-locationsmb-mountoptions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Password`  <a name="cfn-datasync-locationsmb-password"></a>
Specifies the password of the user who can mount your SMB file server and has permission to access the files and folders involved in your transfer. This parameter applies only if `AuthenticationType` is set to `NTLM`.
*Required*: No
*Type*: String
*Pattern*: `^.{0,104}$`
*Maximum*: `104`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServerHostname`  <a name="cfn-datasync-locationsmb-serverhostname"></a>
Specifies the domain name or IP address (IPv4 or IPv6) of the SMB file server that your DataSync agent connects to.
If you're using Kerberos authentication, you must specify a domain name.
*Required*: No
*Type*: String
*Pattern*: `^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-]*[A-Za-z0-9])$`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subdirectory`  <a name="cfn-datasync-locationsmb-subdirectory"></a>
Specifies the name of the share exported by your SMB file server where DataSync will read or write data. You can include a subdirectory in the share path (for example, `/path/to/subdirectory`). Make sure that other SMB clients in your network can also mount this path.
To copy all data in the subdirectory, DataSync must be able to mount the SMB share and access all of its data. For more information, see [Providing DataSync access to SMB file servers](https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html#configuring-smb-permissions).
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_\-\+\./\(\)\$\p{Zs}]+$`
*Maximum*: `4096`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-datasync-locationsmb-tags"></a>
Specifies labels that help you categorize, filter, and search for your AWS resources. We recommend creating at least a name tag for your location.
*Required*: No
*Type*: Array of [Tag](aws-properties-datasync-locationsmb-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`User`  <a name="cfn-datasync-locationsmb-user"></a>
Specifies the user that can mount and access the files, folders, and file metadata in your SMB file server. This parameter applies only if `AuthenticationType` is set to `NTLM`.
For information about choosing a user with the right level of access for your transfer, see [Providing DataSync access to SMB file servers](https://docs.aws.amazon.com/datasync/latest/userguide/create-smb-location.html#configuring-smb-permissions).
*Required*: No
*Type*: String
*Pattern*: `^[^\x5B\x5D\\/:;|=,+*?]{1,104}$`
*Maximum*: `104`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-datasync-locationsmb-return-values"></a>

### Ref
<a name="aws-resource-datasync-locationsmb-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the location resource Amazon Resource Name (ARN). For example:

 `arn:aws:datasync:us-east-2:111222333444:location/loc-07db7abfc326c50s3`

For more information about using the `Ref` function, see [Ref](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-datasync-locationsmb-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [Fn::GetAtt](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-datasync-locationsmb-return-values-fn--getatt-fn--getatt"></a>

`CmkSecretConfig.SecretArn`  <a name="CmkSecretConfig.SecretArn-fn::getatt"></a>
Property description not available.

`LocationArn`  <a name="LocationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the specified SMB location.

`LocationUri`  <a name="LocationUri-fn::getatt"></a>
The URI of the specified SMB location.

## Examples
<a name="aws-resource-datasync-locationsmb--examples"></a>

### Creating an SMB location
<a name="aws-resource-datasync-locationsmb--examples--Creating_an_SMB_location"></a>

The following example specifies an SMB location for DataSync. In this example, the SMB location uses the domain `EXAMPLE` with SMB version 3. The server hostname is `MyServer@example.com`, and the SMB location is in the `/share` subdirectory. This example also specifies the user ID `user-1` for NTLM authentication.

#### JSON
<a name="aws-resource-datasync-locationsmb--examples--Creating_an_SMB_location--json"></a>

```
{
    "AWSTemplateFormatVersion": "2010-09-09",
    "Description": "Creates an SMB location for DataSync",
    "Resources": {
        "LocationSMB": {
            "Type": "AWS::DataSync::LocationSMB",
            "Properties": {
                "AgentArns": [
                    "arn:aws:datasync:us-east-2:111222333444:agent/agent-0b0addbeef44b3nfs,",
                    "arn:aws:datasync:us-east-2:111222333444:agent/agent-2345noo35nnee1123ovo3"
                ],
                "Domain": "EXAMPLE",
                "AuthenticationType": "NTLM",
                "MountOptions": {
                    "Version": "SMB3"
                },
                "Password": "Password",
                "ServerHostname": "MyServer.example.com",
                "Subdirectory": "/share",
                "User": "user-1"
            }
        }
    }
}
```

#### YAML
<a name="aws-resource-datasync-locationsmb--examples--Creating_an_SMB_location--yaml"></a>

```
AWSTemplateFormatVersion: 2010-09-09
Description: Creates an SMB location for DataSync
Resources:
  LocationSMB:
    Type: AWS::DataSync::LocationSMB
    Properties:
      AgentArns:
        - arn:aws:datasync:us-east-2:111222333444:agent/agent-0b0addbeef44b3nfs,
        - arn:aws:datasync:us-east-2:111222333444:agent/agent-2345noo35nnee1123ovo3
      Domain: EXAMPLE
      AuthenticationType: NTLM
      MountOptions:
        Version: SMB3
      Password: Password
      ServerHostname: MyServer.example.com
      Subdirectory: /share
      User: user-1
```
