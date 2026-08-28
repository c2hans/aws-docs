---
source_url: https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchCreateRumMetricDefinitionsError.html
---

# BatchCreateRumMetricDefinitionsError
<a name="API_BatchCreateRumMetricDefinitionsError"></a>

A structure that defines one error caused by a [BatchCreateRumMetricsDefinitions](https://docs.aws.amazon.com/cloudwatchrum/latest/APIReference/API_BatchCreateRumMetricsDefinitions.html) operation.

## Contents
<a name="API_BatchCreateRumMetricDefinitionsError_Contents"></a>

 ** ErrorCode **   <a name="cloudwatchrum-Type-BatchCreateRumMetricDefinitionsError-ErrorCode"></a>
The error code.
Type: String
Required: Yes

 ** ErrorMessage **   <a name="cloudwatchrum-Type-BatchCreateRumMetricDefinitionsError-ErrorMessage"></a>
The error message for this metric definition.
Type: String
Required: Yes

 ** MetricDefinition **   <a name="cloudwatchrum-Type-BatchCreateRumMetricDefinitionsError-MetricDefinition"></a>
The metric definition that caused this error.
Type: [MetricDefinitionRequest](API_MetricDefinitionRequest.md) object
Required: Yes

## See Also
<a name="API_BatchCreateRumMetricDefinitionsError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rum-2018-05-10/BatchCreateRumMetricDefinitionsError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rum-2018-05-10/BatchCreateRumMetricDefinitionsError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rum-2018-05-10/BatchCreateRumMetricDefinitionsError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for CloudWatch RUM. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudwatchrum` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
