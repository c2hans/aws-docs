---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/plan-your-deployment.html
---

# Plan your deployment
<a name="plan-your-deployment"></a>

This section describes the [prerequisites](prerequisites.md), [cost](cost1.md), [configurations for ECS Auto Scaling](configurations-for-elastic.md), [security](security-1.md), [Region](#supported-aws-regions), [deployment scenarios](#deployment-scenarios), and [quota](quotas.md) considerations for planning your deployment.

## Supported AWS Regions
<a name="supported-aws-regions"></a>

Prebid Server on AWS is supported in the following AWS Regions:

| Region name |  |
| --- | --- |
| US East (Ohio) | Asia Pacific (Tokyo) |
| US East (N. Virginia) | Canada (Central) |
| US West (Northern California) | Europe (Frankfurt) |
| US West (Oregon) | Europe (Ireland) |
| Asia Pacific (Mumbai) | Europe (London) |
| Asia Pacific (Osaka) | Europe (Paris) |
| Asia Pacific (Seoul) | Europe (Stockholm) |
| Asia Pacific (Singapore) | South America (São Paulo) |
| Asia Pacific (Sydney) |  |

## Deployment scenarios
<a name="deployment-scenarios"></a>

This solution supports multiple deployment modes depending on your connectivity requirements and whether you are deploying the optional bidder simulator. The following table summarizes the available scenarios and the corresponding `deploy.sh` flags.

| Scenario | Description | deploy.sh flags | Connectivity |
| --- | --- | --- | --- |
| Prebid Server only | Deploy the core Prebid Server stack without a bidder simulator. Bidders are reached via the public internet through NAT Gateways. |  `--profile <p> --region <r>`  | Public internet (NAT Gateway) |
| Prebid Server \+ Simulator (RTB Fabric) | Deploy both stacks with RTB Fabric connectivity. The `simulator-fabric-link.sh` script creates and manages the Fabric Link after deployment. |  `--deploy-bidding-simulator --simulator-connectivity rtb-fabric --profile <p> --region <r>`  | RTB Fabric (Requester Gateway → Fabric Link → Responder Gateway) |
| Prebid Server \+ Simulator (VPC peering) | Deploy both stacks with VPC peering connectivity. Use this mode in Regions where RTB Fabric is not available. |  `--deploy-bidding-simulator --simulator-connectivity vpc-peering --profile <p> --region <r>`  | VPC peering (direct network path) |
| Existing container image | Deploy with a container image that you built earlier, instead of building the image during deployment. |  `--container-image <ecr-image-uri-or-tar-gz-path> --profile <p> --region <r>`  | Any (combine with other flags) |

**Note**
The `--container-image` flag can be combined with any other deployment scenario. It accepts a path to a container image `tar.gz` file or an existing Amazon ECR image URI. For a `tar.gz` file, the script loads the image, creates the `prebid-server-on-aws` Amazon ECR repository if it doesn’t exist, and pushes the image. In both cases, the script sets the `ContainerImage` parameter to the image URI, and the ECS task definition uses that image instead of one built from source.
