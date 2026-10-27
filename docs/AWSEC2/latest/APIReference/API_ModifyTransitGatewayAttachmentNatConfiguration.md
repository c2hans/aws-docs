---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ModifyTransitGatewayAttachmentNatConfiguration.html
---

# ModifyTransitGatewayAttachmentNatConfiguration
<a name="API_ModifyTransitGatewayAttachmentNatConfiguration"></a>

Modifies the NAT configuration for the specified transit gateway attachment. Use this operation to do the following:
+ Enable or disable NAT gateway support for the attachment.
+ Specify whether the transit gateway installs routes for the NAT CIDRs.
+ Replace the NAT gateway rules for the attachment.

Only the owner of the transit gateway can modify the NAT configuration.

With NAT gateway support enabled, the transit gateway translates addresses in each rule's `MatchSourceCidr` range to the corresponding addresses in its `NatCidr` range.

The transit gateway applies changes asynchronously. To check the result, use `GetTransitGatewayAttachmentNatConfiguration`.

## Request Parameters
<a name="API_ModifyTransitGatewayAttachmentNatConfiguration_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **NatGatewayRule.N**
The NAT gateway rules for the attachment. The rules that you specify replace all existing NAT gateway rules for the attachment. You can specify up to 50 rules for an attachment. If you omit this parameter, the existing rules don't change. To remove all rules, use `ResetNatGatewayRules`.
Type: Array of [TransitGatewayNatRuleRequest](API_TransitGatewayNatRuleRequest.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 **NatGatewaySupport**
Specifies whether to enable or disable NAT gateway support for the attachment. To enable NAT gateway support, the attachment must have at least one NAT gateway rule. You can't modify the NAT configuration while NAT gateway support is `enabling` or `disabling`. If you omit this parameter, the current value doesn't change.
Type: String
Valid Values: `enable | disable`
Required: No

 **NatSystemRouteSupport**
Specifies whether the transit gateway installs routes for the NAT CIDRs in the route tables to which the attachment propagates. For VPC attachments, the transit gateway always installs these routes. You can enable or disable this option only for AWS Direct Connect gateway attachments and Site-to-Site VPN attachments that use dynamic routing. For these attachments, the default is `enable`. If you omit this parameter, the current value doesn't change.
Type: String
Valid Values: `enable | disable`
Required: No

 **ResetNatGatewayRules**
Specifies whether to remove all NAT gateway rules from the attachment. If you omit this parameter, the transit gateway doesn't remove any rules. You can't specify this parameter together with `NatGatewayRules`. Because you can't enable NAT gateway support without rules, also set `NatGatewaySupport` to `disable` in the same request if NAT gateway support is currently enabled.
Type: Boolean
Required: No

 **TransitGatewayAttachmentId**
The ID of the transit gateway attachment.
Type: String
Required: Yes

## Response Elements
<a name="API_ModifyTransitGatewayAttachmentNatConfiguration_ResponseElements"></a>

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
<a name="API_ModifyTransitGatewayAttachmentNatConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ModifyTransitGatewayAttachmentNatConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/ModifyTransitGatewayAttachmentNatConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/ModifyTransitGatewayAttachmentNatConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ModifyTransitGatewayAttachmentNatConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/ModifyTransitGatewayAttachmentNatConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ModifyTransitGatewayAttachmentNatConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/ModifyTransitGatewayAttachmentNatConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/ModifyTransitGatewayAttachmentNatConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/ModifyTransitGatewayAttachmentNatConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/ModifyTransitGatewayAttachmentNatConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ModifyTransitGatewayAttachmentNatConfiguration)
