---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_EC2CopyRouteTableAction.html
---

# EC2CopyRouteTableAction
<a name="API_EC2CopyRouteTableAction"></a>

An action that copies the EC2 route table for use in remediation.

## Contents
<a name="API_EC2CopyRouteTableAction_Contents"></a>

 ** RouteTableId **   <a name="fms-Type-EC2CopyRouteTableAction-RouteTableId"></a>
The ID of the copied EC2 route table that is associated with the remediation action.
Type: [ActionTarget](API_ActionTarget.md) object
Required: Yes

 ** VpcId **   <a name="fms-Type-EC2CopyRouteTableAction-VpcId"></a>
The VPC ID of the copied EC2 route table that is associated with the remediation action.
Type: [ActionTarget](API_ActionTarget.md) object
Required: Yes

 ** Description **   <a name="fms-Type-EC2CopyRouteTableAction-Description"></a>
A description of the copied EC2 route table that is associated with the remediation action.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_EC2CopyRouteTableAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/EC2CopyRouteTableAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/EC2CopyRouteTableAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/EC2CopyRouteTableAction)
