---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/architecture-details.html
---

# Architecture details
<a name="architecture-details"></a>

This section describes the components and AWS services that make up this solution and the architecture details on [how these components work together](how-aws-solution-for-prebid-server-works.md).

## AWS services in this solution
<a name="aws-services-in-this-solution"></a>

| AWS service | Description |
| --- | --- |
|  [Amazon CloudFront](https://aws.amazon.com/cloudfront/)  |  **Core**. Serve client requests to Prebid Server application. |
|  [AWS DataSync](https://aws.amazon.com/datasync/)  |  **Core**. Automate transfer of Prebid Server application logs and metrics from Amazon EFS to Amazon S3. |
|  [Amazon ECS](https://aws.amazon.com/ecs/)  |  **Core**. Host and manage containerized Prebid Server application. |
|  [Amazon EFS](https://aws.amazon.com/efs/)  |  **Core**. Centralize storage of Prebid Server application logs and metrics across containers. |
|  [Amazon ElastiCache](https://aws.amazon.com/elasticache/)  |  **Core**. Provide serverless Redis-compatible cache (Valkey) for storing cached bid responses with configurable time-to-live (TTL). |
|  [Elastic Load Balancing](https://aws.amazon.com/elasticloadbalancing/)  |  **Core**. Provide high availability and automate scaling of Prebid Server application containers hosted on Amazon ECS. Route cache requests to Lambda function. |
|  [Amazon EventBridge](https://aws.amazon.com/eventbridge/)  |  **Core**. Send and receive messages between solution resources handling Prebid Server application metrics and logs. |
|  [AWS Glue](https://aws.amazon.com/glue/)  |  **Core.** Transform, catalog, and partition metrics data into Amazon S3 and [AWS Glue Data Catalog](https://docs.aws.amazon.com/glue/latest/dg/catalog-and-crawler.html). |
|  [AWS Identity and Access Management (IAM)](https://aws.amazon.com/iam/)  |  **Core**. Restricts solution resource permissions to least privilege access for security. |
|  [AWS KMS](https://aws.amazon.com/kms/)  |  **Core**. Encrypt and decrypt the data in Amazon S3. |
|  [AWS Lambda](https://aws.amazon.com/lambda/)  |  **Core**. Facilitate deployment and deletion of the solution through [Lambda-backed custom resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources-lambda.html), cleaning archived log and metrics files from Amazon EFS after being moved to Amazon S3 for long term storage, triggering AWS Glue, and handling cache storage and retrieval operations. |
|  [Amazon S3](https://aws.amazon.com/s3/)  |  **Core**. Provide long term storage of Prebid Server application logs and metrics from Amazon EFS. |
|  [AWS Systems Manager](https://aws.amazon.com/systems-manager/)  |  **Core**. Provide application-level resource monitoring and visualization of resource operations and cost data. |
|  [Amazon VPC](https://aws.amazon.com/vpc/)  |  **Core**. Control network permissions between solution resources. |
|  [AWS WAF](https://aws.amazon.com/waf/)  |  **Core**. Provide layer of security around Amazon CloudFront. |
|  [AWS CloudTrail](https://aws.amazon.com/cloudtrail/)  |  **Supporting**. Track activity across solution S3 buckets and Lambda functions. |
|  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)  |  **Supporting**. View logs and subscribe to alarms for AWS Lambda and AWS Glue. |
|  [Amazon Athena](https://aws.amazon.com/athena/)  |  **Optional**. Access AWS Glue Data Catalog and query the Prebid Server application metrics in Amazon S3. |
|  [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/)  |  **Optional**. Provide low-latency, cost-optimized private network connectivity between Prebid Server and bidders without traversing the public internet. |

## CloudFront distribution
<a name="cloudfront-distribution"></a>

The solution uses Amazon CloudFront as the unified network entry point. It receives the incoming auction requests and handles outgoing responses. CloudFront speeds up the distribution of your content by routing each user request through the AWS backbone network to the edge location that can best serve your content. CloudFront provides a TLS endpoint for privacy of requests and responses in transit with the pubic internet. ALB is the configured origin for CloudFront. Direct access to ALB is restricted by using a custom header, enhancing security.

## AWS WAF
<a name="aws-waf"></a>

AWS Web Application Firewall (AWS WAF) and AWS Shield Standard are used as a protection mechanism from Distributed Denial of Service (DDoS) attacks against the Prebid Server cluster. AWS WAF can activate one or more managed rule groups by default after extended testing including rules in the Baseline Rule Group and the IP Reputation Rule Group. You have the option to activate, purchase, or use existing rule subscriptions, or add regular expression or CIDR matching rules as needed.

**Note**
If you want to opt out of using CloudFront and AWS WAF and directly send requests to the ALB, see [How to opt out](configure-the-solution.md#how-to-opt-out).

## Application Load Balancer (ALB)
<a name="application-load-balancer-alb"></a>

ALB distributes incoming request traffic for Prebid Server through the cluster of containers. It provides a single entry point into the cluster and is the primary origin for the CloudFront distribution. ALB also routes cache-related requests (paths starting with `/cache`) to the cache Lambda function, which handles storage and retrieval of cached bid responses in ElastiCache.

## Amazon VPC
<a name="amazon-vpc"></a>

The Amazon Virtual Private Cloud (Amazon VPC) is configured with redundant subnets, routes, and NAT gateways. Security groups permit traffic to and from the subnets. The Amazon VPC contains the network interfaces for the Prebid Server container cluster nodes. It is configured for private IP addresses only and container networks configured within the Amazon VPC use the NAT gateway as a default route to the internet for communication.

When the bidder simulator is deployed, the solution supports two connectivity modes:

 **VPC Peering**

When deploying with the bidder simulator using `--simulator-connectivity vpc-peering`, the solution creates a VPC peering connection between the Prebid Server VPC and the Bidder Simulator VPC. This provides direct, private connectivity between the two environments without traversing the public internet. The peering connection is automatically configured with appropriate routes and security group rules. Use this mode in regions where RTB Fabric is not available.

 **AWS RTB Fabric (recommended)**

When deploying with the bidder simulator using `--simulator-connectivity rtb-fabric`, the solution creates RTB Fabric gateways in each VPC and manages the Fabric Link through the `simulator-fabric-link.sh` script. This provides purpose-built, low-latency connectivity optimized for real-time bidding traffic. See the [AWS RTB Fabric integration](#aws-rtb-fabric-integration) section for details.

## Amazon ECS
<a name="amazon-ecs"></a>

Amazon Elastic Container Service (Amazon ECS) is a fully managed container orchestration service that helps you easily deploy, manage, and scale containerized Prebid Server application. These resources define the configuration, count, and thresholds to scale-out and scale-in the total container count in the ECS cluster. The ECS task and service resource define the operating environment for the cluster and thresholds for scaling and health. Scaling changes are based on CPU, process load, and network traffic (requests per target). For cost optimization, ECS uses a weighted combination of Fargate and [Fargate Spot](https://docs.aws.amazon.com/AmazonECS/latest/bestpracticesguide/ec2-and-fargate-spot.html) instances. There’s a cost benefit to using more Fargate Spot instances, but the risk of unavailability goes up. You might find that after running the solution for a while that a different ratio is better for you.

## AWS RTB Fabric integration (optional)
<a name="aws-rtb-fabric-integration"></a>

 [AWS RTB Fabric](https://aws.amazon.com/rtb-fabric/) is a private network purpose-built for real-time bidding that provides low-latency, cost-optimized connectivity between ad tech participants without traversing the public internet. When deployed, the solution creates gateway resources in CloudFormation and manages the Fabric Link lifecycle through an external script.

### RTB Fabric architecture
<a name="rtb-fabric-architecture"></a>

The RTB Fabric integration spans two VPCs and uses a dedicated private network for bid request traffic:

```
┌─────────────────────────────┐         ┌─────────────────────────────┐
│   PrebidServerStack VPC     │         │  BidderSimulatorStack VPC   │
│                             │         │                             │
│  ┌───────────────────────┐  │         │  ┌───────────────────────┐  │
│  │  ECS Fargate Tasks    │  │         │  │  Lambda Bidder        │  │
│  │  (Prebid Server)      │  │         │  │  (Simulator)          │  │
│  └──────────┬────────────┘  │         │  └──────────▲────────────┘  │
│             │               │         │             │               │
│  ┌──────────▼────────────┐  │         │  ┌──────────┴────────────┐  │
│  │  Requester Gateway    │──┼── RTB ──┼──│  Responder Gateway    │  │
│  │  (HTTPS port 443)     │  │ Fabric  │  │  (HTTP port 80)       │  │
│  └───────────────────────┘  │  Link   │  └───────────────────────┘  │
└─────────────────────────────┘         └─────────────────────────────┘
```

 **Requester Gateway**

Deployed in the Prebid Server VPC, the requester gateway sends bid requests over HTTPS (port 443) through the RTB Fabric private network. Prebid Server is configured to route bid requests to the RTB Fabric link URL instead of directly to bidder endpoints. The gateway is provisioned as part of the PrebidServerStack when `EnableRtbRequesterGateway` is set to `true`.

 **Responder Gateway**

Deployed in the Bidder Simulator VPC, the responder gateway receives bid requests over HTTP (port 80) and forwards them to the bidder simulator Application Load Balancer. The connection uses asymmetric security — HTTPS from requester to responder, with HTTP responses on the internal AWS network. The gateway is provisioned as part of the BidderSimulatorStack when `EnableRtbFabric` is set to `true`.

 **Fabric Link**

The Fabric Link connects the requester and responder gateways through AWS RTB Fabric’s private network. The link provides dedicated bandwidth and low-latency routing optimized for real-time bidding traffic patterns. Unlike the gateways, the Fabric Link is **not** managed by CloudFormation — it is created and deleted by the `simulator-fabric-link.sh` script (see [Script-based link lifecycle](#script-based-link-lifecycle) below).

### WaitForGateway custom resource
<a name="waitforgateway-custom-resource"></a>

The `WaitForGateway` custom resource ensures that the RTB Fabric Requester Gateway is fully provisioned and ready to accept connections before the CloudFormation stack reports completion. Gateway provisioning is asynchronous — the `CfnGateway` resource returns immediately, but the gateway may take several minutes to reach an `ACTIVE` state.

The custom resource uses a Lambda function that:

1. Polls the gateway status using the RTB Fabric API

1. Waits until the gateway reaches `ACTIVE` state

1. Returns success to CloudFormation, allowing dependent resources to proceed

This ensures that any post-deployment steps (such as Fabric Link creation) can rely on the gateway being ready. The `WaitForGateway` resource is gated by the `HasRtbRequesterGateway` condition and depends directly on the `RequesterGateway` resource.

### Script-based link lifecycle
<a name="script-based-link-lifecycle"></a>

The Fabric Link is managed independently of CloudFormation by the `deployment/simulator-fabric-link.sh` script. This design decouples the link lifecycle from stack operations, enabling:
+ Independent link creation and deletion without stack updates
+ Reliable teardown ordering (delete link before destroying stacks)
+ Faster iteration during development (no 5-10 minute stack update cycles)
+ Direct ECS task definition updates (\~30 seconds vs. full stack update)

The script provides three subcommands:

| Subcommand | Description |
| --- | --- |
|  `create`  | Creates a Fabric Link, polls until active with exponential backoff (5s → 10s → 20s → 30s cap, 5-minute timeout), accepts the link, stores the link ID in SSM Parameter Store, and updates the ECS task definition with the link URL. |
|  `delete`  | Reads the link ID from SSM Parameter Store, calls the RTB Fabric DeleteLink API, and removes the SSM parameter. Idempotent — exits successfully if no link exists. |
|  `status`  | Reads the link ID from SSM Parameter Store and displays the current link status, URL, and gateway IDs. |

 **Integration with deployment scripts:**
+  `deploy.sh` invokes `simulator-fabric-link.sh create` after both stacks are deployed (when using `--simulator-connectivity rtb-fabric`)
+  `destroy.sh` invokes `simulator-fabric-link.sh delete` before initiating CloudFormation stack deletion
+ The CI/CD pipeline runs the script as a post-deployment step before functional tests

 **State persistence:**

The script persists the Fabric Link ID in AWS Systems Manager Parameter Store at the path `/{stack-name}/fabric-link/link-id`. This allows the link to be managed across separate script invocations and survives stack updates.

 **ECS task update:**

After link creation, the script registers a new ECS task definition revision with the `AMT_BIDDING_SERVER_SIMULATOR_ENDPOINT` environment variable set to the link URL, then updates the ECS service to trigger a rolling deployment. This approach takes approximately 30 seconds compared to 5-10 minutes for a full CloudFormation stack update.

### VPC peering fallback architecture
<a name="vpc-peering-fallback"></a>

For regions where AWS RTB Fabric is not available, the solution supports direct VPC peering as a fallback connectivity mode. VPC peering provides private connectivity between the Prebid Server VPC and the Bidder Simulator VPC without traversing the public internet.

```
┌─────────────────────────────┐         ┌─────────────────────────────┐
│   PrebidServerStack VPC     │         │  BidderSimulatorStack VPC   │
│                             │         │                             │
│  ┌───────────────────────┐  │         │  ┌───────────────────────┐  │
│  │  ECS Fargate Tasks    │  │         │  │  Lambda Bidder        │  │
│  │  (Prebid Server)      │  │         │  │  (Simulator)          │  │
│  └──────────┬────────────┘  │         │  └──────────▲────────────┘  │
│             │               │         │             │               │
│  ┌──────────▼────────────┐  │   VPC   │  ┌──────────┴────────────┐  │
│  │  Private Subnet       │──┼─Peering─┼──│  ALB                  │  │
│  │  (Route to BSS CIDR)  │  │         │  │  (Bidder endpoint)    │  │
│  └───────────────────────┘  │         │  └───────────────────────┘  │
└─────────────────────────────┘         └─────────────────────────────┘
```

When VPC peering is used:
+ The `SimulatorEndpoint` CloudFormation parameter is set to the bidder simulator ALB DNS name
+ Routes are configured in both VPCs to allow traffic across the peering connection
+ Security groups permit inbound traffic from the peer VPC CIDR
+ The ECS task `AMT_BIDDING_SERVER_SIMULATOR_ENDPOINT` environment variable resolves to the `SimulatorEndpoint` value
+ No RTB Fabric gateways or links are created

 **Choosing between RTB Fabric and VPC peering:**

| Criteria | RTB Fabric | VPC Peering |
| --- | --- | --- |
| Region availability | Requires RTB Fabric support in the deployment region | Available in all AWS regions |
| Latency optimization | Purpose-built for real-time bidding traffic patterns | Standard VPC networking |
| Production readiness | Recommended for production bidder integrations | Suitable for testing or non-RTB regions |
| Setup mechanism |  `deploy.sh --simulator-connectivity rtb-fabric`  |  `deploy.sh --simulator-connectivity vpc-peering`  |

**Note**
RTB Fabric requires the bidder simulator to be deployed as it needs both requester and responder gateways. RTB Fabric must also be available in your deployment region. If RTB Fabric is not available, use VPC peering as the connectivity mode.

## Bidder Simulator (optional)
<a name="bidder-simulator"></a>

The bidder simulator is an optional component that provides a quick start testing environment to validate your Prebid Server deployment without needing to configure external bidders. The simulator includes:

 **Architecture**

The bidder simulator uses a CloudFront \+ Application Load Balancer \+ Lambda architecture to simulate bidder responses. It supports both banner and video ad formats, including VAST instream video.

 **Bidder Simulator Adapter Integration**

When deployed, the solution automatically configures the custom prebid bidder adapter in Prebid Server allowing connectivity to the Bidder Simulator. The adapter files are conditionally included in the Docker build, and environment variables are automatically set for proper integration.

 **Demo Website**

A demo website with Prebid.js integration is included to test the end-to-end flow from prebid.js through Prebid Server to the bidder simulator. The demo supports both banner and video ad units. For usage instructions, see the demo website readme at `source/loadtest/demo/README.md`.

 **Connectivity Options**

The bidder simulator supports two connectivity modes to Prebid Server:
+  **VPC Peering**: Direct private connectivity through VPC peering connection. Use in regions without RTB Fabric support.
+  **RTB Fabric** (recommended): Private network connectivity through AWS RTB Fabric, managed by the `simulator-fabric-link.sh` script.

**Note**
The bidder simulator is intended for testing and validation purposes. For production deployments, configure Prebid Server to connect to your actual bidder endpoints.

## Cache architecture
<a name="cache-architecture"></a>

The solution includes a cache service that stores and retrieves bid responses for Prebid Server. The cache architecture uses the following components:

 **ElastiCache Serverless (Valkey)**

The solution uses Amazon ElastiCache Serverless with Valkey (Redis-compatible) engine to provide a fully managed, serverless cache. The cache is deployed in the private subnets of the VPC and uses IAM authentication for secure access. Cache data is stored with configurable time-to-live (TTL) settings.

 **Cache Lambda Function**

An AWS Lambda function handles cache storage and retrieval operations. The function is invoked through ALB target group rules that route requests with paths starting with `/cache` to the Lambda function. The Lambda function connects to the ElastiCache Serverless cache using IAM authentication and the Redis protocol.

 **Unified Cache Endpoint**

Both Prebid Server containers and client-side code (prebid.js) use the same publicly accessible cache endpoint:
+  **CloudFront deployment**: Cache endpoint is the CloudFront distribution domain
+  **ALB-only deployment**: Cache endpoint is the external ALB DNS name

This unified approach ensures consistent cache access patterns and simplifies the architecture by eliminating the need for separate internal and external cache endpoints.

 **Cache Request Flow**

When Prebid Server needs to cache a bid response:

1. Container sends cache request to the configured `CACHE_HOST` (CloudFront domain or external ALB DNS)

1. Request flows through CloudFront (if deployed) to the external ALB

1. ALB routes the request to the cache Lambda function based on path rules

1. Lambda function stores the bid response in ElastiCache Serverless and returns a cache key

1. Client-side code later retrieves the cached response using the same endpoint

**Note**
The cache service is designed to handle both server-side caching (from Prebid Server containers) and client-side retrieval (from browsers). Using a single public endpoint for both access patterns ensures optimal performance and simplifies configuration.

## Prebid Server container
<a name="prebid-server-container"></a>

This is a docker container that runs the open source Prebid Server and is hosted in [Amazon Elastic Container Registry](https://aws.amazon.com/ecr/) (Amazon ECR). The container differs from the open source project’s default container in configuration settings for areas including log output to the Console and bidding adapter configuration settings.

## Amazon EFS
<a name="amazon-efs"></a>

The EFS file system is mounted and shared among all container instances in the ECS cluster. This file system is used for log capture (operational and metrics), and has the potential to be expanded to include shared configuration and storage related to more advertisement types (for example, video and mobile).

## DataSync (EFS to S3)
<a name="datasync-efs-to-s3"></a>

DataSync is configurated to periodically move rotated log files from each Prebid Server container’s EFS location to an equivalent location in the `DataSyncLogsBucket` S3 bucket. After each file is copied to S3 and verified, it is removed from the EFS file system through a clean-up Lambda function. Essentially, only actively written log files are retained on the EFS file system until the Prebid Server process closes it, rotates it, and starts a new file. Rotated log files are migrated with DataSync. Runtime logs are rotated every 24 hours or when reaching 100 MB. Metrics logs are rotated every one hour or when reaching 100 MB.

## Glue ETL (Metrics processing)
<a name="glue-etl-metrics-processing"></a>

AWS Glue is a serverless data integration service that makes it easy for analytics users to discover, prepare, move, and integrate data from multiple sources. You can use it for analytics, machine learning, and application development. It also includes additional productivity and data ops tooling for authoring, running jobs, and implementing business workflows. This resource is responsible for periodically processing new metrics log files in the `DataSyncLogsBucket` S3 bucket. The CSV-formatted metrics are transformed into several tables and partitioned. After ETL processing completes, the new data is available to clients through AWS Glue Data Catalog.

## AWS Glue Data Catalog
<a name="aws-glue-data-catalog"></a>

AWS AWS Glue Data Catalog provides access for clients to the Prebid Server metric data through Athena or other compatible clients, such as Amazon SageMaker AI, Amazon QuickSight, and JDBC clients. Clients can query and view the Prebid Server metrics data, generate graphs, summaries or inferences using AI/ML.

## Amazon CloudWatch
<a name="cloudwatch"></a>

CloudWatch alarms monitor specific metrics in real-time and proactively notify AWS Management Console users when predefined conditions are met. This solution has several CloudWatch alarms to help monitor its health and performance. These alarms are enabled automatically when the AWS CDK stack is deployed. For details, see the [CloudWatch Alarms](traffic-monitoring.md#amazon-cloudwatch-alarms) section.

**Note**
All resources are created in a single Region specified by the user except for CloudFront and AWS WAF. CloudFront is considered a global resource, and AWS WAF is always created in the `us-east-1` (N.Virginia) Region for configuration with CloudFront.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Deploying a Prebid Server on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
