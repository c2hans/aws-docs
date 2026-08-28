---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-billingconductor-billinggroup-accountgrouping.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::BillingConductor::BillingGroup AccountGrouping
<a name="aws-properties-billingconductor-billinggroup-accountgrouping"></a>

The set of accounts that will be under the billing group. The set of accounts resemble the linked accounts in a consolidated billing family.

## Syntax
<a name="aws-properties-billingconductor-billinggroup-accountgrouping-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-billingconductor-billinggroup-accountgrouping-syntax.json"></a>

```
{
  "[AutoAssociate](#cfn-billingconductor-billinggroup-accountgrouping-autoassociate)" : {{Boolean}},
  "[LinkedAccountIds](#cfn-billingconductor-billinggroup-accountgrouping-linkedaccountids)" : {{[ String, ... ]}},
  "[ResponsibilityTransferArn](#cfn-billingconductor-billinggroup-accountgrouping-responsibilitytransferarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-billingconductor-billinggroup-accountgrouping-syntax.yaml"></a>

```
  [AutoAssociate](#cfn-billingconductor-billinggroup-accountgrouping-autoassociate): {{Boolean}}
  [LinkedAccountIds](#cfn-billingconductor-billinggroup-accountgrouping-linkedaccountids): {{
    - String}}
  [ResponsibilityTransferArn](#cfn-billingconductor-billinggroup-accountgrouping-responsibilitytransferarn): {{String}}
```

## Properties
<a name="aws-properties-billingconductor-billinggroup-accountgrouping-properties"></a>

`AutoAssociate`  <a name="cfn-billingconductor-billinggroup-accountgrouping-autoassociate"></a>
Specifies if this billing group will automatically associate newly added AWS accounts that join your consolidated billing family.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LinkedAccountIds`  <a name="cfn-billingconductor-billinggroup-accountgrouping-linkedaccountids"></a>
The account IDs that make up the billing group. Account IDs must be a part of the consolidated billing family, and not associated with another billing group.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResponsibilityTransferArn`  <a name="cfn-billingconductor-billinggroup-accountgrouping-responsibilitytransferarn"></a>
 The Amazon Resource Name (ARN) that identifies the transfer relationship owned by the Bill Transfer account (caller account). When specified, the PrimaryAccountId is no longer required.
*Required*: No
*Type*: String
*Pattern*: `arn:[a-z0-9][a-z0-9-.]{0,62}:organizations::[0-9]{12}:transfer/o-[a-z0-9]{10,32}/(billing)/(inbound|outbound)/rt-[0-9a-z]{8,32}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
