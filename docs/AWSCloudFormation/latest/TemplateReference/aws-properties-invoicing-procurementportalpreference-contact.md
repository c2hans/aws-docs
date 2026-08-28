---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-invoicing-procurementportalpreference-contact.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Invoicing::ProcurementPortalPreference Contact
<a name="aws-properties-invoicing-procurementportalpreference-contact"></a>

<a name="aws-properties-invoicing-procurementportalpreference-contact-description"></a>The `Contact` property type specifies Property description not available. for an [AWS::Invoicing::ProcurementPortalPreference](aws-resource-invoicing-procurementportalpreference.md).

## Syntax
<a name="aws-properties-invoicing-procurementportalpreference-contact-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-invoicing-procurementportalpreference-contact-syntax.json"></a>

```
{
  "[Email](#cfn-invoicing-procurementportalpreference-contact-email)" : {{String}},
  "[Name](#cfn-invoicing-procurementportalpreference-contact-name)" : {{String}}
}
```

### YAML
<a name="aws-properties-invoicing-procurementportalpreference-contact-syntax.yaml"></a>

```
  [Email](#cfn-invoicing-procurementportalpreference-contact-email): {{String}}
  [Name](#cfn-invoicing-procurementportalpreference-contact-name): {{String}}
```

## Properties
<a name="aws-properties-invoicing-procurementportalpreference-contact-properties"></a>

`Email`  <a name="cfn-invoicing-procurementportalpreference-contact-email"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}$`
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-invoicing-procurementportalpreference-contact-name"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `0`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
