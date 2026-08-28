---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_CreateAssessmentFrameworkControlSet.html
---

# CreateAssessmentFrameworkControlSet
<a name="API_CreateAssessmentFrameworkControlSet"></a>

 A `controlSet` entity that represents a collection of controls in AWS Audit Manager. This doesn't contain the control set ID.

## Contents
<a name="API_CreateAssessmentFrameworkControlSet_Contents"></a>

 ** name **   <a name="auditmanager-Type-CreateAssessmentFrameworkControlSet-name"></a>
 The name of the control set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Pattern: `^[^\\\_]*$`
Required: Yes

 ** controls **   <a name="auditmanager-Type-CreateAssessmentFrameworkControlSet-controls"></a>
 The list of controls within the control set. This doesn't contain the control set ID.
Type: Array of [CreateAssessmentFrameworkControl](API_CreateAssessmentFrameworkControl.md) objects
Array Members: Minimum number of 1 item.
Required: No

## See Also
<a name="API_CreateAssessmentFrameworkControlSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/CreateAssessmentFrameworkControlSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/CreateAssessmentFrameworkControlSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/CreateAssessmentFrameworkControlSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
