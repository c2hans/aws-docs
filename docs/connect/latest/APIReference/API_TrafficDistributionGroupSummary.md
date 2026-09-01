---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_TrafficDistributionGroupSummary.html
---

# TrafficDistributionGroupSummary
<a name="API_TrafficDistributionGroupSummary"></a>

Information about traffic distribution groups.

## Contents
<a name="API_TrafficDistributionGroupSummary_Contents"></a>

 ** Arn **   <a name="connect-Type-TrafficDistributionGroupSummary-Arn"></a>
The Amazon Resource Name (ARN) of the traffic distribution group.
Type: String
Pattern: `^arn:([a-zA-Z0-9-]+):connect:[a-z]+-[a-z-]+-[0-9]+:[0-9]+:traffic-distribution-group/[a-zA-Z0-9_-]+$`
Required: No

 ** Id **   <a name="connect-Type-TrafficDistributionGroupSummary-Id"></a>
The identifier of the traffic distribution group. This can be the ID or the ARN if the API is being called in the Region where the traffic distribution group was created. The ARN must be provided if the call is from the replicated Region.
Type: String
Pattern: `^[a-zA-Z0-9_-]+$`
Required: No

 ** InstanceArn **   <a name="connect-Type-TrafficDistributionGroupSummary-InstanceArn"></a>
The Amazon Resource Name (ARN) of the instance.
Type: String
Pattern: `^arn:([a-zA-Z0-9-]+):connect:[a-z]+-[a-z-]+-[0-9]+:[0-9]+:instance/[a-zA-Z0-9_-]+$`
Required: No

 ** IsDefault **   <a name="connect-Type-TrafficDistributionGroupSummary-IsDefault"></a>
Whether this is the default traffic distribution group created during instance replication. The default traffic distribution group cannot be deleted by the `DeleteTrafficDistributionGroup` API. The default traffic distribution group is deleted as part of the process for deleting a replica.
Type: Boolean
Required: No

 ** Name **   <a name="connect-Type-TrafficDistributionGroupSummary-Name"></a>
The name of the traffic distribution group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[\S].*[\S]$)|(^[\S]$)`
Required: No

 ** Status **   <a name="connect-Type-TrafficDistributionGroupSummary-Status"></a>
The status of the traffic distribution group.
+  `CREATION_IN_PROGRESS` means the previous [CreateTrafficDistributionGroup](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateTrafficDistributionGroup.html) operation is still in progress and has not yet completed.
+  `ACTIVE` means the previous [CreateTrafficDistributionGroup](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateTrafficDistributionGroup.html) operation has succeeded.
+  `CREATION_FAILED` indicates that the previous [CreateTrafficDistributionGroup](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateTrafficDistributionGroup.html) operation has failed.
+  `PENDING_DELETION` means the previous [DeleteTrafficDistributionGroup](https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteTrafficDistributionGroup.html) operation is still in progress and has not yet completed.
+  `DELETION_FAILED` means the previous [DeleteTrafficDistributionGroup](https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteTrafficDistributionGroup.html) operation has failed.
+  `UPDATE_IN_PROGRESS` means the previous [UpdateTrafficDistributionGroup](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateTrafficDistributionGroup.html) operation is still in progress and has not yet completed.
Type: String
Valid Values: `CREATION_IN_PROGRESS | ACTIVE | CREATION_FAILED | PENDING_DELETION | DELETION_FAILED | UPDATE_IN_PROGRESS`
Required: No

## See Also
<a name="API_TrafficDistributionGroupSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/TrafficDistributionGroupSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/TrafficDistributionGroupSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/TrafficDistributionGroupSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
