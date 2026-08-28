---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_ReportOverrides.html
---

# ReportOverrides
<a name="API_ReportOverrides"></a>

The level of detail included in each aspect of your DataSync [task report](https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html).

## Contents
<a name="API_ReportOverrides_Contents"></a>

 ** Deleted **   <a name="DataSync-Type-ReportOverrides-Deleted"></a>
Specifies the level of reporting for the files, objects, and directories that DataSync attempted to delete in your destination location. This only applies if you [configure your task](https://docs.aws.amazon.com/datasync/latest/userguide/configure-metadata.html) to delete data in the destination that isn't in the source.
Type: [ReportOverride](API_ReportOverride.md) object
Required: No

 ** Skipped **   <a name="DataSync-Type-ReportOverrides-Skipped"></a>
Specifies the level of reporting for the files, objects, and directories that DataSync attempted to skip during your transfer.
Type: [ReportOverride](API_ReportOverride.md) object
Required: No

 ** Transferred **   <a name="DataSync-Type-ReportOverrides-Transferred"></a>
Specifies the level of reporting for the files, objects, and directories that DataSync attempted to transfer.
Type: [ReportOverride](API_ReportOverride.md) object
Required: No

 ** Verified **   <a name="DataSync-Type-ReportOverrides-Verified"></a>
Specifies the level of reporting for the files, objects, and directories that DataSync attempted to verify at the end of your transfer.
Type: [ReportOverride](API_ReportOverride.md) object
Required: No

## See Also
<a name="API_ReportOverrides_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/ReportOverrides)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/ReportOverrides)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/ReportOverrides)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
