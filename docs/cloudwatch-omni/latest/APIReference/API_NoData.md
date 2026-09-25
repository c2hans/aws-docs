---
source_url: https://docs.aws.amazon.com/cloudwatch-omni/latest/APIReference/API_NoData.html
---

# NoData
<a name="API_NoData"></a>

Configures how the alert reacts when an evaluation produces no data. `treatAs` carries the resulting state; defaults to `NODATA` when omitted.

## Contents
<a name="API_NoData_Contents"></a>

 ** treatAs **   <a name="cloudwatchomni-Type-NoData-treatAs"></a>
The state to report when an evaluation produces no data.
Type: String
Valid Values: `OK | WARNING | CRITICAL | NODATA`
Required: Yes

## See Also
<a name="API_NoData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudwatchomni-2025-01-01/NoData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudwatchomni-2025-01-01/NoData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudwatchomni-2025-01-01/NoData)
