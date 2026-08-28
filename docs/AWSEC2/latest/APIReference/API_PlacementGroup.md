---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_PlacementGroup.html
---

# PlacementGroup
<a name="API_PlacementGroup"></a>

Describes a placement group.

## Contents
<a name="API_PlacementGroup_Contents"></a>

 ** groupArn **
The Amazon Resource Name (ARN) of the placement group.
Type: String
Required: No

 ** groupId **
The ID of the placement group.
Type: String
Required: No

 ** groupName **
The name of the placement group.
Type: String
Required: No

 ** linkedGroupId **
Reserved for future use.
Type: String
Required: No

 ** operator **
The service provider that manages the Placement Group.
Type: [OperatorResponse](API_OperatorResponse.md) object
Required: No

 ** parentGroupId **
The ID of the parent placement group.
Type: String
Required: No

 ** partitionCount **
The number of partitions. Valid only if **strategy** is set to `partition`.
Type: Integer
Required: No

 ** spreadLevel **
The spread level for the placement group. *Only* Outpost placement groups can be spread across hosts.
Type: String
Valid Values: `host | rack`
Required: No

 ** state **
The state of the placement group.
Type: String
Valid Values: `pending | available | deleting | deleted`
Required: No

 ** strategy **
The placement strategy.
Type: String
Valid Values: `cluster | spread | partition | precision-time`
Required: No

 ** TagSet.N **
Any tags applied to the placement group.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_PlacementGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/PlacementGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/PlacementGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/PlacementGroup)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
