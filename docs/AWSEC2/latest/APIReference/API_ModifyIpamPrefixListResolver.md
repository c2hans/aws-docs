---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyIpamPrefixListResolver.html
---

# ModifyIpamPrefixListResolver
<a name="API_ModifyIpamPrefixListResolver"></a>

Modifies an IPAM prefix list resolver. You can update the description and CIDR selection rules. Changes to rules will trigger re-evaluation and potential updates to associated prefix lists.

## Request Parameters
<a name="API_ModifyIpamPrefixListResolver_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Description**
A new description for the IPAM prefix list resolver.
Type: String
Required: No

 **DryRun**
A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **IpamPrefixListResolverId**
The ID of the IPAM prefix list resolver to modify.
Type: String
Required: Yes

 **Rule.N**
The updated CIDR selection rules for the resolver. These rules replace the existing rules entirely.
Type: Array of [IpamPrefixListResolverRuleRequest](API_IpamPrefixListResolverRuleRequest.md) objects
Required: No

## Response Elements
<a name="API_ModifyIpamPrefixListResolver_ResponseElements"></a>

The following elements are returned by the service.

 **ipamPrefixListResolver**
Information about the modified IPAM prefix list resolver.
Type: [IpamPrefixListResolver](API_IpamPrefixListResolver.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_ModifyIpamPrefixListResolver_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ModifyIpamPrefixListResolver_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyIpamPrefixListResolver)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyIpamPrefixListResolver)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyIpamPrefixListResolver)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyIpamPrefixListResolver)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyIpamPrefixListResolver)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyIpamPrefixListResolver)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyIpamPrefixListResolver)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyIpamPrefixListResolver)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyIpamPrefixListResolver)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyIpamPrefixListResolver)
