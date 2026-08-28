---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_TaskExecutionFoldersListedDetail.html
---

# TaskExecutionFoldersListedDetail
<a name="API_TaskExecutionFoldersListedDetail"></a>

The number of directories that DataSync finds at your locations.

**Note**
Applies only to [Enhanced mode tasks](https://docs.aws.amazon.com/datasync/latest/userguide/choosing-task-mode.html).

## Contents
<a name="API_TaskExecutionFoldersListedDetail_Contents"></a>

 ** AtDestinationForDelete **   <a name="DataSync-Type-TaskExecutionFoldersListedDetail-AtDestinationForDelete"></a>
The number of directories that DataSync finds at your destination location. This counter is only applicable if you [configure your task](https://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html#task-option-file-object-handling) to delete data in the destination that isn't in the source.
Type: Long
Required: No

 ** AtSource **   <a name="DataSync-Type-TaskExecutionFoldersListedDetail-AtSource"></a>
The number of directories that DataSync finds at your source location.
+ With a [manifest](https://docs.aws.amazon.com/datasync/latest/userguide/transferring-with-manifest.html), DataSync lists only what's in your manifest (and not everything at your source location).
+ With an include [filter](https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html), DataSync lists only what matches the filter at your source location.
+ With an exclude filter, DataSync lists everything at your source location before applying the filter.
Type: Long
Required: No

## See Also
<a name="API_TaskExecutionFoldersListedDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/TaskExecutionFoldersListedDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/TaskExecutionFoldersListedDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/TaskExecutionFoldersListedDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
