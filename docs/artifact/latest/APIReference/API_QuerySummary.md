---
source_url: https://docs.aws.amazon.com/artifact/latest/APIReference/API_QuerySummary.html
---

# QuerySummary
<a name="API_QuerySummary"></a>

Summary information about a single query within a compliance inquiry.

## Contents
<a name="API_QuerySummary_Contents"></a>

 ** createdAt **   <a name="artifact-Type-QuerySummary-createdAt"></a>
Timestamp indicating when the query was created.
Type: Timestamp
Required: Yes

 ** query **   <a name="artifact-Type-QuerySummary-query"></a>
The actual query text.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^<>]*`
Required: Yes

 ** queryIdentifier **   <a name="artifact-Type-QuerySummary-queryIdentifier"></a>
Sequential identifier of the query within the inquiry.
Type: Integer
Required: Yes

 ** status **   <a name="artifact-Type-QuerySummary-status"></a>
Current processing status of the query.
Type: String
Valid Values: `PROCESSING | COMPLETED | FAILED`
Required: Yes

 ** statusMessage **   <a name="artifact-Type-QuerySummary-statusMessage"></a>
Descriptive status message.
Type: String
Valid Values: `Query processing is complete. | Query processing is in-progress. | An internal error occurred while processing the query. Try again at a later time. | Query is pending human review. | Query contains restricted or unsupported content.`
Required: Yes

 ** citations **   <a name="artifact-Type-QuerySummary-citations"></a>
Supporting citations for the response.
Type: Array of [Citation](API_Citation.md) objects
Required: No

 ** response **   <a name="artifact-Type-QuerySummary-response"></a>
Generated response to the query.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^<>]*`
Required: No

 ** reviewType **   <a name="artifact-Type-QuerySummary-reviewType"></a>
Type of review for the response.
Type: String
Valid Values: `HUMAN | AI`
Required: No

 ** updatedResponseVersions **   <a name="artifact-Type-QuerySummary-updatedResponseVersions"></a>
Ordered list of response version history entries, oldest first.
Type: Array of [ResponseVersion](API_ResponseVersion.md) objects
Required: No

## See Also
<a name="API_QuerySummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/artifact-2018-05-10/QuerySummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/artifact-2018-05-10/QuerySummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/artifact-2018-05-10/QuerySummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Artifact. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query artifact` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
