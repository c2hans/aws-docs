---
source_url: https://docs.aws.amazon.com/appfabric/latest/api/API_IngestionSummary.html
---

# IngestionSummary
<a name="API_IngestionSummary"></a>

Contains a summary of an ingestion.

## Contents
<a name="API_IngestionSummary_Contents"></a>

 ** app **   <a name="appfabric-Type-IngestionSummary-app"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** arn **   <a name="appfabric-Type-IngestionSummary-arn"></a>
The Amazon Resource Name (ARN) of the ingestion.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:.+`
Required: Yes

 ** state **   <a name="appfabric-Type-IngestionSummary-state"></a>
The status of the ingestion.
Type: String
Valid Values: `enabled | disabled`
Required: Yes

 ** tenantId **   <a name="appfabric-Type-IngestionSummary-tenantId"></a>
The ID of the application tenant.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: Yes

## See Also
<a name="API_IngestionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appfabric-2023-05-19/IngestionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appfabric-2023-05-19/IngestionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appfabric-2023-05-19/IngestionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppFabric. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appfabric` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
