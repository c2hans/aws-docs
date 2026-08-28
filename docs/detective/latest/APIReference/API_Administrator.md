---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_Administrator.html
---

# Administrator
<a name="API_Administrator"></a>

Information about the Detective administrator account for an organization.

## Contents
<a name="API_Administrator_Contents"></a>

 ** AccountId **   <a name="detective-Type-Administrator-AccountId"></a>
The AWS account identifier of the Detective administrator account for the organization.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]+$`
Required: No

 ** DelegationTime **   <a name="detective-Type-Administrator-DelegationTime"></a>
The date and time when the Detective administrator account was enabled. The value is an ISO8601 formatted string. For example, `2021-08-18T16:35:56.284Z`.
Type: Timestamp
Required: No

 ** GraphArn **   <a name="detective-Type-Administrator-GraphArn"></a>
The ARN of the organization behavior graph.
Type: String
Pattern: `^arn:aws[-\w]{0,10}?:detective:[-\w]{2,20}?:\d{12}?:graph:[abcdef\d]{32}?$`
Required: No

## See Also
<a name="API_Administrator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/Administrator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/Administrator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/Administrator)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Detective. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query detective` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
