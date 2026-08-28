---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_BrandSummary.html
---

# BrandSummary
<a name="API_BrandSummary"></a>

A summary of the brand.

## Contents
<a name="API_BrandSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-BrandSummary-Arn"></a>
The Amazon Resource Name (ARN) of the brand.
Type: String
Required: No

 ** BrandId **   <a name="QS-Type-BrandSummary-BrandId"></a>
The ID of the Quick brand.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: No

 ** BrandName **   <a name="QS-Type-BrandSummary-BrandName"></a>
The name of the brand.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[ -ÿ]+`
Required: No

 ** BrandStatus **   <a name="QS-Type-BrandSummary-BrandStatus"></a>
The status of the brand.
Type: String
Valid Values: `CREATE_IN_PROGRESS | CREATE_SUCCEEDED | CREATE_FAILED | DELETE_IN_PROGRESS | DELETE_FAILED`
Required: No

 ** CreatedTime **   <a name="QS-Type-BrandSummary-CreatedTime"></a>
The time that the brand was created.
Type: Timestamp
Required: No

 ** Description **   <a name="QS-Type-BrandSummary-Description"></a>
The description of the brand.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[ -ÿ]+`
Required: No

 ** LastUpdatedTime **   <a name="QS-Type-BrandSummary-LastUpdatedTime"></a>
The time when the brand was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_BrandSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/BrandSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/BrandSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/BrandSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
