---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-panorama-applicationinstance.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Panorama::ApplicationInstance
<a name="aws-resource-panorama-applicationinstance"></a>

**Important**
End of support notice: On May 31, 2026, AWS will end support for AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama resources. For more information, see [AWS Panorama end of support](https://docs.aws.amazon.com/panorama/latest/dev/panorama-end-of-support.html).

Creates an application instance and deploys it to a device.

## Syntax
<a name="aws-resource-panorama-applicationinstance-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-panorama-applicationinstance-syntax.json"></a>

```
{
  "Type" : "AWS::Panorama::ApplicationInstance",
  "Properties" : {
      "[ApplicationInstanceIdToReplace](#cfn-panorama-applicationinstance-applicationinstanceidtoreplace)" : {{String}},
      "[DefaultRuntimeContextDevice](#cfn-panorama-applicationinstance-defaultruntimecontextdevice)" : {{String}},
      "[Description](#cfn-panorama-applicationinstance-description)" : {{String}},
      "[ManifestOverridesPayload](#cfn-panorama-applicationinstance-manifestoverridespayload)" : {{ManifestOverridesPayload}},
      "[ManifestPayload](#cfn-panorama-applicationinstance-manifestpayload)" : {{ManifestPayload}},
      "[Name](#cfn-panorama-applicationinstance-name)" : {{String}},
      "[RuntimeRoleArn](#cfn-panorama-applicationinstance-runtimerolearn)" : {{String}},
      "[Tags](#cfn-panorama-applicationinstance-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-panorama-applicationinstance-syntax.yaml"></a>

```
Type: AWS::Panorama::ApplicationInstance
Properties:
  [ApplicationInstanceIdToReplace](#cfn-panorama-applicationinstance-applicationinstanceidtoreplace): {{String}}
  [DefaultRuntimeContextDevice](#cfn-panorama-applicationinstance-defaultruntimecontextdevice): {{String}}
  [Description](#cfn-panorama-applicationinstance-description): {{String}}
  [ManifestOverridesPayload](#cfn-panorama-applicationinstance-manifestoverridespayload): {{
    ManifestOverridesPayload}}
  [ManifestPayload](#cfn-panorama-applicationinstance-manifestpayload): {{
    ManifestPayload}}
  [Name](#cfn-panorama-applicationinstance-name): {{String}}
  [RuntimeRoleArn](#cfn-panorama-applicationinstance-runtimerolearn): {{String}}
  [Tags](#cfn-panorama-applicationinstance-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-panorama-applicationinstance-properties"></a>

`ApplicationInstanceIdToReplace`  <a name="cfn-panorama-applicationinstance-applicationinstanceidtoreplace"></a>
The ID of an application instance to replace with the new instance.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9\-\_]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`DefaultRuntimeContextDevice`  <a name="cfn-panorama-applicationinstance-defaultruntimecontextdevice"></a>
The device's ID.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9\-\_]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-panorama-applicationinstance-description"></a>
A description for the application instance.
*Required*: No
*Type*: String
*Pattern*: `^.*$`
*Minimum*: `0`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ManifestOverridesPayload`  <a name="cfn-panorama-applicationinstance-manifestoverridespayload"></a>
Setting overrides for the application manifest.
*Required*: No
*Type*: [ManifestOverridesPayload](aws-properties-panorama-applicationinstance-manifestoverridespayload.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ManifestPayload`  <a name="cfn-panorama-applicationinstance-manifestpayload"></a>
The application's manifest document.
*Required*: Yes
*Type*: [ManifestPayload](aws-properties-panorama-applicationinstance-manifestpayload.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-panorama-applicationinstance-name"></a>
A name for the application instance.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9\-\_]+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RuntimeRoleArn`  <a name="cfn-panorama-applicationinstance-runtimerolearn"></a>
The ARN of a runtime role for the application instance.
*Required*: No
*Type*: String
*Pattern*: `^arn:[a-z0-9][-.a-z0-9]{0,62}:iam::[0-9]{12}:role/.+$`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-panorama-applicationinstance-tags"></a>
Tags for the application instance.
*Required*: No
*Type*: Array of [Tag](aws-properties-panorama-applicationinstance-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-panorama-applicationinstance-return-values"></a>

### Ref
<a name="aws-resource-panorama-applicationinstance-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns a unique identifier for this resource.

### Fn::GetAtt
<a name="aws-resource-panorama-applicationinstance-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-panorama-applicationinstance-return-values-fn--getatt-fn--getatt"></a>

`ApplicationInstanceId`  <a name="ApplicationInstanceId-fn::getatt"></a>
The application instance's ID.

`Arn`  <a name="Arn-fn::getatt"></a>
The application instance's ARN.

`CreatedTime`  <a name="CreatedTime-fn::getatt"></a>
The application instance's created time.

`DefaultRuntimeContextDeviceName`  <a name="DefaultRuntimeContextDeviceName-fn::getatt"></a>
The application instance's default runtime context device name.

`HealthStatus`  <a name="HealthStatus-fn::getatt"></a>
The application instance's health status.

`LastUpdatedTime`  <a name="LastUpdatedTime-fn::getatt"></a>
The application instance's last updated time.

`Status`  <a name="Status-fn::getatt"></a>
The application instance's status.

`StatusDescription`  <a name="StatusDescription-fn::getatt"></a>
The application instance's status description.
