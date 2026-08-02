---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-workspacesthinclient-environment.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::WorkSpacesThinClient::Environment
<a name="aws-resource-workspacesthinclient-environment"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkSpaces Thin Client. After March 31, 2027, you will no longer be able to access the WorkSpaces Thin Client console or WorkSpaces Thin Client resources. For more information, see [Amazon WorkSpaces Thin Client end of support](https://docs.aws.amazon.com/workspaces-thin-client/latest/ug/workspacesthinclient-end-of-support.html).

Describes an environment.

## Syntax
<a name="aws-resource-workspacesthinclient-environment-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-workspacesthinclient-environment-syntax.json"></a>

```
{
  "Type" : "AWS::WorkSpacesThinClient::Environment",
  "Properties" : {
      "[DesiredSoftwareSetId](#cfn-workspacesthinclient-environment-desiredsoftwaresetid)" : {{String}},
      "[DesktopArn](#cfn-workspacesthinclient-environment-desktoparn)" : {{String}},
      "[DesktopEndpoint](#cfn-workspacesthinclient-environment-desktopendpoint)" : {{String}},
      "[DeviceCreationTags](#cfn-workspacesthinclient-environment-devicecreationtags)" : {{[ Tag, ... ]}},
      "[KmsKeyArn](#cfn-workspacesthinclient-environment-kmskeyarn)" : {{String}},
      "[MaintenanceWindow](#cfn-workspacesthinclient-environment-maintenancewindow)" : {{MaintenanceWindow}},
      "[Name](#cfn-workspacesthinclient-environment-name)" : {{String}},
      "[SoftwareSetUpdateMode](#cfn-workspacesthinclient-environment-softwaresetupdatemode)" : {{String}},
      "[SoftwareSetUpdateSchedule](#cfn-workspacesthinclient-environment-softwaresetupdateschedule)" : {{String}},
      "[Tags](#cfn-workspacesthinclient-environment-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-workspacesthinclient-environment-syntax.yaml"></a>

```
Type: AWS::WorkSpacesThinClient::Environment
Properties:
  [DesiredSoftwareSetId](#cfn-workspacesthinclient-environment-desiredsoftwaresetid): {{String}}
  [DesktopArn](#cfn-workspacesthinclient-environment-desktoparn): {{String}}
  [DesktopEndpoint](#cfn-workspacesthinclient-environment-desktopendpoint): {{String}}
  [DeviceCreationTags](#cfn-workspacesthinclient-environment-devicecreationtags): {{
    - Tag}}
  [KmsKeyArn](#cfn-workspacesthinclient-environment-kmskeyarn): {{String}}
  [MaintenanceWindow](#cfn-workspacesthinclient-environment-maintenancewindow): {{
    MaintenanceWindow}}
  [Name](#cfn-workspacesthinclient-environment-name): {{String}}
  [SoftwareSetUpdateMode](#cfn-workspacesthinclient-environment-softwaresetupdatemode): {{String}}
  [SoftwareSetUpdateSchedule](#cfn-workspacesthinclient-environment-softwaresetupdateschedule): {{String}}
  [Tags](#cfn-workspacesthinclient-environment-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-workspacesthinclient-environment-properties"></a>

`DesiredSoftwareSetId`  <a name="cfn-workspacesthinclient-environment-desiredsoftwaresetid"></a>
The ID of the software set to apply.
*Required*: No
*Type*: String
*Pattern*: `^[0-9]{1,9}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DesktopArn`  <a name="cfn-workspacesthinclient-environment-desktoparn"></a>
The Amazon Resource Name (ARN) of the desktop to stream from Amazon WorkSpaces, WorkSpaces Secure Browser, or WorkSpaces Applications.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[\w+=\/,.@-]+:[a-zA-Z0-9\-]+:[a-zA-Z0-9\-]*:[0-9]{0,12}:[a-zA-Z0-9\-\/\._]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DesktopEndpoint`  <a name="cfn-workspacesthinclient-environment-desktopendpoint"></a>
The URL for the identity provider login (only for environments that use WorkSpaces Applications).
*Required*: No
*Type*: String
*Pattern*: `^(https:\/\/)[a-z0-9]+([\-\.]{1}[a-z0-9]+)*\.[a-z]{2,32}(:[0-9]{1,5})?(\/.*)?$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DeviceCreationTags`  <a name="cfn-workspacesthinclient-environment-devicecreationtags"></a>
An array of key-value pairs to apply to the newly created devices for this environment.
*Required*: No
*Type*: Array of [Tag](aws-properties-workspacesthinclient-environment-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`KmsKeyArn`  <a name="cfn-workspacesthinclient-environment-kmskeyarn"></a>
The Amazon Resource Name (ARN) of the AWS Key Management Service key used to encrypt the environment.
*Required*: No
*Type*: String
*Pattern*: `^arn:[\w+=\/,.@-]+:kms:[a-zA-Z0-9\-]*:[0-9]{0,12}:key\/[a-zA-Z0-9-]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MaintenanceWindow`  <a name="cfn-workspacesthinclient-environment-maintenancewindow"></a>
A specification for a time window to apply software updates.
*Required*: No
*Type*: [MaintenanceWindow](aws-properties-workspacesthinclient-environment-maintenancewindow.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-workspacesthinclient-environment-name"></a>
The name of the environment.
*Required*: No
*Type*: String
*Pattern*: `^.+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SoftwareSetUpdateMode`  <a name="cfn-workspacesthinclient-environment-softwaresetupdatemode"></a>
An option to define which software updates to apply.
*Required*: No
*Type*: String
*Allowed values*: `USE_LATEST | USE_DESIRED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SoftwareSetUpdateSchedule`  <a name="cfn-workspacesthinclient-environment-softwaresetupdateschedule"></a>
An option to define if software updates should be applied within a maintenance window.
*Required*: No
*Type*: String
*Allowed values*: `USE_MAINTENANCE_WINDOW | APPLY_IMMEDIATELY`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-workspacesthinclient-environment-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-workspacesthinclient-environment-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-workspacesthinclient-environment-return-values"></a>

### Ref
<a name="aws-resource-workspacesthinclient-environment-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a unique identifier for this resource.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-workspacesthinclient-environment-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-workspacesthinclient-environment-return-values-fn--getatt-fn--getatt"></a>

`ActivationCode`  <a name="ActivationCode-fn::getatt"></a>
The activation code to register a device to the environment.

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the environment.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp of when the environment was created.

`DesktopType`  <a name="DesktopType-fn::getatt"></a>
The type of streaming desktop for the environment.

`PendingSoftwareSetId`  <a name="PendingSoftwareSetId-fn::getatt"></a>
The ID of the software set that is pending to be installed.

`PendingSoftwareSetVersion`  <a name="PendingSoftwareSetVersion-fn::getatt"></a>
The version of the software set that is pending to be installed.

`RegisteredDevicesCount`  <a name="RegisteredDevicesCount-fn::getatt"></a>
The number of devices registered to the environment.

`SoftwareSetComplianceStatus`  <a name="SoftwareSetComplianceStatus-fn::getatt"></a>
Describes if the software currently installed on all devices in the environment is a supported version.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp of when the device was updated.
