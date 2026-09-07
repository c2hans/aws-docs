---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/automating-aws-infrastructure-documentation-generation-and-analysis/architecture.html
---

# Architecture of the Infrastructure Documentation Generator
<a name="architecture"></a>

The Infrastructure Documentation Generator is designed with a modular architecture. The system works in the following major phases:
+ Resource scanning –The initial process of querying AWS services to discover and inventory resources, collecting metadata and policies needed for further documentation and dependency analysis. The subsequent phases rely on the data collected in this phase.
+ Documentation generation – The system creates detailed Markdown-based reports that describe AWS resource configurations, best practices, and security posture.
+ Dependency mapping – A process that analyzes resource-based policies and identifiers to build a graph of how AWS resources relate and interact with each other, enabling visualization of resource connections and access paths.

Each phase follows a structured sequence of steps, as shown in the following diagram.

![Workflow phases of resource scanning, documentation generation, and dependency mapping.](https://docs.aws.amazon.com/prescriptive-guidance/latest/automating-aws-infrastructure-documentation-generation-and-analysis/images/guide-img/1ecac3aa-b4fc-4e34-a08c-2c0eb2350189/images/e5f5fef3-e3bc-4874-b6c5-0b5c28bf61e2.png)

## Resource scanning phase
<a name="resource-scanning-phase.ffa7169f-cc53-52a1-b462-3560baf8a194"></a>

The following steps occur in the resource scanning phase:

1. **Request resource information** – The process begins when a client sends an initial request to the system to gather information about their AWS infrastructure.

1. **Request resource scan** – The resource scanner component activates and prepares to scan multiple AWS services. It formulates the appropriate API calls to collect comprehensive infrastructure data.

1. **Authenticate and access** – The system uses the AWS SDK for Python (Boto3) to interact with AWS services by making authenticated API requests using the provided credentials. This establishes a valid session for retrieving resource information.

1. **Authorize access to query resources** – AWS Identity and Access Management (IAM) role permissions are verified to confirm the scanner has the appropriate access rights to query the required AWS services. This serves as a crucial security check before retrieving resource data.

1. **Store resource data** – The system collects detailed configuration data from various AWS services, including instance details, network configurations, storage settings, and service relationships.

1. **Transfer resource data to cache storage** – The collected data is efficiently moved to local disk cache storage. This enables faster access and reduces repeated API calls to AWS services, improving performance.

1. **Respond with resource configuration** – The system compiles the collected data into a structured format suitable for client consumption and prepares it for transmission back to the client.

1. **Display resource configurations** – The formatted resource configuration data is presented to the client through the interface, showing detailed insights into their AWSinfrastructure.

## Documentation generation phase
<a name="documentation-generation-phase.3a63843e-068b-5de8-9a91-186a07947d73"></a>

1. **Request documentation generation** – The client initiates the documentation process based on the scanned resource data, triggering the documentation generator component.

1. **Use resource configurations** – The system retrieves cached resource data from the scanning phase to serve as the foundation for documentation generation.

1. **Initiate AI documentation generation** – The system begins the AI-powered documentation process using Amazon Bedrock, preparing the necessary context and prompts for documentation creation.

1. **Authenticate for **Amazon Bedrock** API** – The system establishes a connection to Amazon Bedrock by making authenticated API requests with valid credentials.

1. **Authorize access for documentation** – IAM permissions are verified to make sure that the system is allowed to use Amazon Bedrock for generating documentation.

1. **Store generated AI documentation** – The AI-generated documentation is saved in persistent storage for future reference.

1. **Transfer documentation to cache** – The generated documentation is copied into cache storage for quicker access and performance.

1. **Return documentation response** – The system formats and sends the generated documentation back to the client.

1. **Display documentation** – The documentation is presented to the client through the interface in a clear and organized format.

## Dependency mapping phase
<a name="dependency-mapping-phase.eae9c31b-c22e-534c-9ba3-a0acccfcf4f5"></a>

1. **Request dependency analysis** –The client initiates the process to analyze and map relationships between AWS resources.

1. **Use resource configurations** – The system accesses cached resource data from the scanning phase to identify interdependencies among resources.

1. **Initiate relationship analysis** – The dependency mapper processes the resource data to identify and map connections between AWS services.

1. **Authenticate for **Amazon Bedrock – The system establishes a connection to Amazon Bedrock by making authenticated API requests with valid credentials.

1. **Authorize access for dependency analysis** – IAM permissions are verified to ensure the system can use Amazon Bedrock for dependency analysis tasks.

1. **Store dependency results** – The completed dependency analysis results are saved in persistent storage.

1. **Transfer mappings to cache** – Dependency mapping data is moved into cache storage for faster access and reuse.

1. **Return dependency response** – The system prepares and sends the dependency analysis results back to the client.

1. **Display dependency graph** – The final dependency relationships are visualized and shown to the client as an interactive graph, illustrating service connections and resource dependencies.
