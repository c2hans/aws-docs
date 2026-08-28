---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-athena-workgroup-managedqueryresultsconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Athena::WorkGroup ManagedQueryResultsConfiguration
<a name="aws-properties-athena-workgroup-managedqueryresultsconfiguration"></a>

 The configuration for storing results in Athena owned storage, which includes whether this feature is enabled; whether encryption configuration, if any, is used for encrypting query results.

## Syntax
<a name="aws-properties-athena-workgroup-managedqueryresultsconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-athena-workgroup-managedqueryresultsconfiguration-syntax.json"></a>

```
{
  "[Enabled](#cfn-athena-workgroup-managedqueryresultsconfiguration-enabled)" : {{Boolean}},
  "[EncryptionConfiguration](#cfn-athena-workgroup-managedqueryresultsconfiguration-encryptionconfiguration)" : {{ManagedStorageEncryptionConfiguration}}
}
```

### YAML
<a name="aws-properties-athena-workgroup-managedqueryresultsconfiguration-syntax.yaml"></a>

```
  [Enabled](#cfn-athena-workgroup-managedqueryresultsconfiguration-enabled): {{Boolean}}
  [EncryptionConfiguration](#cfn-athena-workgroup-managedqueryresultsconfiguration-encryptionconfiguration): {{
    ManagedStorageEncryptionConfiguration}}
```

## Properties
<a name="aws-properties-athena-workgroup-managedqueryresultsconfiguration-properties"></a>

`Enabled`  <a name="cfn-athena-workgroup-managedqueryresultsconfiguration-enabled"></a>
If set to true, allows you to store query results in Athena owned storage. If set to false, workgroup member stores query results in location specified under `ResultConfiguration$OutputLocation`. The default is false. A workgroup cannot have the `ResultConfiguration$OutputLocation` parameter when you set this field to true.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`EncryptionConfiguration`  <a name="cfn-athena-workgroup-managedqueryresultsconfiguration-encryptionconfiguration"></a>
If you encrypt query and calculation results in Athena owned storage, this field indicates the encryption option (for example, SSE\_KMS or CSE\_KMS) and key information.
*Required*: No
*Type*: [ManagedStorageEncryptionConfiguration](aws-properties-athena-workgroup-managedstorageencryptionconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
