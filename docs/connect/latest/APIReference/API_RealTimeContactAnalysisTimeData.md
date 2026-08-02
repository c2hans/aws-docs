---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_RealTimeContactAnalysisTimeData.html
---

# RealTimeContactAnalysisTimeData
<a name="API_RealTimeContactAnalysisTimeData"></a>

Object describing time with which the segment is associated. It can have different representations of time. Currently supported: absoluteTime

## Contents
<a name="API_RealTimeContactAnalysisTimeData_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** AbsoluteTime **   <a name="connect-Type-RealTimeContactAnalysisTimeData-AbsoluteTime"></a>
Time represented in ISO 8601 format: yyyy-MM-ddThh:mm:ss.SSSZ. For example, 2019-11-08T02:41:28.172Z.
Type: Timestamp
Required: No

## See Also
<a name="API_RealTimeContactAnalysisTimeData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/RealTimeContactAnalysisTimeData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/RealTimeContactAnalysisTimeData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/RealTimeContactAnalysisTimeData)
