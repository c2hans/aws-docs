---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iotmanagedintegrations-managedthing.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTManagedIntegrations::ManagedThing
<a name="aws-resource-iotmanagedintegrations-managedthing"></a>

Creates a managed thing. A managed thing contains the device identifier, protocol supported, and capabilities of the device in a protocol-specific format.

## Syntax
<a name="aws-resource-iotmanagedintegrations-managedthing-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iotmanagedintegrations-managedthing-syntax.json"></a>

```
{
  "Type" : "AWS::IoTManagedIntegrations::ManagedThing",
  "Properties" : {
      "[AuthenticationMaterial](#cfn-iotmanagedintegrations-managedthing-authenticationmaterial)" : {{String}},
      "[AuthenticationMaterialType](#cfn-iotmanagedintegrations-managedthing-authenticationmaterialtype)" : {{String}},
      "[Brand](#cfn-iotmanagedintegrations-managedthing-brand)" : {{String}},
      "[CapabilityReport](#cfn-iotmanagedintegrations-managedthing-capabilityreport)" : {{CapabilityReport}},
      "[Classification](#cfn-iotmanagedintegrations-managedthing-classification)" : {{String}},
      "[CredentialLockerId](#cfn-iotmanagedintegrations-managedthing-credentiallockerid)" : {{String}},
      "[MetaData](#cfn-iotmanagedintegrations-managedthing-metadata)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Model](#cfn-iotmanagedintegrations-managedthing-model)" : {{String}},
      "[Name](#cfn-iotmanagedintegrations-managedthing-name)" : {{String}},
      "[Owner](#cfn-iotmanagedintegrations-managedthing-owner)" : {{String}},
      "[Role](#cfn-iotmanagedintegrations-managedthing-role)" : {{String}},
      "[SerialNumber](#cfn-iotmanagedintegrations-managedthing-serialnumber)" : {{String}},
      "[Tags](#cfn-iotmanagedintegrations-managedthing-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-iotmanagedintegrations-managedthing-syntax.yaml"></a>

```
Type: AWS::IoTManagedIntegrations::ManagedThing
Properties:
  [AuthenticationMaterial](#cfn-iotmanagedintegrations-managedthing-authenticationmaterial): {{String}}
  [AuthenticationMaterialType](#cfn-iotmanagedintegrations-managedthing-authenticationmaterialtype): {{String}}
  [Brand](#cfn-iotmanagedintegrations-managedthing-brand): {{String}}
  [CapabilityReport](#cfn-iotmanagedintegrations-managedthing-capabilityreport): {{
    CapabilityReport}}
  [Classification](#cfn-iotmanagedintegrations-managedthing-classification): {{String}}
  [CredentialLockerId](#cfn-iotmanagedintegrations-managedthing-credentiallockerid): {{String}}
  [MetaData](#cfn-iotmanagedintegrations-managedthing-metadata): {{
    {{Key}}: {{Value}}}}
  [Model](#cfn-iotmanagedintegrations-managedthing-model): {{String}}
  [Name](#cfn-iotmanagedintegrations-managedthing-name): {{String}}
  [Owner](#cfn-iotmanagedintegrations-managedthing-owner): {{String}}
  [Role](#cfn-iotmanagedintegrations-managedthing-role): {{String}}
  [SerialNumber](#cfn-iotmanagedintegrations-managedthing-serialnumber): {{String}}
  [Tags](#cfn-iotmanagedintegrations-managedthing-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-iotmanagedintegrations-managedthing-properties"></a>

`AuthenticationMaterial`  <a name="cfn-iotmanagedintegrations-managedthing-authenticationmaterial"></a>
The authentication material defining the device connectivity setup requests. The authentication materials used are the device bar code.
*Required*: No
*Type*: String
*Pattern*: `^[0-9A-Za-z!#$%&()*\+\-;<=>?@^_`{|}~\/: ]+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AuthenticationMaterialType`  <a name="cfn-iotmanagedintegrations-managedthing-authenticationmaterialtype"></a>
The type of authentication material used for device connectivity setup requests.
*Required*: No
*Type*: String
*Allowed values*: `WIFI_SETUP_QR_BAR_CODE | ZWAVE_QR_BAR_CODE | ZIGBEE_QR_BAR_CODE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Brand`  <a name="cfn-iotmanagedintegrations-managedthing-brand"></a>
The brand of the device.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9-_ ]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CapabilityReport`  <a name="cfn-iotmanagedintegrations-managedthing-capabilityreport"></a>
A report of the capabilities for the managed thing.
*Required*: No
*Type*: [CapabilityReport](aws-properties-iotmanagedintegrations-managedthing-capabilityreport.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Classification`  <a name="cfn-iotmanagedintegrations-managedthing-classification"></a>
The classification of the managed thing such as light bulb or thermostat.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`CredentialLockerId`  <a name="cfn-iotmanagedintegrations-managedthing-credentiallockerid"></a>
The identifier of the credential locker for the managed thing.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9]*$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`MetaData`  <a name="cfn-iotmanagedintegrations-managedthing-metadata"></a>
The metadata for the managed thing.
The `managedThing metadata` parameter is used for associating attributes with a `managedThing` that can be used for grouping over-the-air (OTA) tasks. Name value pairs in `metadata `can be used in the `OtaTargetQueryString` parameter for the `CreateOtaTask` API operation.
*Required*: No
*Type*: Object of String
*Pattern*: `[a-zA-Z0-9_.,@/:#-]+`
*Maximum*: `800`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Model`  <a name="cfn-iotmanagedintegrations-managedthing-model"></a>
The model of the device.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9-_ ]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-iotmanagedintegrations-managedthing-name"></a>
The name of the managed thing representing the physical device.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Owner`  <a name="cfn-iotmanagedintegrations-managedthing-owner"></a>
Owner of the device, usually an indication of whom the device belongs to. This value should not contain personal identifiable information.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9_.,@-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Role`  <a name="cfn-iotmanagedintegrations-managedthing-role"></a>
The type of device used. This will be the hub controller, cloud device, or IoT device.
*Required*: Yes
*Type*: String
*Allowed values*: `CONTROLLER | DEVICE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SerialNumber`  <a name="cfn-iotmanagedintegrations-managedthing-serialnumber"></a>
The serial number of the device.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9-_ ]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-iotmanagedintegrations-managedthing-tags"></a>
A set of key/value pairs that are used to manage the managed thing.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-iotmanagedintegrations-managedthing-return-values"></a>

### Ref
<a name="aws-resource-iotmanagedintegrations-managedthing-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the managed thing name.

### Fn::GetAtt
<a name="aws-resource-iotmanagedintegrations-managedthing-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-iotmanagedintegrations-managedthing-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the managed thing.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp value of when the device creation request occurred.

`Id`  <a name="Id-fn::getatt"></a>
The id of the managed thing.

`Identifier`  <a name="Identifier-fn::getatt"></a>
The id of the managed thing.

`ProvisioningStatus`  <a name="ProvisioningStatus-fn::getatt"></a>
The provisioning status of the device in the provisioning workflow for onboarding to IoT managed integrations.

`UniversalProductCode`  <a name="UniversalProductCode-fn::getatt"></a>
The universal product code (UPC) of the device model. The UPC is typically used in the United States of America and Canada.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp value of when the managed thing was last updated at.
