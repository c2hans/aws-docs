---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/automating-aws-infrastructure-documentation-generation-and-analysis/document-generation.html
---

# Document generation
<a name="document-generation"></a>

The *documentation generation* component converts scanned AWS infrastructure data into AI-powered analyses and structured documentation. It uses [Claude by Anthropic in Amazon Bedrock](https://aws.amazon.com/bedrock/anthropic/) to perform in-depth analysis, produce recommendations, and format results as Markdown.

For large datasets, the component applies an intelligent chunking strategy and synthesizes or combines chunk outputs to produce a final analysis artifact. *Intelligent chunking* is a technique to divide large infrastructure datasets into manageable subsets for analysis by generative AI services (for example, Claude on Amazon Bedrock). [Chunking](https://docs.aws.amazon.com/bedrock/latest/userguide/kb-chunking.html) helps bypass token or size limits while preserving analytical accuracy. The final documentation is displayed directly in the UI. Users can also download the complete Markdown file for offline review.

## Key responsibilities of the document generation component
<a name="key-doc-generation"></a>

This section describes the key actions and responsibilities of the document generation component.

### Analyze infrastructure data and create detailed analysis outputs
<a name="analyze-infrastructure-data-and-create-detailed-analysis-outputs.8e65fec7-7a89-5f69-ab6c-82cb67bdc0f8"></a>

The component ingests the JSON response from the resource scanning phase and determines the appropriate strategy. For smaller datasets, it runs a single-call analysis with Amazon Bedrock to generate a [Markdown](https://www.markdownguide.org/basic-syntax/) report. For larger datasets, it uses intelligent chunking, analyzing subsets individually and then combining results into a unified document.

The system uses the [generate\_infrastructure\_report](https://github.com/awslabs/InfraDocGen/blob/dc1ea8a4ebdba821f6954a2b03c4fecbec809c10/services/bedrock_service.py#L39) function, which intelligently determines whether the infrastructure data requires a single-call analysis or chunked processing based on its size.

### Produce AI-powered documentation with actionable recommendations
<a name="produce-ai-powered-documentation-with-actionable-recommendations.e2623dfb-9297-535f-a28d-3f05adc5eb41"></a>

The system generates Markdown documentation that includes findings, severity levels, and optimization or remediation recommendations. Users can choose from four analysis types—comprehensive, security, cost, or performance. Users can also provide a custom prompt to tailor the analysis to their specific needs (for example, compliance checks or compute security posture).

The [create\_single\_analysis\_prompt](https://github.com/awslabs/InfraDocGen/blob/dc1ea8a4ebdba821f6954a2b03c4fecbec809c10/services/bedrock_service.py#L1590C10-L1590C39) function highlights how the system tailors the user preference and creates the necessary prompt for generating a custom Markdown report.

### Handle large-scale inputs using chunking and combination/synthesis
<a name="handle-large-scale-inputs-using-chunking-and-combination-synthesis.c98e0cf0-d1f7-5120-bf8a-cb0a0c8a9532"></a>

When infrastructure data exceeds token limits, the dataset is divided into intelligent chunks. Each chunk is processed with Amazon Bedrock. Then, it's either combined directly or synthesized through an additional Amazon Bedrock call to produce a cohesive final report. Partial results and metadata are preserved for traceability.

The [InfrastructureChunker](https://github.com/awslabs/InfraDocGen/blob/dc1ea8a4ebdba821f6954a2b03c4fecbec809c10/services/chunking_utils.py#L15) class is responsible for intelligently splitting large infrastructure data into manageable chunks based on AWS services. This approach helps to make sure that token limits for Amazon Bedrock processing are not exceeded.

### Retry, backoff, and error handling
<a name="retry--backoff--and-error-handling.adef8dfc-7193-5502-b257-4177c5a0aba4"></a>

To ensure reliability, the component implements retries with exponential backoff when Amazon Bedrock throttling or API errors occur. Failed chunks are logged, and the final report contains an "Analysis Limitations" section if any subset could not be processed.

The [call\_claude\_with\_retry](https://github.com/awslabs/InfraDocGen/blob/dc1ea8a4ebdba821f6954a2b03c4fecbec809c10/services/bedrock_service.py#L263) function implements robust retry logic with exponential backoff. If the API call encounters a rate-limiting issue (such as throttling), it retries up to a maximum number of attempts with progressively increasing delays. Non-rate-limit errors are handled separately, with immediate failure and logging.

### UI integration and delivery
<a name="ui-integration-and-delivery.73c5b9d9-ebff-5cd7-a48e-5b84d4854dac"></a>

The generated Markdown report is rendered in the UI for interactive viewing. Users can also download the Markdown file directly for offline use or integration into documentation systems.

## Workflow of the document generation component
<a name="workflow-doc-generation"></a>

The document generation component uses the following workflow:

1. **Request documentation generation** – The client requests documentation by providing the normalized scan JSON. The request may include a selected analysis type (comprehensive, security, cost, or performance) and an optional custom prompt to refine scope.

1. **Estimate data size and decide strategy** – The system estimates token usage to decide between a single comprehensive Amazon Bedrock call or splitting the dataset into multiple intelligent chunks for parallel analysis.

1. **Create prompts** – For single-call cases, the system builds a detailed expert prompt that requests findings, risks, and recommendations. For chunked cases, chunk-specific prompts are created, each embedding contextual instructions and the selected analysis type or custom prompt.

1. **Call Amazon Bedrock **– The prompts are sent to the Amazon Bedrock runtime. For chunked analysis, each chunk is processed sequentially with conservative backoff and retry logic to avoid hitting rate limits.

1. **Combine or synthesize chunk outputs** – If chunking was used, the component either combines chunk outputs into a single Markdown document or synthesizes them into a cohesive analysis with a final Amazon Bedrock call. If some chunks failed, their status is recorded and an "Analysis Limitations" note is added.

1. **Add metadata and return result** – The final output is packaged with metadata (for example, model used, chunking strategy, timings, and error details) and delivered back to the client. In the UI, the Markdown is displayed interactively, and the download option is provided for exporting the report.

## User view of document generation
<a name="ui-view-doc-generation"></a>

The AI-generated Markdown analysis report is shown directly in the UI with a structured, readable format. Users can preview findings, risks, and recommendations in the browser and download the full Markdown file for offline reference.
