---
source_url: https://docs.aws.amazon.com/arc-region-switch/latest/api/API_ArcRoutingControlConfiguration.html
---

# ArcRoutingControlConfiguration
<a name="API_ArcRoutingControlConfiguration"></a>

Configuration for ARC routing controls used in a Region switch plan. Routing controls are simple on/off switches that you can use to shift traffic away from an impaired Region.

## Contents
<a name="API_ArcRoutingControlConfiguration_Contents"></a>

 ** regionAndRoutingControls **   <a name="regionswitch-Type-ArcRoutingControlConfiguration-regionAndRoutingControls"></a>
The Region and ARC routing controls for the configuration.
Type: String to array of [ArcRoutingControlState](API_ArcRoutingControlState.md) objects map
Required: Yes

 ** crossAccountRole **   <a name="regionswitch-Type-ArcRoutingControlConfiguration-crossAccountRole"></a>
The cross account role for the configuration.
Type: String
Pattern: `arn:aws[a-zA-Z0-9-]*:iam::[0-9]{12}:role/.+`
Required: No

 ** externalId **   <a name="regionswitch-Type-ArcRoutingControlConfiguration-externalId"></a>
The external ID (secret key) for the configuration.
Type: String
Required: No

 ** timeoutMinutes **   <a name="regionswitch-Type-ArcRoutingControlConfiguration-timeoutMinutes"></a>
The timeout value specified for the configuration.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_ArcRoutingControlConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/arc-region-switch-2022-07-26/ArcRoutingControlConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/arc-region-switch-2022-07-26/ArcRoutingControlConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/arc-region-switch-2022-07-26/ArcRoutingControlConfiguration)
