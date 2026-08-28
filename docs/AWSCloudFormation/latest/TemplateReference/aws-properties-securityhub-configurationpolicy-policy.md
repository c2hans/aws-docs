---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-securityhub-configurationpolicy-policy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SecurityHub::ConfigurationPolicy Policy
<a name="aws-properties-securityhub-configurationpolicy-policy"></a>

 An object that defines how AWS Security Hub CSPM is configured. It includes whether Security Hub CSPM is enabled or disabled, a list of enabled security standards, a list of enabled or disabled security controls, and a list of custom parameter values for specified controls. If you provide a list of security controls that are enabled in the configuration policy, Security Hub CSPM disables all other controls (including newly released controls). If you provide a list of security controls that are disabled in the configuration policy, Security Hub CSPM enables all other controls (including newly released controls).

## Syntax
<a name="aws-properties-securityhub-configurationpolicy-policy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-securityhub-configurationpolicy-policy-syntax.json"></a>

```
{
  "[SecurityHub](#cfn-securityhub-configurationpolicy-policy-securityhub)" : {{SecurityHubPolicy}}
}
```

### YAML
<a name="aws-properties-securityhub-configurationpolicy-policy-syntax.yaml"></a>

```
  [SecurityHub](#cfn-securityhub-configurationpolicy-policy-securityhub): {{
    SecurityHubPolicy}}
```

## Properties
<a name="aws-properties-securityhub-configurationpolicy-policy-properties"></a>

`SecurityHub`  <a name="cfn-securityhub-configurationpolicy-policy-securityhub"></a>
 The AWS service that the configuration policy applies to.
*Required*: No
*Type*: [SecurityHubPolicy](aws-properties-securityhub-configurationpolicy-securityhubpolicy.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
