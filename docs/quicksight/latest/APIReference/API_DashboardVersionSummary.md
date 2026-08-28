---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DashboardVersionSummary.html
---

# DashboardVersionSummary
<a name="API_DashboardVersionSummary"></a>

Dashboard version summary.

## Contents
<a name="API_DashboardVersionSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-DashboardVersionSummary-Arn"></a>
The Amazon Resource Name (ARN) of the resource.
Type: String
Required: No

 ** CreatedTime **   <a name="QS-Type-DashboardVersionSummary-CreatedTime"></a>
The time that this dashboard version was created.
Type: Timestamp
Required: No

 ** Description **   <a name="QS-Type-DashboardVersionSummary-Description"></a>
Description.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** SourceEntityArn **   <a name="QS-Type-DashboardVersionSummary-SourceEntityArn"></a>
Source entity ARN.
Type: String
Required: No

 ** Status **   <a name="QS-Type-DashboardVersionSummary-Status"></a>
The HTTP status of the request.
Type: String
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETED`
Required: No

 ** VersionNumber **   <a name="QS-Type-DashboardVersionSummary-VersionNumber"></a>
Version number.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_DashboardVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DashboardVersionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DashboardVersionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DashboardVersionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
