---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ProvisionIpamByoasn.html
---

# ProvisionIpamByoasn
<a name="API_ProvisionIpamByoasn"></a>

Provisions your Autonomous System Number (ASN) for use in your AWS account. This action requires authorization context for Amazon to bring the ASN to an AWS account. For more information, see [Tutorial: Bring your ASN to IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-byoasn.html) in the *Amazon VPC IPAM guide*.

## Request Parameters
<a name="API_ProvisionIpamByoasn_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Asn**
A public 2-byte or 4-byte ASN.
Type: String
Required: Yes

 **AsnAuthorizationContext**
An ASN authorization context.
Type: [AsnAuthorizationContext](API_AsnAuthorizationContext.md) object
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **IpamId**
An IPAM ID.
Type: String
Required: Yes

## Response Elements
<a name="API_ProvisionIpamByoasn_ResponseElements"></a>

The following elements are returned by the service.

 **byoasn**
An ASN and BYOIP CIDR association.
Type: [Byoasn](API_Byoasn.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_ProvisionIpamByoasn_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ProvisionIpamByoasn_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ProvisionIpamByoasn)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ProvisionIpamByoasn)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ProvisionIpamByoasn)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ProvisionIpamByoasn)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ProvisionIpamByoasn)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ProvisionIpamByoasn)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ProvisionIpamByoasn)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ProvisionIpamByoasn)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ProvisionIpamByoasn)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ProvisionIpamByoasn)
