---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-collaboration-modelinferencepaymentconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::Collaboration ModelInferencePaymentConfig
<a name="aws-properties-cleanrooms-collaboration-modelinferencepaymentconfig"></a>

An object representing the collaboration member's model inference payment responsibilities set by the collaboration creator.

## Syntax
<a name="aws-properties-cleanrooms-collaboration-modelinferencepaymentconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-collaboration-modelinferencepaymentconfig-syntax.json"></a>

```
{
  "[IsResponsible](#cfn-cleanrooms-collaboration-modelinferencepaymentconfig-isresponsible)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-cleanrooms-collaboration-modelinferencepaymentconfig-syntax.yaml"></a>

```
  [IsResponsible](#cfn-cleanrooms-collaboration-modelinferencepaymentconfig-isresponsible): {{Boolean}}
```

## Properties
<a name="aws-properties-cleanrooms-collaboration-modelinferencepaymentconfig-properties"></a>

`IsResponsible`  <a name="cfn-cleanrooms-collaboration-modelinferencepaymentconfig-isresponsible"></a>
Indicates whether the collaboration creator has configured the collaboration member to pay for model inference costs (`TRUE`) or has not configured the collaboration member to pay for model inference costs (`FALSE`).
One or more members can be configured as payer candidates for model inference costs.
If the collaboration creator hasn't specified anyone as the member paying for model inference costs, then the member who can query is the default payer.
*Required*: Yes
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
