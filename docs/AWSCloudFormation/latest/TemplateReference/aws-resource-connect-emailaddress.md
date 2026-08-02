---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-connect-emailaddress.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::EmailAddress
<a name="aws-resource-connect-emailaddress"></a>

Create new email address in the specified Connect Customer instance. For more information about email addresses, see [Create email addresses](https://docs.aws.amazon.com/connect/latest/adminguide/create-email-address1.html) in the Connect Customer Administrator Guide.

## Syntax
<a name="aws-resource-connect-emailaddress-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-connect-emailaddress-syntax.json"></a>

```
{
  "Type" : "AWS::Connect::EmailAddress",
  "Properties" : {
      "[AliasConfigurations](#cfn-connect-emailaddress-aliasconfigurations)" : {{[ AliasConfiguration, ... ]}},
      "[Description](#cfn-connect-emailaddress-description)" : {{String}},
      "[DisplayName](#cfn-connect-emailaddress-displayname)" : {{String}},
      "[EmailAddress](#cfn-connect-emailaddress-emailaddress)" : {{String}},
      "[InstanceArn](#cfn-connect-emailaddress-instancearn)" : {{String}},
      "[Tags](#cfn-connect-emailaddress-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-connect-emailaddress-syntax.yaml"></a>

```
Type: AWS::Connect::EmailAddress
Properties:
  [AliasConfigurations](#cfn-connect-emailaddress-aliasconfigurations): {{
    - AliasConfiguration}}
  [Description](#cfn-connect-emailaddress-description): {{String}}
  [DisplayName](#cfn-connect-emailaddress-displayname): {{String}}
  [EmailAddress](#cfn-connect-emailaddress-emailaddress): {{String}}
  [InstanceArn](#cfn-connect-emailaddress-instancearn): {{String}}
  [Tags](#cfn-connect-emailaddress-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-connect-emailaddress-properties"></a>

`AliasConfigurations`  <a name="cfn-connect-emailaddress-aliasconfigurations"></a>
A list of alias configurations for this email address, showing which email addresses forward to this primary address. Each configuration contains the email address ID of an alias that forwards emails to this address.
*Required*: No
*Type*: Array of [AliasConfiguration](aws-properties-connect-emailaddress-aliasconfiguration.md)
*Maximum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-connect-emailaddress-description"></a>
The description of the email address.
*Required*: No
*Type*: String
*Pattern*: `(^[\S].*[\S]$)|(^[\S]$)`
*Minimum*: `1`
*Maximum*: `250`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DisplayName`  <a name="cfn-connect-emailaddress-displayname"></a>
The display name of email address.
*Required*: No
*Type*: String
*Pattern*: `(^[\S].*[\S]$)|(^[\S]$)`
*Minimum*: `0`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EmailAddress`  <a name="cfn-connect-emailaddress-emailaddress"></a>
The email address, including the domain.
*Required*: Yes
*Type*: String
*Pattern*: `([^\s@]+@[^\s@]+\.[^\s@]+)`
*Minimum*: `1`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`InstanceArn`  <a name="cfn-connect-emailaddress-instancearn"></a>
The Amazon Resource Name (ARN) of the instance.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z]+-[0-9]{1}:[0-9]{1,20}:instance/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
*Minimum*: `1`
*Maximum*: `250`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-connect-emailaddress-tags"></a>
An array of key-value pairs to apply to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-connect-emailaddress-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-connect-emailaddress-return-values"></a>

### Ref
<a name="aws-resource-connect-emailaddress-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the email address. For example:

 `{ "Ref": "myEmailAddress" }`

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-connect-emailaddress-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-connect-emailaddress-return-values-fn--getatt-fn--getatt"></a>

`EmailAddressArn`  <a name="EmailAddressArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the email address.
