---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DryRunResults.html
---

# DryRunResults
<a name="API_DryRunResults"></a>

Results of a dry run performed in an update domain request.

## Contents
<a name="API_DryRunResults_Contents"></a>

 ** DeploymentType **   <a name="opensearchservice-Type-DryRunResults-DeploymentType"></a>
 Specifies the way in which OpenSearch Service will apply an update. Possible values are:
+  **Blue/Green** - The update requires a blue/green deployment.
+  **DynamicUpdate** - No blue/green deployment required
+  **Undetermined** - The domain is in the middle of an update and can't predict the deployment type. Try again after the update is complete.
+  **None** - The request doesn't include any configuration changes.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 128.
Required: No

 ** Message **   <a name="opensearchservice-Type-DryRunResults-Message"></a>
A message corresponding to the deployment type.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_DryRunResults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DryRunResults)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DryRunResults)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DryRunResults)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
