---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/deploy-the-solution.html
---

# Deploy the solution
<a name="deploy-the-solution"></a>

This solution uses [AWS CDK and stacks](https://docs.aws.amazon.com/cdk/v2/guide/home.html) to automate its deployment. The CDK code specifies the AWS resources included in this solution and their properties. The CDK stack provisions the resources that are described in the template.

**Important**
This solution includes an option to send anonymized operational metrics to AWS. We use this data to better understand how customers use this solution and related services and products. AWS owns the data gathered through this survey. Data collection is subject to the [AWS Privacy Notice](https://aws.amazon.com/privacy/).
To opt out of this feature, modify the CDK code before deploying. For more information, see the [Anonymized data collection](anonymized-data-collection.md) section of this guide.

## Prerequisites
<a name="prerequisties"></a>

You need an AWS account with permissions to deploy CDK stack and all the resources defined within the stack for this solution. The `AdministratorAccess` IAM policy, which provides full access to AWS services and resources is sufficient to deploy this solution.

## Deployment process overview
<a name="deployment-process-overview"></a>

Deploy the solution guidance using the AWS CDK stack available in the [Github repository](https://github.com/aws-solutions-library-samples/prebid-server-deployment-on-aws).

Before you launch the solution, review the [cost](cost1.md), [architecture](architecture-overview.md), [network security](security-1.md), and other considerations discussed earlier in this guide.

The solution consists of two CDK stacks:

1.  **Main Prebid Server Stack**: The core infrastructure for running Prebid Server (always deployed)

1.  **Bidder Simulator Stack**: An optional stack for quick start testing and validation

### Deployment methods
<a name="deployment-methods"></a>

 **Quick Deploy with deploy.sh (Recommended)**

For a streamlined deployment experience on Linux/macOS, use the provided `deploy.sh` script:

```
# Deploy Prebid Server only (no simulator)
./deploy.sh --profile <your-aws-cli-profile> --region <your-region>

# Deploy with bidder simulator (RTB Fabric connectivity — default)
./deploy.sh --deploy-bidding-simulator --profile <your-aws-cli-profile> --region <your-region>

# Deploy with bidder simulator (VPC peering fallback for non-RTB regions)
./deploy.sh --deploy-bidding-simulator --simulator-connectivity vpc-peering --profile <your-aws-cli-profile> --region <your-region>

# Deploy with RTB Fabric gateway for future partner onboarding (no simulator)
./deploy.sh --enable-rtb-requester-gateway --profile <your-aws-cli-profile> --region <your-region>

# Deploy with a pre-built container image (tar.gz)
./deploy.sh --container-image deployment/container/prebid-server.tar.gz --profile <your-aws-cli-profile> --region <your-region>

# Deploy with an existing ECR image URI
./deploy.sh --container-image 123456789012.dkr.ecr.us-east-1.amazonaws.com/prebid-server:latest --profile <your-aws-cli-profile> --region <your-region>

# Deploy with analytics enabled
./deploy.sh --enable-log-analytics --profile <your-aws-cli-profile> --region <your-region>

# Synthesize CloudFormation templates (no deployment)
./deploy.sh --synth --profile <your-aws-cli-profile> --region <your-region>
```

The `deploy.sh` script automatically:
+ Performs a two-step deployment when `--deploy-bidding-simulator` is used (BidderSimulatorStack first, then PrebidServerStack with outputs as parameters)
+ Copies AMT bidder files to the Docker build context for the simulator
+ Handles container image loading and ECR push when `--container-image` points to a tar.gz file
+ Creates the RTB Fabric Link via `simulator-fabric-link.sh` after deployment (when using RTB Fabric connectivity)
+ Sets up the Python virtual environment and installs dependencies

#### deploy.sh flags
<a name="deploy-sh-flags"></a>

| Flag | Default | Description |
| --- | --- | --- |
|  `--deploy-bidding-simulator`  |  `false`  | Deploy the optional BidderSimulatorStack for quick start testing. Triggers the two-step deployment flow. |
|  `--simulator-connectivity MODE`  |  `rtb-fabric`  | Connectivity model between Prebid Server and the bidder simulator. Values: `rtb-fabric` (default, uses AWS RTB Fabric) or `vpc-peering` (fallback for regions without RTB Fabric). |
|  `--enable-rtb-requester-gateway`  |  `false`  | Provision an RTB Fabric Requester Gateway in the PrebidServerStack for partner onboarding. Use this when you want the gateway without deploying the simulator. |
|  `--container-image PATH_OR_URI`  |  *(build from source)*  | Container image source. Accepts a local tar.gz file path (the script loads, tags, and pushes to ECR) or an existing ECR image URI. When omitted, CDK builds the container from source during deployment. |
|  `--enable-log-analytics`  |  `false`  | Enable the custom analytics adapter for detailed auction-level data collection through the ETL pipeline. |
|  `--profile PROFILE`  |  *(none)*  | AWS CLI profile to use for all AWS operations. |
|  `--region REGION`  |  *(none)*  | AWS region to deploy to. |
|  `--synth`  |  *(deploy)*  | Run `cdk synth` instead of `cdk deploy`. Generates CloudFormation templates without deploying. |

#### Two-step deployment flow
<a name="two-step-deployment"></a>

When `--deploy-bidding-simulator` is specified, `deploy.sh` performs a two-step deployment:

1.  **Step 1 — Deploy BidderSimulatorStack:** Deploys the bidder simulator infrastructure (VPC, ALB, Lambda bidder, and optionally the RTB Fabric Responder Gateway). The script reads CloudFormation outputs from this stack to configure the next step.

1.  **Step 2 — Deploy PrebidServerStack:** Deploys the core Prebid Server infrastructure, passing BidderSimulatorStack outputs as CloudFormation parameters (for example, `EnableRtbRequesterGateway=true` for RTB Fabric, or VPC peering parameters for the VPC peering path).

This ordering ensures that the PrebidServerStack receives the correct connectivity parameters from the already-deployed simulator stack.

#### RTB Fabric Link (post-deployment step)
<a name="fabric-link-post-deployment"></a>

When deploying with `--simulator-connectivity rtb-fabric` (the default), `deploy.sh` automatically runs `deployment/simulator-fabric-link.sh create` after both stacks are deployed. This script:
+ Creates an RTB Fabric Link between the Requester Gateway (PrebidServerStack) and the Responder Gateway (BidderSimulatorStack)
+ Polls the link status with exponential backoff until it becomes active
+ Accepts the link from the responder side (same-account simulator)
+ Updates the ECS task definition with the Fabric Link URL endpoint
+ Triggers a rolling ECS deployment (\~30 seconds)

The Fabric Link is managed independently of CloudFormation — no stack update is required. The link ID is persisted in AWS Systems Manager Parameter Store for lifecycle management.

You can also manage the Fabric Link manually:

```
# Check link status
./deployment/simulator-fabric-link.sh status --stack-name prebid-server-deployment-on-aws --profile <profile> --region <region>

# Delete the link (run before stack destruction)
./deployment/simulator-fabric-link.sh delete --stack-name prebid-server-deployment-on-aws --profile <profile> --region <region>
```

 **Manual Deployment with AWS CDK**

For customization or manual deployment:

```
cd source/infrastructure

# Bootstrap CDK (required once)
cdk bootstrap --cloudformation-execution-policies arn:aws:iam::aws:policy/AdministratorAccess

# Deploy Prebid Server only
cdk deploy prebid-server-deployment-on-aws --profile <your-aws-cli-profile> --region <your-region>

# Deploy with bidder simulator (two-step: deploy BSS first, then PSS with parameters)
cdk deploy BiddingServerSimulator --context deployBiddingSimulator=true --profile <your-aws-cli-profile> --region <your-region>
cdk deploy prebid-server-deployment-on-aws --context deployBiddingSimulator=true \
    --parameters prebid-server-deployment-on-aws:EnableRtbRequesterGateway=true \
    --profile <your-aws-cli-profile> --region <your-region>

# Deploy with analytics enabled
cdk deploy prebid-server-deployment-on-aws --context deployBiddingSimulator=true \
    --parameters prebid-server-deployment-on-aws:EnableLogAnalytics=true \
    --profile <your-aws-cli-profile> --region <your-region>
```

**Note**
When deploying manually with CDK, you must run `deployment/simulator-fabric-link.sh create` separately after deployment to establish the RTB Fabric Link.

For detailed deployment instructions and prerequisites, see the "Deployment Steps" section in the [Git repo readme](https://github.com/aws-solutions-library-samples/prebid-server-deployment-on-aws).

### Deployment options
<a name="deployment-options"></a>

 **Bidder Simulator (`--deploy-bidding-simulator`)**

Deploys an optional bidder simulator stack for quick start testing. The simulator includes:
+ Internal ALB \+ Lambda bidder
+ Support for banner and video ad formats (including VAST instream video)
+ Demo website with Prebid.js integration
+ Automatic AMT adapter configuration

When the simulator is deployed, `deploy.sh` uses a two-step deployment flow: BidderSimulatorStack deploys first, then PrebidServerStack receives the simulator outputs as CloudFormation parameters.

 **Simulator Connectivity (`--simulator-connectivity`)**

Controls how Prebid Server connects to the bidder simulator:
+  `rtb-fabric` (default) — Uses AWS RTB Fabric for low-latency, cost-optimized private network connectivity. Creates a Requester Gateway in the Prebid Server VPC and connects to the Responder Gateway in the Bidder Simulator VPC via a Fabric Link. The link is created automatically by `simulator-fabric-link.sh` after deployment.
+  `vpc-peering` — Uses VPC peering with direct routes and security group rules. Use this as a fallback for regions where RTB Fabric is not available.

 **RTB Requester Gateway (`--enable-rtb-requester-gateway`)**

Provisions an RTB Fabric Requester Gateway in the PrebidServerStack without deploying the simulator. Use this when you want to prepare the gateway for future partner onboarding. After deployment, create Fabric Links manually using the AWS CLI or `simulator-fabric-link.sh`.

 **Container Image (`--container-image`)**

Specifies a custom container image source instead of building from source during deployment:
+  **tar.gz file path** — The script loads the image into the local container runtime, creates an ECR repository, tags, and pushes the image. Example: `--container-image deployment/container/prebid-server.tar.gz`
+  **ECR URI** — Uses an existing image directly. Example: `--container-image 123456789012.dkr.ecr.us-east-1.amazonaws.com/prebid-server:latest`

 **Analytics Adapter (`--enable-log-analytics`)**

Enables the custom analytics adapter for detailed auction-level data collection. This provides comprehensive business intelligence data through the ETL pipeline.

You can view the status of the stack in the AWS CloudFormation console in the **Status** column. You should receive a CREATE\_COMPLETE status in approximately 10 minutes.

 **Time to deploy:** Approximately 10–15 minutes (varies based on optional components). When using RTB Fabric connectivity, the Fabric Link creation adds approximately 30–60 seconds after stack deployment.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Deploying a Prebid Server on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
