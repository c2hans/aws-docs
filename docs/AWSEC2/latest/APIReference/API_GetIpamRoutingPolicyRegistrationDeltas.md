---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetIpamRoutingPolicyRegistrationDeltas.html
---

# GetIpamRoutingPolicyRegistrationDeltas
<a name="API_GetIpamRoutingPolicyRegistrationDeltas"></a>

Retrieves the history of routing policy registration changes for an IPAM internet registry association. We recommend using pagination to ensure that the operation returns quickly and successfully.

## Request Parameters
<a name="API_GetIpamRoutingPolicyRegistrationDeltas_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ChronologicalOrder**
The chronological order to return results in. Valid values: `forward` \| `reverse`.
Type: String
Valid Values: `forward | reverse`
Required: No

 **DeltaId**
Filter results to a specific delta ID.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **EndTime**
The end of the time range to filter deltas by.
Type: Timestamp
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

 **StartTime**
The start of the time range to filter deltas by.
Type: Timestamp
Required: No

## Response Elements
<a name="API_GetIpamRoutingPolicyRegistrationDeltas_ResponseElements"></a>

The following elements are returned by the service.

 **ipamRoutingPolicyRegistrationDeltaSet**
The routing policy registration deltas.
Type: Array of [IpamRoutingPolicyRegistrationDelta](API_IpamRoutingPolicyRegistrationDelta.md) objects

 **nextToken**
The token to use to retrieve the next page of results.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_GetIpamRoutingPolicyRegistrationDeltas_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetIpamRoutingPolicyRegistrationDeltas_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetIpamRoutingPolicyRegistrationDeltas)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetIpamRoutingPolicyRegistrationDeltas)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetIpamRoutingPolicyRegistrationDeltas)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetIpamRoutingPolicyRegistrationDeltas)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetIpamRoutingPolicyRegistrationDeltas)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetIpamRoutingPolicyRegistrationDeltas)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetIpamRoutingPolicyRegistrationDeltas)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetIpamRoutingPolicyRegistrationDeltas)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetIpamRoutingPolicyRegistrationDeltas)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetIpamRoutingPolicyRegistrationDeltas)
