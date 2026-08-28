---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-writeprovisionedthroughputsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::GlobalTable WriteProvisionedThroughputSettings
<a name="aws-properties-dynamodb-globaltable-writeprovisionedthroughputsettings"></a>

Specifies an auto scaling policy for write capacity. This policy will be applied to all replicas. This setting must be specified if `BillingMode` is set to `PROVISIONED`.

## Syntax
<a name="aws-properties-dynamodb-globaltable-writeprovisionedthroughputsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dynamodb-globaltable-writeprovisionedthroughputsettings-syntax.json"></a>

```
{
  "[WriteCapacityAutoScalingSettings](#cfn-dynamodb-globaltable-writeprovisionedthroughputsettings-writecapacityautoscalingsettings)" : {{CapacityAutoScalingSettings}}
}
```

### YAML
<a name="aws-properties-dynamodb-globaltable-writeprovisionedthroughputsettings-syntax.yaml"></a>

```
  [WriteCapacityAutoScalingSettings](#cfn-dynamodb-globaltable-writeprovisionedthroughputsettings-writecapacityautoscalingsettings): {{
    CapacityAutoScalingSettings}}
```

## Properties
<a name="aws-properties-dynamodb-globaltable-writeprovisionedthroughputsettings-properties"></a>

`WriteCapacityAutoScalingSettings`  <a name="cfn-dynamodb-globaltable-writeprovisionedthroughputsettings-writecapacityautoscalingsettings"></a>
Specifies auto scaling settings for the replica table or global secondary index.
*Required*: No
*Type*: [CapacityAutoScalingSettings](aws-properties-dynamodb-globaltable-capacityautoscalingsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
