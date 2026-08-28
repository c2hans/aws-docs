---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-invoicing-invoiceunit-rule.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Invoicing::InvoiceUnit Rule
<a name="aws-properties-invoicing-invoiceunit-rule"></a>

The `InvoiceUnitRule` object used to update invoice units.

## Syntax
<a name="aws-properties-invoicing-invoiceunit-rule-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-invoicing-invoiceunit-rule-syntax.json"></a>

```
{
  "[LinkedAccounts](#cfn-invoicing-invoiceunit-rule-linkedaccounts)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-invoicing-invoiceunit-rule-syntax.yaml"></a>

```
  [LinkedAccounts](#cfn-invoicing-invoiceunit-rule-linkedaccounts): {{
    - String}}
```

## Properties
<a name="aws-properties-invoicing-invoiceunit-rule-properties"></a>

`LinkedAccounts`  <a name="cfn-invoicing-invoiceunit-rule-linkedaccounts"></a>
The list of `LINKED_ACCOUNT` IDs where charges are included within the invoice unit.
*Required*: Yes
*Type*: Array of String
*Minimum*: `12`
*Maximum*: `12`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
