---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AssociateIpamByoasn.html
---

# AssociateIpamByoasn
<a name="API_AssociateIpamByoasn"></a>

Associates your Autonomous System Number (ASN) with a BYOIP CIDR that you own in the same AWS Region. For more information, see [Tutorial: Bring your ASN to IPAM](https://docs.aws.amazon.com/vpc/latest/ipam/tutorials-byoasn.html) in the *Amazon VPC IPAM guide*.

After the association succeeds, the ASN is eligible for advertisement. You can view the association with [DescribeByoipCidrs](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeByoipCidrs.html). You can advertise the CIDR with [AdvertiseByoipCidr](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AdvertiseByoipCidr.html).

## Request Parameters
<a name="API_AssociateIpamByoasn_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **Asn**
A public 2-byte or 4-byte ASN.
Type: String
Required: Yes

 **Cidr**
The BYOIP CIDR you want to associate with an ASN.
Type: String
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_AssociateIpamByoasn_ResponseElements"></a>

The following elements are returned by the service.

 **asnAssociation**
The ASN and BYOIP CIDR association.
Type: [AsnAssociation](API_AsnAssociation.md) object

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_AssociateIpamByoasn_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_AssociateIpamByoasn_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/AssociateIpamByoasn)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/AssociateIpamByoasn)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AssociateIpamByoasn)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/AssociateIpamByoasn)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AssociateIpamByoasn)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/AssociateIpamByoasn)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/AssociateIpamByoasn)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/AssociateIpamByoasn)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/AssociateIpamByoasn)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AssociateIpamByoasn)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
