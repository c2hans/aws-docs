---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_MeteredProductSummary.html
---

# MeteredProductSummary
<a name="API_MeteredProductSummary"></a>

The details of a metered product.

## Contents
<a name="API_MeteredProductSummary_Contents"></a>

 ** family **   <a name="deadlinecloud-Type-MeteredProductSummary-family"></a>
The family to which the metered product belongs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** port **   <a name="deadlinecloud-Type-MeteredProductSummary-port"></a>
The port on which the metered product should run.
Type: Integer
Valid Range: Minimum value of 1024. Maximum value of 65535.
Required: Yes

 ** productId **   <a name="deadlinecloud-Type-MeteredProductSummary-productId"></a>
The product ID.
Type: String
Pattern: `[0-9a-z]{1,32}-[.0-9a-z]{1,32}`
Required: Yes

 ** vendor **   <a name="deadlinecloud-Type-MeteredProductSummary-vendor"></a>
The vendor.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## See Also
<a name="API_MeteredProductSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/MeteredProductSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/MeteredProductSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/MeteredProductSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
