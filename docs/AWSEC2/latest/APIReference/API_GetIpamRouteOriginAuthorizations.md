---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetIpamRouteOriginAuthorizations.html
---

# GetIpamRouteOriginAuthorizations
<a name="API_GetIpamRouteOriginAuthorizations"></a>

Retrieves the current Route Origin Authorizations (ROAs) published to the RPKI for an IPAM internet registry association. We recommend using pagination to ensure that the operation returns quickly and successfully.

## Request Parameters
<a name="API_GetIpamRouteOriginAuthorizations_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Cidr**
Filter results to a specific CIDR prefix.
Type: String
Required: No

 **DryRun**
Checks whether you have the required permissions for the operation, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
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
<a name="API_GetIpamRouteOriginAuthorizations_ResponseElements"></a>

The following elements are returned by the service.

 **ipamRouteOriginAuthorizationSet**
The Route Origin Authorizations published to the RPKI.
Type: Array of [IpamRouteOriginAuthorizationInfo](API_IpamRouteOriginAuthorizationInfo.md) objects

 **nextToken**
The token to use to retrieve the next page of results.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_GetIpamRouteOriginAuthorizations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetIpamRouteOriginAuthorizations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetIpamRouteOriginAuthorizations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetIpamRouteOriginAuthorizations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetIpamRouteOriginAuthorizations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetIpamRouteOriginAuthorizations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetIpamRouteOriginAuthorizations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetIpamRouteOriginAuthorizations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetIpamRouteOriginAuthorizations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetIpamRouteOriginAuthorizations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetIpamRouteOriginAuthorizations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetIpamRouteOriginAuthorizations)
