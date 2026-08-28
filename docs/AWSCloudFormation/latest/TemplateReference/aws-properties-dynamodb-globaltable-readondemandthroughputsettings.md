---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-readondemandthroughputsettings.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::GlobalTable ReadOnDemandThroughputSettings
<a name="aws-properties-dynamodb-globaltable-readondemandthroughputsettings"></a>

Sets the read request settings for a replica table or a replica global secondary index. You can only specify this setting if your resource uses the `PAY_PER_REQUEST``BillingMode`.

## Syntax
<a name="aws-properties-dynamodb-globaltable-readondemandthroughputsettings-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dynamodb-globaltable-readondemandthroughputsettings-syntax.json"></a>

```
{
  "[MaxReadRequestUnits](#cfn-dynamodb-globaltable-readondemandthroughputsettings-maxreadrequestunits)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-dynamodb-globaltable-readondemandthroughputsettings-syntax.yaml"></a>

```
  [MaxReadRequestUnits](#cfn-dynamodb-globaltable-readondemandthroughputsettings-maxreadrequestunits): {{Integer}}
```

## Properties
<a name="aws-properties-dynamodb-globaltable-readondemandthroughputsettings-properties"></a>

`MaxReadRequestUnits`  <a name="cfn-dynamodb-globaltable-readondemandthroughputsettings-maxreadrequestunits"></a>
Maximum number of read request units for the specified replica of a global table.
*Required*: No
*Type*: Integer
*Minimum*: `1`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
