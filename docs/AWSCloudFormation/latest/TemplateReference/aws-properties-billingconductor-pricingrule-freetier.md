---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-billingconductor-pricingrule-freetier.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BillingConductor::PricingRule FreeTier
<a name="aws-properties-billingconductor-pricingrule-freetier"></a>

The possible AWS Free Tier configurations.

## Syntax
<a name="aws-properties-billingconductor-pricingrule-freetier-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-billingconductor-pricingrule-freetier-syntax.json"></a>

```
{
  "[Activated](#cfn-billingconductor-pricingrule-freetier-activated)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-billingconductor-pricingrule-freetier-syntax.yaml"></a>

```
  [Activated](#cfn-billingconductor-pricingrule-freetier-activated): {{Boolean}}
```

## Properties
<a name="aws-properties-billingconductor-pricingrule-freetier-properties"></a>

`Activated`  <a name="cfn-billingconductor-pricingrule-freetier-activated"></a>
Activate or deactivate AWS Free Tier.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
