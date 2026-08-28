---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_DocumentReviewerResponseSource.html
---

# DocumentReviewerResponseSource
<a name="API_DocumentReviewerResponseSource"></a>

Information about a reviewer's response to a document review request.

## Contents
<a name="API_DocumentReviewerResponseSource_Contents"></a>

 ** Comment **   <a name="systemsmanager-Type-DocumentReviewerResponseSource-Comment"></a>
The comment entered by a reviewer as part of their document review response.
Type: Array of [DocumentReviewCommentSource](API_DocumentReviewCommentSource.md) objects
Array Members: Minimum number of 0 items. Maximum number of 1 item.
Required: No

 ** CreateTime **   <a name="systemsmanager-Type-DocumentReviewerResponseSource-CreateTime"></a>
The date and time that a reviewer entered a response to a document review request.
Type: Timestamp
Required: No

 ** Reviewer **   <a name="systemsmanager-Type-DocumentReviewerResponseSource-Reviewer"></a>
The user in your organization assigned to review a document request.
Type: String
Length Constraints: Maximum length of 50.
Pattern: `^[a-zA-Z0-9_\-.]{1,128}$`
Required: No

 ** ReviewStatus **   <a name="systemsmanager-Type-DocumentReviewerResponseSource-ReviewStatus"></a>
The current review status of a new custom SSM document created by a member of your organization, or of the latest version of an existing SSM document.
Only one version of a document can be in the APPROVED state at a time. When a new version is approved, the status of the previous version changes to REJECTED.
Only one version of a document can be in review, or PENDING, at a time.
Type: String
Valid Values: `APPROVED | NOT_REVIEWED | PENDING | REJECTED`
Required: No

 ** UpdatedTime **   <a name="systemsmanager-Type-DocumentReviewerResponseSource-UpdatedTime"></a>
The date and time that a reviewer last updated a response to a document review request.
Type: Timestamp
Required: No

## See Also
<a name="API_DocumentReviewerResponseSource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/DocumentReviewerResponseSource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/DocumentReviewerResponseSource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/DocumentReviewerResponseSource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
