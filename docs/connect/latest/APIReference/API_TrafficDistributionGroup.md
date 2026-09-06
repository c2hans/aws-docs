---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_TrafficDistributionGroup.html
---

# TrafficDistributionGroup
<a name="API_TrafficDistributionGroup"></a>

Information about a traffic distribution group.

## Contents
<a name="API_TrafficDistributionGroup_Contents"></a>

 ** Arn **   <a name="connect-Type-TrafficDistributionGroup-Arn"></a>
The Amazon Resource Name (ARN) of the traffic distribution group.
Type: String
Pattern: `^arn:([a-zA-Z0-9-]+):connect:[a-z]+-[a-z-]+-[0-9]+:[0-9]+:traffic-distribution-group/[a-zA-Z0-9_-]+$`
Required: No

 ** Description **   <a name="connect-Type-TrafficDistributionGroup-Description"></a>
The description of the traffic distribution group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `(^[\S].*[\S]$)|(^[\S]$)`
Required: No

 ** Id **   <a name="connect-Type-TrafficDistributionGroup-Id"></a>
The identifier of the traffic distribution group. This can be the ID or the ARN if the API is being called in the Region where the traffic distribution group was created. The ARN must be provided if the call is from the replicated Region.
Type: String
Pattern: `^[a-zA-Z0-9_-]+$`
Required: No

 ** InstanceArn **   <a name="connect-Type-TrafficDistributionGroup-InstanceArn"></a>
The Amazon Resource Name (ARN).
Type: String
Pattern: `^arn:([a-zA-Z0-9-]+):connect:[a-z]+-[a-z-]+-[0-9]+:[0-9]+:instance/[a-zA-Z0-9_-]+$`
Required: No

 ** IsDefault **   <a name="connect-Type-TrafficDistributionGroup-IsDefault"></a>
Whether this is the default traffic distribution group created during instance replication. The default traffic distribution group cannot be deleted by the `DeleteTrafficDistributionGroup` API. The default traffic distribution group is deleted as part of the process for deleting a replica.
The `SignInConfig` distribution is available only on a default `TrafficDistributionGroup` (see the `IsDefault` parameter in the [TrafficDistributionGroup](https://docs.aws.amazon.com/connect/latest/APIReference/API_TrafficDistributionGroup.html) data type). If you call `UpdateTrafficDistribution` with a modified `SignInConfig` and a non-default `TrafficDistributionGroup`, an `InvalidRequestException` is returned.
Type: Boolean
Required: No

 ** Name **   <a name="connect-Type-TrafficDistributionGroup-Name"></a>
The name of the traffic distribution group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(^[\S].*[\S]$)|(^[\S]$)`
Required: No

 ** Status **   <a name="connect-Type-TrafficDistributionGroup-Status"></a>
The status of the traffic distribution group.
+  `CREATION_IN_PROGRESS` means the previous [CreateTrafficDistributionGroup](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateTrafficDistributionGroup.html) operation is still in progress and has not yet completed.
+  `ACTIVE` means the previous [CreateTrafficDistributionGroup](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateTrafficDistributionGroup.html) operation has succeeded.
+  `CREATION_FAILED` indicates that the previous [CreateTrafficDistributionGroup](https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateTrafficDistributionGroup.html) operation has failed.
+  `PENDING_DELETION` means the previous [DeleteTrafficDistributionGroup](https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteTrafficDistributionGroup.html) operation is still in progress and has not yet completed.
+  `DELETION_FAILED` means the previous [DeleteTrafficDistributionGroup](https://docs.aws.amazon.com/connect/latest/APIReference/API_DeleteTrafficDistributionGroup.html) operation has failed.
+  `UPDATE_IN_PROGRESS` means the previous [UpdateTrafficDistribution](https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateTrafficDistribution.html) operation is still in progress and has not yet completed.
Type: String
Valid Values: `CREATION_IN_PROGRESS | ACTIVE | CREATION_FAILED | PENDING_DELETION | DELETION_FAILED | UPDATE_IN_PROGRESS`
Required: No

 ** Tags **   <a name="connect-Type-TrafficDistributionGroup-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_TrafficDistributionGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/TrafficDistributionGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/TrafficDistributionGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/TrafficDistributionGroup)
