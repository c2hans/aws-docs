---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyIpamPrefixListResolverTarget.html
---

# ModifyIpamPrefixListResolverTarget
<a name="API_ModifyIpamPrefixListResolverTarget"></a>

Modifies an IPAM prefix list resolver target. You can update version tracking settings and the desired version of the target prefix list.

## Request Parameters
<a name="API_ModifyIpamPrefixListResolverTarget_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **ClientToken**
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **DesiredVersion**
The desired version of the prefix list to target. This allows you to pin the target to a specific version.
Type: Long
Required: No

 **DryRun**
A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **IpamPrefixListResolverTargetId**
The ID of the IPAM prefix list resolver target to modify.
Type: String
Required: Yes

 **TrackLatestVersion**
Indicates whether the resolver target should automatically track the latest version of the prefix list. When enabled, the target will always synchronize with the most current version.
Choose this for automatic updates when you want your prefix lists to stay current with infrastructure changes without manual intervention.
Type: Boolean
Required: No

## Response Elements
<a name="API_ModifyIpamPrefixListResolverTarget_ResponseElements"></a>

The following elements are returned by the service.

 **ipamPrefixListResolverTarget**
Information about the modified IPAM prefix list resolver target.
Type: [IpamPrefixListResolverTarget](API_IpamPrefixListResolverTarget.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_ModifyIpamPrefixListResolverTarget_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ModifyIpamPrefixListResolverTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyIpamPrefixListResolverTarget)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyIpamPrefixListResolverTarget)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyIpamPrefixListResolverTarget)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyIpamPrefixListResolverTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyIpamPrefixListResolverTarget)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyIpamPrefixListResolverTarget)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyIpamPrefixListResolverTarget)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyIpamPrefixListResolverTarget)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyIpamPrefixListResolverTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyIpamPrefixListResolverTarget)
