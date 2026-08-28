---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_RdsLimitlessDbDetails.html
---

# RdsLimitlessDbDetails
<a name="API_RdsLimitlessDbDetails"></a>

Contains information about the resource type `RDSLimitlessDB` that is involved in a GuardDuty finding.

## Contents
<a name="API_RdsLimitlessDbDetails_Contents"></a>

 ** dbClusterIdentifier **   <a name="guardduty-Type-RdsLimitlessDbDetails-dbClusterIdentifier"></a>
The name of the database cluster that is a part of the Limitless Database.
Type: String
Required: No

 ** dbShardGroupArn **   <a name="guardduty-Type-RdsLimitlessDbDetails-dbShardGroupArn"></a>
The Amazon Resource Name (ARN) that identifies the DB shard group.
Type: String
Required: No

 ** dbShardGroupIdentifier **   <a name="guardduty-Type-RdsLimitlessDbDetails-dbShardGroupIdentifier"></a>
The name associated with the Limitless DB shard group.
Type: String
Required: No

 ** dbShardGroupResourceId **   <a name="guardduty-Type-RdsLimitlessDbDetails-dbShardGroupResourceId"></a>
The resource identifier of the DB shard group within the Limitless Database.
Type: String
Required: No

 ** engine **   <a name="guardduty-Type-RdsLimitlessDbDetails-engine"></a>
The database engine of the database instance involved in the finding.
Type: String
Required: No

 ** engineVersion **   <a name="guardduty-Type-RdsLimitlessDbDetails-engineVersion"></a>
The version of the database engine.
Type: String
Required: No

 ** tags **   <a name="guardduty-Type-RdsLimitlessDbDetails-tags"></a>
Information about the tag key-value pair.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_RdsLimitlessDbDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/RdsLimitlessDbDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/RdsLimitlessDbDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/RdsLimitlessDbDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
