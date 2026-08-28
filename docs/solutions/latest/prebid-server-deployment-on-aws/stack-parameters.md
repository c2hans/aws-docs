---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/stack-parameters.html
---

# CloudFormation Stack Parameters
<a name="stack-parameters"></a>

The following table lists the CloudFormation parameters for the PrebidServerStack.

| Parameter | Default | Description |
| --- | --- | --- |
|  **InstallCloudFrontAndWAF**  |  `Yes`  | Specifies whether to deploy a CloudFront distribution and AWS WAF. If set to `Yes`, the solution creates and configures a CloudFront distribution to serve your content. If set to `No`, provide your own SSL certificate. |
|  **SSLCertificateARN**  |  *(empty)*  | The ARN of an SSL certificate in AWS Certificate Manager associated with a domain name. Only required if **InstallCloudFrontAndWAF** is set to `No`. |
|  **ECSTaskMinCapacity**  |  `2`  | The minimum number of running tasks that Amazon ECS maintains for the Prebid Server service during autoscaling. |
|  **ECSTaskMaxCapacity**  |  `300`  | The maximum number of running tasks that Amazon ECS maintains for the Prebid Server service during autoscaling. |
|  **RequestsPerTargetThreshold**  |  `5000`  | The number of requests per target to trigger scaling up the Prebid Server ECS service. |
|  **SpotInstanceWeight**  |  `1`  | Spot instance weight configuration (on-demand weight fixed at 1). |
|  **ContainerImageUri**  |  *(empty)*  | An ECR image URI to use instead of building the container from source. When empty, CDK builds the Prebid Server container image during deployment. |
|  **EnableRtbRequesterGateway**  |  `false`  | When `true`, provisions an RTB Fabric Requester Gateway in the Prebid Server VPC. Required for RTB Fabric connectivity (set automatically by `deploy.sh` when using `--simulator-connectivity rtb-fabric`). |
|  **EnableLogAnalytics**  |  `false`  | When `true`, enables the custom analytics adapter for auction-level data collection through the ETL pipeline. |
|  **SimulatorEndpoint**  |  *(empty)*  | The bidder simulator ALB endpoint URL for VPC peering connectivity. Set automatically by `deploy.sh` when using `--simulator-connectivity vpc-peering`. |

**Note**
The `deploy.sh` script sets these parameters automatically based on the flags you provide. You only need to set parameters manually when using `cdk deploy` directly.

**Note**
CloudFront distribution is the recommended configuration for this solution because this configuration provides enhanced security and performance. Refer to the [Opt out of using CloudFront and AWS WAF](configure-the-solution.md#opt-out-of-cloudfront-and-waf) section for more information about the benefits of using CloudFront and AWS WAF together, and steps to disable CloudFront and AWS WAF if desired.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Deploying a Prebid Server on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
