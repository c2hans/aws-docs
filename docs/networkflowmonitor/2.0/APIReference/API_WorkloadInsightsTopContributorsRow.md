---
source_url: https://docs.aws.amazon.com/networkflowmonitor/2.0/APIReference/API_WorkloadInsightsTopContributorsRow.html
---

# WorkloadInsightsTopContributorsRow
<a name="API_WorkloadInsightsTopContributorsRow"></a>

A row for a top contributor for a scope.

## Contents
<a name="API_WorkloadInsightsTopContributorsRow_Contents"></a>

 ** accountId **   <a name="networkflowmonitor-Type-WorkloadInsightsTopContributorsRow-accountId"></a>
The account ID for a specific row of data.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 12.
Pattern: `[0-9]{12}`
Required: No

 ** localAz **   <a name="networkflowmonitor-Type-WorkloadInsightsTopContributorsRow-localAz"></a>
The identifier for the Availability Zone where the local resource is located.
Type: String
Required: No

 ** localRegion **   <a name="networkflowmonitor-Type-WorkloadInsightsTopContributorsRow-localRegion"></a>
The AWS Region where the local resource is located.
Type: String
Required: No

 ** localSubnetArn **   <a name="networkflowmonitor-Type-WorkloadInsightsTopContributorsRow-localSubnetArn"></a>
The Amazon Resource Name (ARN) of a local subnet.
Type: String
Required: No

 ** localSubnetId **   <a name="networkflowmonitor-Type-WorkloadInsightsTopContributorsRow-localSubnetId"></a>
The subnet identifier for the local resource.
Type: String
Pattern: `subnet-[a-zA-Z0-9]{8,32}`
Required: No

 ** localVpcArn **   <a name="networkflowmonitor-Type-WorkloadInsightsTopContributorsRow-localVpcArn"></a>
The Amazon Resource Name (ARN) of a local VPC.
Type: String
Required: No

 ** localVpcId **   <a name="networkflowmonitor-Type-WorkloadInsightsTopContributorsRow-localVpcId"></a>
The identifier for the VPC for the local resource.
Type: String
Pattern: `vpc-[a-zA-Z0-9]{8,32}`
Required: No

 ** remoteIdentifier **   <a name="networkflowmonitor-Type-WorkloadInsightsTopContributorsRow-remoteIdentifier"></a>
The identifier of a remote resource. For a VPC or subnet, this identifier is the VPC Amazon Resource Name (ARN) or subnet ARN. For an Availability Zone, this identifier is the AZ name, for example, us-west-2b. For an AWS Region , this identifier is the Region name, for example, us-west-2.
Type: String
Required: No

 ** value **   <a name="networkflowmonitor-Type-WorkloadInsightsTopContributorsRow-value"></a>
The value for a metric.
Type: Long
Required: No

## See Also
<a name="API_WorkloadInsightsTopContributorsRow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkflowmonitor-2023-04-19/WorkloadInsightsTopContributorsRow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkflowmonitor-2023-04-19/WorkloadInsightsTopContributorsRow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkflowmonitor-2023-04-19/WorkloadInsightsTopContributorsRow)
