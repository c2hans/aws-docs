---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-writeondemandthroughputsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::GlobalTable WriteOnDemandThroughputSettings
<a name="aws-properties-dynamodb-globaltable-writeondemandthroughputsettings"></a>

Sets the write request settings for a global table or a global secondary index. You can only specify this setting if your resource uses the `PAY_PER_REQUEST``BillingMode`.

## Syntax
<a name="aws-properties-dynamodb-globaltable-writeondemandthroughputsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dynamodb-globaltable-writeondemandthroughputsettings-syntax.json"></a>

```
{
  "[MaxWriteRequestUnits](#cfn-dynamodb-globaltable-writeondemandthroughputsettings-maxwriterequestunits)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-dynamodb-globaltable-writeondemandthroughputsettings-syntax.yaml"></a>

```
  [MaxWriteRequestUnits](#cfn-dynamodb-globaltable-writeondemandthroughputsettings-maxwriterequestunits): {{Integer}}
```

## Properties
<a name="aws-properties-dynamodb-globaltable-writeondemandthroughputsettings-properties"></a>

`MaxWriteRequestUnits`  <a name="cfn-dynamodb-globaltable-writeondemandthroughputsettings-maxwriterequestunits"></a>
Maximum number of write request settings for the specified replica of a global table.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
