---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-receiptfilter-filter.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::ReceiptFilter Filter
<a name="aws-properties-ses-receiptfilter-filter"></a>

Specifies an IP address filter.

## Syntax
<a name="aws-properties-ses-receiptfilter-filter-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-receiptfilter-filter-syntax.json"></a>

```
{
  "[IpFilter](#cfn-ses-receiptfilter-filter-ipfilter)" : {{IpFilter}},
  "[Name](#cfn-ses-receiptfilter-filter-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-receiptfilter-filter-syntax.yaml"></a>

```
  [IpFilter](#cfn-ses-receiptfilter-filter-ipfilter): {{
    IpFilter}}
  [Name](#cfn-ses-receiptfilter-filter-name): {{String}}
```

## Properties
<a name="aws-properties-ses-receiptfilter-filter-properties"></a>

`IpFilter`  <a name="cfn-ses-receiptfilter-filter-ipfilter"></a>
A structure that provides the IP addresses to block or allow, and whether to block or allow incoming mail from them.
*Required*: Yes
*Type*: [IpFilter](aws-properties-ses-receiptfilter-ipfilter.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-ses-receiptfilter-filter-name"></a>
The name of the IP address filter. The name must meet the following requirements:
+ Contain only ASCII letters (a-z, A-Z), numbers (0-9), underscores (\_), or dashes (-).
+ Start and end with a letter or number.
+ Contain 64 characters or fewer.
*Required*: No
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
