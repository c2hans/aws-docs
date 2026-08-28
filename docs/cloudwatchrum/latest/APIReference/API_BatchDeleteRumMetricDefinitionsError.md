---
source_url: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchDeleteRumMetricDefinitionsError.html
---

# BatchDeleteRumMetricDefinitionsError
<a name="API_BatchDeleteRumMetricDefinitionsError"></a>

A structure that defines one error caused by a [BatchCreateRumMetricsDefinitions](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchDeleteRumMetricsDefinitions.html) operation.

## Contents
<a name="API_BatchDeleteRumMetricDefinitionsError_Contents"></a>

 ** ErrorCode **   <a name="cloudwatchrum-Type-BatchDeleteRumMetricDefinitionsError-ErrorCode"></a>
The error code.
Type: String
Required: Yes

 ** ErrorMessage **   <a name="cloudwatchrum-Type-BatchDeleteRumMetricDefinitionsError-ErrorMessage"></a>
The error message for this metric definition.
Type: String
Required: Yes

 ** MetricDefinitionId **   <a name="cloudwatchrum-Type-BatchDeleteRumMetricDefinitionsError-MetricDefinitionId"></a>
The ID of the metric definition that caused this error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## See Also
<a name="API_BatchDeleteRumMetricDefinitionsError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rum-2018-05-10/BatchDeleteRumMetricDefinitionsError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rum-2018-05-10/BatchDeleteRumMetricDefinitionsError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rum-2018-05-10/BatchDeleteRumMetricDefinitionsError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CloudWatch RUM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatchrum` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
