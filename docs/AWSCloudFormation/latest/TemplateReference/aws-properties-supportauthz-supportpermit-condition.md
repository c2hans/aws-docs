---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-supportauthz-supportpermit-condition.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SupportAuthZ::SupportPermit Condition
<a name="aws-properties-supportauthz-supportpermit-condition"></a>

A time-window condition that controls when a support permit is active. Specify exactly one of `AllowAfter` or `AllowBefore`.

## Syntax
<a name="aws-properties-supportauthz-supportpermit-condition-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-supportauthz-supportpermit-condition-syntax.json"></a>

```
{
  "[AllowAfter](#cfn-supportauthz-supportpermit-condition-allowafter)" : {{String}},
  "[AllowBefore](#cfn-supportauthz-supportpermit-condition-allowbefore)" : {{String}}
}
```

### YAML
<a name="aws-properties-supportauthz-supportpermit-condition-syntax.yaml"></a>

```
  [AllowAfter](#cfn-supportauthz-supportpermit-condition-allowafter): {{String}}
  [AllowBefore](#cfn-supportauthz-supportpermit-condition-allowbefore): {{String}}
```

## Properties
<a name="aws-properties-supportauthz-supportpermit-condition-properties"></a>

`AllowAfter`  <a name="cfn-supportauthz-supportpermit-condition-allowafter"></a>
The permit is active only after this time. Specify the value as an ISO 8601 date-time string, such as `2026-09-01T00:00:00Z`.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`AllowBefore`  <a name="cfn-supportauthz-supportpermit-condition-allowbefore"></a>
The permit is active only before this time. Specify the value as an ISO 8601 date-time string, such as `2026-12-31T23:59:59Z`.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
