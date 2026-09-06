---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeVpcEndpointAssociations.html
---

# DescribeVpcEndpointAssociations
<a name="API_DescribeVpcEndpointAssociations"></a>

Describes the VPC resources, VPC endpoint services, Amazon Lattice services, or service networks associated with the VPC endpoint.

## Request Parameters
<a name="API_DescribeVpcEndpointAssociations_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `vpc-endpoint-id` - The ID of the VPC endpoint.
+  `associated-resource-accessibility` - The association state. When the state is `accessible`, it returns `AVAILABLE`. When the state is `inaccessible`, it returns `PENDING` or `FAILED`.
+  `association-id` - The ID of the VPC endpoint association.
+  `associated-resource-id` - The ID of the associated resource configuration.
+  `service-network-arn` - The Amazon Resource Name (ARN) of the associated service network. Only VPC endpoints of type service network will be returned.
+  `resource-configuration-group-arn` - The Amazon Resource Name (ARN) of the resource configuration of type GROUP.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **MaxResults**
The maximum page size.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 **NextToken**
The pagination token.
Type: String
Required: No

 **VpcEndpointId.N**
The IDs of the VPC endpoints.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeVpcEndpointAssociations_ResponseElements"></a>

The following elements are returned by the service.

 **nextToken**
The pagination token.
Type: String

 **requestId**
The ID of the request.
Type: String

 **vpcEndpointAssociationSet**
Details of the endpoint associations.
Type: Array of [VpcEndpointAssociation](API_VpcEndpointAssociation.md) objects

## Errors
<a name="API_DescribeVpcEndpointAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DescribeVpcEndpointAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeVpcEndpointAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeVpcEndpointAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeVpcEndpointAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeVpcEndpointAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeVpcEndpointAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeVpcEndpointAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeVpcEndpointAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeVpcEndpointAssociations)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeVpcEndpointAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeVpcEndpointAssociations)
