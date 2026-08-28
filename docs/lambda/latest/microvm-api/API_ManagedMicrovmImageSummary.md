---
source_url: https://docs.aws.amazon.com/lambda/latest/microvm-api/API_ManagedMicrovmImageSummary.html
---

# ManagedMicrovmImageSummary
<a name="API_ManagedMicrovmImageSummary"></a>

Contains summary information about a managed MicroVM image.

## Contents
<a name="API_ManagedMicrovmImageSummary_Contents"></a>

 ** createdAt **   <a name="lambdamicrovm-Type-ManagedMicrovmImageSummary-createdAt"></a>
The timestamp when the managed MicroVM image was created.
Type: Timestamp
Required: Yes

 ** imageArn **   <a name="lambdamicrovm-Type-ManagedMicrovmImageSummary-imageArn"></a>
The ARN of the managed MicroVM image.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\s]+`
Required: Yes

 ** updatedAt **   <a name="lambdamicrovm-Type-ManagedMicrovmImageSummary-updatedAt"></a>
The timestamp when the managed MicroVM image was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_ManagedMicrovmImageSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-microvms-2025-09-09/ManagedMicrovmImageSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-microvms-2025-09-09/ManagedMicrovmImageSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-microvms-2025-09-09/ManagedMicrovmImageSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda MicroVMs. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
