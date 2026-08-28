---
source_url: https://docs.aws.amazon.com/awscloudtrail/latest/APIReference/API_ImportsListItem.html
---

# ImportsListItem
<a name="API_ImportsListItem"></a>

 Contains information about an import that was returned by a lookup request.

## Contents
<a name="API_ImportsListItem_Contents"></a>

 ** CreatedTimestamp **   <a name="awscloudtrail-Type-ImportsListItem-CreatedTimestamp"></a>
 The timestamp of the import's creation.
Type: Timestamp
Required: No

 ** Destinations **   <a name="awscloudtrail-Type-ImportsListItem-Destinations"></a>
 The ARN of the destination event data store.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 3. Maximum length of 256.
Pattern: `^[a-zA-Z0-9._/\-:]+$`
Required: No

 ** ImportId **   <a name="awscloudtrail-Type-ImportsListItem-ImportId"></a>
 The ID of the import.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-f0-9\-]+$`
Required: No

 ** ImportStatus **   <a name="awscloudtrail-Type-ImportsListItem-ImportStatus"></a>
 The status of the import.
Type: String
Valid Values: `INITIALIZING | IN_PROGRESS | FAILED | STOPPED | COMPLETED`
Required: No

 ** UpdatedTimestamp **   <a name="awscloudtrail-Type-ImportsListItem-UpdatedTimestamp"></a>
 The timestamp of the import's last update.
Type: Timestamp
Required: No

## See Also
<a name="API_ImportsListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudtrail-2013-11-01/ImportsListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudtrail-2013-11-01/ImportsListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudtrail-2013-11-01/ImportsListItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudTrail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query awscloudtrail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
