---
source_url: https://docs.aws.amazon.com/health/latest/APIReference/API_AffectedEntity.html
---

# AffectedEntity
<a name="API_AffectedEntity"></a>

Information about an entity that is affected by a Health event.

## Contents
<a name="API_AffectedEntity_Contents"></a>

 ** awsAccountId **   <a name="AWSHealth-Type-AffectedEntity-awsAccountId"></a>
The 12-digit AWS account number that contains the affected entity.
Type: String
Length Constraints: Maximum length of 12.
Pattern: `^\S+$`
Required: No

 ** entityArn **   <a name="AWSHealth-Type-AffectedEntity-entityArn"></a>
The unique identifier for the entity. Format: `arn:aws:health:entity-region:aws-account:entity/entity-id `. Example: `arn:aws:health:us-east-1:111222333444:entity/AVh5GGT7ul1arKr1sE1K`
Type: String
Length Constraints: Maximum length of 1600.
Pattern: `.{0,1600}`
Required: No

 ** entityMetadata **   <a name="AWSHealth-Type-AffectedEntity-entityMetadata"></a>
Additional metadata about the affected entity.
Type: String to string map
Key Length Constraints: Maximum length of 1024.
Value Length Constraints: Maximum length of 1024.
Required: No

 ** entityUrl **   <a name="AWSHealth-Type-AffectedEntity-entityUrl"></a>
The URL of the affected entity.
Type: String
Required: No

 ** entityValue **   <a name="AWSHealth-Type-AffectedEntity-entityValue"></a>
The ID of the affected entity.
Type: String
Length Constraints: Maximum length of 1224.
Pattern: `.{0,1224}`
Required: No

 ** eventArn **   <a name="AWSHealth-Type-AffectedEntity-eventArn"></a>
The unique identifier for the event. The event ARN has the `arn:aws:health:event-region::event/SERVICE/EVENT_TYPE_CODE/EVENT_TYPE_PLUS_ID ` format.
For example, an event ARN might look like the following:
 `arn:aws:health:us-east-1::event/EC2/EC2_INSTANCE_RETIREMENT_SCHEDULED/EC2_INSTANCE_RETIREMENT_SCHEDULED_ABC123-DEF456`
Type: String
Length Constraints: Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+(-[a-z]+)?)?:health:[^:]*:[^:]*:event(?:/[\w-]+){3}`
Required: No

 ** lastUpdatedTime **   <a name="AWSHealth-Type-AffectedEntity-lastUpdatedTime"></a>
The most recent time that the entity was updated.
Type: Timestamp
Required: No

 ** statusCode **   <a name="AWSHealth-Type-AffectedEntity-statusCode"></a>
The most recent status of the entity affected by the event. The possible values are `IMPAIRED`, `UNIMPAIRED`, `UNKNOWN`, `PENDING`, and `RESOLVED`.
Type: String
Valid Values: `IMPAIRED | UNIMPAIRED | UNKNOWN | PENDING | RESOLVED`
Required: No

 ** tags **   <a name="AWSHealth-Type-AffectedEntity-tags"></a>
A map of entity tags attached to the affected entity.
Currently, the `tags` property isn't supported.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Maximum length of 127.
Key Pattern: `.{0,127}`
Value Length Constraints: Maximum length of 255.
Value Pattern: `.{0,255}`
Required: No

## See Also
<a name="API_AffectedEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/health-2016-08-04/AffectedEntity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/health-2016-08-04/AffectedEntity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/health-2016-08-04/AffectedEntity)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query health` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
