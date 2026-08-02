---
source_url: https://docs.aws.amazon.com/lambda/latest/microvm-api/API_Hooks.html
---

# Hooks
<a name="API_Hooks"></a>

Lifecycle hook configuration for MicroVMs and MicroVM images.

## Contents
<a name="API_Hooks_Contents"></a>

 ** microvmHooks **   <a name="lambdamicrovm-Type-Hooks-microvmHooks"></a>
The lifecycle hooks for MicroVM events.
Type: [MicrovmHooks](API_MicrovmHooks.md) object
Required: No

 ** microvmImageHooks **   <a name="lambdamicrovm-Type-Hooks-microvmImageHooks"></a>
The hooks for MicroVM image build events.
Type: [MicrovmImageHooks](API_MicrovmImageHooks.md) object
Required: No

 ** port **   <a name="lambdamicrovm-Type-Hooks-port"></a>
The port number on which the hooks listener runs.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

## See Also
<a name="API_Hooks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-microvms-2025-09-09/Hooks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-microvms-2025-09-09/Hooks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-microvms-2025-09-09/Hooks)
