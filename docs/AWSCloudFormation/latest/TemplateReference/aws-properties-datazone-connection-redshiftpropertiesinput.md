---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datazone-connection-redshiftpropertiesinput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataZone::Connection RedshiftPropertiesInput
<a name="aws-properties-datazone-connection-redshiftpropertiesinput"></a>

The Amazon Redshift properties.

## Syntax
<a name="aws-properties-datazone-connection-redshiftpropertiesinput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datazone-connection-redshiftpropertiesinput-syntax.json"></a>

```
{
  "[Credentials](#cfn-datazone-connection-redshiftpropertiesinput-credentials)" : {{RedshiftCredentials}},
  "[DatabaseName](#cfn-datazone-connection-redshiftpropertiesinput-databasename)" : {{String}},
  "[Host](#cfn-datazone-connection-redshiftpropertiesinput-host)" : {{String}},
  "[LineageSync](#cfn-datazone-connection-redshiftpropertiesinput-lineagesync)" : {{RedshiftLineageSyncConfigurationInput}},
  "[Port](#cfn-datazone-connection-redshiftpropertiesinput-port)" : {{Number}},
  "[Storage](#cfn-datazone-connection-redshiftpropertiesinput-storage)" : {{RedshiftStorageProperties}}
}
```

### YAML
<a name="aws-properties-datazone-connection-redshiftpropertiesinput-syntax.yaml"></a>

```
  [Credentials](#cfn-datazone-connection-redshiftpropertiesinput-credentials): {{
    RedshiftCredentials}}
  [DatabaseName](#cfn-datazone-connection-redshiftpropertiesinput-databasename): {{String}}
  [Host](#cfn-datazone-connection-redshiftpropertiesinput-host): {{String}}
  [LineageSync](#cfn-datazone-connection-redshiftpropertiesinput-lineagesync): {{
    RedshiftLineageSyncConfigurationInput}}
  [Port](#cfn-datazone-connection-redshiftpropertiesinput-port): {{Number}}
  [Storage](#cfn-datazone-connection-redshiftpropertiesinput-storage): {{
    RedshiftStorageProperties}}
```

## Properties
<a name="aws-properties-datazone-connection-redshiftpropertiesinput-properties"></a>

`Credentials`  <a name="cfn-datazone-connection-redshiftpropertiesinput-credentials"></a>
The Amaon Redshift credentials.
*Required*: No
*Type*: [RedshiftCredentials](aws-properties-datazone-connection-redshiftcredentials.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`DatabaseName`  <a name="cfn-datazone-connection-redshiftpropertiesinput-databasename"></a>
The Amazon Redshift database name.
*Required*: No
*Type*: String
*Pattern*: `^[a-z0-9_-]+$`
*Minimum*: `1`
*Maximum*: `64`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Host`  <a name="cfn-datazone-connection-redshiftpropertiesinput-host"></a>
The Amazon Redshift host.
*Required*: No
*Type*: String
*Pattern*: `^[\S]*$`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`LineageSync`  <a name="cfn-datazone-connection-redshiftpropertiesinput-lineagesync"></a>
The lineage sync of the Amazon Redshift.
*Required*: No
*Type*: [RedshiftLineageSyncConfigurationInput](aws-properties-datazone-connection-redshiftlineagesyncconfigurationinput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-datazone-connection-redshiftpropertiesinput-port"></a>
The Amaon Redshift port.
*Required*: No
*Type*: Number
*Minimum*: `0`
*Maximum*: `65535`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Storage`  <a name="cfn-datazone-connection-redshiftpropertiesinput-storage"></a>
The Amazon Redshift storage.
*Required*: No
*Type*: [RedshiftStorageProperties](aws-properties-datazone-connection-redshiftstorageproperties.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
