---
source_url: https://docs.aws.amazon.com/rtb-fabric/latest/api/API_FlowModule.html
---

# FlowModule

A version attached to a flow, with its settings.

## Contents
<a name="API_FlowModule_Contents"></a>

 ** moduleVersionArn **   <a name="rtbfabric-Type-FlowModule-moduleVersionArn"></a>
The version to attach. It must be ACTIVE and available to you (see ListAvailableModuleVersions). You can keep a version that's already in the link's flows after it's deprecated, but you can't give it a higher share of traffic.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1011.
Pattern: `arn:aws[a-zA-Z-]*:rtbfabric:[a-z0-9-]+::modules/module-[a-zA-Z0-9]{1,25}/versions/(0|[1-9]\d{0,9})\.(0|[1-9]\d{0,9})\.(0|[1-9]\d{0,9})`
Required: Yes

 ** name **   <a name="rtbfabric-Type-FlowModule-name"></a>
The module's name, unique within the flow. It can't be a name that RTB Fabric reserves for the modules it adds, such as DefaultRateLimiter or ErrorMasking.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Za-z0-9][A-Za-z0-9-]*`
Required: Yes

 ** activationPercentage **   <a name="rtbfabric-Type-FlowModule-activationPercentage"></a>
The percentage of the flow's requests that the module runs on. The flow skips the module on the rest of the requests. The default is 100. The no-bid module requires this setting, and the Rate Limiter Module accepts only 100.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** configurationValues **   <a name="rtbfabric-Type-FlowModule-configurationValues"></a>
The module's parameters, as a JSON string. Modules from vendors accept only `threshold` (0 through 1) and `lookupMiss` (CONTINUE or NO\_BID), within what the version's `configurationSchema` allows. A `lookupMiss` of NO\_BID requires FILTER in `selectedActions`. Built-in modules take the parameters in their `configurationSchema`. RTB Fabric rejects a value that fails with ValidationException. Omit it when the schema is empty or fully defaulted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.
Required: No

 ** failureMode **   <a name="rtbfabric-Type-FlowModule-failureMode"></a>
Specifies what happens when the module's call fails or times out. OPEN continues the flow, and CLOSED ends the request with a no-bid response. Modules from vendors default to OPEN. For a built-in module without this setting, an error ends the request. The Rate Limiter Module doesn't accept this setting.
Type: String
Valid Values: `OPEN | CLOSED`
Required: No

 ** selectedActions **   <a name="rtbfabric-Type-FlowModule-selectedActions"></a>
The capabilities to turn on, chosen from the version's `configurableActions`. If the version exposes one, it's the default. If the version exposes more than one, this field is required. If it exposes none, omit this field.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 16 items.
Valid Values: `FILTER | ENRICH_REQUEST_EXT | ENRICH_REQUEST_HEADERS | OBSERVE`
Required: No

## See Also
<a name="API_FlowModule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rtbfabric-2023-05-15/FlowModule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rtbfabric-2023-05-15/FlowModule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rtbfabric-2023-05-15/FlowModule)
