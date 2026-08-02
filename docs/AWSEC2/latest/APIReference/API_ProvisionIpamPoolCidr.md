---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ProvisionIpamPoolCidr.html
---

# ProvisionIpamPoolCidr
<a name="API_ProvisionIpamPoolCidr"></a>

Provision a CIDR to an IPAM pool. You can use this action to provision new CIDRs to a top-level pool or to transfer a CIDR from a top-level pool to a pool within it.

For more information, see [Provision CIDRs to pools](https://docs.aws.amazon.com/vpc/latest/ipam/prov-cidr-ipam.html) in the *Amazon VPC IPAM User Guide*.

## Request Parameters
<a name="API_ProvisionIpamPoolCidr_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Cidr**
The CIDR you want to assign to the IPAM pool. Either "NetmaskLength" or "Cidr" is required. This value will be null if you specify "NetmaskLength" and will be filled in during the provisioning process.
Type: String
Required: No

 **CidrAuthorizationContext**
A signed document that proves that you are authorized to bring a specified IP address range to Amazon using BYOIP. This option only applies to IPv4 and IPv6 pools in the public scope.
Type: [IpamCidrAuthorizationContext](API_IpamCidrAuthorizationContext.md) object
Required: No

 **ClientToken**
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request. For more information, see [Ensuring idempotency](https://docs.aws.amazon.com/ec2/latest/devguide/ec2-api-idempotency.html).
Type: String
Required: No

 **DryRun**
A check for whether you have the required permissions for the action without actually making the request and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **IpamExternalResourceVerificationTokenId**
Verification token ID. This option only applies to IPv4 and IPv6 pools in the public scope.
Type: String
Required: No

 **IpamPoolId**
The ID of the IPAM pool to which you want to assign a CIDR.
Type: String
Required: Yes

 **NetmaskLength**
The netmask length of the CIDR you'd like to provision to a pool. Can be used for provisioning Amazon-provided IPv6 CIDRs to top-level pools and for provisioning CIDRs to pools with source pools. Cannot be used to provision BYOIP CIDRs to top-level pools. Either "NetmaskLength" or "Cidr" is required.
Type: Integer
Required: No

 **VerificationMethod**
The method for verifying control of a public IP address range. Defaults to `remarks-x509` if not specified. This option only applies to IPv4 and IPv6 pools in the public scope.
Type: String
Valid Values: `remarks-x509 | dns-token`
Required: No

## Response Elements
<a name="API_ProvisionIpamPoolCidr_ResponseElements"></a>

The following elements are returned by the service.

 **ipamPoolCidr**
Information about the provisioned CIDR.
Type: [IpamPoolCidr](API_IpamPoolCidr.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_ProvisionIpamPoolCidr_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ProvisionIpamPoolCidr_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ProvisionIpamPoolCidr)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ProvisionIpamPoolCidr)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ProvisionIpamPoolCidr)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ProvisionIpamPoolCidr)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ProvisionIpamPoolCidr)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ProvisionIpamPoolCidr)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ProvisionIpamPoolCidr)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ProvisionIpamPoolCidr)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ProvisionIpamPoolCidr)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ProvisionIpamPoolCidr)
