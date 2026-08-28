---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-cassandra-keyspace-replicationspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Cassandra::Keyspace ReplicationSpecification
<a name="aws-properties-cassandra-keyspace-replicationspecification"></a>

You can use `ReplicationSpecification` to configure the `ReplicationStrategy` of a keyspace in Amazon Keyspaces.

The `ReplicationSpecification` property applies automatically to all tables in the keyspace.

To review the permissions that are required to add a new Region to a single-Region keyspace, see [Configure the IAM permissions required to add an AWS Region to a keyspace](https://docs.aws.amazon.com/keyspaces/latest/devguide/howitworks_replication_permissions_addReplica.html) in the *Amazon Keyspaces Developer Guide*.

For more information about multi-Region replication, see [Multi-Region replication](https://docs.aws.amazon.com/keyspaces/latest/devguide/multiRegion-replication.html) in the *Amazon Keyspaces Developer Guide*.

## Syntax
<a name="aws-properties-cassandra-keyspace-replicationspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-cassandra-keyspace-replicationspecification-syntax.json"></a>

```
{
  "[RegionList](#cfn-cassandra-keyspace-replicationspecification-regionlist)" : {{[ String, ... ]}},
  "[ReplicationStrategy](#cfn-cassandra-keyspace-replicationspecification-replicationstrategy)" : {{String}}
}
```

### YAML
<a name="aws-properties-cassandra-keyspace-replicationspecification-syntax.yaml"></a>

```
  [RegionList](#cfn-cassandra-keyspace-replicationspecification-regionlist): {{
    - String}}
  [ReplicationStrategy](#cfn-cassandra-keyspace-replicationspecification-replicationstrategy): {{String}}
```

## Properties
<a name="aws-properties-cassandra-keyspace-replicationspecification-properties"></a>

`RegionList`  <a name="cfn-cassandra-keyspace-replicationspecification-regionlist"></a>
Specifies the AWS Regions that the keyspace is replicated in. You must specify at least two Regions, including the Region that the keyspace is being created in.
To specify a Region [that's disabled by default](https://docs.aws.amazon.com/accounts/latest/reference/manage-acct-regions.html#rande-manage-enable), you must first enable the Region. For more information, see [Multi-Region replication in AWS Regions disabled by default](https://docs.aws.amazon.com/keyspaces/latest/devguide/multiRegion-replication_how-it-works.html#howitworks_mrr_opt_in) in the *Amazon Keyspaces Developer Guide*.
*Required*: No
*Type*: Array of String
*Minimum*: `2`
*Maximum*: `20`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReplicationStrategy`  <a name="cfn-cassandra-keyspace-replicationspecification-replicationstrategy"></a>
The options are:
+ `SINGLE_REGION` (optional)
+  `MULTI_REGION`
If no value is specified, the default is `SINGLE_REGION`. If `MULTI_REGION` is specified, `RegionList` is required.
*Required*: No
*Type*: String
*Allowed values*: `SINGLE_REGION | MULTI_REGION`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
