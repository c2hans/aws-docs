---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ViewVersionSummary.html
---

# ViewVersionSummary
<a name="API_ViewVersionSummary"></a>

A summary of a view version's metadata.

## Contents
<a name="API_ViewVersionSummary_Contents"></a>

 ** Arn **   <a name="connect-Type-ViewVersionSummary-Arn"></a>
The Amazon Resource Name (ARN) of the view version.
Type: String
Required: No

 ** Description **   <a name="connect-Type-ViewVersionSummary-Description"></a>
The description of the view version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^([\p{L}\p{N}_.:\/=+\-@,()']+[\p{L}\p{Z}\p{N}_.:\/=+\-@,()']*)$`
Required: No

 ** Id **   <a name="connect-Type-ViewVersionSummary-Id"></a>
The identifier of the view version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Pattern: `^[a-zA-Z0-9\_\-:\/$]+$`
Required: No

 ** Name **   <a name="connect-Type-ViewVersionSummary-Name"></a>
The name of the view version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^([\p{L}\p{N}_.:\/=+\-@()']+[\p{L}\p{Z}\p{N}_.:\/=+\-@()']*)$`
Required: No

 ** Type **   <a name="connect-Type-ViewVersionSummary-Type"></a>
The type of the view version.
Type: String
Valid Values: `CUSTOMER_MANAGED | AWS_MANAGED`
Required: No

 ** Version **   <a name="connect-Type-ViewVersionSummary-Version"></a>
The sequentially incremented version of the view version.
Type: Integer
Required: No

 ** VersionDescription **   <a name="connect-Type-ViewVersionSummary-VersionDescription"></a>
The description of the view version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Pattern: `^([\p{L}\p{N}_.:\/=+\-@,()']+[\p{L}\p{Z}\p{N}_.:\/=+\-@,()']*)$`
Required: No

## See Also
<a name="API_ViewVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ViewVersionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ViewVersionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ViewVersionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
