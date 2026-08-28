---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ConfigParameter.html
---

# ConfigParameter
<a name="API_ConfigParameter"></a>

An array of key-value pairs to set for advanced control over Amazon Redshift Serverless.

## Contents
<a name="API_ConfigParameter_Contents"></a>

 ** parameterKey **   <a name="redshiftserverless-Type-ConfigParameter-parameterKey"></a>
The key of the parameter. The options are `auto_mv`, `datestyle`, `enable_case_sensitive_identifier`, `enable_user_activity_logging`, `query_group`, `search_path`, `require_ssl`, `use_fips_ssl`, and either `wlm_json_configuration` or query monitoring metrics that let you define performance boundaries. You can either specify individual query monitoring metrics (such as `max_scan_row_count`, `max_query_execution_time`) or use `wlm_json_configuration` to define query queues with rules, but not both. If you're using `wlm_json_configuration`, the maximum size of `parameterValue` is 8000 characters. For more information about query monitoring rules and available metrics, see [Query monitoring metrics for Amazon Redshift Serverless](https://docs.aws.amazon.com/redshift/latest/dg/cm-c-wlm-query-monitoring-rules.html#cm-c-wlm-query-monitoring-metrics-serverless).
Type: String
Required: No

 ** parameterValue **   <a name="redshiftserverless-Type-ConfigParameter-parameterValue"></a>
The value of the parameter to set.
Type: String
Required: No

## See Also
<a name="API_ConfigParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/ConfigParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/ConfigParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/ConfigParameter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Redshift Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query redshift-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
