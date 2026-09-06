---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-collaboration-querycomputepaymentconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::Collaboration QueryComputePaymentConfig
<a name="aws-properties-cleanrooms-collaboration-querycomputepaymentconfig"></a>

An object representing the collaboration member's payment responsibilities set by the collaboration creator for query compute costs.

## Syntax
<a name="aws-properties-cleanrooms-collaboration-querycomputepaymentconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-collaboration-querycomputepaymentconfig-syntax.json"></a>

```
{
  "[IsResponsible](#cfn-cleanrooms-collaboration-querycomputepaymentconfig-isresponsible)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-cleanrooms-collaboration-querycomputepaymentconfig-syntax.yaml"></a>

```
  [IsResponsible](#cfn-cleanrooms-collaboration-querycomputepaymentconfig-isresponsible): {{Boolean}}
```

## Properties
<a name="aws-properties-cleanrooms-collaboration-querycomputepaymentconfig-properties"></a>

`IsResponsible`  <a name="cfn-cleanrooms-collaboration-querycomputepaymentconfig-isresponsible"></a>
Indicates whether the collaboration creator has configured the collaboration member to pay for query compute costs (`TRUE`) or has not configured the collaboration member to pay for query compute costs (`FALSE`).
One or more members can be configured as payer candidates for query compute costs.
If the collaboration creator hasn't specified anyone as the member paying for query compute costs, then the member who can query is the default payer.
*Required*: Yes
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
