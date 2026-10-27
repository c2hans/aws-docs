---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetTransitGatewayAttachmentNatConfiguration.html
---

# GetTransitGatewayAttachmentNatConfiguration
<a name="API_GetTransitGatewayAttachmentNatConfiguration"></a>

Describes the NAT configuration for the specified transit gateway attachment. Only the owner of the transit gateway can describe the NAT configuration.

## Request Parameters
<a name="API_GetTransitGatewayAttachmentNatConfiguration_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **TransitGatewayAttachmentId**
The ID of the transit gateway attachment.
Type: String
Required: Yes

## Response Elements
<a name="API_GetTransitGatewayAttachmentNatConfiguration_ResponseElements"></a>

The following elements are returned by the service.

 **natGatewayRuleSet**
The NAT gateway rules for the attachment.
Type: Array of [TransitGatewayNatRule](API_TransitGatewayNatRule.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 **natGatewaySupport**
The state of NAT gateway support for the attachment.
Type: String
Valid Values: `enabled | disabled | enabling | disabling`

 **natSystemRouteSupport**
Specifies whether the transit gateway installs routes for the NAT CIDRs in the route tables to which the attachment propagates.
Type: String
Valid Values: `enable | disable`

 **requestId**
The ID of the request.
Type: String

 **transitGatewayAttachmentId**
The ID of the transit gateway attachment.
Type: String

## Errors
<a name="API_GetTransitGatewayAttachmentNatConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetTransitGatewayAttachmentNatConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetTransitGatewayAttachmentNatConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetTransitGatewayAttachmentNatConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetTransitGatewayAttachmentNatConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetTransitGatewayAttachmentNatConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetTransitGatewayAttachmentNatConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetTransitGatewayAttachmentNatConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetTransitGatewayAttachmentNatConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetTransitGatewayAttachmentNatConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetTransitGatewayAttachmentNatConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetTransitGatewayAttachmentNatConfiguration)
