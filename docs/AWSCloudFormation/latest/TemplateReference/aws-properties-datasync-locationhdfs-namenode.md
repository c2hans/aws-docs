---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-datasync-locationhdfs-namenode.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DataSync::LocationHDFS NameNode
<a name="aws-properties-datasync-locationhdfs-namenode"></a>

The NameNode of the Hadoop Distributed File System (HDFS). The NameNode manages the file system's namespace and performs operations such as opening, closing, and renaming files and directories. The NameNode also contains the information to map blocks of data to the DataNodes.

## Syntax
<a name="aws-properties-datasync-locationhdfs-namenode-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-datasync-locationhdfs-namenode-syntax.json"></a>

```
{
  "[Hostname](#cfn-datasync-locationhdfs-namenode-hostname)" : {{String}},
  "[Port](#cfn-datasync-locationhdfs-namenode-port)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-datasync-locationhdfs-namenode-syntax.yaml"></a>

```
  [Hostname](#cfn-datasync-locationhdfs-namenode-hostname): {{String}}
  [Port](#cfn-datasync-locationhdfs-namenode-port): {{Integer}}
```

## Properties
<a name="aws-properties-datasync-locationhdfs-namenode-properties"></a>

`Hostname`  <a name="cfn-datasync-locationhdfs-namenode-hostname"></a>
The hostname of the NameNode in the HDFS cluster. This value is the IP address or Domain Name Service (DNS) name of the NameNode. An agent that's installed on-premises uses this hostname to communicate with the NameNode in the network.
*Required*: Yes
*Type*: String
*Pattern*: `^(([a-zA-Z0-9\-]*[a-zA-Z0-9])\.)*([A-Za-z0-9\-]*[A-Za-z0-9])$`
*Maximum*: `255`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Port`  <a name="cfn-datasync-locationhdfs-namenode-port"></a>
The port that the NameNode uses to listen to client requests.
*Required*: Yes
*Type*: Integer
*Minimum*: `1`
*Maximum*: `65536`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
