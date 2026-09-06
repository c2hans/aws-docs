---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetIpamRouteProtectionFindings.html
---

# GetIpamRouteProtectionFindings
<a name="API_GetIpamRouteProtectionFindings"></a>

Retrieves route protection findings for an IPAM. Route protection findings show the Resource Public Key Infrastructure (RPKI) validation status of your Bring Your Own IP (BYOIP) routes. Findings identify routes that have valid, invalid, or unknown validation states. We recommend using pagination to ensure that the operation returns quickly and successfully.

## Request Parameters
<a name="API_GetIpamRouteProtectionFindings_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
One or more filters to apply to the results.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **IpamId**
The ID of the IPAM to retrieve route protection findings for.
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
<a name="API_GetIpamRouteProtectionFindings_ResponseElements"></a>

The following elements are returned by the service.

 **ipamId**
The ID of the IPAM.
Type: String

 **nextToken**
The token to use to retrieve the next page of results.
Type: String

 **requestId**
The ID of the request.
Type: String

 **routeProtectionFindingSet**
The route protection findings.
Type: Array of [IpamRouteProtectionFinding](API_IpamRouteProtectionFinding.md) objects

## Errors
<a name="API_GetIpamRouteProtectionFindings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetIpamRouteProtectionFindings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetIpamRouteProtectionFindings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetIpamRouteProtectionFindings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetIpamRouteProtectionFindings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetIpamRouteProtectionFindings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetIpamRouteProtectionFindings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetIpamRouteProtectionFindings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetIpamRouteProtectionFindings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetIpamRouteProtectionFindings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetIpamRouteProtectionFindings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetIpamRouteProtectionFindings)
