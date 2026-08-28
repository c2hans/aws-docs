---
source_url: https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_MonitorTopContributorsRow.html
---

# MonitorTopContributorsRow
<a name="API_MonitorTopContributorsRow"></a>

A set of information for a top contributor network flow in a monitor. In a monitor, Network Flow Monitor returns information about the network flows for top contributors for each metric. Top contributors are network flows with the top values for each metric type.

## Contents
<a name="API_MonitorTopContributorsRow_Contents"></a>

 ** destinationCategory **   <a name="networkflowmonitor-Type-MonitorTopContributorsRow-destinationCategory"></a>
The destination category for a top contributors row. Destination categories can be one of the following:
+  `INTRA_AZ`: Top contributor network flows within a single Availability Zone
+  `INTER_AZ`: Top contributor network flows between Availability Zones
+  `INTER_REGION`: Top contributor network flows between Regions (to the edge of another Region)
+  `INTER_VPC`: Top contributor network flows between VPCs
+  `AWS_SERVICES`: Top contributor network flows to or from AWS services
+  `UNCLASSIFIED`: Top contributor network flows that do not have a bucket classification
Type: String
Valid Values: `INTRA_AZ | INTER_AZ | INTER_VPC | UNCLASSIFIED | AMAZON_S3 | AMAZON_DYNAMODB | INTER_REGION`
Required: No

 ** dnatIp **   <a name="networkflowmonitor-Type-MonitorTopContributorsRow-dnatIp"></a>
The destination network address translation (DNAT) IP address for a top contributor network flow.
Type: String
Required: No

 ** kubernetesMetadata **   <a name="networkflowmonitor-Type-MonitorTopContributorsRow-kubernetesMetadata"></a>
Meta data about Kubernetes resources.
Type: [KubernetesMetadata](API_KubernetesMetadata.md) object
Required: No

 ** localAz **   <a name="networkflowmonitor-Type-MonitorTopContributorsRow-localAz"></a>
The Availability Zone for the local resource for a top contributor network flow.
Type: String
Required: No

 ** localInstanceArn **   <a name="networkflowmonitor-Type-MonitorTopContributorsRow-localInstanceArn"></a>
The Amazon Resource Name (ARN) of a local resource.
Type: String
Required: No

 ** localInstanceId **   <a name="networkflowmonitor-Type-MonitorTopContributorsRow-localInstanceId"></a>
The instance identifier for the local resource for a top contributor network flow.
Type: String
Pattern: `i-[a-zA-Z0-9]{8,32}`
Required: No

 ** localIp **   <a name="networkflowmonitor-Type-MonitorTopContributorsRow-localIp"></a>
The IP address of the local resource for a top contributor network flow.
Type: String
Required: No

 ** localRegion **   <a name="networkflowmonitor-Type-MonitorTopContributorsRow-localRegion"></a>
The AWS Region for the local resource for a top contributor network flow.
Type: String
Required: No

 ** localSubnetArn **   <a name="networkflowmonitor-Type-MonitorTopContributorsRow-localSubnetArn"></a>
The Amazon Resource Name (ARN) of a local subnet.
Type: String
Required: No

 ** localSubnetId **   <a name="networkflowmonitor-Type-MonitorTopContributorsRow-localSubnetId"></a>
The subnet ID for the local resource for a top contributor network flow.
Type: String
Pattern: `subnet-[a-zA-Z0-9]{8,32}`
Required: No

 ** localVpcArn **   <a name="networkflowmonitor-Type-MonitorTopContributorsRow-localVpcArn"></a>
The Amazon Resource Name (ARN) of a local VPC.
Type: String
Required: No

 ** localVpcId **   <a name="networkflowmonitor-Type-MonitorTopContributorsRow-localVpcId"></a>
The VPC ID for a top contributor network flow for the local resource.
Type: String
Pattern: `vpc-[a-zA-Z0-9]{8,32}`
Required: No

 ** remoteAz **   <a name="networkflowmonitor-Type-MonitorTopContributorsRow-remoteAz"></a>
The Availability Zone for the remote resource for a top contributor network flow.
Type: String
Required: No

 ** remoteInstanceArn **   <a name="networkflowmonitor-Type-MonitorTopContributorsRow-remoteInstanceArn"></a>
The Amazon Resource Name (ARN) of a remote resource.
Type: String
Required: No

 ** remoteInstanceId **   <a name="networkflowmonitor-Type-MonitorTopContributorsRow-remoteInstanceId"></a>
The instance identifier for the remote resource for a top contributor network flow.
Type: String
Pattern: `i-[a-zA-Z0-9]{8,32}`
Required: No

 ** remoteIp **   <a name="networkflowmonitor-Type-MonitorTopContributorsRow-remoteIp"></a>
The IP address of the remote resource for a top contributor network flow.
Type: String
Required: No

 ** remoteRegion **   <a name="networkflowmonitor-Type-MonitorTopContributorsRow-remoteRegion"></a>
The AWS Region for the remote resource for a top contributor network flow.
Type: String
Required: No

 ** remoteSubnetArn **   <a name="networkflowmonitor-Type-MonitorTopContributorsRow-remoteSubnetArn"></a>
The Amazon Resource Name (ARN) of a remote subnet.
Type: String
Required: No

 ** remoteSubnetId **   <a name="networkflowmonitor-Type-MonitorTopContributorsRow-remoteSubnetId"></a>
The subnet ID for the remote resource for a top contributor network flow.
Type: String
Pattern: `subnet-[a-zA-Z0-9]{8,32}`
Required: No

 ** remoteVpcArn **   <a name="networkflowmonitor-Type-MonitorTopContributorsRow-remoteVpcArn"></a>
The Amazon Resource Name (ARN) of a remote VPC.
Type: String
Required: No

 ** remoteVpcId **   <a name="networkflowmonitor-Type-MonitorTopContributorsRow-remoteVpcId"></a>
The VPC ID for a top contributor network flow for the remote resource.
Type: String
Pattern: `vpc-[a-zA-Z0-9]{8,32}`
Required: No

 ** snatIp **   <a name="networkflowmonitor-Type-MonitorTopContributorsRow-snatIp"></a>
The secure network address translation (SNAT) IP address for a top contributor network flow.
Type: String
Required: No

 ** targetPort **   <a name="networkflowmonitor-Type-MonitorTopContributorsRow-targetPort"></a>
The target port.
Type: Integer
Required: No

 ** traversedConstructs **   <a name="networkflowmonitor-Type-MonitorTopContributorsRow-traversedConstructs"></a>
The constructs traversed by a network flow.
Type: Array of [TraversedComponent](API_TraversedComponent.md) objects
Required: No

 ** value **   <a name="networkflowmonitor-Type-MonitorTopContributorsRow-value"></a>
The value of the metric for a top contributor network flow.
Type: Long
Required: No

## See Also
<a name="API_MonitorTopContributorsRow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkflowmonitor-2023-04-19/MonitorTopContributorsRow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkflowmonitor-2023-04-19/MonitorTopContributorsRow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkflowmonitor-2023-04-19/MonitorTopContributorsRow)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Network Flow Monitor. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query networkflowmonitor` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
