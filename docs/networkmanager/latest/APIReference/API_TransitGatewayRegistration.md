---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_TransitGatewayRegistration.html
---

# TransitGatewayRegistration
<a name="API_TransitGatewayRegistration"></a>

Describes the registration of a transit gateway to a global network.

## Contents
<a name="API_TransitGatewayRegistration_Contents"></a>

 ** GlobalNetworkId **   <a name="networkmanager-Type-TransitGatewayRegistration-GlobalNetworkId"></a>
The ID of the global network.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 50.
Pattern: `[\s\S]*`
Required: No

 ** State **   <a name="networkmanager-Type-TransitGatewayRegistration-State"></a>
The state of the transit gateway registration.
Type: [TransitGatewayRegistrationStateReason](API_TransitGatewayRegistrationStateReason.md) object
Required: No

 ** TransitGatewayArn **   <a name="networkmanager-Type-TransitGatewayRegistration-TransitGatewayArn"></a>
The Amazon Resource Name (ARN) of the transit gateway.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[\s\S]*`
Required: No

## See Also
<a name="API_TransitGatewayRegistration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/TransitGatewayRegistration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/TransitGatewayRegistration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/TransitGatewayRegistration)
