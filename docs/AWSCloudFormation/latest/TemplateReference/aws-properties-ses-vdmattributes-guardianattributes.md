---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-vdmattributes-guardianattributes.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::VdmAttributes GuardianAttributes
<a name="aws-properties-ses-vdmattributes-guardianattributes"></a>

An object containing additional settings for your VDM configuration as applicable to the Guardian.

## Syntax
<a name="aws-properties-ses-vdmattributes-guardianattributes-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-vdmattributes-guardianattributes-syntax.json"></a>

```
{
  "[OptimizedSharedDelivery](#cfn-ses-vdmattributes-guardianattributes-optimizedshareddelivery)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-vdmattributes-guardianattributes-syntax.yaml"></a>

```
  [OptimizedSharedDelivery](#cfn-ses-vdmattributes-guardianattributes-optimizedshareddelivery): {{String}}
```

## Properties
<a name="aws-properties-ses-vdmattributes-guardianattributes-properties"></a>

`OptimizedSharedDelivery`  <a name="cfn-ses-vdmattributes-guardianattributes-optimizedshareddelivery"></a>
Specifies the status of your VDM optimized shared delivery. Can be one of the following:
+ `ENABLED` – Amazon SES enables optimized shared delivery for your account.
+ `DISABLED` – Amazon SES disables optimized shared delivery for your account.
*Required*: No
*Type*: String
*Pattern*: `ENABLED|DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
