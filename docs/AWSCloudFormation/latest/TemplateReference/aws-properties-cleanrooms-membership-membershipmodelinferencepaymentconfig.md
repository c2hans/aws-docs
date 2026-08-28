---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-membership-membershipmodelinferencepaymentconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::Membership MembershipModelInferencePaymentConfig
<a name="aws-properties-cleanrooms-membership-membershipmodelinferencepaymentconfig"></a>

An object representing the collaboration member's model inference payment responsibilities set by the collaboration creator.

## Syntax
<a name="aws-properties-cleanrooms-membership-membershipmodelinferencepaymentconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-membership-membershipmodelinferencepaymentconfig-syntax.json"></a>

```
{
  "[IsResponsible](#cfn-cleanrooms-membership-membershipmodelinferencepaymentconfig-isresponsible)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-cleanrooms-membership-membershipmodelinferencepaymentconfig-syntax.yaml"></a>

```
  [IsResponsible](#cfn-cleanrooms-membership-membershipmodelinferencepaymentconfig-isresponsible): {{Boolean}}
```

## Properties
<a name="aws-properties-cleanrooms-membership-membershipmodelinferencepaymentconfig-properties"></a>

`IsResponsible`  <a name="cfn-cleanrooms-membership-membershipmodelinferencepaymentconfig-isresponsible"></a>
Indicates whether the collaboration member has accepted to pay for model inference costs (`TRUE`) or has not accepted to pay for model inference costs (`FALSE`).
If the collaboration creator has not specified anyone to pay for model inference costs, then the member who can query is the default payer.
An error message is returned for the following reasons:
+ If you set the value to `FALSE` but you are responsible to pay for model inference costs.
+ If you set the value to `TRUE` but you are not responsible to pay for model inference costs.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
