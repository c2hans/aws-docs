---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-iotmanagedintegrations-credentiallocker.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoTManagedIntegrations::CredentialLocker
<a name="aws-resource-iotmanagedintegrations-credentiallocker"></a>

Create a credential locker.

**Note**
This operation will not trigger the creation of all the manufacturing resources.

## Syntax
<a name="aws-resource-iotmanagedintegrations-credentiallocker-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-iotmanagedintegrations-credentiallocker-syntax.json"></a>

```
{
  "Type" : "AWS::IoTManagedIntegrations::CredentialLocker",
  "Properties" : {
      "[Name](#cfn-iotmanagedintegrations-credentiallocker-name)" : {{String}},
      "[Tags](#cfn-iotmanagedintegrations-credentiallocker-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-iotmanagedintegrations-credentiallocker-syntax.yaml"></a>

```
Type: AWS::IoTManagedIntegrations::CredentialLocker
Properties:
  [Name](#cfn-iotmanagedintegrations-credentiallocker-name): {{String}}
  [Tags](#cfn-iotmanagedintegrations-credentiallocker-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-iotmanagedintegrations-credentiallocker-properties"></a>

`Name`  <a name="cfn-iotmanagedintegrations-credentiallocker-name"></a>
The name of the credential locker.
*Required*: No
*Type*: String
*Pattern*: `^[A-Za-z0-9-_ ]+$`
*Minimum*: `1`
*Maximum*: `128`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-iotmanagedintegrations-credentiallocker-tags"></a>
A set of key/value pairs that are used to manage the credential locker.
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-iotmanagedintegrations-credentiallocker-return-values"></a>

### Ref
<a name="aws-resource-iotmanagedintegrations-credentiallocker-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the name of the credential locker.

### Fn::GetAtt
<a name="aws-resource-iotmanagedintegrations-credentiallocker-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-iotmanagedintegrations-credentiallocker-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the credential locker.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp value of when the credential locker requset occurred.

`Id`  <a name="Id-fn::getatt"></a>
The identifier of the credential locker.

`Identifier`  <a name="Identifier-fn::getatt"></a>
The identifier of the credential locker.
