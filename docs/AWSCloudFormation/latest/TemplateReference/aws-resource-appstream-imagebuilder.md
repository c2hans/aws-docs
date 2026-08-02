---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-appstream-imagebuilder.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AppStream::ImageBuilder
<a name="aws-resource-appstream-imagebuilder"></a>

The `AWS::AppStream::ImageBuilder` resource creates an image builder for Amazon WorkSpaces Applications. An image builder is a virtual machine that is used to create an image.

The initial state of the image builder is `PENDING`. When it is ready, the state is `RUNNING`.

## Syntax
<a name="aws-resource-appstream-imagebuilder-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-appstream-imagebuilder-syntax.json"></a>

```
{
  "Type" : "AWS::AppStream::ImageBuilder",
  "Properties" : {
      "[AccessEndpoints](#cfn-appstream-imagebuilder-accessendpoints)" : {{[ AccessEndpoint, ... ]}},
      "[AppstreamAgentVersion](#cfn-appstream-imagebuilder-appstreamagentversion)" : {{String}},
      "[Description](#cfn-appstream-imagebuilder-description)" : {{String}},
      "[DisplayName](#cfn-appstream-imagebuilder-displayname)" : {{String}},
      "[DomainJoinInfo](#cfn-appstream-imagebuilder-domainjoininfo)" : {{DomainJoinInfo}},
      "[EnableDefaultInternetAccess](#cfn-appstream-imagebuilder-enabledefaultinternetaccess)" : {{Boolean}},
      "[IamRoleArn](#cfn-appstream-imagebuilder-iamrolearn)" : {{String}},
      "[ImageArn](#cfn-appstream-imagebuilder-imagearn)" : {{String}},
      "[ImageName](#cfn-appstream-imagebuilder-imagename)" : {{String}},
      "[InstanceType](#cfn-appstream-imagebuilder-instancetype)" : {{String}},
      "[Name](#cfn-appstream-imagebuilder-name)" : {{String}},
      "[RootVolumeConfig](#cfn-appstream-imagebuilder-rootvolumeconfig)" : {{VolumeConfig}},
      "[SoftwaresToInstall](#cfn-appstream-imagebuilder-softwarestoinstall)" : {{[ String, ... ]}},
      "[SoftwaresToUninstall](#cfn-appstream-imagebuilder-softwarestouninstall)" : {{[ String, ... ]}},
      "[Tags](#cfn-appstream-imagebuilder-tags)" : {{[ Tag, ... ]}},
      "[VpcConfig](#cfn-appstream-imagebuilder-vpcconfig)" : {{VpcConfig}}
    }
}
```

### YAML
<a name="aws-resource-appstream-imagebuilder-syntax.yaml"></a>

```
Type: AWS::AppStream::ImageBuilder
Properties:
  [AccessEndpoints](#cfn-appstream-imagebuilder-accessendpoints): {{
    - AccessEndpoint}}
  [AppstreamAgentVersion](#cfn-appstream-imagebuilder-appstreamagentversion): {{String}}
  [Description](#cfn-appstream-imagebuilder-description): {{String}}
  [DisplayName](#cfn-appstream-imagebuilder-displayname): {{String}}
  [DomainJoinInfo](#cfn-appstream-imagebuilder-domainjoininfo): {{
    DomainJoinInfo}}
  [EnableDefaultInternetAccess](#cfn-appstream-imagebuilder-enabledefaultinternetaccess): {{Boolean}}
  [IamRoleArn](#cfn-appstream-imagebuilder-iamrolearn): {{String}}
  [ImageArn](#cfn-appstream-imagebuilder-imagearn): {{String}}
  [ImageName](#cfn-appstream-imagebuilder-imagename): {{String}}
  [InstanceType](#cfn-appstream-imagebuilder-instancetype): {{String}}
  [Name](#cfn-appstream-imagebuilder-name): {{String}}
  [RootVolumeConfig](#cfn-appstream-imagebuilder-rootvolumeconfig): {{
    VolumeConfig}}
  [SoftwaresToInstall](#cfn-appstream-imagebuilder-softwarestoinstall): {{
    - String}}
  [SoftwaresToUninstall](#cfn-appstream-imagebuilder-softwarestouninstall): {{
    - String}}
  [Tags](#cfn-appstream-imagebuilder-tags): {{
    - Tag}}
  [VpcConfig](#cfn-appstream-imagebuilder-vpcconfig): {{
    VpcConfig}}
```

## Properties
<a name="aws-resource-appstream-imagebuilder-properties"></a>

`AccessEndpoints`  <a name="cfn-appstream-imagebuilder-accessendpoints"></a>
The list of virtual private cloud (VPC) interface endpoint objects. Administrators can connect to the image builder only through the specified endpoints.
*Required*: No
*Type*: Array of [AccessEndpoint](aws-properties-appstream-imagebuilder-accessendpoint.md)
*Minimum*: `1`
*Maximum*: `4`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`AppstreamAgentVersion`  <a name="cfn-appstream-imagebuilder-appstreamagentversion"></a>
The version of the WorkSpaces Applications agent to use for this image builder. To use the latest version of the WorkSpaces Applications agent, specify [LATEST].
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-appstream-imagebuilder-description"></a>
The description to display.
*Required*: No
*Type*: String
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-appstream-imagebuilder-displayname"></a>
The image builder name to display.
*Required*: No
*Type*: String
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DomainJoinInfo`  <a name="cfn-appstream-imagebuilder-domainjoininfo"></a>
The name of the directory and organizational unit (OU) to use to join the image builder to a Microsoft Active Directory domain.
*Required*: No
*Type*: [DomainJoinInfo](aws-properties-appstream-imagebuilder-domainjoininfo.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EnableDefaultInternetAccess`  <a name="cfn-appstream-imagebuilder-enabledefaultinternetaccess"></a>
Enables or disables default internet access for the image builder.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IamRoleArn`  <a name="cfn-appstream-imagebuilder-iamrolearn"></a>
The ARN of the IAM role that is applied to the image builder. To assume a role, the image builder calls the AWS Security Token Service`AssumeRole` API operation and passes the ARN of the role to use. The operation creates a new session with temporary credentials. WorkSpaces Applications retrieves the temporary credentials and creates the **appstream\_machine\_role** credential profile on the instance.
For more information, see [Using an IAM Role to Grant Permissions to Applications and Scripts Running on WorkSpaces Applications Streaming Instances](https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html) in the *Amazon WorkSpaces Applications Administration Guide*.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageArn`  <a name="cfn-appstream-imagebuilder-imagearn"></a>
The ARN of the public, private, or shared image to use.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ImageName`  <a name="cfn-appstream-imagebuilder-imagename"></a>
The name of the image used to create the image builder.
*Required*: No
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceType`  <a name="cfn-appstream-imagebuilder-instancetype"></a>
The instance type to use when launching the image builder. The following instance types are available:
+ stream.standard.small
+ stream.standard.medium
+ stream.standard.large
+ stream.compute.large
+ stream.compute.xlarge
+ stream.compute.2xlarge
+ stream.compute.4xlarge
+ stream.compute.8xlarge
+ stream.memory.large
+ stream.memory.xlarge
+ stream.memory.2xlarge
+ stream.memory.4xlarge
+ stream.memory.8xlarge
+ stream.memory.z1d.large
+ stream.memory.z1d.xlarge
+ stream.memory.z1d.2xlarge
+ stream.memory.z1d.3xlarge
+ stream.memory.z1d.6xlarge
+ stream.memory.z1d.12xlarge
+ stream.graphics-design.large
+ stream.graphics-design.xlarge
+ stream.graphics-design.2xlarge
+ stream.graphics-design.4xlarge
+ stream.graphics.g4dn.xlarge
+ stream.graphics.g4dn.2xlarge
+ stream.graphics.g4dn.4xlarge
+ stream.graphics.g4dn.8xlarge
+ stream.graphics.g4dn.12xlarge
+ stream.graphics.g4dn.16xlarge
+ stream.graphics.g5.xlarge
+ stream.graphics.g5.2xlarge
+ stream.graphics.g5.4xlarge
+ stream.graphics.g5.8xlarge
+ stream.graphics.g5.16xlarge
+ stream.graphics.g5.12xlarge
+ stream.graphics.g5.24xlarge
+ stream.graphics.g6.xlarge
+ stream.graphics.g6.2xlarge
+ stream.graphics.g6.4xlarge
+ stream.graphics.g6.8xlarge
+ stream.graphics.g6.16xlarge
+ stream.graphics.g6.12xlarge
+ stream.graphics.g6.24xlarge
+ stream.graphics.gr6.4xlarge
+ stream.graphics.gr6.8xlarge
+ stream.graphics.g6f.large
+ stream.graphics.g6f.xlarge
+ stream.graphics.g6f.2xlarge
+ stream.graphics.g6f.4xlarge
+ stream.graphics.gr6f.4xlarge
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-appstream-imagebuilder-name"></a>
A unique name for the image builder.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RootVolumeConfig`  <a name="cfn-appstream-imagebuilder-rootvolumeconfig"></a>
The current configuration of the root volume for the image builder, including the storage size in GB.
*Required*: No
*Type*: [VolumeConfig](aws-properties-appstream-imagebuilder-volumeconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SoftwaresToInstall`  <a name="cfn-appstream-imagebuilder-softwarestoinstall"></a>
The list of license included applications to install on the image builder during creation.
Possible values include the following:
+ Microsoft\_Office\_2021\_LTSC\_Professional\_Plus\_32Bit
+ Microsoft\_Office\_2021\_LTSC\_Professional\_Plus\_64Bit
+ Microsoft\_Office\_2024\_LTSC\_Professional\_Plus\_32Bit
+ Microsoft\_Office\_2024\_LTSC\_Professional\_Plus\_64Bit
+ Microsoft\_Visio\_2021\_LTSC\_Professional\_32Bit
+ Microsoft\_Visio\_2021\_LTSC\_Professional\_64Bit
+ Microsoft\_Visio\_2024\_LTSC\_Professional\_32Bit
+ Microsoft\_Visio\_2024\_LTSC\_Professional\_64Bit
+ Microsoft\_Project\_2021\_Professional\_32Bit
+ Microsoft\_Project\_2021\_Professional\_64Bit
+ Microsoft\_Project\_2024\_Professional\_32Bit
+ Microsoft\_Project\_2024\_Professional\_64Bit
+ Microsoft\_Office\_2021\_LTSC\_Standard\_32Bit
+ Microsoft\_Office\_2021\_LTSC\_Standard\_64Bit
+ Microsoft\_Office\_2024\_LTSC\_Standard\_32Bit
+ Microsoft\_Office\_2024\_LTSC\_Standard\_64Bit
+ Microsoft\_Visio\_2021\_LTSC\_Standard\_32Bit
+ Microsoft\_Visio\_2021\_LTSC\_Standard\_64Bit
+ Microsoft\_Visio\_2024\_LTSC\_Standard\_32Bit
+ Microsoft\_Visio\_2024\_LTSC\_Standard\_64Bit
+ Microsoft\_Project\_2021\_Standard\_32Bit
+ Microsoft\_Project\_2021\_Standard\_64Bit
+ Microsoft\_Project\_2024\_Standard\_32Bit
+ Microsoft\_Project\_2024\_Standard\_64Bit
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SoftwaresToUninstall`  <a name="cfn-appstream-imagebuilder-softwarestouninstall"></a>
The list of license included applications to uninstall from the image builder during creation.
Possible values include the following:
+ Microsoft\_Office\_2021\_LTSC\_Professional\_Plus\_32Bit
+ Microsoft\_Office\_2021\_LTSC\_Professional\_Plus\_64Bit
+ Microsoft\_Office\_2024\_LTSC\_Professional\_Plus\_32Bit
+ Microsoft\_Office\_2024\_LTSC\_Professional\_Plus\_64Bit
+ Microsoft\_Visio\_2021\_LTSC\_Professional\_32Bit
+ Microsoft\_Visio\_2021\_LTSC\_Professional\_64Bit
+ Microsoft\_Visio\_2024\_LTSC\_Professional\_32Bit
+ Microsoft\_Visio\_2024\_LTSC\_Professional\_64Bit
+ Microsoft\_Project\_2021\_Professional\_32Bit
+ Microsoft\_Project\_2021\_Professional\_64Bit
+ Microsoft\_Project\_2024\_Professional\_32Bit
+ Microsoft\_Project\_2024\_Professional\_64Bit
+ Microsoft\_Office\_2021\_LTSC\_Standard\_32Bit
+ Microsoft\_Office\_2021\_LTSC\_Standard\_64Bit
+ Microsoft\_Office\_2024\_LTSC\_Standard\_32Bit
+ Microsoft\_Office\_2024\_LTSC\_Standard\_64Bit
+ Microsoft\_Visio\_2021\_LTSC\_Standard\_32Bit
+ Microsoft\_Visio\_2021\_LTSC\_Standard\_64Bit
+ Microsoft\_Visio\_2024\_LTSC\_Standard\_32Bit
+ Microsoft\_Visio\_2024\_LTSC\_Standard\_64Bit
+ Microsoft\_Project\_2021\_Standard\_32Bit
+ Microsoft\_Project\_2021\_Standard\_64Bit
+ Microsoft\_Project\_2024\_Standard\_32Bit
+ Microsoft\_Project\_2024\_Standard\_64Bit
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-appstream-imagebuilder-tags"></a>
An array of key-value pairs.
*Required*: No
*Type*: Array of [Tag](aws-properties-appstream-imagebuilder-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcConfig`  <a name="cfn-appstream-imagebuilder-vpcconfig"></a>
The VPC configuration for the image builder. You can specify only one subnet.
*Required*: No
*Type*: [VpcConfig](aws-properties-appstream-imagebuilder-vpcconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-appstream-imagebuilder-return-values"></a>

### Ref
<a name="aws-resource-appstream-imagebuilder-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-appstream-imagebuilder-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-appstream-imagebuilder-return-values-fn--getatt-fn--getatt"></a>

`StreamingUrl`  <a name="StreamingUrl-fn::getatt"></a>
The URL to start an image builder streaming session, returned as a string.

## See also
<a name="aws-resource-appstream-imagebuilder--seealso"></a>
+ [CreateImageBuilder](https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateImageBuilder.html) in the *Amazon WorkSpaces Applications API Reference*
