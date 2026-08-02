---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-route53profiles-profile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Route53Profiles::Profile
<a name="aws-resource-route53profiles-profile"></a>

 A complex type that includes settings for a Route 53 Profile.

## Syntax
<a name="aws-resource-route53profiles-profile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-route53profiles-profile-syntax.json"></a>

```
{
  "Type" : "AWS::Route53Profiles::Profile",
  "Properties" : {
      "[Name](#cfn-route53profiles-profile-name)" : {{String}},
      "[Tags](#cfn-route53profiles-profile-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-route53profiles-profile-syntax.yaml"></a>

```
Type: AWS::Route53Profiles::Profile
Properties:
  [Name](#cfn-route53profiles-profile-name): {{String}}
  [Tags](#cfn-route53profiles-profile-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-route53profiles-profile-properties"></a>

`Name`  <a name="cfn-route53profiles-profile-name"></a>
 Name of the Profile.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-route53profiles-profile-tags"></a>
A list of the tag keys and values that you want to associate with the profile.
*Required*: No
*Type*: Array of [Tag](aws-properties-route53profiles-profile-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-route53profiles-profile-return-values"></a>

### Ref
<a name="aws-resource-route53profiles-profile-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns`Profile` ID for the profile, such as `rp-9e6daa461example`.

For more information about using the `Ref` function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-route53profiles-profile-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-route53profiles-profile-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
 The Amazon Resource Name (ARN) of the Profile.

`ClientToken`  <a name="ClientToken-fn::getatt"></a>
 The `ClientToken` value that was assigned when the Profile was created.

`Id`  <a name="Id-fn::getatt"></a>
 ID of the Profile.

`ShareStatus`  <a name="ShareStatus-fn::getatt"></a>
 Sharing status for the Profile.
