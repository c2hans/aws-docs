---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-licensemanager-license-provisionalconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::LicenseManager::License ProvisionalConfiguration
<a name="aws-properties-licensemanager-license-provisionalconfiguration"></a>

Details about a provisional configuration.

## Syntax
<a name="aws-properties-licensemanager-license-provisionalconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-licensemanager-license-provisionalconfiguration-syntax.json"></a>

```
{
  "[MaxTimeToLiveInMinutes](#cfn-licensemanager-license-provisionalconfiguration-maxtimetoliveinminutes)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-licensemanager-license-provisionalconfiguration-syntax.yaml"></a>

```
  [MaxTimeToLiveInMinutes](#cfn-licensemanager-license-provisionalconfiguration-maxtimetoliveinminutes): {{Integer}}
```

## Properties
<a name="aws-properties-licensemanager-license-provisionalconfiguration-properties"></a>

`MaxTimeToLiveInMinutes`  <a name="cfn-licensemanager-license-provisionalconfiguration-maxtimetoliveinminutes"></a>
Maximum time for the provisional configuration, in minutes.
*Required*: Yes
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
