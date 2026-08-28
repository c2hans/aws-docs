---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-iot-accountauditconfiguration-auditcheckconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::IoT::AccountAuditConfiguration AuditCheckConfiguration
<a name="aws-properties-iot-accountauditconfiguration-auditcheckconfiguration"></a>

Which audit checks are enabled and disabled for this account.

## Syntax
<a name="aws-properties-iot-accountauditconfiguration-auditcheckconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-iot-accountauditconfiguration-auditcheckconfiguration-syntax.json"></a>

```
{
  "[Enabled](#cfn-iot-accountauditconfiguration-auditcheckconfiguration-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-iot-accountauditconfiguration-auditcheckconfiguration-syntax.yaml"></a>

```
  [Enabled](#cfn-iot-accountauditconfiguration-auditcheckconfiguration-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-iot-accountauditconfiguration-auditcheckconfiguration-properties"></a>

`Enabled`  <a name="cfn-iot-accountauditconfiguration-auditcheckconfiguration-enabled"></a>
True if this audit check is enabled for this account.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
