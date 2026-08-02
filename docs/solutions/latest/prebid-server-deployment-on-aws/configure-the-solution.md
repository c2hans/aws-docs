---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/configure-the-solution.html
---

# Configure the solution
<a name="configure-the-solution"></a>

This section provides instructions for configuring Guidance for Deploying a Prebid Server on AWS.

## Opting out of using CloudFront and AWS WAF
<a name="opt-out-of-cloudfront-and-waf"></a>

By default, this solution deploys CloudFront and AWS WAF.

### Benefits of using CloudFront and AWS WAF
<a name="cloudfront-waf-benefits"></a>

CloudFront helps reduce latency by delivering data through globally dispersed Points of Presence (PoPs) with automated network mapping and intelligent routing. It cuts costs with consolidated requests, customizable pricing options, and zero fees for data transfer out from AWS origins. CloudFront can cache objects and serve them directly to users (viewers), reducing the load on your Application Load Balancer.

The Application Load Balancer is conﬁgured to forward requests that contain a custom secret header value to enhance security. CloudFront automatically adds this custom HTTP header to the requests. This secret value is unique and is generated when you deploy the stack. For added protection, the Application Load Balancer security group is conﬁgured with the CloudFront managed preﬁx list. This contains the IP address ranges of all CloudFront globally distributed origin-facing servers. The CloudFront managed preﬁx list allows inbound traﬃc to your origin only from CloudFront origin-facing servers, preventing any non CloudFront traﬃc from reaching your origin.

AWS WAF provides additional security by preventing distributed denial of service (DDoS) and helps more easily monitor, block, or rate-limit common and pervasive bots. It improves web traﬃc visibility with granular control over how metrics are emitted.

### How to opt out
<a name="how-to-opt-out"></a>

For users who decide not to use CloudFront and AWS WAF with this solution, follow these steps:

1. Obtain an SSL server certificate for your domain by [requesting](https://docs.aws.amazon.com/acm/latest/userguide/acm-public-certificates.html) or [importing](https://docs.aws.amazon.com/acm/latest/userguide/import-certificate-api-cli.html) it in AWS Certificate Manager (ACM) in the same Region where you plan to launch your stack.

1. Validate the ACM certificate request by adding the required DNS CNAME record.

1. Before doing cdk deploy set the AWS CDK stack parameter **deploy\_cloudfront\_and\_waf\_param** in the file [stack\_cfn\_parameters.py](https://github.com/aws-solutions-library-samples/prebid-server-deployment-on-aws/tree/main/source/infrastructure/prebid_server/stack_cfn_parameters.py) to `No`.

1. Enter the SSL certificate ARN in AWS CDK stack parameter **ssl\_certificate\_param** .

1. After you deploy the stack, access the ALB DNS name from the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/), on the **Outputs** tab, from the value for **PrebidALBDNSName**.

1. Update your domain’s public hosted zone by creating a CNAME record that points to the ALB’s Fully Qualified Domain Name (FQDN) obtained in step 5.

## CloudFormation parameters
<a name="cloudformation-parameters"></a>

This section describes the CloudFormation parameters available for the PrebidServerStack and BidderSimulatorStack. These parameters are configured at deploy time via the `deploy.sh` script or directly through CloudFormation.

### PrebidServerStack parameters
<a name="prebidserverstack-parameters"></a>

The following table lists the CloudFormation parameters for the primary Prebid Server stack (`prebid-server-deployment-on-aws`).

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
|  `InstallCloudFrontAndWAF`  | String |  `Yes`  | Deploy CloudFront and AWS WAF for content delivery and DDoS protection. Set to `No` to use your own CDN (requires `SSLCertificateARN`). |
|  `SSLCertificateARN`  | String |  *(empty)*  | ARN of an SSL certificate in AWS Certificate Manager. Required only when `InstallCloudFrontAndWAF` is set to `No`. |
|  `ECSTaskMinCapacity`  | Number |  `2`  | Minimum number of ECS Fargate tasks for the Prebid Server service. Provides baseline redundancy. |
|  `ECSTaskMaxCapacity`  | Number |  `300`  | Maximum number of ECS Fargate tasks the service can scale to under load. |
|  `RequestsPerTargetThreshold`  | Number |  `5000`  | Number of requests per target that triggers ECS auto-scaling. Valid range: 100–10000. |
|  `SpotInstanceWeight`  | Number |  `1`  | Relative capacity weight for Fargate Spot instances. Set to `0` to use only on-demand capacity. |
|  `ContainerImageUri`  | String |  *(empty)*  | ECR image URI for the Prebid Server container. Leave empty to build from source during deployment. See [ContainerImageUri parameter](#container-image-parameter). |
|  `EnableLogAnalytics`  | String |  `false`  | Enable auction-level log analytics pipeline (EFS → DataSync → S3 → Glue ETL → Athena). Allowed values: `true`, `false`. |
|  `EnableRtbRequesterGateway`  | String |  `false`  | Provision an RTB Fabric Requester Gateway for partner connectivity. The Fabric Link lifecycle is managed by the `simulator-fabric-link.sh` script. Allowed values: `true`, `false`. |
|  `SimulatorVpcId`  | String |  *(empty)*  | VPC ID of the BidderSimulatorStack. Required for VPC peering connectivity mode. |
|  `SimulatorAlbSgId`  | String |  *(empty)*  | ALB Security Group ID from the BidderSimulatorStack. Allows traffic from PrebidServerStack VPC over VPC peering. |
|  `SimulatorRouteTableId1`  | String |  *(empty)*  | First private subnet route table ID from the BidderSimulatorStack VPC. Used for return traffic routing over VPC peering. |
|  `SimulatorRouteTableId2`  | String |  *(empty)*  | Second private subnet route table ID from the BidderSimulatorStack VPC. Used for return traffic routing over VPC peering. |
|  `SimulatorEndpoint`  | String |  *(empty)*  | Internal ALB DNS name of the bidder simulator. Used as the ECS bidder endpoint when VPC peering is the connectivity model. |

### BidderSimulatorStack parameters
<a name="biddersimulatorstack-parameters"></a>

The following table lists the CloudFormation parameters for the optional Bidder Simulator stack (`BiddingServerSimulator`).

| Parameter | Type | Default | Description |
| --- | --- | --- | --- |
|  `EnableRtbFabric`  | String |  `true`  | Deploy an RTB Fabric Responder Gateway in the simulator VPC. Set to `false` for VPC peering mode. Allowed values: `true`, `false`. |

### Connectivity modes
<a name="connectivity-modes"></a>

The solution supports two connectivity models between the Prebid Server and the Bidder Simulator (or partner bidders). Choose the appropriate mode based on your region and requirements.

#### RTB Fabric (recommended)
<a name="rtb-fabric-mode"></a>

RTB Fabric provides a private, low-latency network for real-time bidding traffic between a Requester Gateway (in the Prebid Server VPC) and a Responder Gateway (in the bidder VPC).

 **When to use:** Default mode. Use when deploying in an AWS Region that supports RTB Fabric.

 **How it works:**

1. Set `EnableRtbRequesterGateway=true` on PrebidServerStack to provision the Requester Gateway.

1. Set `EnableRtbFabric=true` on BidderSimulatorStack to provision the Responder Gateway.

1. After both stacks are deployed, the `simulator-fabric-link.sh` script creates a Fabric Link connecting the two gateways, waits for it to become active, and updates the ECS task definition with the link URL.

 **deploy.sh usage:**

```
./deploy.sh --deploy-bidding-simulator --simulator-connectivity rtb-fabric \
  --profile <profile> --region <region>
```

#### VPC peering (fallback)
<a name="vpc-peering-mode"></a>

VPC peering provides direct network connectivity between the Prebid Server VPC and the Bidder Simulator VPC using standard AWS VPC peering.

 **When to use:** Fallback for AWS Regions where RTB Fabric is not available.

 **How it works:**

1. Set `EnableRtbFabric=false` on BidderSimulatorStack (no Responder Gateway).

1. The `deploy.sh` script reads VPC peering parameters (VPC ID, ALB Security Group ID, route table IDs, and ALB endpoint) from BidderSimulatorStack outputs and passes them to PrebidServerStack.

1. PrebidServerStack creates the VPC peering connection, routes, and security group rules automatically.

 **deploy.sh usage:**

```
./deploy.sh --deploy-bidding-simulator --simulator-connectivity vpc-peering \
  --profile <profile> --region <region>
```

**Note**
The VPC peering parameters (`SimulatorVpcId`, `SimulatorAlbSgId`, `SimulatorRouteTableId1`, `SimulatorRouteTableId2`, `SimulatorEndpoint`) are populated automatically by `deploy.sh` when using `--simulator-connectivity vpc-peering`. You do not need to set them manually.

### ContainerImageUri parameter
<a name="container-image-parameter"></a>

The `ContainerImageUri` parameter controls how the Prebid Server container image is sourced.

| Value | Behavior |
| --- | --- |
|  *(empty, default)*  | The solution builds the Prebid Server container image from source during deployment. This is the standard CDK deployment path — CodeBuild compiles the Java application, builds the Docker image, and pushes it to ECR. |
| ECR image URI (e.g., `123456789012.dkr.ecr.us-east-1.amazonaws.com/prebid-server:latest`) | The solution uses the specified pre-built container image directly. No build step is performed. Use this when deploying via synthesized CloudFormation templates or when you have a custom Prebid Server image in ECR. |

 **Common use cases for ContainerImageUri:**
+  **Pre-built image from GitHub release** — The repository includes a pre-built container image at `deployment/container/prebid-server.tar.gz` (tracked via Git LFS). The `deploy.sh --container-image` flag loads this tar.gz, pushes it to ECR, and passes the resulting URI as `ContainerImageUri`.
+  **Custom Prebid Server build** — If you maintain a custom fork of Prebid Server Java with additional adapters or patches, build your image separately, push to ECR, and provide the URI.
+  **CloudFormation-only deployment** — When deploying the synthesized template directly (without CDK), provide a pre-existing ECR image URI since CodeBuild is not available in this path.

## Managing configuration files for the solution
<a name="manage-configuration-files-for-the-solution"></a>

This section provides detailed instructions for updating configuration files for the Prebid Server and restarting the cluster. It also covers file descriptions, recovery from configuration mistakes, and guidance on using the S3 bucket’s versioning feature for rollback.

### Finding the S3 bucket for prebid configuration files
<a name="finding-the-s3-bucket-for-prebid-configuration-files"></a>

The S3 bucket used for Prebid Server configuration files is created automatically by the stack. To locate the bucket where the configuration files are stored, follow these steps:

1.  **Access the CloudFormation stack outputs** - Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation).

1.  **Select the Prebid Server stack** - From the list of stacks, select the stack that is responsible for creating your Prebid Server environment.

1.  **View the outputs** - After selecting the stack, choose the **Outputs** tab.

1.  **Locate the S3 bucket link** - Find the **Output** entry that starts with `ContainerImagePrebidSolutionConfigBucket`. This output contains a direct link to the S3 bucket where the configuration files are stored.

1.  **Navigate to the S3 bucket** - Choose the link in the output to navigate to the root of the S3 bucket. From there, you see the folder structure containing the `default/` and `current/` configuration files.

After you locate the bucket, you can download, modify, and manage the Prebid Server configuration files as described in the following sections.

This S3 bucket is retained after the stack is deleted. To delete the bucket, see [Deleting the Amazon S3 buckets](uninstall-the-solution.md#deleting-the-amazon-s3-buckets)

### Making configuration changes
<a name="making-configuration-changes"></a>

When working with the Prebid Server, maintain separation between default and custom configurations. Make updates to the configuration files in the `/prebid-server/current/` folder in your S3 bucket, and never in the `/prebid-server/default/` folder. After you update the files, redeploy your cluster to apply the changes.

Important folders:
+  `default/` - Stores baseline configuration files for Prebid Server, which should not be modified.
+  `current/` - Used for custom configuration files that override the defaults.

### Updating configuration files and restarting the cluster
<a name="updating-configuration-files-and-restarting-the-cluster"></a>

1.  **Identify the configuration files to modify**

   1. Check the `/prebid-server/default/` folder in the S3 bucket for the baseline configuration files.

   1. Download the relevant file from the `/prebid-server/default/` folder to your workstation. You cannot modify the files directly in the S3 bucket.

1.  **Edit the configuration files**

   1. After you download the file to your workstation, make the required changes.

   1. Upload the modified file back to the `/prebid-server/current/` folder in your S3 bucket.

      Common configuration files include:
      +  `prebid-config.yaml` - Contains the main configuration settings for the Prebid Server instance.
      +  `prebid-logging.xml` - Manages logging levels and output formats for Prebid Server logs.
      +  `entrypoint.sh` - Custom script that initializes and launches the Prebid Server containers.

   For detailed information about how to configure Prebid Server, refer to the [Prebid Server Java Documentation](https://docs.prebid.org/prebid-server/overview/prebid-server-overview.html).

1.  **Document custom scripts**

   If you need to modify or add a script such as `entrypoint.sh` (which is custom), ensure that the following details are documented:

   1.  **Purpose** - What the script is used for (for example, starting services, managing environment variables).

   1.  **Usage** - Specific configurations, dependencies, or parameters used.

   1.  **Modification** - How to safely edit the script.

    **Example**: The `entrypoint.sh` script ensures that the necessary environment variables are set before starting the Prebid Server. It can be updated to handle different runtime configurations.

1.  **Test your changes in a test stack**

   Before applying changes to the production environment, test the configuration updates. Deploy a test stack in an AWS account to ensure that the changes work as expected, avoiding disruption to the production environment.

1.  **Deploy the custom configuration**

   After making and testing your changes, complete the following steps:

   1. Upload the updated files to the `/prebid-server/current/` folder in the S3 bucket.

   1. Force a redeployment of your ECS cluster by following [Amazon ECS documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-console-v2.html) for initiating a redeployment.

1.  **Verify the deployment**

   After you complete the redeployment, verify that the new configuration has been applied and that the Prebid Server is functioning as expected. Check the logs and monitor key metrics to ensure that no errors are occurring.

### Description of important files
<a name="description-of-important-files"></a>

1.  `prebid-config.yaml`

   Contains the core configuration for running Prebid Server. This file manages settings such as:
   + Bidder adapters
   + Server ports
   + Caching rules
   + Analytics adapters

   Refer to the [Prebid Server Configuration Guide](https://docs.prebid.org/prebid-server/hosting/pbs-hosting.html) for detailed usage instructions.

1.  `prebid-logging.xml`

   Defines logging levels and output destinations for Prebid Server logs. Adjustments to this file control the verbosity and detail of logging, critical for debugging and auditing purposes.

    **Example modification**: Change the logging level from `INFO` to `DEBUG` for troubleshooting.

   Documentation: [Prebid Server Logging](https://docs.prebid.org/prebid-server/endpoints/pbs-endpoint-admin.html#get-loggingchangelevel).

1.  `entrypoint.sh`

   This is the script responsible for initializing the Prebid Server container. It sets up environment variables, runs prerequisite commands, and starts the Prebid Server.

   Document custom steps or configurations made to this script.

1.  **Custom files**

   Document the custom files added to the `/current/` folder in terms of their purpose, usage, and changes that can be made.

### Configuring the analytics adapter
<a name="configuring-analytics-adapter"></a>

The solution includes a custom analytics adapter called `psdoaAnalytics` that provides detailed auction-level data collection. This adapter is configured in the `prebid-config.yaml` file.

 **Default Configuration**

By default, the analytics adapter is disabled. The configuration in `prebid-config.yaml` looks like this:

```
analytics:
  global:
    adapters: "psdoaAnalytics"
  psdoa:
    enabled: ${LOG_ANALYTICS_ENABLED}
```

 **Enabling the Analytics Adapter**

To enable the analytics adapter, you have two options:

1.  **During deployment** - Use the `--enable-log-analytics` flag when deploying with the `deploy.sh` script or set the CDK context `enableLogAnalytics=true` when using CDK directly.

1.  **After deployment** - Update the environment variable in the ECS task definition:

   1. Navigate to the Amazon ECS console and select your Prebid Server cluster.

   1. Update the task definition to set `LOG_ANALYTICS_ENABLED=true`.

   1. Force a new deployment of the ECS service to apply the changes.

 **Data Collection**

When enabled, the analytics adapter captures comprehensive auction data including:
+ Bid requests and responses
+ Winning bids and auction outcomes
+ Bidder performance metrics
+ Transaction details

This data is written to log files and processed through the same ETL pipeline as operational metrics, making it available for analysis through AWS Glue Data Catalog and Amazon Athena.

**Note**
Enabling the analytics adapter increases log volume and storage costs. The additional data provides valuable business intelligence but should be evaluated based on your analytics requirements and budget constraints.

### Recovering from a mistake in the config files
<a name="recovering-from-a-mistake-in-the-config-files"></a>

Mistakes in configuration files can lead to failed deployments or runtime errors. Because S3 bucket versioning is enabled, you can revert to previous configurations. See [How S3 Versioning works](https://docs.aws.amazon.com/AmazonS3/latest/userguide/versioning-workflows.html) for more information.

1.  **Identify the issue**

   Review the logs or errors generated during deployment. You can access logs through several methods:
   + Navigate to the **Logs** tab under the Prebid Amazon ECS service in the AWS Management Console to review consolidated output from all containers.
   + Navigate to a specific **Task** in Amazon ECS, and view the **Logs** tab for output from that specific container.
   + Check **CloudWatch Logs** in the log group named ` <STACK-NAME>-PrebidContainerLogGroup[.red]<ID> `. Use [Log Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/AnalyzingLogData.html) or [Live Tail](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CloudWatchLogs_LiveTail.html) to observe and search the logs.

     For more detailed instructions on how to access Amazon ECS and CloudWatch Logs, refer to the [Amazon ECS Logs documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_cloudwatch_logs.html).

1.  **Check S3 version history**

   Navigate to your S3 bucket and use versioning to locate the previous, stable version of the configuration file:

   1. Select the file from the `/current/` folder and enable the **Show versions** switch.

   1. Locate the correct version of the file before the mistake was introduced.

1.  **Restore the previous version**

   After you’ve identified the correct file version, restore it by selecting it and replacing the current file. You can also remove the problematic file from the `/current/` folder to allow the original file in the `/default/` folder to take precedence.

1.  **Redeploy the cluster**

   After restoring the stable version, follow the redeployment steps to update your Amazon ECS cluster with the corrected configuration.

#### Best practices for recovery
<a name="best-practices-for-recovery"></a>
+  **Backup** - Always create a backup of your current configuration before making any changes.
+  **Testing** - Test configurations in a test stack before applying changes to production.
+  **Document** - Keep detailed notes on the changes made, including the rationale behind the modifications, to simplify troubleshooting and rollback if needed.

By maintaining a clear separation between default and custom configurations and using S3 bucket versioning, you can safely and effectively update your Prebid Server setup. Always test thoroughly and document changes to ensure smooth deployments and easy recovery from any configuration issues.
