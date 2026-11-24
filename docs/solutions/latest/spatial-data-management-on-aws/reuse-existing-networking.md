---
source_url: https://docs.aws.amazon.com/solutions/latest/spatial-data-management-on-aws/reuse-existing-networking.html
---

# Reuse Existing Networking Infrastructure

By default, Spatial Data Management on AWS creates a new Amazon Virtual Private Cloud (Amazon VPC) with all required subnets, NAT gateways, and VPC endpoints. If your organization already has a VPC that meets the solution’s networking requirements, you can deploy the solution into that existing VPC instead.

**Important**
The choice to use an existing VPC is permanent for the lifetime of the stack. You cannot switch from a solution-managed VPC to a customer-provided VPC (or vice versa) on an existing deployment. If you need to change this configuration, deploy a new stack.

## Overview
<a name="byo-vpc-overview"></a>

When you provide an existing VPC, the solution:
+ Imports your VPC instead of creating one
+ Skips creation of the internet gateway and NAT gateways (your VPC must already provide outbound internet access)
+ Uses the subnet IDs you provide — no auto-discovery
+ Validates all prerequisites at deploy time and fails with a descriptive error if any requirement is not met
+ Never modifies your existing VPC resources — route tables, network ACLs, security groups, and endpoint configurations are read-only

You must pre-create all required VPC endpoints before deploying (unless you set `UseVpcEndpoints=No`). The solution validates that all required endpoints exist and fails with a clear error listing any that are missing.

The solution does create new resources inside your VPC: security groups for AWS Lambda functions. These are resources owned by the solution and do not modify any existing customer resources.

## Prerequisites
<a name="byo-vpc-prerequisites"></a>

Before deploying with an existing VPC, verify that your VPC meets all of the following requirements. The solution validates most of these at deploy time and fails with a descriptive error if a requirement is not met.

### VPC Requirements
<a name="byo-vpc-requirements"></a>

| Requirement | How to configure | Validated at deploy time |
| --- | --- | --- |
| DNS hostnames enabled | In the VPC console, choose **Actions**, **Edit VPC settings**, and enable **DNS hostnames**  | Yes |
| DNS support enabled | In the VPC console, choose **Actions**, **Edit VPC settings**, and enable **DNS resolution**  | Yes |

### Subnet Requirements
<a name="byo-subnet-requirements"></a>

You may provide isolated and private subnet IDs using the `ExistingIsolatedSubnetIds` and `ExistingPrivateSubnetIds` CloudFormation parameters. The solution validates the provided subnets but does not auto-discover them.

 `ExistingIsolatedSubnetIds` is optional. If omitted, all Lambda functions are placed in the private subnets. This is acceptable if your organization does not use isolated subnets, but removes the network-level isolation for core data-plane Lambdas.

The solution requires two types of subnets, each spanning at least 2 Availability Zones:

 **Isolated subnets** (optional) — Used for core data-plane Lambda functions (ResourceOperation, AssetWatcher, AssetsSearchIndexer, SystemBootstrap). These subnets must have no internet route. All AWS service access goes through VPC endpoints. If you do not provide isolated subnets, these Lambdas are placed in the private subnets instead.

 **Private subnets** — Used for connector and identity Lambda functions (ConnectorInvocation, CognitoIdentity, MetricEmitter, MetricsReporting). These subnets must have a route to the internet for outbound access (for example, via a NAT gateway, NAT instance, or Transit Gateway).

| Requirement | How to configure | Validated at deploy time |
| --- | --- | --- |
| Provide at least 2 isolated subnet IDs (comma-separated) (optional) | Set the `ExistingIsolatedSubnetIds` parameter, or omit to place all Lambdas in private subnets | Yes (only if provided) |
| Isolated subnets belong to the specified VPC | Verify subnet IDs are in the correct VPC | Yes |
| Isolated subnets span at least 2 Availability Zones | Create isolated subnets in at least 2 distinct Availability Zones | Yes |
| Isolated subnets have no internet route | Route table must not have a `0.0.0.0/0` route via a NAT gateway or internet gateway | Yes |
| Provide at least 2 private subnet IDs (comma-separated) | Set the `ExistingPrivateSubnetIds` parameter | Yes |
| Private subnets belong to the specified VPC | Verify subnet IDs are in the correct VPC | Yes |
| Private subnets span at least 2 Availability Zones | Create private subnets in at least 2 distinct Availability Zones | Yes |
| Private subnets have an outbound internet route | Route table must have a `0.0.0.0/0` route (for example, via a NAT gateway or Transit Gateway) | Yes |

### Network ACL Requirements
<a name="byo-nacl-requirements"></a>

The default VPC network ACL (allow-all) satisfies all requirements. If you use custom network ACLs, configure the following minimum rules.

**Important**
The ephemeral port rules (TCP 1024–65535) are critical. When a Lambda function calls a VPC endpoint on port 443, the endpoint responds on an ephemeral port from the VPC CIDR. Without these rules, Lambda functions receive timeout errors that can appear as misleading messages such as `Package @aws-sdk/client-ssm does not exist`.

 **Isolated subnets (Lambda to VPC endpoints):**

| Direction | Protocol | Port range | CIDR | Purpose |
| --- | --- | --- | --- | --- |
| Outbound | TCP | 443 | VPC CIDR | Lambda to VPC endpoints (HTTPS requests) |
| Outbound | TCP | 1024–65535 | VPC CIDR | Return traffic from VPC endpoint responses |
| Inbound | TCP | 443 | VPC CIDR | Lambda HTTPS requests arriving at VPC endpoint ENIs |
| Inbound | TCP | 1024–65535 | VPC CIDR | VPC endpoint responses returning to Lambda |

 **Private subnets (Lambda to VPC endpoints and internet):**

| Direction | Protocol | Port range | CIDR | Purpose |
| --- | --- | --- | --- | --- |
| Outbound | TCP | 443 | 0.0.0.0/0 | Lambda to external APIs (via NAT gateway or equivalent) |
| Outbound | TCP | 1024–65535 | VPC CIDR | Lambda to VPC endpoints (return traffic) |
| Inbound | TCP | 443 | VPC CIDR | VPC endpoints to Lambda (HTTPS requests) |
| Inbound | TCP | 1024–65535 | VPC CIDR | VPC endpoints to Lambda (responses on ephemeral ports) |
| Inbound | TCP | 1024–65535 | 0.0.0.0/0 | Return traffic from internet |

### VPC Endpoint Requirements
<a name="byo-endpoint-requirements"></a>

You must pre-create all required VPC endpoints before deploying the solution, unless you set `UseVpcEndpoints=No`. The solution validates that all required endpoints exist and fails with a clear error listing any that are missing. The solution does not create VPC endpoints in your existing VPC.

**Note**
If your VPC uses only private subnets with NAT gateways (no isolated subnets) and you prefer not to create VPC endpoints, set `UseVpcEndpoints=No`. In this mode, Lambda functions reach AWS services over the internet via your NAT gateway. VPC endpoint validation is skipped. You can still provide an `ExistingOpenSearchVpcEndpointId` to keep the OpenSearch collection private (VPC-only access) even without other VPC endpoints.

Each Interface VPC endpoint’s security group must allow inbound TCP 443 from the VPC CIDR block. The solution validates this at deploy time.

Gateway endpoints (Amazon S3 and Amazon DynamoDB) must be associated with the route tables of your isolated subnets. The solution validates this at deploy time.

The following VPC endpoints are required:

| Service | Purpose |
| --- | --- |
| Amazon S3 (Gateway) | Core data-plane Lambda access to asset storage |
| Amazon DynamoDB (Gateway) | Core data-plane Lambda access to metadata tables |
| Amazon SQS | AssetWatcher and ConnectorInvocation event sources |
| AWS Lambda | Cross-Lambda invocation |
| AWS Security Token Service (AWS STS) | AssumeRole for client-vended credentials |
| AWS Key Management Service (AWS KMS) | Pagination token encryption and decryption |
| AWS Secrets Manager | CloudFront key pair retrieval |
| AWS Systems Manager | Parameter Store reads |
| Amazon CloudWatch Logs | Lambda log shipping |
| Amazon Verified Permissions | Authorization checks |
| AWS Glue | Athena catalog access for audit queries |
| Amazon Athena | Audit event queries |
| Amazon API Gateway (`execute-api`) | Internal API calls |
| Amazon Location Service (`geo.places`) | Location search |
| AWS Deadline Cloud (`deadline.management`) | Job creation and management (required only when `DeployDeadlineCloud=true`) |
| Amazon OpenSearch Serverless (`aoss`) | Search index access — provide the endpoint ID using `ExistingOpenSearchVpcEndpointId`  |

**Note**
Amazon OpenSearch Serverless VPC endpoints are created using the OpenSearch Serverless console or API, not the standard VPC endpoint console. After creating the endpoint, provide its ID using the `ExistingOpenSearchVpcEndpointId` parameter.

## CloudFormation Parameters
<a name="byo-vpc-parameters"></a>

To deploy with an existing VPC, set the following parameters when launching the CloudFormation stack:

| Parameter | Description | Default | Valid values |
| --- | --- | --- | --- |
|  `ExistingVpcId`  | ID of an existing VPC to deploy into instead of creating a new one | Empty (the solution creates a new VPC) | Valid VPC ID (`vpc-<hex>`) or empty |
|  `ExistingVpcCidrBlock`  | CIDR block of the existing VPC (for example, `10.0.0.0/16`) | Empty | Valid CIDR range or empty |
|  `ExistingIsolatedSubnetIds`  | Comma-separated IDs of isolated subnets (no internet route) in the existing VPC. Optional — if omitted, all Lambdas are placed in private subnets. | Empty | Comma-separated subnet IDs or empty |
|  `ExistingPrivateSubnetIds`  | Comma-separated IDs of private subnets (with outbound internet route) in the existing VPC | Empty | Comma-separated subnet IDs or empty |
|  `ExistingOpenSearchVpcEndpointId`  | ID of the Amazon OpenSearch Serverless VPC endpoint in the existing VPC | Empty | Valid VPC endpoint ID (`vpce-<hex>`) or empty |
|  `UseVpcEndpoints`  | For bring-your-own (BYO) VPC deployments: controls whether VPC endpoint validation and creation is required. Set to `No` if your VPC uses only private subnets with NAT gateways and you do not want to create VPC endpoints. When set to `No`, Lambda functions reach AWS services over the internet via NAT instead of through VPC endpoints. The `ExistingOpenSearchVpcEndpointId` parameter is still honored when provided — the OpenSearch collection remains VPC-private even with `UseVpcEndpoints=No`. Only applicable when `ExistingVpcId` is provided. |  `Yes`  |  `Yes` or `No`  |

All five parameters are required when `ExistingVpcId` is set, except `ExistingIsolatedSubnetIds` which is optional and `ExistingOpenSearchVpcEndpointId` which is only required when `UseVpcEndpoints` is `Yes`. Leave all parameters empty to use the default behavior, where the solution creates all networking resources.

These parameters are immutable once set, except for `UseVpcEndpoints` which can be toggled on stack updates. You cannot change the other parameters on a stack update. See [Immutability and stack updates](#byo-vpc-immutability).

## Deployment Steps
<a name="byo-vpc-deploy-steps"></a>

To deploy the solution with an existing VPC:

1. Complete all [prerequisites](#byo-vpc-prerequisites) before starting the deployment, including pre-creating all required VPC endpoints.

1. Follow the standard [deployment steps](deployment-steps.md).

1. In **Step 3: Specify Stack Parameters**, set the following parameters:
   +  `ExistingVpcId` — your VPC ID (for example, `vpc-0a1b2c3d4e5f67890`)
   +  `ExistingVpcCidrBlock` — your VPC CIDR block (for example, `10.0.0.0/16`)
   +  `ExistingIsolatedSubnetIds` — (optional) comma-separated isolated subnet IDs (for example, `subnet-aaa,subnet-bbb`). If omitted, all Lambdas are placed in private subnets.
   +  `ExistingPrivateSubnetIds` — comma-separated private subnet IDs (for example, `subnet-ccc,subnet-ddd`)
   +  `ExistingOpenSearchVpcEndpointId` — your AOSS VPC endpoint ID (for example, `vpce-0a1b2c3d4e5f67890`). Required when `UseVpcEndpoints=Yes`.
   +  `UseVpcEndpoints` — (optional) set to `No` to skip VPC endpoint requirements. Defaults to `Yes`.

1. Complete the remaining deployment steps.

The deploy-time validation custom resource runs before any solution resources are created. If your VPC does not meet the requirements, the stack fails with a descriptive error message identifying the specific issue. Correct the issue and then redeploy the stack.

## Common Validation Errors
<a name="byo-vpc-validation-errors"></a>

Validation runs as a CloudFormation custom resource in the **DeploymentBootstrapStack** nested stack, before any other solution resources are created. If validation fails, the stack rolls back with a `CREATE_FAILED` status.

To find the error message:

1. Open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/).

1. Select your main stack (for example, `SpatialDataManagement`).

1. Choose the **Events** tab and look for a `CREATE_FAILED` event on the resource named `DeploymentBootstrapStackNestedStack`.

1. Select that nested stack to open it.

1. In the nested stack’s **Events** tab, find the `CREATE_FAILED` event on the resource named `DeploymentValidation`. The **Status reason** column contains the descriptive error message.

Alternatively, use the AWS CLI:

```bash
aws cloudformation describe-stack-events \
  --stack-name $(aws cloudformation list-stack-resources \
    --stack-name SpatialDataManagement \
    --query 'StackResourceSummaries[?contains(LogicalResourceId, `DeploymentBootstrap`)].PhysicalResourceId' \
    --output text) \
  --query 'StackEvents[?ResourceStatus==`CREATE_FAILED`].[LogicalResourceId,ResourceStatusReason]' \
  --output table
```

Replace `SpatialDataManagement` with your stack name if different.

| Error message | Resolution |
| --- | --- |
|  `VPC vpc-xxx does not have DNS hostnames enabled`  | Enable DNS hostnames in your VPC settings |
|  `VPC vpc-xxx does not have DNS support enabled`  | Enable DNS resolution in your VPC settings |
|  `ExistingPrivateSubnetIds is required when ExistingVpcId is provided`  | Set the `ExistingPrivateSubnetIds` parameter with at least 2 private subnet IDs |
|  `ExistingOpenSearchVpcEndpointId is required when ExistingVpcId is provided`  | Create an Amazon OpenSearch Serverless VPC endpoint and provide its ID, or set `UseVpcEndpoints=No` to skip this requirement (OpenSearch will be publicly accessible) |
|  `Isolated subnets must span at least 2 AZs, found 1`  | Provide isolated subnet IDs in at least 2 distinct Availability Zones |
|  `Private subnets must span at least 2 AZs, found 1`  | Provide private subnet IDs in at least 2 distinct Availability Zones |
|  `Isolated subnet subnet-xxx has a 0.0.0.0/0 route — must have no internet egress`  | Remove the default route from the isolated subnet’s route table |
|  `Private subnet subnet-xxx has no internet route — ConnectorInvocation Lambda requires internet`  | Add a `0.0.0.0/0` route via a NAT gateway, Transit Gateway, or Virtual Private Gateway to the private subnet’s route table |
|  `NACL acl-xxx on isolated subnets blocks TCP 443 outbound to VPC CIDR (VPC endpoints)`  | Add an outbound rule allowing TCP 443 to the VPC CIDR to the isolated subnet network ACL |
|  `NACL acl-xxx on isolated subnets blocks TCP 443 inbound from VPC CIDR (VPC endpoints)`  | Add an inbound rule allowing TCP 443 from the VPC CIDR to the isolated subnet network ACL |
|  `NACL acl-xxx on isolated subnets blocks TCP ephemeral outbound to VPC CIDR (return traffic)`  | Add an outbound rule allowing TCP 1024–65535 to the VPC CIDR to the isolated subnet network ACL |
|  `NACL acl-xxx on isolated subnets blocks TCP ephemeral inbound from VPC CIDR (endpoint responses)`  | Add an inbound rule allowing TCP 1024–65535 from the VPC CIDR to the isolated subnet network ACL |
|  `NACL acl-xxx on private subnets blocks TCP 443 outbound to 0.0.0.0/0 (internet via NAT)`  | Add an outbound rule allowing TCP 443 to 0.0.0.0/0 to the private subnet network ACL |
|  `NACL acl-xxx on private subnets blocks TCP 443 inbound from VPC CIDR (VPC endpoints)`  | Add an inbound rule allowing TCP 443 from the VPC CIDR to the private subnet network ACL |
|  `NACL acl-xxx on private subnets blocks TCP ephemeral outbound to VPC CIDR (return traffic)`  | Add an outbound rule allowing TCP 1024–65535 to the VPC CIDR to the private subnet network ACL |
|  `NACL acl-xxx on private subnets blocks TCP ephemeral inbound from VPC CIDR (endpoint responses)`  | Add an inbound rule allowing TCP 1024–65535 from the VPC CIDR to the private subnet network ACL |
|  `NACL acl-xxx on private subnets blocks TCP ephemeral inbound from 0.0.0.0/0 (internet return traffic)`  | Add an inbound rule allowing TCP 1024–65535 from 0.0.0.0/0 to the private subnet network ACL |
|  `Missing required VPC endpoints in VPC vpc-xxx: sqs, kms`  | Create the listed VPC endpoints before deploying the solution |
|  `Gateway endpoint vpce-xxx (s3) is not associated with isolated subnet route tables`  | Associate the S3 or DynamoDB gateway endpoint with the route tables of your isolated subnets |
|  `VPC endpoint vpce-xxx has no security group allowing inbound TCP 443 from 10.0.0.0/16`  | Add an inbound rule allowing TCP 443 from the VPC CIDR to the endpoint’s security group |

## Immutability and Stack Updates
<a name="byo-vpc-immutability"></a>

Once deployed with an existing VPC, the following parameters are immutable and cannot be changed on a stack update:
+  `ExistingVpcId`
+  `ExistingVpcCidrBlock`
+  `ExistingIsolatedSubnetIds`
+  `ExistingPrivateSubnetIds`
+  `ExistingOpenSearchVpcEndpointId`

The `UseVpcEndpoints` parameter is **not** immutable — you can change it between `Yes` and `No` on stack updates. For example, you can start with `UseVpcEndpoints=No` during initial testing and later switch to `Yes` after creating VPC endpoints for production.

Attempting to change any of the immutable parameters causes the stack update to fail with a descriptive error. To change the VPC configuration, deploy a new stack.

When performing stack updates (for example, to upgrade the solution version), you do not need to re-enter these parameters — the solution persists the VPC configuration and resolves it automatically on updates.
