---
source_url: https://docs.aws.amazon.com/ARG/latest/APIReference/API_TagSyncTaskItem.html
---

# TagSyncTaskItem
<a name="API_TagSyncTaskItem"></a>

The Amazon resource name (ARN) of the tag-sync task.

## Contents
<a name="API_TagSyncTaskItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CreatedAt **   <a name="ARG-Type-TagSyncTaskItem-CreatedAt"></a>
The timestamp of when the tag-sync task was created.
Type: Timestamp
Required: No

 ** ErrorMessage **   <a name="ARG-Type-TagSyncTaskItem-ErrorMessage"></a>
The specific error message in cases where the tag-sync task status is `Error`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** GroupArn **   <a name="ARG-Type-TagSyncTaskItem-GroupArn"></a>
The Amazon resource name (ARN) of the application group.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+)*:resource-groups:[a-z]{2}(-[a-z]+)+-\d{1}:[0-9]{12}:group/([a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26})`
Required: No

 ** GroupName **   <a name="ARG-Type-TagSyncTaskItem-GroupName"></a>
The name of the application group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `[a-zA-Z0-9_\.-]{1,300}|[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26}`
Required: No

 ** ResourceQuery **   <a name="ARG-Type-TagSyncTaskItem-ResourceQuery"></a>
The query you can use to define a resource group or a search for resources. A `ResourceQuery` specifies both a query `Type` and a `Query` string as JSON string objects. See the examples section for example JSON strings. For more information about creating a resource group with a resource query, see [Build queries and groups in AWS Resource Groups](https://docs.aws.amazon.com/ARG/latest/userguide/gettingstarted-query.html) in the * AWS Resource Groups User Guide*
When you combine all of the elements together into a single string, any double quotes that are embedded inside another double quote pair must be escaped by preceding the embedded double quote with a backslash character (\\). For example, a complete `ResourceQuery` parameter must be formatted like the following CLI parameter example:
 `--resource-query '{"Type":"TAG_FILTERS_1_0","Query":"{\"ResourceTypeFilters\":[\"AWS::AllSupported\"],\"TagFilters\":[{\"Key\":\"Stage\",\"Values\":[\"Test\"]}]}"}'`
In the preceding example, all of the double quote characters in the value part of the `Query` element must be escaped because the value itself is surrounded by double quotes. For more information, see [Quoting strings](https://docs.aws.amazon.com/cli/latest/userguide/cli-usage-parameters-quoting-strings.html) in the * AWS Command Line Interface User Guide*.
For the complete list of resource types that you can use in the array value for `ResourceTypeFilters`, see [Resources you can use with AWS Resource Groups and Tag Editor](https://docs.aws.amazon.com/ARG/latest/userguide/supported-resources.html) in the * AWS Resource Groups User Guide*. For example:
 `"ResourceTypeFilters":["AWS::S3::Bucket", "AWS::EC2::Instance"]`
Type: [ResourceQuery](API_ResourceQuery.md) object
Required: No

 ** RoleArn **   <a name="ARG-Type-TagSyncTaskItem-RoleArn"></a>
The Amazon resource name (ARN) of the role assumed by the service to tag and untag resources on your behalf.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:iam::\d{12}:role/?[a-zA-Z_0-9+=,.@\-_/]+`
Required: No

 ** Status **   <a name="ARG-Type-TagSyncTaskItem-Status"></a>
The status of the tag-sync task.
Valid values include:
+  `ACTIVE` - The tag-sync task is actively managing resources in the application by adding or removing the `awsApplication` tag from resources when they are tagged or untagged with the specified tag key-value pair.
+  `ERROR` - The tag-sync task is not actively managing resources in the application. Review the `ErrorMessage` for more information about resolving the error.
Type: String
Valid Values: `ACTIVE | ERROR`
Required: No

 ** TagKey **   <a name="ARG-Type-TagSyncTaskItem-TagKey"></a>
The tag key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** TagValue **   <a name="ARG-Type-TagSyncTaskItem-TagValue"></a>
The tag value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** TaskArn **   <a name="ARG-Type-TagSyncTaskItem-TaskArn"></a>
The Amazon resource name (ARN) of the tag-sync task.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 1600.
Pattern: `arn:aws(-[a-z]+)*:resource-groups:[a-z]{2}(-[a-z]+)+-\d{1}:[0-9]{12}:group/[a-zA-Z0-9_\.-]{1,150}/[a-z0-9]{26}/tag-sync-task/[a-z0-9]{26}`
Required: No

## See Also
<a name="API_TagSyncTaskItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-groups-2017-11-27/TagSyncTaskItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-groups-2017-11-27/TagSyncTaskItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-groups-2017-11-27/TagSyncTaskItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Resource Groups & Tagging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ARG` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
