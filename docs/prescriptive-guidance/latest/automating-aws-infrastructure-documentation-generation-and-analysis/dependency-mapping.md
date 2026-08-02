---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/automating-aws-infrastructure-documentation-generation-and-analysis/dependency-mapping.html
---

# Dependency mapping
<a name="dependency-mapping"></a>

The *dependency mapping* component analyzes relationships between AWS resources and builds a comprehensive graph of how AWS services interact with each other. Unlike the scanning phase (which only inventories resources) and the documentation phase (which explains configurations and best practices), dependency mapping focuses on interconnections. To infer how resources are linked, this phase relies heavily on resource-based policies (for example, Amazon S3 bucket policies, Lambda execution permissions, Amazon SNS or Amazon SQS access controls).

While the system produces a structured Markdown document for consistency and auditability, the same data is also consumed by the UI to generate an interactive graph view. This makes it possible to explore resource connections visually, identify access paths, and spot potential misconfigurations.

## Key responsibilities of the dependency mapping component
<a name="key-depend-map"></a>

This section describes the key actions and responsibilities of the dependency mapping component.

### Extract policies and identifiers
<a name="extract-policies-and-identifiers.3d0ead7a-9e46-5b49-b2af-e2e45ae1ec2a"></a>

The process begins by examining the infrastructure data (JSON from the scanning phase) and isolating all resources that expose policies, such as Amazon S3 buckets, Lambda functions, Amazon SNS topics, Amazon SQS queues, or Amazon EC2 instances with IAM profiles. For each resource, the system extracts identifiers and any attached resource-based policies. Examples of identifiers are IDs, [Amazon Resource Names (ARNs)](https://docs.aws.amazon.com/glossary/latest/reference/glos-chap.html#ARN), and names. These identifiers and policies form the basis of relationship discovery.

The [extract\_resource\_policies](https://github.com/awslabs/InfraDocGen/blob/dc1ea8a4ebdba821f6954a2b03c4fecbec809c10/services/policy_extractor.py#L15) function handles the extraction of policies and identifiers, by processing the infrastructure data to extract resources with attached policies, such as Amazon S3 buckets and Amazon EC2 instances.

### Construct resource ARNs
<a name="construct-resource-arns.f4bdeaa8-bfd1-57bd-b9cd-893637ee4391"></a>

Where possible, full ARNs are extracted directly from the resource metadata. For resources that don't provide ARNs explicitly, the system reconstructs them by using service-specific patterns. This approach guarantees a uniform representation across all resources, which is essential for cross-service dependency analysis.

The [extract\_resource\_arn](https://github.com/awslabs/InfraDocGen/blob/dc1ea8a4ebdba821f6954a2b03c4fecbec809c10/services/policy_extractor.py#L146) function handles the process of constructing ARNs. It either directly extracts ARNs from resource metadata or reconstructs them by using service-specific patterns defined in `ARN_CONSTRUCTION_MAP`.

### Dependency analysis powered by Amazon Bedrock
<a name="dependency-analysis-powered-by-9999999999999999brlong-.71f576c9-b064-5e1e-a7b5-c0933b63d3cc"></a>

After policies and ARNs are extracted, the system generates structured prompts that are passed to Amazon Bedrock (using the Claude 3.7 Sonnet model). The prompts strictly enforce a structured Markdown output format where each resource and its connections are described in a predictable schema. This approach helps to produce output that machines can parse, and humans can read.

The [generate\_resource\_mapping\_from\_infra\_data](https://github.com/awslabs/InfraDocGen/blob/dc1ea8a4ebdba821f6954a2b03c4fecbec809c10/services/bedrock_service.py#L483) function generates a service-by-service Markdown output after extracting and processing resource based policies using Amazon Bedrock.

### Continuation and retry handling
<a name="continuation-and-retry-handling.54bd362c-3289-553f-8102-78b44b97e011"></a>

The mapping process includes a continuation mechanism that does the following:

1. If Amazon Bedrock can't analyze all resources in a single call, it returns `CONTINUE_ANALYSIS`.

1. The system generates a continuation prompt with the remaining resources, waits briefly (to avoid rate limits), and retries.

1. This cycle repeats until all resources are analyzed or the marker is detected.

The [generate\_service\_markdown\_with\_continuation](https://github.com/awslabs/InfraDocGen/blob/dc1ea8a4ebdba821f6954a2b03c4fecbec809c10/services/policy_extractor.py#L146) function ensures that services are processed sequentially and that the continuation prompt logic is handled with retries in case of rate limits or incomplete analysis.

### Aggregation and combination
<a name="aggregation-and-combination.afd977ad-8381-50b3-b395-c77401e3dd85"></a>

Finally, all per-service dependency mappings are merged into a single, consolidated Markdown document.

This process is handled by the method [combine\_service\_markdown\_results](https://github.com/awslabs/InfraDocGen/blob/dc1ea8a4ebdba821f6954a2b03c4fecbec809c10/services/bedrock_service.py#L958). It ensures that all the dependency mappings are merged in a logical, readable format. The format starts with a header, followed by the total resources, successful services, and resource dependencies for each service. The final document presents both the successes and failures of the analysis in a structured way.

### Graph conversion for UI
<a name="graph-conversion-for-ui.78458bcb-d922-55c9-8eba-8dbce9e98dda"></a>

The Markdown output is parsed and transformed into a **graph data model** (nodes and edges) using [React Flow](https://www.npmjs.com/package/reactflow) as follows:
+ *Nodes* represent resources such as Lambda functions, Amazon S3 buckets, and Amazon DynamoDB tables.
+ *Edges *represent connections or access relationships such as Lambda to `S3: InvokeFunction`. This enables the frontend to render a **network graph** where dependencies can be visually explored.

## Workflow of the dependency mapping component
<a name="workflow-depend-map"></a>

The dependency mapping component uses the following workflow:

1. **Input: infrastructure data** – The dependency mapping process begins with the JSON output generated in the document generation phase. This file contains detailed information about AWS resources, their metadata, and any attached resource-based policies, serving as the foundation for all subsequent analysis.

1. **Policy extraction** – Before relationships can be mapped, the system runs a policy extractor that identifies resources with attached policies. It normalizes identifiers such as ARNs, cleans up service-specific variations, and outputs a refined dataset focused only on resources relevant for dependency mapping.

1. **Prompt construction** – After the clean dataset is prepared, the system constructs specialized prompts tailored for Amazon Bedrock (which is using Claude). These prompts embed extracted policy data and enforce strict Markdown formatting rules, so that the AI generates structured, machine-readable, and human-readable output instead of free-form text.

1. **Amazon Bedrock analysis** – Amazon Bedrock processes the prepared dataset and generates dependency mappings by analyzing policies and resource metadata. To handle large infrastructures, the system includes retry and continuation support, allowing analysis to continue seamlessly across multiple calls until all resources are covered.

1. **Aggregation and post-processing** – Outputs from individual service analyses are aggregated into a single unified document. During this stage, duplicates are removed and errors are flagged. Metadata, such as total resources analyzed, services covered, and processing time, is appended for completeness.

1. **Graph transformation** – The structured Markdown output from Amazon Bedrock is transformed into a graph data model. Each resource becomes a node and relationships derived from policies or metadata are represented as edges, enabling a clear visualization of dependencies and access flows.

1. **Visualization in UI** – Finally, the dependency graph is rendered in the UI using [React Flow](https://reactflow.dev/), where users can explore it interactively. Features like zoom, filtering, and search help engineers and security teams to quickly identify relationships, spot misconfigurations, and understand the broader AWS resource landscape.

## User view of dependency mapping
<a name="user-view-depend-map"></a>

The dependency mapping results are displayed as an interactive graph in the UI. Users can explore resource relationships visually, making it easier to understand complex dependencies across AWS services. You can also select any specific resource card to focus on its specific dependencies.
