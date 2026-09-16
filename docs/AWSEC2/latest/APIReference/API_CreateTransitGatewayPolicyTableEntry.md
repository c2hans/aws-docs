---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_CreateTransitGatewayPolicyTableEntry.html
---

# CreateTransitGatewayPolicyTableEntry
<a name="API_CreateTransitGatewayPolicyTableEntry"></a>

Creates an entry in a transit gateway policy table to route matching traffic to a specified route table.

## Request Parameters
<a name="API_CreateTransitGatewayPolicyTableEntry_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **PolicyRule**
The matching criteria for the policy table entry.
Type: [TransitGatewayRequestPolicyRule](API_TransitGatewayRequestPolicyRule.md) object
Required: No

 **PolicyRuleNumber**
The rule number for the policy table entry. Lower rule numbers are evaluated first and take precedence.
Type: String
Required: Yes

 **TargetRouteTableId**
The ID of the transit gateway route table to use for traffic matching this rule.
Type: String
Required: Yes

 **TransitGatewayPolicyTableId**
The ID of the transit gateway policy table.
Type: String
Required: Yes

## Response Elements
<a name="API_CreateTransitGatewayPolicyTableEntry_ResponseElements"></a>

The following elements are returned by the service.

 **requestId**
The ID of the request.
Type: String

 **transitGatewayPolicyTableEntry**
Describes a transit gateway policy table entry
Type: [TransitGatewayPolicyTableEntry](API_TransitGatewayPolicyTableEntry.md) object

## Errors
<a name="API_CreateTransitGatewayPolicyTableEntry_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateTransitGatewayPolicyTableEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/CreateTransitGatewayPolicyTableEntry)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/CreateTransitGatewayPolicyTableEntry)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/CreateTransitGatewayPolicyTableEntry)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/CreateTransitGatewayPolicyTableEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/CreateTransitGatewayPolicyTableEntry)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/CreateTransitGatewayPolicyTableEntry)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/CreateTransitGatewayPolicyTableEntry)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/CreateTransitGatewayPolicyTableEntry)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/CreateTransitGatewayPolicyTableEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/CreateTransitGatewayPolicyTableEntry)
