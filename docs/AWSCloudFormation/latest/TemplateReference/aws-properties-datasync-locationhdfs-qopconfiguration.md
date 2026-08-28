---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datasync-locationhdfs-qopconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationHDFS QopConfiguration
<a name="aws-properties-datasync-locationhdfs-qopconfiguration"></a>

The Quality of Protection (QOP) configuration specifies the Remote Procedure Call (RPC) and data transfer privacy settings configured on the Hadoop Distributed File System (HDFS) cluster.

## Syntax
<a name="aws-properties-datasync-locationhdfs-qopconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datasync-locationhdfs-qopconfiguration-syntax.json"></a>

```
{
  "[DataTransferProtection](#cfn-datasync-locationhdfs-qopconfiguration-datatransferprotection)" : {{String}},
  "[RpcProtection](#cfn-datasync-locationhdfs-qopconfiguration-rpcprotection)" : {{String}}
}
```

### YAML
<a name="aws-properties-datasync-locationhdfs-qopconfiguration-syntax.yaml"></a>

```
  [DataTransferProtection](#cfn-datasync-locationhdfs-qopconfiguration-datatransferprotection): {{String}}
  [RpcProtection](#cfn-datasync-locationhdfs-qopconfiguration-rpcprotection): {{String}}
```

## Properties
<a name="aws-properties-datasync-locationhdfs-qopconfiguration-properties"></a>

`DataTransferProtection`  <a name="cfn-datasync-locationhdfs-qopconfiguration-datatransferprotection"></a>
The data transfer protection setting configured on the HDFS cluster. This setting corresponds to your `dfs.data.transfer.protection` setting in the `hdfs-site.xml` file on your Hadoop cluster.
*Required*: No
*Type*: String
*Allowed values*: `AUTHENTICATION | INTEGRITY | PRIVACY | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RpcProtection`  <a name="cfn-datasync-locationhdfs-qopconfiguration-rpcprotection"></a>
The Remote Procedure Call (RPC) protection setting configured on the HDFS cluster. This setting corresponds to your `hadoop.rpc.protection` setting in your `core-site.xml` file on your Hadoop cluster.
*Required*: No
*Type*: String
*Allowed values*: `AUTHENTICATION | INTEGRITY | PRIVACY | DISABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
