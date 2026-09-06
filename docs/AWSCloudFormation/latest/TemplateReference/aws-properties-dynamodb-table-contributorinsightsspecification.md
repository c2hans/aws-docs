---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-table-contributorinsightsspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::Table ContributorInsightsSpecification
<a name="aws-properties-dynamodb-table-contributorinsightsspecification"></a>

Configures contributor insights settings for a table or one of its indexes.

## Syntax
<a name="aws-properties-dynamodb-table-contributorinsightsspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dynamodb-table-contributorinsightsspecification-syntax.json"></a>

```
{
  "[Enabled](#cfn-dynamodb-table-contributorinsightsspecification-enabled)" : {{Boolean}},
  "[Mode](#cfn-dynamodb-table-contributorinsightsspecification-mode)" : {{String}}
}
```

### YAML
<a name="aws-properties-dynamodb-table-contributorinsightsspecification-syntax.yaml"></a>

```
  [Enabled](#cfn-dynamodb-table-contributorinsightsspecification-enabled): {{Boolean}}
  [Mode](#cfn-dynamodb-table-contributorinsightsspecification-mode): {{String}}
```

## Properties
<a name="aws-properties-dynamodb-table-contributorinsightsspecification-properties"></a>

`Enabled`  <a name="cfn-dynamodb-table-contributorinsightsspecification-enabled"></a>
Indicates whether CloudWatch Contributor Insights are to be enabled (true) or disabled (false).
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Mode`  <a name="cfn-dynamodb-table-contributorinsightsspecification-mode"></a>
Specifies the CloudWatch Contributor Insights mode for a table. Valid values are `ACCESSED_AND_THROTTLED_KEYS` (tracks all access and throttled events) or `THROTTLED_KEYS` (tracks only throttled events). This setting determines what type of contributor insights data is collected for the table.
*Required*: No
*Type*: String
*Allowed values*: `ACCESSED_AND_THROTTLED_KEYS | THROTTLED_KEYS`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
