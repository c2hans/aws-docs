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
| Pre-built container image | Deploy using the pre-built container image from the repository instead of building from source. Requires Git LFS. |  `--container-image deployment/container/prebid-server.tar.gz --profile <p> --region <r>`  | Any (combine with other flags) |

**Note**
The `--container-image` flag can be combined with any other deployment scenario. When specified, the script loads the container tar.gz, pushes it to ECR, and uses it for the ECS task definition instead of building from the Dockerfile.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Deploying a Prebid Server on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
