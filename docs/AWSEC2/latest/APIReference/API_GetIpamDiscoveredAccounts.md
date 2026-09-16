---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetIpamDiscoveredAccounts.html
---

# GetIpamDiscoveredAccounts
<a name="API_GetIpamDiscoveredAccounts"></a>

Gets IPAM discovered accounts. A discovered account is an AWS account that is monitored under a resource discovery. If you have integrated IPAM with AWS Organizations, all accounts in the organization are discovered accounts. Only the IPAM account can get all discovered accounts in the organization.

## Request Parameters
<a name="API_GetIpamDiscoveredAccounts_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DiscoveryRegion**
The AWS Region that the account information is returned from.
Type: String
Required: Yes

 **DryRun**
A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
Discovered account filters.
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **IpamResourceDiscoveryId**
A resource discovery ID.
Type: String
Required: Yes

 **MaxResults**
The maximum number of discovered accounts to return in one page of results.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 1000.
Required: No

 **NextToken**
Specify the pagination token from a previous request to retrieve the next page of results.
Type: String
Required: No

## Response Elements
<a name="API_GetIpamDiscoveredAccounts_ResponseElements"></a>

The following elements are returned by the service.

 **ipamDiscoveredAccountSet**
Discovered accounts.
Type: Array of [IpamDiscoveredAccount](API_IpamDiscoveredAccount.md) objects

 **nextToken**
Specify the pagination token from a previous request to retrieve the next page of results.
Type: String

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_GetIpamDiscoveredAccounts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetIpamDiscoveredAccounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetIpamDiscoveredAccounts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetIpamDiscoveredAccounts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetIpamDiscoveredAccounts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetIpamDiscoveredAccounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetIpamDiscoveredAccounts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetIpamDiscoveredAccounts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetIpamDiscoveredAccounts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetIpamDiscoveredAccounts)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetIpamDiscoveredAccounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetIpamDiscoveredAccounts)
