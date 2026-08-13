---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-securityhub-hubv2.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::HubV2
<a name="aws-resource-securityhub-hubv2"></a>

Returns details about the service resource in your account.

## Syntax
<a name="aws-resource-securityhub-hubv2-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-securityhub-hubv2-syntax.json"></a>

```
{
  "Type" : "AWS::SecurityHub::HubV2",
  "Properties" : {
      "[Tags](#cfn-securityhub-hubv2-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-securityhub-hubv2-syntax.yaml"></a>

```
Type: AWS::SecurityHub::HubV2
Properties:
  [Tags](#cfn-securityhub-hubv2-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-securityhub-hubv2-properties"></a>

`Tags`  <a name="cfn-securityhub-hubv2-tags"></a>
The tags to add to the hub V2 resource when you enable Security Hub.
*Required*: No
*Type*: Object of String
*Pattern*: `^(?!aws:)[a-zA-Z+-=._:/]{1,128}$`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-securityhub-hubv2-return-values"></a>

### Ref
<a name="aws-resource-securityhub-hubv2-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the `HubV2Arn` for the `HubV2` resource created: `arn:aws:securityhub:region:123456789012:hubv2/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-securityhub-hubv2-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-securityhub-hubv2-return-values-fn--getatt-fn--getatt"></a>

`HubV2Arn`  <a name="HubV2Arn-fn::getatt"></a>
The ARN of the service resource.

`SubscribedAt`  <a name="SubscribedAt-fn::getatt"></a>
The date and time when the service was enabled in the account.
