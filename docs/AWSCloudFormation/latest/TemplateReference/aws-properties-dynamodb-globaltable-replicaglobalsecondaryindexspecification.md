---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-dynamodb-globaltable-replicaglobalsecondaryindexspecification.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::DynamoDB::GlobalTable ReplicaGlobalSecondaryIndexSpecification
<a name="aws-properties-dynamodb-globaltable-replicaglobalsecondaryindexspecification"></a>

Represents the properties of a global secondary index that can be set on a per-replica basis.

## Syntax
<a name="aws-properties-dynamodb-globaltable-replicaglobalsecondaryindexspecification-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-dynamodb-globaltable-replicaglobalsecondaryindexspecification-syntax.json"></a>

```
{
  "[ContributorInsightsSpecification](#cfn-dynamodb-globaltable-replicaglobalsecondaryindexspecification-contributorinsightsspecification)" : {{ContributorInsightsSpecification}},
  "[IndexName](#cfn-dynamodb-globaltable-replicaglobalsecondaryindexspecification-indexname)" : {{String}},
  "[ReadOnDemandThroughputSettings](#cfn-dynamodb-globaltable-replicaglobalsecondaryindexspecification-readondemandthroughputsettings)" : {{ReadOnDemandThroughputSettings}},
  "[ReadProvisionedThroughputSettings](#cfn-dynamodb-globaltable-replicaglobalsecondaryindexspecification-readprovisionedthroughputsettings)" : {{ReadProvisionedThroughputSettings}}
}
```

### YAML
<a name="aws-properties-dynamodb-globaltable-replicaglobalsecondaryindexspecification-syntax.yaml"></a>

```
  [ContributorInsightsSpecification](#cfn-dynamodb-globaltable-replicaglobalsecondaryindexspecification-contributorinsightsspecification): {{
    ContributorInsightsSpecification}}
  [IndexName](#cfn-dynamodb-globaltable-replicaglobalsecondaryindexspecification-indexname): {{String}}
  [ReadOnDemandThroughputSettings](#cfn-dynamodb-globaltable-replicaglobalsecondaryindexspecification-readondemandthroughputsettings): {{
    ReadOnDemandThroughputSettings}}
  [ReadProvisionedThroughputSettings](#cfn-dynamodb-globaltable-replicaglobalsecondaryindexspecification-readprovisionedthroughputsettings): {{
    ReadProvisionedThroughputSettings}}
```

## Properties
<a name="aws-properties-dynamodb-globaltable-replicaglobalsecondaryindexspecification-properties"></a>

`ContributorInsightsSpecification`  <a name="cfn-dynamodb-globaltable-replicaglobalsecondaryindexspecification-contributorinsightsspecification"></a>
Updates the status for contributor insights for a specific table or index. CloudWatch Contributor Insights for DynamoDB graphs display the partition key and (if applicable) sort key of frequently accessed items and frequently throttled items in plaintext. If you require the use of AWS Key Management Service (KMS) to encrypt this table’s partition key and sort key data with an AWS managed key or customer managed key, you should not enable CloudWatch Contributor Insights for DynamoDB for this table.
*Required*: No
*Type*: [ContributorInsightsSpecification](aws-properties-dynamodb-globaltable-contributorinsightsspecification.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IndexName`  <a name="cfn-dynamodb-globaltable-replicaglobalsecondaryindexspecification-indexname"></a>
The name of the global secondary index. The name must be unique among all other indexes on this table.
*Required*: Yes
*Type*: String
*Minimum*: `3`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ReadOnDemandThroughputSettings`  <a name="cfn-dynamodb-globaltable-replicaglobalsecondaryindexspecification-readondemandthroughputsettings"></a>
Sets the read request settings for a replica global secondary index. You can only specify this setting if your resource uses the `PAY_PER_REQUEST``BillingMode`.
*Required*: No
*Type*: [ReadOnDemandThroughputSettings](aws-properties-dynamodb-globaltable-readondemandthroughputsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ReadProvisionedThroughputSettings`  <a name="cfn-dynamodb-globaltable-replicaglobalsecondaryindexspecification-readprovisionedthroughputsettings"></a>
Allows you to specify the read capacity settings for a replica global secondary index when the `BillingMode` is set to `PROVISIONED`.
*Required*: No
*Type*: [ReadProvisionedThroughputSettings](aws-properties-dynamodb-globaltable-readprovisionedthroughputsettings.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
