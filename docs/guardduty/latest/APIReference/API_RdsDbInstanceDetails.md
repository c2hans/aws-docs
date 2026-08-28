---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_RdsDbInstanceDetails.html
---

# RdsDbInstanceDetails
<a name="API_RdsDbInstanceDetails"></a>

Contains information about the resource type `RDSDBInstance` involved in a GuardDuty finding.

## Contents
<a name="API_RdsDbInstanceDetails_Contents"></a>

 ** dbClusterIdentifier **   <a name="guardduty-Type-RdsDbInstanceDetails-dbClusterIdentifier"></a>
The identifier of the database cluster that contains the database instance ID involved in the finding.
Type: String
Required: No

 ** dbInstanceArn **   <a name="guardduty-Type-RdsDbInstanceDetails-dbInstanceArn"></a>
The Amazon Resource Name (ARN) that identifies the database instance involved in the finding.
Type: String
Required: No

 ** dbInstanceIdentifier **   <a name="guardduty-Type-RdsDbInstanceDetails-dbInstanceIdentifier"></a>
The identifier associated to the database instance that was involved in the finding.
Type: String
Required: No

 ** dbiResourceId **   <a name="guardduty-Type-RdsDbInstanceDetails-dbiResourceId"></a>
The unique ID of the database resource involved in the activity that prompted GuardDuty to generate the finding.
Type: String
Required: No

 ** engine **   <a name="guardduty-Type-RdsDbInstanceDetails-engine"></a>
The database engine of the database instance involved in the finding.
Type: String
Required: No

 ** engineVersion **   <a name="guardduty-Type-RdsDbInstanceDetails-engineVersion"></a>
The version of the database engine that was involved in the finding.
Type: String
Required: No

 ** tags **   <a name="guardduty-Type-RdsDbInstanceDetails-tags"></a>
Information about the tag key-value pairs.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_RdsDbInstanceDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/RdsDbInstanceDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/RdsDbInstanceDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/RdsDbInstanceDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GuardDuty. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query guardduty` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
