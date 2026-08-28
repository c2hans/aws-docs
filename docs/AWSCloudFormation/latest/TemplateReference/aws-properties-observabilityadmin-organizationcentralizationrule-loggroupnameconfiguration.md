---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-observabilityadmin-organizationcentralizationrule-loggroupnameconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ObservabilityAdmin::OrganizationCentralizationRule LogGroupNameConfiguration
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-loggroupnameconfiguration"></a>

Configuration that specifies a naming pattern for destination log groups created during centralization. The pattern supports static text and dynamic variables that are replaced with source attributes when log groups are created.

## Syntax
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-loggroupnameconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-loggroupnameconfiguration-syntax.json"></a>

```
{
  "[LogGroupNamePattern](#cfn-observabilityadmin-organizationcentralizationrule-loggroupnameconfiguration-loggroupnamepattern)" : {{String}}
}
```

### YAML
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-loggroupnameconfiguration-syntax.yaml"></a>

```
  [LogGroupNamePattern](#cfn-observabilityadmin-organizationcentralizationrule-loggroupnameconfiguration-loggroupnamepattern): {{String}}
```

## Properties
<a name="aws-properties-observabilityadmin-organizationcentralizationrule-loggroupnameconfiguration-properties"></a>

`LogGroupNamePattern`  <a name="cfn-observabilityadmin-organizationcentralizationrule-loggroupnameconfiguration-loggroupnamepattern"></a>
The pattern used to generate destination log group names during centralization. The pattern can contain static text and dynamic variables that are replaced with source attributes. If a variable cannot be resolved, it inherits the value from its parent variable in the hierarchy. The pattern must be between 1 and 512 characters.
Supported variables:
+ **${source.logGroup}** — The original log group name from the source account.
+ **${source.accountId}** — The AWS account ID where the log originated.
+ **${source.region}** — The AWS Region where the log originated.
+ **${source.org.id}** — The AWS Organization ID of the source account.
+ **${source.org.ouId}** — The organizational unit ID of the source account.
+ **${source.org.rootId}** — The organization Root ID.
+ **${source.org.path}** — The organizational path from account to root.
*Required*: Yes
*Type*: String
*Pattern*: `^(?:[\._\-/#A-Za-z0-9]+|\$\{[A-Za-z]+(?:\.[A-Za-z]+){1,2}\})+$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
