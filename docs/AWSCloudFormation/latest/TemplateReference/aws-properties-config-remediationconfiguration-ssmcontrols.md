---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-config-remediationconfiguration-ssmcontrols.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Config::RemediationConfiguration SsmControls
<a name="aws-properties-config-remediationconfiguration-ssmcontrols"></a>

AWS Systems Manager (SSM) specific remediation controls.

## Syntax
<a name="aws-properties-config-remediationconfiguration-ssmcontrols-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-config-remediationconfiguration-ssmcontrols-syntax.json"></a>

```
{
  "[ConcurrentExecutionRatePercentage](#cfn-config-remediationconfiguration-ssmcontrols-concurrentexecutionratepercentage)" : {{Integer}},
  "[ErrorPercentage](#cfn-config-remediationconfiguration-ssmcontrols-errorpercentage)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-config-remediationconfiguration-ssmcontrols-syntax.yaml"></a>

```
  [ConcurrentExecutionRatePercentage](#cfn-config-remediationconfiguration-ssmcontrols-concurrentexecutionratepercentage): {{Integer}}
  [ErrorPercentage](#cfn-config-remediationconfiguration-ssmcontrols-errorpercentage): {{Integer}}
```

## Properties
<a name="aws-properties-config-remediationconfiguration-ssmcontrols-properties"></a>

`ConcurrentExecutionRatePercentage`  <a name="cfn-config-remediationconfiguration-ssmcontrols-concurrentexecutionratepercentage"></a>
The maximum percentage of remediation actions allowed to run in parallel on the non-compliant resources for that specific rule. You can specify a percentage, such as 10%. The default value is 10.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ErrorPercentage`  <a name="cfn-config-remediationconfiguration-ssmcontrols-errorpercentage"></a>
The percentage of errors that are allowed before SSM stops running automations on non-compliant resources for that specific rule. You can specify a percentage of errors, for example 10%. If you do not specifiy a percentage, the default is 50%. For example, if you set the ErrorPercentage to 40% for 10 non-compliant resources, then SSM stops running the automations when the fifth error is received.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Maximum*: `100`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
