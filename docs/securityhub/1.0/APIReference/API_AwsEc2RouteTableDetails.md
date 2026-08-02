---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEc2RouteTableDetails.html
---

# AwsEc2RouteTableDetails
<a name="API_AwsEc2RouteTableDetails"></a>

 Provides details about a route table for the specified VPC.

## Contents
<a name="API_AwsEc2RouteTableDetails_Contents"></a>

 ** AssociationSet **   <a name="securityhub-Type-AwsEc2RouteTableDetails-AssociationSet"></a>
 The associations between a route table and one or more subnets or a gateway.
Type: Array of [AssociationSetDetails](API_AssociationSetDetails.md) objects
Required: No

 ** OwnerId **   <a name="securityhub-Type-AwsEc2RouteTableDetails-OwnerId"></a>
 The ID of the AWS account that owns the route table.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PropagatingVgwSet **   <a name="securityhub-Type-AwsEc2RouteTableDetails-PropagatingVgwSet"></a>
 Describes a virtual private gateway propagating route.
Type: Array of [PropagatingVgwSetDetails](API_PropagatingVgwSetDetails.md) objects
Required: No

 ** RouteSet **   <a name="securityhub-Type-AwsEc2RouteTableDetails-RouteSet"></a>
 The routes in the route table.
Type: Array of [RouteSetDetails](API_RouteSetDetails.md) objects
Required: No

 ** RouteTableId **   <a name="securityhub-Type-AwsEc2RouteTableDetails-RouteTableId"></a>
 The ID of the route table.
Type: String
Pattern: `.*\S.*`
Required: No

 ** VpcId **   <a name="securityhub-Type-AwsEc2RouteTableDetails-VpcId"></a>
 The ID of the virtual private cloud (VPC).
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEc2RouteTableDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEc2RouteTableDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEc2RouteTableDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEc2RouteTableDetails)
