---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-tenant-reputationpolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::Tenant ReputationPolicy
<a name="aws-properties-ses-tenant-reputationpolicy"></a>

<a name="aws-properties-ses-tenant-reputationpolicy-description"></a>The `ReputationPolicy` property type specifies Property description not available. for an [AWS::SES::Tenant](aws-resource-ses-tenant.md).

## Syntax
<a name="aws-properties-ses-tenant-reputationpolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-tenant-reputationpolicy-syntax.json"></a>

```
{
  "[ReputationEntityPolicy](#cfn-ses-tenant-reputationpolicy-reputationentitypolicy)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-tenant-reputationpolicy-syntax.yaml"></a>

```
  [ReputationEntityPolicy](#cfn-ses-tenant-reputationpolicy-reputationentitypolicy): {{String}}
```

## Properties
<a name="aws-properties-ses-tenant-reputationpolicy-properties"></a>

`ReputationEntityPolicy`  <a name="cfn-ses-tenant-reputationpolicy-reputationentitypolicy"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:[a-z0-9-]+:ses:[a-z0-9-]+:aws:reputation-policy/(none|standard|strict)$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
