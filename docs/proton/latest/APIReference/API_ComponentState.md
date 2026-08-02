---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_ComponentState.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# ComponentState
<a name="API_ComponentState"></a>

The detailed data about the current state of the component.

## Contents
<a name="API_ComponentState_Contents"></a>

 ** serviceInstanceName **   <a name="proton-Type-ComponentState-serviceInstanceName"></a>
The name of the service instance that this component is attached to. Provided when a component is attached to a service instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `.*(^$)|^[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: No

 ** serviceName **   <a name="proton-Type-ComponentState-serviceName"></a>
The name of the service that `serviceInstanceName` is associated with. Provided when a component is attached to a service instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 100.
Pattern: `.*(^$)|^[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: No

 ** serviceSpec **   <a name="proton-Type-ComponentState-serviceSpec"></a>
The service spec that the component uses to access service inputs. Provided when a component is attached to a service instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Required: No

 ** templateFile **   <a name="proton-Type-ComponentState-templateFile"></a>
The template file used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Required: No

## See Also
<a name="API_ComponentState_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/ComponentState)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/ComponentState)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/ComponentState)
