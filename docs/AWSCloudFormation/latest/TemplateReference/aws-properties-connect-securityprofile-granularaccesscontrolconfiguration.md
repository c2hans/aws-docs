---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-connect-securityprofile-granularaccesscontrolconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Connect::SecurityProfile GranularAccessControlConfiguration
<a name="aws-properties-connect-securityprofile-granularaccesscontrolconfiguration"></a>

Contains granular access control configuration for security profiles, including data table access permissions.

## Syntax
<a name="aws-properties-connect-securityprofile-granularaccesscontrolconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-connect-securityprofile-granularaccesscontrolconfiguration-syntax.json"></a>

```
{
  "[DataTableAccessControlConfiguration](#cfn-connect-securityprofile-granularaccesscontrolconfiguration-datatableaccesscontrolconfiguration)" : {{DataTableAccessControlConfiguration}}
}
```

### YAML
<a name="aws-properties-connect-securityprofile-granularaccesscontrolconfiguration-syntax.yaml"></a>

```
  [DataTableAccessControlConfiguration](#cfn-connect-securityprofile-granularaccesscontrolconfiguration-datatableaccesscontrolconfiguration): {{
    DataTableAccessControlConfiguration}}
```

## Properties
<a name="aws-properties-connect-securityprofile-granularaccesscontrolconfiguration-properties"></a>

`DataTableAccessControlConfiguration`  <a name="cfn-connect-securityprofile-granularaccesscontrolconfiguration-datatableaccesscontrolconfiguration"></a>
The access control configuration for data tables.
*Required*: No
*Type*: [DataTableAccessControlConfiguration](aws-properties-connect-securityprofile-datatableaccesscontrolconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
