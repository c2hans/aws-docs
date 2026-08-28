---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_osis_PipelineSummary.html
---

# PipelineSummary
<a name="API_osis_PipelineSummary"></a>

Summary information for an OpenSearch Ingestion pipeline.

## Contents
<a name="API_osis_PipelineSummary_Contents"></a>

 ** CreatedAt **   <a name="opensearchservice-Type-osis_PipelineSummary-CreatedAt"></a>
The date and time when the pipeline was created.
Type: Timestamp
Required: No

 ** Destinations **   <a name="opensearchservice-Type-osis_PipelineSummary-Destinations"></a>
A list of destinations to which the pipeline writes data.
Type: Array of [PipelineDestination](API_osis_PipelineDestination.md) objects
Required: No

 ** LastUpdatedAt **   <a name="opensearchservice-Type-osis_PipelineSummary-LastUpdatedAt"></a>
The date and time when the pipeline was last updated.
Type: Timestamp
Required: No

 ** MaxUnits **   <a name="opensearchservice-Type-osis_PipelineSummary-MaxUnits"></a>
The maximum pipeline capacity, in Ingestion Compute Units (ICUs).
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** MinUnits **   <a name="opensearchservice-Type-osis_PipelineSummary-MinUnits"></a>
The minimum pipeline capacity, in Ingestion Compute Units (ICUs).
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** PipelineArn **   <a name="opensearchservice-Type-osis_PipelineSummary-PipelineArn"></a>
The Amazon Resource Name (ARN) of the pipeline.
Type: String
Length Constraints: Minimum length of 46. Maximum length of 76.
Pattern: `^arn:(aws|aws\-cn|aws\-us\-gov|aws\-iso|aws\-iso\-b):osis:.+:pipeline\/.+$`
Required: No

 ** PipelineName **   <a name="opensearchservice-Type-osis_PipelineSummary-PipelineName"></a>
The name of the pipeline.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: No

 ** Status **   <a name="opensearchservice-Type-osis_PipelineSummary-Status"></a>
The current status of the pipeline.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | CREATE_FAILED | UPDATE_FAILED | STARTING | START_FAILED | STOPPING | STOPPED`
Required: No

 ** StatusReason **   <a name="opensearchservice-Type-osis_PipelineSummary-StatusReason"></a>
Information about a pipeline's current status.
Type: [PipelineStatusReason](API_osis_PipelineStatusReason.md) object
Required: No

 ** Tags **   <a name="opensearchservice-Type-osis_PipelineSummary-Tags"></a>
A list of tags associated with the given pipeline.
Type: Array of [Tag](API_osis_Tag.md) objects
Required: No

## See Also
<a name="API_osis_PipelineSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/osis-2022-01-01/PipelineSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/osis-2022-01-01/PipelineSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/osis-2022-01-01/PipelineSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
