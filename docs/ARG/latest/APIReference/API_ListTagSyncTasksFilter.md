---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_ListTagSyncTasksFilter.html
---

# ListTagSyncTasksFilter
<a name="API_ListTagSyncTasksFilter"></a>

Returns tag-sync tasks filtered by the Amazon resource name (ARN) or name of a specified application group.

## Contents
<a name="API_ListTagSyncTasksFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** GroupArn **   <a name="ARG-Type-ListTagSyncTasksFilter-GroupArn"></a>
The Amazon resource name (ARN) of the application group.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+)*:resource-groups:[a-z]{2}(-[a-z]+)+-\d{1}:[0-9]{12}:group/([a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26})`
Required: No

 ** GroupName **   <a name="ARG-Type-ListTagSyncTasksFilter-GroupName"></a>
The name of the application group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `[a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26}`
Required: No

## See Also
<a name="API_ListTagSyncTasksFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/ListTagSyncTasksFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/ListTagSyncTasksFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/ListTagSyncTasksFilter)
