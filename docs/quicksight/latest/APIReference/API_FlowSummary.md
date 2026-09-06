---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_FlowSummary.html
---

# FlowSummary
<a name="API_FlowSummary"></a>

The basic information of the flow exluding its definition specifying the steps.

## Contents
<a name="API_FlowSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-FlowSummary-Arn"></a>
The Amazon Resource Name (ARN) of the flow.
Type: String
Required: Yes

 ** CreatedTime **   <a name="QS-Type-FlowSummary-CreatedTime"></a>
The time this flow was created.
Type: Timestamp
Required: Yes

 ** FlowId **   <a name="QS-Type-FlowSummary-FlowId"></a>
The unique identifier of the flow.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

 ** Name **   <a name="QS-Type-FlowSummary-Name"></a>
The display name of the flow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: Yes

 ** CreatedBy **   <a name="QS-Type-FlowSummary-CreatedBy"></a>
The identifier of the principal who created the flow.
Type: String
Required: No

 ** Description **   <a name="QS-Type-FlowSummary-Description"></a>
The description of the flow.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** LastPublishedAt **   <a name="QS-Type-FlowSummary-LastPublishedAt"></a>
The last time this flow was published.
Type: Timestamp
Required: No

 ** LastPublishedBy **   <a name="QS-Type-FlowSummary-LastPublishedBy"></a>
The identifier of the last principal who published the flow.
Type: String
Required: No

 ** LastUpdatedBy **   <a name="QS-Type-FlowSummary-LastUpdatedBy"></a>
The identifier of the last principal who updated the flow.
Type: String
Required: No

 ** LastUpdatedTime **   <a name="QS-Type-FlowSummary-LastUpdatedTime"></a>
The last time this flow was modified.
Type: Timestamp
Required: No

 ** PublishState **   <a name="QS-Type-FlowSummary-PublishState"></a>
The publish state for the flow. The valid values are `DRAFT`, `PUBLISHED`, or `PENDING_APPROVAL`.
Type: String
Valid Values: `PUBLISHED | DRAFT | PENDING_APPROVAL`
Required: No

 ** RunCount **   <a name="QS-Type-FlowSummary-RunCount"></a>
The number of runs done for the flow.
Type: Integer
Required: No

 ** UserCount **   <a name="QS-Type-FlowSummary-UserCount"></a>
The number of users who have used the flow.
Type: Integer
Required: No

## See Also
<a name="API_FlowSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/FlowSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/FlowSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/FlowSummary)
