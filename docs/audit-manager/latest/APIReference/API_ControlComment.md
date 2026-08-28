---
source_url: https://docs.aws.amazon.com/audit-manager/latest/APIReference/API_ControlComment.html
---

# ControlComment
<a name="API_ControlComment"></a>

 A comment that's posted by a user on a control. This includes the author's name, the comment text, and a timestamp.

## Contents
<a name="API_ControlComment_Contents"></a>

 ** authorName **   <a name="auditmanager-Type-ControlComment-authorName"></a>
 The name of the user who authored the comment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-_()\s\+=,.@]+$`
Required: No

 ** commentBody **   <a name="auditmanager-Type-ControlComment-commentBody"></a>
 The body text of a control comment.
Type: String
Length Constraints: Maximum length of 500.
Pattern: `^[\w\W\s\S]*$`
Required: No

 ** postedDate **   <a name="auditmanager-Type-ControlComment-postedDate"></a>
 The time when the comment was posted.
Type: Timestamp
Required: No

## See Also
<a name="API_ControlComment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/auditmanager-2017-07-25/ControlComment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/auditmanager-2017-07-25/ControlComment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/auditmanager-2017-07-25/ControlComment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Audit Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query audit-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
