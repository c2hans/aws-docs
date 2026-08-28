---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AppConfig.html
---

# AppConfig
<a name="API_AppConfig"></a>

Configuration settings for an OpenSearch application. For more information, see [Using the OpenSearch user interface in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/application.html).

## Contents
<a name="API_AppConfig_Contents"></a>

 ** key **   <a name="opensearchservice-Type-AppConfig-key"></a>
The configuration item to set, such as the admin role for the OpenSearch application.
Type: String
Valid Values: `opensearchDashboards.dashboardAdmin.users | opensearchDashboards.dashboardAdmin.groups`
Required: No

 ** value **   <a name="opensearchservice-Type-AppConfig-value"></a>
The value assigned to the configuration key, such as an IAM user ARN.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

## See Also
<a name="API_AppConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/AppConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/AppConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/AppConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
