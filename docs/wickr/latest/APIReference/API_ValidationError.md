---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_ValidationError.html
---

# ValidationError
<a name="API_ValidationError"></a>

One or more fields in the request failed validation. This error provides detailed information about which fields were invalid and why, allowing you to correct the request and retry.

HTTP Status Code returned: 422

## Contents
<a name="API_ValidationError_Contents"></a>

 ** message **   <a name="wickr-Type-ValidationError-message"></a>
A message describing the validation error error that occurred.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** reasons **   <a name="wickr-Type-ValidationError-reasons"></a>
A list of validation error details, where each item identifies a specific field that failed validation and explains the reason for the failure.
Type: Array of [ErrorDetail](API_ErrorDetail.md) objects
Required: No

## See Also
<a name="API_ValidationError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/ValidationError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
