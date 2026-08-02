---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/automating-aws-infrastructure-documentation-generation-and-analysis/resource-scanning.html
---

# Resource scanning
<a name="resource-scanning"></a>

The *resource scanning* component is the foundation of the Infrastructure Documentation Generator. Its job is to discover and inventory AWS resources across AWS Regions in a consistent and structured way. This process is critical because all subsequent phases (documentation generation and dependency mapping) rely on the data collected here.

## Key responsibilities of the resource scanning component
<a name="key-resource-scan"></a>

This section describes the key actions and responsibilities of the resource scanning component.

### Enumerate AWS resources
<a name="enumerate-9999999999999999aws--resources.b9bd0d1f-bed7-52c5-9984-aa2cd45794e0"></a>

The resource scanner begins by identifying all AWS resources across AWS services. For each service, it performs targeted API calls through AWS SDK for Python (Boto3) to retrieve detailed configurations. Many AWS services consist of multiple sub-resources, such as Amazon Elastic Compute Cloud (Amazon EC2) instances, volumes, and security groups. The scanner systematically captures them all to ensure complete visibility of the cloud environment.

The scanner uses a declarative configuration approach through the [SERVICE\_SCAN\_FUNCTIONS](https://github.com/awslabs/InfraDocGen/blob/dc1ea8a4ebdba821f6954a2b03c4fecbec809c10/constants.py#L33) dictionary, which maps each AWS service to its specific API calls and response structures.

### Optimize parallel execution
<a name="optimize-parallel-execution.321a6020-3d61-5908-8ca3-5ddbcd3c096b"></a>

To maximize efficiency when scanning large AWS environments, the system implements parallel processing across multiple AWS Regions and services simultaneously. Using a thread pool architecture, the scanner distributes API calls across concurrent workers, dramatically reducing total execution time.

The core of this parallel execution strategy is implemented in the [scan\_resources](https://github.com/awslabs/InfraDocGen/blob/dc1ea8a4ebdba821f6954a2b03c4fecbec809c10/services/discovery_service.py#L96) function, which orchestrates the entire scanning process using Python's `concurrent.futures` framework.

### Extract resource-based policies
<a name="extract-resource-based-policies.9704e142-faac-5f56-8dd7-3bc9f1389c23"></a>

Certain AWS services expose [resource-based policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#policies_resource-based) that define how external entities can interact with them. Examples of such services are Amazon Simple Storage Service (Amazon S3), AWS Lambda, Amazon Simple Notification Service (Amazon SNS), and Amazon Simple Queue Service (Amazon SQS). The scanner retrieves these policies directly from the resources and attaches them to the discovered metadata. This provides valuable context for understanding not only what resources exist but also how they are secured and who can access them.

The [add\_lambda\_resource\_policies](https://github.com/awslabs/InfraDocGen/blob/dc1ea8a4ebdba821f6954a2b03c4fecbec809c10/services/discovery_service.py#L248) function retrieves and attaches resource-based policies to Lambda functions, enriching the resource data.

### Normalize and filter fields
<a name="normalize-and-filter-fields.7e39a58f-5cd5-5302-a4e7-57525f68480e"></a>

AWS API responses can be verbose, containing extensive metadata that isn't always useful for documentation. To address this, the scanner filters responses down to a consistent set of essential fields, such as `Name`, `Arn`, and `Id`. This normalization ensures the results are lightweight, uniform, and easier to consume for both human readers and downstream processes like dependency mapping or documentation generation.

The [filter\_resource\_field](https://github.com/awslabs/InfraDocGen/blob/dc1ea8a4ebdba821f6954a2b03c4fecbec809c10/services/discovery_service.py#L13) function implements the tool's field filtering strategy, defining essential fields in [RESOURCE\_ESSENTIAL\_FIELDS](https://github.com/awslabs/InfraDocGen/blob/dc1ea8a4ebdba821f6954a2b03c4fecbec809c10/constants.py#L317) for each resource type. The function applies these filters to create consistent, streamlined resource representations:

### Return results in JSON format
<a name="return-results-in-json-format.ecce64a6-4bd8-513c-adc3-270aa9ae7231"></a>

All scanned data is returned in a structured JSON format. The output includes details of AWS services and Regions scanned, lists of discovered resources with metadata, aggregated resource counts, and any attached policies. This JSON representation serves as a standardized contract between the scanning component and other parts of the system, supporting interoperability and easy integration with visualization, analysis, or reporting layers.

### UI integration and delivery
<a name="ui-integration-and-delivery.df34dfac-95dc-54c2-9bd7-9ac1fae21950"></a>

The scanned results are displayed in the UI with expandable sections, grouped by service and Region. Users can drill down into specific AWS services and explore discovered resources interactively before moving to further phases.

## Workflow of the resource scanning component
<a name="workflow-resource-scanning"></a>

The resource scanning component uses the following workflow:

1. **Start scan** – The process begins when the client (through an API or UI) initiates a scan request. The client provides AWS credentials or specifies a target account and IAM role to assume. This input allows the system to securely access the required AWS environment.

1. **Create session** – The system establishes an [SDK for Python (Boto3)](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html) session with the provided credentials. If scanning across multiple accounts, AWS Security Token Service (AWS STS) is used to assume the specified IAM role in the target AWS account. All subsequent API calls are executed within this authenticated and authorized context.

1. **Discover AWS Regions and AWS services** – The scanner enumerates all available Regions and builds a service catalog of API operations to be performed. Both Regional services (such as Amazon EC2 and AWS Lambda) and global services (such as IAM and Amazon Route 53) are included to ensure full coverage.

1. **Parallel execution** – Using a [thread pool](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor), the scanner issues API calls across Regions and services in parallel. This design significantly reduces scan time and enables scalability across large, multi-account AWS environments.

1. **Process responses and attach policies** – The raw API responses are normalized and filtered to include only essential fields (such as `Name`, `Arn`, and `Id`). During this stage, the scanner also retrieves resource-based policies from services that expose them (for example, Amazon S3 buckets, Lambda functions, Amazon SNS topics, and Amazon SQS queues). These policies are directly attached to the corresponding resources in the results, providing deeper insight into access configurations.

1. **Aggregate results** – Results from all Regions and services are combined into a single structured JSON document. This aggregated output includes metadata about Regions and services scanned, discovered resources, resource counts, and attached policies. The JSON format makes the results easy to consume for downstream processes such as dependency mapping, documentation generation, or visualization in the UI.

## Example JSON output
<a name="example-json-output"></a>

The following example shows typical JSON output when scanning Amazon S3 buckets and Lambda functions. This output includes the AWS account ID, scan timestamp, AWS Regions and AWS services scanned, and detailed resource information including names and ARNs. For each resource, it also indicates whether a resource-based policy is present (as shown for the S3 bucket) or absent (as shown for the Lambda function).

```
{
  "account_id": "123456789012",
  "scan_time": "2025-09-03 10:20:15",
  "regions_scanned": ["us-east-1", "us-west-2"],
  "services_scanned": ["s3", "lambda"],
  "resources": [
    {
      "service": "s3",
      "region": "us-east-1",
      "function": "list_buckets",
      "resources": [
        {
           "Name": "my-app-bucket",
           "Arn": "arn:aws:s3:::my-app-bucket",
           "resource_based_policy":
            {
              "Version": "2012-10-17",
              "Statement": [...]
            }
        }
       ],
      "resource_count": 1
    },
    {
      "service": "lambda",
      "region": "us-west-2",
      "function": "list_functions",
      "resources": [
        {
           "FunctionName": "process-data-fn",
           "Arn": "arn:aws:lambda:us-west-2:123456789012:function:process-data-fn",
           "resource_based_policy": null
        }
      ],
      "resource_count": 1
    }
  ]
}
```

## User view of resource scanning
<a name="ui-view-resource-scanning"></a>

The scanned infrastructure is displayed in the UI as expandable sections organized by AWS service and Region. Users can drill down into each service to view discovered resources and attached resource-based policies.
