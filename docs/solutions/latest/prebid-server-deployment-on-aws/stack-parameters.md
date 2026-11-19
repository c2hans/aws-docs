---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/stack-parameters.html
---

# CloudFormation Stack Parameters

The following table lists the CloudFormation parameters for the PrebidServerStack.

| Parameter | Default | Description |
| --- | --- | --- |
|  **InstallCloudFrontAndWAF**  |  `Yes`  | Specifies whether to deploy a CloudFront distribution and AWS WAF. If set to `Yes`, the solution creates and configures a CloudFront distribution to serve your content. If set to `No`, provide your own SSL certificate. |
|  **SSLCertificateARN**  |  *(empty)*  | The ARN of an SSL certificate in AWS Certificate Manager associated with a domain name. Only required if **InstallCloudFrontAndWAF** is set to `No`. |
|  **ECSTaskMinCapacity**  |  `2`  | The minimum number of running tasks that Amazon ECS maintains for the Prebid Server service during autoscaling. |
|  **ECSTaskMaxCapacity**  |  `300`  | The maximum number of running tasks that Amazon ECS maintains for the Prebid Server service during autoscaling. |
|  **RequestsPerTargetThreshold**  |  `5000`  | The number of requests per target to trigger scaling up the Prebid Server ECS service. |
|  **SpotInstanceWeight**  |  `1`  | Spot instance weight configuration (on-demand weight fixed at 1). |
|  **ContainerImageUri**  |  *(empty)*  | Reserved. This parameter is declared in the template but this version of the solution does not use its value. To deploy a pre-built or custom container image, use `deploy.sh --container-image`, which sets the `ContainerImage` parameter. See [Container image configuration](configure-the-solution.md#container-image-parameter). |
|  **EnableRtbRequesterGateway**  |  `false`  | When `true`, provisions an RTB Fabric Requester Gateway in the Prebid Server VPC. Required for RTB Fabric connectivity (set automatically by `deploy.sh` when using `--simulator-connectivity rtb-fabric`). |
|  **EnableLogAnalytics**  |  `false`  | When `true`, enables the custom analytics adapter for auction-level data collection through the ETL pipeline. |
|  **SimulatorEndpoint**  |  *(empty)*  | The bidder simulator ALB endpoint URL for VPC peering connectivity. Set automatically by `deploy.sh` when using `--simulator-connectivity vpc-peering`. |
|  **SimulatorVpcId**  |  *(empty)*  | The VPC ID of the bidder simulator, for VPC peering connectivity. Set automatically by `deploy.sh` when using `--simulator-connectivity vpc-peering`. |
|  **SimulatorAlbSgId**  |  *(empty)*  | The security group ID of the bidder simulator ALB, for VPC peering connectivity. Set automatically by `deploy.sh` when using `--simulator-connectivity vpc-peering`. |
|  **SimulatorRouteTableId1**  |  *(empty)*  | The first private route table ID in the bidder simulator VPC, for VPC peering connectivity. Set automatically by `deploy.sh` when using `--simulator-connectivity vpc-peering`. |
|  **SimulatorRouteTableId2**  |  *(empty)*  | The second private route table ID in the bidder simulator VPC, for VPC peering connectivity. Set automatically by `deploy.sh` when using `--simulator-connectivity vpc-peering`. |

For the parameters of the BidderSimulatorStack, see [BidderSimulatorStack parameters](configure-the-solution.md#biddersimulatorstack-parameters).

**Note**
The `deploy.sh` script sets these parameters automatically based on the flags you provide. You only need to set parameters manually when using `cdk deploy` directly.

**Note**
CloudFront distribution is the recommended configuration for this solution because this configuration provides enhanced security and performance. Refer to the [Opt out of using CloudFront and AWS WAF](configure-the-solution.md#opt-out-of-cloudfront-and-waf) section for more information about the benefits of using CloudFront and AWS WAF together, and steps to disable CloudFront and AWS WAF if desired.
