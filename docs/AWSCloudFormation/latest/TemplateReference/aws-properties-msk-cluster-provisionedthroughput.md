---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-cluster-provisionedthroughput.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::Cluster ProvisionedThroughput
<a name="aws-properties-msk-cluster-provisionedthroughput"></a>

Contains information about provisioned throughput for EBS storage volumes attached to kafka broker nodes.

## Syntax
<a name="aws-properties-msk-cluster-provisionedthroughput-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-cluster-provisionedthroughput-syntax.json"></a>

```
{
  "[Enabled](#cfn-msk-cluster-provisionedthroughput-enabled)" : {{Boolean}},
  "[VolumeThroughput](#cfn-msk-cluster-provisionedthroughput-volumethroughput)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-msk-cluster-provisionedthroughput-syntax.yaml"></a>

```
  [Enabled](#cfn-msk-cluster-provisionedthroughput-enabled): {{Boolean}}
  [VolumeThroughput](#cfn-msk-cluster-provisionedthroughput-volumethroughput): {{Integer}}
```

## Properties
<a name="aws-properties-msk-cluster-provisionedthroughput-properties"></a>

`Enabled`  <a name="cfn-msk-cluster-provisionedthroughput-enabled"></a>
Provisioned throughput is on or off.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VolumeThroughput`  <a name="cfn-msk-cluster-provisionedthroughput-volumethroughput"></a>
Throughput value of the EBS volumes for the data drive on each kafka broker node in MiB per second.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
