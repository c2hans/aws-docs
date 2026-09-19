---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-supportauthz-supportpermit-actionset.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SupportAuthZ::SupportPermit ActionSet
<a name="aws-properties-supportauthz-supportpermit-actionset"></a>

The set of actions a support permit grants. Specify exactly one of `AllActions` or `Actions`.

## Syntax
<a name="aws-properties-supportauthz-supportpermit-actionset-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-supportauthz-supportpermit-actionset-syntax.json"></a>

```
{
  "[Actions](#cfn-supportauthz-supportpermit-actionset-actions)" : {{[ String, ... ]}},
  "[AllActions](#cfn-supportauthz-supportpermit-actionset-allactions)" : {{Json}}
}
```

### YAML
<a name="aws-properties-supportauthz-supportpermit-actionset-syntax.yaml"></a>

```
  [Actions](#cfn-supportauthz-supportpermit-actionset-actions): {{
    - String}}
  [AllActions](#cfn-supportauthz-supportpermit-actionset-allactions): {{Json}}
```

## Properties
<a name="aws-properties-supportauthz-supportpermit-actionset-properties"></a>

`Actions`  <a name="cfn-supportauthz-supportpermit-actionset-actions"></a>
An explicit list of actions to grant. Each action is a service-namespaced action string, such as `ec2:DescribeInstances`. Don't specify this property together with `AllActions`.
*Required*: No
*Type*: Array of String
*Minimum*: `3 | 1`
*Maximum*: `255 | 10`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AllActions`  <a name="cfn-supportauthz-supportpermit-actionset-allactions"></a>
Grants all supported actions. Specify an empty object (`{}`) to grant every action. Don't specify this property together with `Actions`.
*Required*: No
*Type*: Json
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
