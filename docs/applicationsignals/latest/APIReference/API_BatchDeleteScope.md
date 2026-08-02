---
source_url: https://docs.aws.amazon.com/applicationsignals/latest/APIReference/API_BatchDeleteScope.html
---

# BatchDeleteScope
<a name="API_BatchDeleteScope"></a>

Scope parameters for bulk delete by scope.

## Contents
<a name="API_BatchDeleteScope_Contents"></a>

 ** Environment **   <a name="applicationsignals-Type-BatchDeleteScope-Environment"></a>
The environment identifier for the instrumentation configurations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9:/+=,.@_-]+`
Required: Yes

 ** InstrumentationType **   <a name="applicationsignals-Type-BatchDeleteScope-InstrumentationType"></a>
The instrumentation type: `BREAKPOINT` or `PROBE`.
Type: String
Valid Values: `BREAKPOINT | PROBE`
Required: Yes

 ** Service **   <a name="applicationsignals-Type-BatchDeleteScope-Service"></a>
The service name for the instrumentation configurations.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z0-9:/+=,.@_-]+`
Required: Yes

## See Also
<a name="API_BatchDeleteScope_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/application-signals-2024-04-15/BatchDeleteScope)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/application-signals-2024-04-15/BatchDeleteScope)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/application-signals-2024-04-15/BatchDeleteScope)
