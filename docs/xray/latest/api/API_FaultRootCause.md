---
source_url: https://docs.aws.amazon.com/xray/latest/api/API_FaultRootCause.html
---

# FaultRootCause
<a name="API_FaultRootCause"></a>

The root cause information for a trace summary fault.

## Contents
<a name="API_FaultRootCause_Contents"></a>

 ** ClientImpacting **   <a name="xray-Type-FaultRootCause-ClientImpacting"></a>
A flag that denotes that the root cause impacts the trace client.
Type: Boolean
Required: No

 ** Services **   <a name="xray-Type-FaultRootCause-Services"></a>
A list of corresponding services. A service identifies a segment and it contains a name, account ID, type, and inferred flag.
Type: Array of [FaultRootCauseService](API_FaultRootCauseService.md) objects
Required: No

## See Also
<a name="API_FaultRootCause_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/xray-2016-04-12/FaultRootCause)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/xray-2016-04-12/FaultRootCause)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/xray-2016-04-12/FaultRootCause)
