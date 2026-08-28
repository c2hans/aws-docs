---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ProjectsForRule.html
---

# ProjectsForRule
<a name="API_ProjectsForRule"></a>

Specifies projects in which the rule is created.

## Contents
<a name="API_ProjectsForRule_Contents"></a>

 ** selectionMode **   <a name="datazone-Type-ProjectsForRule-selectionMode"></a>
The selection mode of the rule.
Type: String
Valid Values: `ALL | SPECIFIC`
Required: Yes

 ** specificProjects **   <a name="datazone-Type-ProjectsForRule-specificProjects"></a>
The specific projects in which the rule is created.
Type: Array of strings
Array Members: Minimum number of 1 item.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: No

## See Also
<a name="API_ProjectsForRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ProjectsForRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ProjectsForRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ProjectsForRule)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
