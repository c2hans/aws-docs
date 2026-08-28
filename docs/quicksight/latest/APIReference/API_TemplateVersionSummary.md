---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_TemplateVersionSummary.html
---

# TemplateVersionSummary
<a name="API_TemplateVersionSummary"></a>

The template version.

## Contents
<a name="API_TemplateVersionSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-TemplateVersionSummary-Arn"></a>
The Amazon Resource Name (ARN) of the template version.
Type: String
Required: No

 ** CreatedTime **   <a name="QS-Type-TemplateVersionSummary-CreatedTime"></a>
The time that this template version was created.
Type: Timestamp
Required: No

 ** Description **   <a name="QS-Type-TemplateVersionSummary-Description"></a>
The description of the template version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

 ** Status **   <a name="QS-Type-TemplateVersionSummary-Status"></a>
The status of the template version.
Type: String
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETED`
Required: No

 ** VersionNumber **   <a name="QS-Type-TemplateVersionSummary-VersionNumber"></a>
The version number of the template version.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_TemplateVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/TemplateVersionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/TemplateVersionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/TemplateVersionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
