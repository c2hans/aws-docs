---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-bedrockagentcore-capacityprovider-launchparameters.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BedrockAgentCore::CapacityProvider LaunchParameters
<a name="aws-properties-bedrockagentcore-capacityprovider-launchparameters"></a>

<a name="aws-properties-bedrockagentcore-capacityprovider-launchparameters-description"></a>The `LaunchParameters` property type specifies Property description not available. for an [AWS::BedrockAgentCore::CapacityProvider](aws-resource-bedrockagentcore-capacityprovider.md).

## Syntax
<a name="aws-properties-bedrockagentcore-capacityprovider-launchparameters-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-bedrockagentcore-capacityprovider-launchparameters-syntax.json"></a>

```
{
  "[CapacityReservationSpecification](#cfn-bedrockagentcore-capacityprovider-launchparameters-capacityreservationspecification)" : {{CapacityReservationSpecification}},
  "[EphemeralVolumes](#cfn-bedrockagentcore-capacityprovider-launchparameters-ephemeralvolumes)" : {{[ EphemeralBlockDeviceMapping, ... ]}},
  "[InstanceProfileArn](#cfn-bedrockagentcore-capacityprovider-launchparameters-instanceprofilearn)" : {{String}},
  "[InstanceRequirements](#cfn-bedrockagentcore-capacityprovider-launchparameters-instancerequirements)" : {{InstanceRequirements}},
  "[LicenseSpecifications](#cfn-bedrockagentcore-capacityprovider-launchparameters-licensespecifications)" : {{[ LicenseSpecification, ... ]}},
  "[Monitoring](#cfn-bedrockagentcore-capacityprovider-launchparameters-monitoring)" : {{String}},
  "[OperatingSystem](#cfn-bedrockagentcore-capacityprovider-launchparameters-operatingsystem)" : {{String}},
  "[PropagatedTags](#cfn-bedrockagentcore-capacityprovider-launchparameters-propagatedtags)" : {{{{{Key}}: {{Value}}, ...}}},
  "[SshKeyName](#cfn-bedrockagentcore-capacityprovider-launchparameters-sshkeyname)" : {{String}}
}
```

### YAML
<a name="aws-properties-bedrockagentcore-capacityprovider-launchparameters-syntax.yaml"></a>

```
  [CapacityReservationSpecification](#cfn-bedrockagentcore-capacityprovider-launchparameters-capacityreservationspecification): {{
    CapacityReservationSpecification}}
  [EphemeralVolumes](#cfn-bedrockagentcore-capacityprovider-launchparameters-ephemeralvolumes): {{
    - EphemeralBlockDeviceMapping}}
  [InstanceProfileArn](#cfn-bedrockagentcore-capacityprovider-launchparameters-instanceprofilearn): {{String}}
  [InstanceRequirements](#cfn-bedrockagentcore-capacityprovider-launchparameters-instancerequirements): {{
    InstanceRequirements}}
  [LicenseSpecifications](#cfn-bedrockagentcore-capacityprovider-launchparameters-licensespecifications): {{
    - LicenseSpecification}}
  [Monitoring](#cfn-bedrockagentcore-capacityprovider-launchparameters-monitoring): {{String}}
  [OperatingSystem](#cfn-bedrockagentcore-capacityprovider-launchparameters-operatingsystem): {{String}}
  [PropagatedTags](#cfn-bedrockagentcore-capacityprovider-launchparameters-propagatedtags): {{
    {{Key}}: {{Value}}}}
  [SshKeyName](#cfn-bedrockagentcore-capacityprovider-launchparameters-sshkeyname): {{String}}
```

## Properties
<a name="aws-properties-bedrockagentcore-capacityprovider-launchparameters-properties"></a>

`CapacityReservationSpecification`  <a name="cfn-bedrockagentcore-capacityprovider-launchparameters-capacityreservationspecification"></a>
Property description not available.
*Required*: No
*Type*: [CapacityReservationSpecification](aws-properties-bedrockagentcore-capacityprovider-capacityreservationspecification.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`EphemeralVolumes`  <a name="cfn-bedrockagentcore-capacityprovider-launchparameters-ephemeralvolumes"></a>
Property description not available.
*Required*: No
*Type*: Array of [EphemeralBlockDeviceMapping](aws-properties-bedrockagentcore-capacityprovider-ephemeralblockdevicemapping.md)
*Maximum*: `5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceProfileArn`  <a name="cfn-bedrockagentcore-capacityprovider-launchparameters-instanceprofilearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^arn:aws(-[^:]+)?:iam::[0-9]{12}:instance-profile/([!-~]{1,510}/)?([\w+=,.@-]{1,128})$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceRequirements`  <a name="cfn-bedrockagentcore-capacityprovider-launchparameters-instancerequirements"></a>
Property description not available.
*Required*: Yes
*Type*: [InstanceRequirements](aws-properties-bedrockagentcore-capacityprovider-instancerequirements.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`LicenseSpecifications`  <a name="cfn-bedrockagentcore-capacityprovider-launchparameters-licensespecifications"></a>
Property description not available.
*Required*: No
*Type*: Array of [LicenseSpecification](aws-properties-bedrockagentcore-capacityprovider-licensespecification.md)
*Maximum*: `5`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Monitoring`  <a name="cfn-bedrockagentcore-capacityprovider-launchparameters-monitoring"></a>
Property description not available.
*Required*: No
*Type*: String
*Allowed values*: `BASIC | DETAILED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`OperatingSystem`  <a name="cfn-bedrockagentcore-capacityprovider-launchparameters-operatingsystem"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `LINUX_X86_64 | LINUX_ARM64 | MAC_ARM64 | WINDOWS_X86_64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PropagatedTags`  <a name="cfn-bedrockagentcore-capacityprovider-launchparameters-propagatedtags"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `^.+$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SshKeyName`  <a name="cfn-bedrockagentcore-capacityprovider-launchparameters-sshkeyname"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[!-~][ -~]*[!-~]$|^[!-~]$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
