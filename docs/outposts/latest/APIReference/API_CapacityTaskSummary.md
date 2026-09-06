---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_CapacityTaskSummary.html
---

# CapacityTaskSummary
<a name="API_CapacityTaskSummary"></a>

The summary of the capacity task.

## Contents
<a name="API_CapacityTaskSummary_Contents"></a>

 ** AssetId **   <a name="outposts-Type-CapacityTaskSummary-AssetId"></a>
The ID of the asset. An Outpost asset can be a single server within an Outposts rack or an Outposts server configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^(\w+)$`
Required: No

 ** CapacityTaskId **   <a name="outposts-Type-CapacityTaskSummary-CapacityTaskId"></a>
The ID of the specified capacity task.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `^cap-[a-f0-9]{17}$`
Required: No

 ** CapacityTaskStatus **   <a name="outposts-Type-CapacityTaskSummary-CapacityTaskStatus"></a>
The status of the capacity task.
Type: String
Valid Values: `REQUESTED | IN_PROGRESS | FAILED | COMPLETED | WAITING_FOR_EVACUATION | CANCELLATION_IN_PROGRESS | CANCELLED`
Required: No

 ** CompletionDate **   <a name="outposts-Type-CapacityTaskSummary-CompletionDate"></a>
The date that the specified capacity task successfully ran.
Type: Timestamp
Required: No

 ** CreationDate **   <a name="outposts-Type-CapacityTaskSummary-CreationDate"></a>
The date that the specified capacity task was created.
Type: Timestamp
Required: No

 ** LastModifiedDate **   <a name="outposts-Type-CapacityTaskSummary-LastModifiedDate"></a>
The date that the specified capacity was last modified.
Type: Timestamp
Required: No

 ** OrderId **   <a name="outposts-Type-CapacityTaskSummary-OrderId"></a>
The ID of the AWS Outposts order of the host associated with the capacity task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `oo-[a-f0-9]{17}$`
Required: No

 ** OutpostId **   <a name="outposts-Type-CapacityTaskSummary-OutpostId"></a>
The ID of the Outpost associated with the specified capacity task.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 180.
Pattern: `^(arn:aws([a-z-]+)?:outposts:[a-z\d-]+:\d{12}:outpost/)?op-[a-f0-9]{17}$`
Required: No

## See Also
<a name="API_CapacityTaskSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/CapacityTaskSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/CapacityTaskSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/CapacityTaskSummary)
