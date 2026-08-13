---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iotmanagedintegrations-provisioningprofile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTManagedIntegrations::ProvisioningProfile
<a name="aws-resource-iotmanagedintegrations-provisioningprofile"></a>

Create a provisioning profile for a device to execute the provisioning flows using a provisioning template. The provisioning template is a document that defines the set of resources and policies applied to a device during the provisioning process.

## Syntax
<a name="aws-resource-iotmanagedintegrations-provisioningprofile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iotmanagedintegrations-provisioningprofile-syntax.json"></a>

```
{
  "Type" : "AWS::IoTManagedIntegrations::ProvisioningProfile",
  "Properties" : {
      "[CaCertificate](#cfn-iotmanagedintegrations-provisioningprofile-cacertificate)" : {{String}},
      "[Name](#cfn-iotmanagedintegrations-provisioningprofile-name)" : {{String}},
      "[ProvisioningType](#cfn-iotmanagedintegrations-provisioningprofile-provisioningtype)" : {{String}},
      "[Tags](#cfn-iotmanagedintegrations-provisioningprofile-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-iotmanagedintegrations-provisioningprofile-syntax.yaml"></a>

```
Type: AWS::IoTManagedIntegrations::ProvisioningProfile
Properties:
  [CaCertificate](#cfn-iotmanagedintegrations-provisioningprofile-cacertificate): {{String}}
  [Name](#cfn-iotmanagedintegrations-provisioningprofile-name): {{String}}
  [ProvisioningType](#cfn-iotmanagedintegrations-provisioningprofile-provisioningtype): {{String}}
  [Tags](#cfn-iotmanagedintegrations-provisioningprofile-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-iotmanagedintegrations-provisioningprofile-properties"></a>

`CaCertificate`  <a name="cfn-iotmanagedintegrations-provisioningprofile-cacertificate"></a>
The id of the certificate authority (CA) certificate.
*Required*: No
*Type*: String
*Pattern*: `^-----BEGIN CERTIFICATE-----.*(.|\ )*-----END CERTIFICATE-----\n?$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-iotmanagedintegrations-provisioningprofile-name"></a>
The name of the provisioning template.
*Required*: No
*Type*: String
*Pattern*: `^[0-9A-Za-z_-]+$`
*Minimum*: `1`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ProvisioningType`  <a name="cfn-iotmanagedintegrations-provisioningprofile-provisioningtype"></a>
The type of provisioning workflow the device uses for onboarding to IoT managed integrations.
*Required*: Yes
*Type*: String
*Allowed values*: `FLEET_PROVISIONING | JITR`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-iotmanagedintegrations-provisioningprofile-tags"></a>
A set of key/value pairs that are used to manage the provisioning profile.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-iotmanagedintegrations-provisioningprofile-return-values"></a>

### Ref
<a name="aws-resource-iotmanagedintegrations-provisioningprofile-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the provisioning profile template name

### Fn::GetAtt
<a name="aws-resource-iotmanagedintegrations-provisioningprofile-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-iotmanagedintegrations-provisioningprofile-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the provisioning template used in the provisioning profile.

`ClaimCertificate`  <a name="ClaimCertificate-fn::getatt"></a>
The id of the claim certificate.

`Id`  <a name="Id-fn::getatt"></a>
The provisioning profile id.

`Identifier`  <a name="Identifier-fn::getatt"></a>
The provisioning template the device uses for the provisioning process.
