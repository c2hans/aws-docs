---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cleanrooms-membership-membershipjobcomputepaymentconfig.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::Membership MembershipJobComputePaymentConfig
<a name="aws-properties-cleanrooms-membership-membershipjobcomputepaymentconfig"></a>

An object representing the payment responsibilities accepted by the collaboration member for query and job compute costs.

## Syntax
<a name="aws-properties-cleanrooms-membership-membershipjobcomputepaymentconfig-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cleanrooms-membership-membershipjobcomputepaymentconfig-syntax.json"></a>

```
{
  "[IsResponsible](#cfn-cleanrooms-membership-membershipjobcomputepaymentconfig-isresponsible)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-cleanrooms-membership-membershipjobcomputepaymentconfig-syntax.yaml"></a>

```
  [IsResponsible](#cfn-cleanrooms-membership-membershipjobcomputepaymentconfig-isresponsible): {{Boolean}}
```

## Properties
<a name="aws-properties-cleanrooms-membership-membershipjobcomputepaymentconfig-properties"></a>

`IsResponsible`  <a name="cfn-cleanrooms-membership-membershipjobcomputepaymentconfig-isresponsible"></a>
Indicates whether the collaboration member has accepted to pay for job compute costs (`TRUE`) or has not accepted to pay for query and job compute costs (`FALSE`).
There can be one or more members who are designated as payer candidates for queries and jobs.
An error message is returned for the following reasons:
+ If you set the value to `FALSE` but you are responsible to pay for query and job compute costs.
+ If you set the value to `TRUE` but you are not responsible to pay for query and job compute costs.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
