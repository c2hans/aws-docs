---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cassandra-table-billingmode.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cassandra::Table BillingMode
<a name="aws-properties-cassandra-table-billingmode"></a>

Determines the billing mode for the table - on-demand or provisioned.

## Syntax
<a name="aws-properties-cassandra-table-billingmode-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cassandra-table-billingmode-syntax.json"></a>

```
{
  "[Mode](#cfn-cassandra-table-billingmode-mode)" : {{String}},
  "[ProvisionedThroughput](#cfn-cassandra-table-billingmode-provisionedthroughput)" : {{ProvisionedThroughput}}
}
```

### YAML
<a name="aws-properties-cassandra-table-billingmode-syntax.yaml"></a>

```
  [Mode](#cfn-cassandra-table-billingmode-mode): {{String}}
  [ProvisionedThroughput](#cfn-cassandra-table-billingmode-provisionedthroughput): {{
    ProvisionedThroughput}}
```

## Properties
<a name="aws-properties-cassandra-table-billingmode-properties"></a>

`Mode`  <a name="cfn-cassandra-table-billingmode-mode"></a>
The billing mode for the table:
+ On-demand mode - `ON_DEMAND`
+ Provisioned mode - `PROVISIONED`
**Note**
If you choose `PROVISIONED` mode, then you also need to specify provisioned throughput (read and write capacity) for the table.
Valid values: `ON_DEMAND` \| `PROVISIONED`
*Required*: Yes
*Type*: String
*Allowed values*: `PROVISIONED | ON_DEMAND`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProvisionedThroughput`  <a name="cfn-cassandra-table-billingmode-provisionedthroughput"></a>
The provisioned read capacity and write capacity for the table. For more information, see [Provisioned throughput capacity mode](https://docs.aws.amazon.com/keyspaces/latest/devguide/ReadWriteCapacityMode.html#ReadWriteCapacityMode.Provisioned) in the *Amazon Keyspaces Developer Guide*.
*Required*: No
*Type*: [ProvisionedThroughput](aws-properties-cassandra-table-provisionedthroughput.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
