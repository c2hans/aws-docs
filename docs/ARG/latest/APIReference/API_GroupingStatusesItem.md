---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_GroupingStatusesItem.html
---

# GroupingStatusesItem
<a name="API_GroupingStatusesItem"></a>

The information about a grouping or ungrouping resource action.

## Contents
<a name="API_GroupingStatusesItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Action **   <a name="ARG-Type-GroupingStatusesItem-Action"></a>
Describes the resource grouping action with values of `GROUP` or `UNGROUP`.
Type: String
Valid Values: `GROUP | UNGROUP`
Required: No

 ** ErrorCode **   <a name="ARG-Type-GroupingStatusesItem-ErrorCode"></a>
Specifies the error code that was raised.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** ErrorMessage **   <a name="ARG-Type-GroupingStatusesItem-ErrorMessage"></a>
A message that explains the `ErrorCode`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** ResourceArn **   <a name="ARG-Type-GroupingStatusesItem-ResourceArn"></a>
The Amazon resource name (ARN) of a resource.
Type: String
Pattern: `arn:aws(-[a-z]+)*:[a-z0-9\-]*:([a-z]{2}(-[a-z]+)+-\d{1})?:([0-9]{12})?:.+`
Required: No

 ** Status **   <a name="ARG-Type-GroupingStatusesItem-Status"></a>
Describes the resource grouping status with values of `SUCCESS`, `FAILED`, `IN_PROGRESS`, or `SKIPPED`.
Type: String
Valid Values: `SUCCESS | FAILED | IN_PROGRESS | SKIPPED`
Required: No

 ** UpdatedAt **   <a name="ARG-Type-GroupingStatusesItem-UpdatedAt"></a>
A timestamp of when the status was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_GroupingStatusesItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/GroupingStatusesItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/GroupingStatusesItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/GroupingStatusesItem)
