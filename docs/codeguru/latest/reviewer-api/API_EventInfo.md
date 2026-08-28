---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_EventInfo.html
---

# EventInfo
<a name="API_EventInfo"></a>

Information about an event. The event might be a push, pull request, scheduled request, or another type of event.

## Contents
<a name="API_EventInfo_Contents"></a>

 ** Name **   <a name="reviewer-Type-EventInfo-Name"></a>
The name of the event. The possible names are `pull_request`, `workflow_dispatch`, `schedule`, and `push`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^[ \-A-Z_a-z]+$`
Required: No

 ** State **   <a name="reviewer-Type-EventInfo-State"></a>
The state of an event. The state might be open, closed, or another state.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^[ \-A-Z_a-z]+$`
Required: No

## See Also
<a name="API_EventInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codeguru-reviewer-2019-09-19/EventInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codeguru-reviewer-2019-09-19/EventInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codeguru-reviewer-2019-09-19/EventInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru Reviewer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
