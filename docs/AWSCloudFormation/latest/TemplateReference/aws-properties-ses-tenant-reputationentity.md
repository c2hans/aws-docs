---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-tenant-reputationentity.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::Tenant ReputationEntity
<a name="aws-properties-ses-tenant-reputationentity"></a>

An object that contains information about a reputation entity, including its reference, type, policy, status records, and reputation impact.

## Syntax
<a name="aws-properties-ses-tenant-reputationentity-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-tenant-reputationentity-syntax.json"></a>

```
{
  "[Policy](#cfn-ses-tenant-reputationentity-policy)" : {{ReputationPolicy}}
}
```

### YAML
<a name="aws-properties-ses-tenant-reputationentity-syntax.yaml"></a>

```
  [Policy](#cfn-ses-tenant-reputationentity-policy): {{
    ReputationPolicy}}
```

## Properties
<a name="aws-properties-ses-tenant-reputationentity-properties"></a>

`Policy`  <a name="cfn-ses-tenant-reputationentity-policy"></a>
Property description not available.
*Required*: Yes
*Type*: [ReputationPolicy](aws-properties-ses-tenant-reputationpolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
