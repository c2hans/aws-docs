---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetIpamInternetRegistryAssociationCidrs.html
---

# GetIpamInternetRegistryAssociationCidrs
<a name="API_GetIpamInternetRegistryAssociationCidrs"></a>

Retrieves IP address CIDRs registered with an internet registry for an IPAM internet registry association. We recommend using pagination to ensure that the operation returns quickly and successfully.

## Request Parameters
<a name="API_GetIpamInternetRegistryAssociationCidrs_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters to apply to the results.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **IpamInternetRegistryAssociationId**
The ID of the IPAM internet registry association.
Type: String
Required: Yes

 **MaxResults**
The maximum number of results to return in a single call. If not specified, all available results are returned. To retrieve the remaining results, make another call with the returned `nextToken` value.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 1000.
Required: No

 **NextToken**
The token for the next page of results.
Type: String
Required: No

## Response Elements
<a name="API_GetIpamInternetRegistryAssociationCidrs_ResponseElements"></a>

The following elements are returned by the service.

 **ipamInternetRegistryAssociationCidrSet**
The CIDRs registered with the internet registry.
Type: Array of [IpamInternetRegistryAssociationCidr](API_IpamInternetRegistryAssociationCidr.md) objects

 **nextToken**
The token to use to retrieve the next page of results.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_GetIpamInternetRegistryAssociationCidrs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetIpamInternetRegistryAssociationCidrs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetIpamInternetRegistryAssociationCidrs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetIpamInternetRegistryAssociationCidrs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetIpamInternetRegistryAssociationCidrs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetIpamInternetRegistryAssociationCidrs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetIpamInternetRegistryAssociationCidrs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetIpamInternetRegistryAssociationCidrs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetIpamInternetRegistryAssociationCidrs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetIpamInternetRegistryAssociationCidrs)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetIpamInternetRegistryAssociationCidrs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetIpamInternetRegistryAssociationCidrs)
