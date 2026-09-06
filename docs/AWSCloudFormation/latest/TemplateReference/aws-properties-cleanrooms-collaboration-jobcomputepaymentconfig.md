---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-collaboration-jobcomputepaymentconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::Collaboration JobComputePaymentConfig
<a name="aws-properties-cleanrooms-collaboration-jobcomputepaymentconfig"></a>

An object representing the collaboration member's payment responsibilities set by the collaboration creator for query and job compute costs.

## Syntax
<a name="aws-properties-cleanrooms-collaboration-jobcomputepaymentconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-collaboration-jobcomputepaymentconfig-syntax.json"></a>

```
{
  "[IsResponsible](#cfn-cleanrooms-collaboration-jobcomputepaymentconfig-isresponsible)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-cleanrooms-collaboration-jobcomputepaymentconfig-syntax.yaml"></a>

```
  [IsResponsible](#cfn-cleanrooms-collaboration-jobcomputepaymentconfig-isresponsible): {{Boolean}}
```

## Properties
<a name="aws-properties-cleanrooms-collaboration-jobcomputepaymentconfig-properties"></a>

`IsResponsible`  <a name="cfn-cleanrooms-collaboration-jobcomputepaymentconfig-isresponsible"></a>
Indicates whether the collaboration creator has configured the collaboration member to pay for query and job compute costs (`TRUE`) or has not configured the collaboration member to pay for query and job compute costs (`FALSE`).
One or more members can be configured as payer candidates for query and job compute costs.
An error is returned if the collaboration creator sets a `FALSE` value for the member who can run queries and jobs.
*Required*: Yes
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)
