---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CapacityManagerMonitoredTagKey.html
---

# CapacityManagerMonitoredTagKey
<a name="API_CapacityManagerMonitoredTagKey"></a>

 Describes a tag key that is being monitored by Capacity Manager, including its activation status and the earliest available data point.

## Contents
<a name="API_CapacityManagerMonitoredTagKey_Contents"></a>

 ** capacityManagerProvided **
 Indicates whether this tag key is provided by Capacity Manager by default, rather than being user-activated.
Type: Boolean
Required: No

 ** earliestDatapointTimestamp **
 The earliest timestamp from which tag data is available for queries, in UTC ISO 8601 format.
Type: Timestamp
Required: No

 ** status **
 The current status of the monitored tag key. Valid values are `activating`, `activated`, `deactivating`, and `suspended`.
Type: String
Valid Values: `activating | activated | deactivating | suspended`
Required: No

 ** statusMessage **
 A message providing additional details about the current status of the monitored tag key.
Type: String
Required: No

 ** tagKey **
 The tag key being monitored.
Type: String
Required: No

## See Also
<a name="API_CapacityManagerMonitoredTagKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CapacityManagerMonitoredTagKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CapacityManagerMonitoredTagKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CapacityManagerMonitoredTagKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
