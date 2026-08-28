---
source_url: https://docs.aws.amazon.com/datasync/latest/apireference/API_ReportOverride.html
---

# ReportOverride
<a name="API_ReportOverride"></a>

Specifies the level of detail for a particular aspect of your DataSync [task report](https://docs.aws.amazon.com/datasync/latest/userguide/task-reports.html).

## Contents
<a name="API_ReportOverride_Contents"></a>

 ** ReportLevel **   <a name="DataSync-Type-ReportOverride-ReportLevel"></a>
Specifies whether your task report includes errors only or successes and errors.
For example, your report might mostly include only what didn't go well in your transfer (`ERRORS_ONLY`). At the same time, you want to verify that your [task filter](https://docs.aws.amazon.com/datasync/latest/userguide/filtering.html) is working correctly. In this situation, you can get a list of what files DataSync successfully skipped and if something transferred that you didn't to transfer (`SUCCESSES_AND_ERRORS`).
Type: String
Valid Values: `ERRORS_ONLY | SUCCESSES_AND_ERRORS`
Required: No

## See Also
<a name="API_ReportOverride_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datasync-2018-11-09/ReportOverride)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datasync-2018-11-09/ReportOverride)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datasync-2018-11-09/ReportOverride)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for DataSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datasync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
