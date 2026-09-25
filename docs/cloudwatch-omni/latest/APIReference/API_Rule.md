---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_Rule.html
---

# Rule
<a name="API_Rule"></a>

Top-level rule definition.

 `telemetryRule` members are optional at the Smithy level to support PATCH semantics on UpdateAlert (send only the sub-blocks you want to change). On CreateAlert, presence is enforced by the service-side validator.

## Contents
<a name="API_Rule_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** telemetryRule **   <a name="cloudwatchomni-Type-Rule-telemetryRule"></a>
The telemetry-based rule definition.
Type: [TelemetryRule](API_TelemetryRule.md) object
Required: No

## See Also
<a name="API_Rule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/Rule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/Rule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/Rule)
