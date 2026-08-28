---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/use-the-solution.html
---

# Use the solution
<a name="use-the-solution"></a>

## Demo website
<a name="demo-website"></a>

The solution includes a demo website that demonstrates end-to-end integration with Prebid.js and provides a working example of banner and video ad units.

### Accessing the demo website
<a name="accessing-the-demo-website"></a>

After deploying the solution with the bidder simulator:

1. Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home?).

1. Locate the `BiddingServerSimulator` stack.

1. In the **Outputs** tab, find the `DemoWebsiteUrl` value.

1. Open the URL in your web browser to access the demo website.

The demo website includes:
+ Banner ad unit examples
+ Video ad unit examples with VAST instream video support
+ Integration with Prebid.js showing real-time bidding flow
+ Visual demonstration of ad rendering

For detailed information about the demo website implementation and customization options, see the [demo website README](https://github.com/aws-solutions-library-samples/prebid-server-deployment-on-aws/tree/main/source/loadtest/demo) in the GitHub repository.

## Managing RTB Fabric Links
<a name="managing-rtb-fabric-links"></a>

The solution includes a lifecycle management script (`deployment/simulator-fabric-link.sh`) that creates, deletes, and checks the status of RTB Fabric Links independently of CloudFormation stack operations. The script manages the link via direct API calls and persists the link ID in AWS Systems Manager Parameter Store.

**Note**
When you deploy with `deploy.sh --deploy-bidding-simulator --simulator-connectivity rtb-fabric`, the script runs automatically. Use the script directly when you need to manage the link independently of a full deployment.

### Script usage
<a name="simulator-fabric-link-usage"></a>

```
deployment/simulator-fabric-link.sh <subcommand> [options]
```

#### Subcommands
<a name="subcommands"></a>

| Subcommand | Description |
| --- | --- |
|  `create`  | Create a Fabric Link between the Requester Gateway (PrebidServerStack) and a Responder Gateway, wait for it to become active, accept it, and update the ECS task definition with the link URL. |
|  `delete`  | Delete an existing Fabric Link and remove the stored link ID from SSM Parameter Store. |
|  `status`  | Check the current status of the Fabric Link, including link state, URL, and gateway IDs. |

#### Options
<a name="options"></a>

| Option | Description |
| --- | --- |
|  `--stack-name NAME`  | PrebidServerStack name (required for all subcommands) |
|  `--responder-gateway-id ID`  | Responder Gateway ID (required for `create`) |
|  `--profile PROFILE`  | AWS CLI profile to use |
|  `--region REGION`  | AWS region |

#### Exit codes
<a name="exit-codes"></a>

| Code | Meaning |
| --- | --- |
|  `0`  | Success (or no link exists for `delete`/`status`) |
|  `1`  | General error (API failure, timeout, invalid arguments) |

### Create a Fabric Link
<a name="create-a-fabric-link"></a>

The `create` subcommand performs the following steps:

1. Retrieves the Requester Gateway ID and ECS cluster/service names from PrebidServerStack CloudFormation outputs.

1. Checks if a link already exists (via SSM parameter). If so, prints the current status and exits.

1. Calls the RTB Fabric CreateLink API.

1. Polls the link status with exponential backoff (5s → 10s → 20s → 30s cap, 5-minute timeout).

1. Accepts the link from the responder side once it becomes active.

1. Stores the link ID in SSM Parameter Store at `/{stack-name}/fabric-link/link-id`.

1. Registers a new ECS task definition revision with the link URL as the `AMT_BIDDING_SERVER_SIMULATOR_ENDPOINT` environment variable.

1. Updates the ECS service to trigger a rolling deployment (\~30 seconds).

1. Outputs the link URL to stdout.

```
# Create a Fabric Link for the simulator
deployment/simulator-fabric-link.sh create \
    --stack-name prebid-server-deployment-on-aws \
    --responder-gateway-id rgw-abc123def456 \
    --profile my-profile \
    --region us-east-1
```

### Delete a Fabric Link
<a name="delete-a-fabric-link"></a>

The `delete` subcommand reads the link ID from SSM Parameter Store and calls the RTB Fabric DeleteLink API. If no link exists, it exits cleanly with code 0.

```
# Delete the Fabric Link
deployment/simulator-fabric-link.sh delete \
    --stack-name prebid-server-deployment-on-aws \
    --profile my-profile \
    --region us-east-1
```

**Note**
The `delete` subcommand does not update the ECS task definition. The next `deploy.sh` run or `create` invocation resets the environment variable.

### Check Fabric Link status
<a name="check-fabric-link-status"></a>

The `status` subcommand retrieves the link ID from SSM Parameter Store and displays the current link state, URL, and gateway IDs.

```
# Check link status
deployment/simulator-fabric-link.sh status \
    --stack-name prebid-server-deployment-on-aws \
    --profile my-profile \
    --region us-east-1
```

If no Fabric Link is configured, the script prints an informational message and exits with code 0.

## Partner onboarding (manual steps)
<a name="partner-onboarding"></a>

For production partner integrations, Fabric Links are created manually rather than through the simulator script. The `simulator-fabric-link.sh` script is scoped to the same-account bidder simulator only.

To onboard a partner bidder via RTB Fabric:

1.  **Create the Fabric Link**

   Use the AWS CLI to create a link from your Requester Gateway to the partner’s Responder Gateway:

   ```
   aws rtbfabric create-link \
       --gateway-id <your-requester-gateway-id> \
       --peer-gateway-id <partner-responder-gateway-id> \
       --region us-east-1
   ```

1.  **Share the link ID with the partner**

   Provide the link ID to the partner so they can accept the link from their account. The link remains in `PENDING_ACCEPTANCE` state until the partner accepts.

1.  **Partner accepts the link**

   The partner runs the following command from their AWS account:

   ```
   aws rtbfabric accept-link \
       --link-id <link-id> \
       --gateway-id <partner-responder-gateway-id> \
       --region us-east-1
   ```

1.  **Update Prebid Server configuration**

   After the link becomes active, retrieve the link URL and update `prebid-config.yaml` in the S3 configuration bucket:

   ```
   # Get the requester gateway domain
   DOMAIN=$(aws rtbfabric get-requester-gateway \
       --gateway-id <your-requester-gateway-id> \
       --query 'RequesterGateway.Domain' \
       --output text \
       --region us-east-1)

   # Construct the link URL
   LINK_URL="https://${DOMAIN}/link/<link-id>"
   ```

   Add the partner’s bid adapter configuration to `prebid-config.yaml` with the link URL as the endpoint, then upload the updated file to the S3 configuration bucket.

1.  **Force ECS redeployment**

   Trigger a rolling deployment so ECS tasks pick up the updated configuration:

   ```
   aws ecs update-service \
       --cluster <ecs-cluster-name> \
       --service <ecs-service-name> \
       --force-new-deployment \
       --region us-east-1
   ```

**Tip**
You can find the ECS cluster and service names in the PrebidServerStack CloudFormation outputs (`EcsClusterName` and `EcsServiceName`).

## Container image customization
<a name="container-image-customization"></a>

The solution supports three paths for providing the Prebid Server container image.

### Option 1: Use the pre-built container image (tar.gz)
<a name="use-pre-built-image"></a>

The GitHub repository includes a pre-built container image at `deployment/container/prebid-server.tar.gz`, tracked via Git LFS.

```
# Ensure Git LFS is installed (required to download the binary)
git lfs install
git lfs pull

# Deploy using the pre-built image
./deploy.sh \
    --container-image deployment/container/prebid-server.tar.gz \
    --profile my-profile \
    --region us-east-1
```

The deploy script automatically loads the tar.gz into the local container runtime, pushes it to ECR, and passes the ECR URI to the CloudFormation stack.

**Note**
Without Git LFS installed, the tar.gz file is a small pointer file. Run `git lfs pull` to download the actual binary.

### Option 2: Build from source (default)
<a name="build-from-source"></a>

When no `--container-image` option is provided, the deploy script builds the container image from source using the Dockerfile at `deployment/ecr/prebid-server/Dockerfile`. This is the default behavior.

```
# Build from source (default — no --container-image flag)
./deploy.sh \
    --deploy-bidding-simulator \
    --profile my-profile \
    --region us-east-1
```

This path requires a running container runtime (Docker or Finch) and builds the image during CDK deployment.

### Option 3: Use an existing ECR image URI
<a name="use-existing-ecr-uri"></a>

If you maintain your own container registry or have a custom Prebid Server image, pass the full ECR URI directly:

```
./deploy.sh \
    --container-image 123456789012.dkr.ecr.us-east-1.amazonaws.com/prebid-server:v1.2.0 \
    --profile my-profile \
    --region us-east-1
```

The deploy script skips the container build step and passes the URI directly to the CloudFormation `ContainerImage` parameter.

## Testing RTB Fabric connectivity
<a name="testing-rtb-fabric-connectivity"></a>

After deploying the solution with RTB Fabric integration, you can verify that bid requests are being routed through the AWS RTB Fabric private network.

### Verify Fabric Link status
<a name="verify-fabric-link-status"></a>

Use the `status` subcommand to check the link state:

```
deployment/simulator-fabric-link.sh status \
    --stack-name prebid-server-deployment-on-aws \
    --profile my-profile \
    --region us-east-1
```

Alternatively, verify via the console:

1. Sign in to the [AWS RTB Fabric console](https://console.aws.amazon.com/rtbfabric/home?).

1. Navigate to **Fabric Links** in the left navigation pane.

1. Locate the Fabric Link created by the solution (named with your stack name prefix).

1. Verify the link status is **Active**.

### Monitor RTB Fabric metrics
<a name="monitor-rtb-fabric-metrics"></a>

RTB Fabric provides CloudWatch metrics for monitoring traffic through the Fabric Link:

1. Sign in to the [Amazon CloudWatch console](https://console.aws.amazon.com/cloudwatch/home?).

1. Navigate to **Metrics** > **All metrics**.

1. Select the **RTBFabric** namespace.

1. View metrics such as:
   +  `RequestCount` - Number of bid requests sent through the Fabric Link
   +  `DataTransferred` - Amount of data transferred through the link
   +  `Latency` - Request latency through the Fabric Link

## Querying metrics with Athena
<a name="querying-metrics-with-athena"></a>

Metrics collected from the Prebid Server application running on ECS are stored in the `MetricsEtl` S3 bucket for querying with Athena.

This section details information on the [metric definitions](metric-definitions.md), [Glue table schemas](glue-table-schemas.md), and [example queries](example-queries.md) to get started.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Deploying a Prebid Server on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
