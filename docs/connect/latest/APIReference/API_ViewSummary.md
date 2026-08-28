---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ViewSummary.html
---

# ViewSummary
<a name="API_ViewSummary"></a>

A summary of a view's metadata.

## Contents
<a name="API_ViewSummary_Contents"></a>

 ** Arn **   <a name="connect-Type-ViewSummary-Arn"></a>
The Amazon Resource Name (ARN) of the view.
Type: String
Required: No

 ** Description **   <a name="connect-Type-ViewSummary-Description"></a>
The description of the view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^([\p{L}\p{N}_.:\/=+\-@,()']+[\p{L}\p{Z}\p{N}_.:\/=+\-@,()']*)$`
Required: No

 ** Id **   <a name="connect-Type-ViewSummary-Id"></a>
The identifier of the view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `^[a-zA-Z0-9\_\-:\/$]+$`
Required: No

 ** Name **   <a name="connect-Type-ViewSummary-Name"></a>
The name of the view.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^([\p{L}\p{N}_.:\/=+\-@()']+[\p{L}\p{Z}\p{N}_.:\/=+\-@()']*)$`
Required: No

 ** Status **   <a name="connect-Type-ViewSummary-Status"></a>
Indicates the view status as either `SAVED` or `PUBLISHED`. The `PUBLISHED` status will initiate validation on the content.
Type: String
Valid Values: `PUBLISHED | SAVED`
Required: No

 ** Type **   <a name="connect-Type-ViewSummary-Type"></a>
The type of the view.
Type: String
Valid Values: `CUSTOMER_MANAGED | AWS_MANAGED`
Required: No

## See Also
<a name="API_ViewSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ViewSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ViewSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ViewSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
