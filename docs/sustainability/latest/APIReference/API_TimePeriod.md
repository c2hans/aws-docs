---
source_url: https://docs.aws.amazon.com/sustainability/latest/APIReference/API_TimePeriod.html
---

# TimePeriod
<a name="API_TimePeriod"></a>

Represents a duration of time defined by start and end timestamps. If there is no impact data available for a selected period, the response returns an empty `Results` array.

## Contents
<a name="API_TimePeriod_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** End **   <a name="sustainability-Type-TimePeriod-End"></a>
The end (exclusive) of the time period. ISO-8601 formatted timestamp, for example: `YYYY-MM-DDThh:mm:ss.sssZ`
Type: Timestamp
Required: Yes

 ** Start **   <a name="sustainability-Type-TimePeriod-Start"></a>
The start (inclusive) of the time period. ISO-8601 formatted timestamp, for example: `YYYY-MM-DDThh:mm:ss.sssZ`
Type: Timestamp
Required: Yes

## See Also
<a name="API_TimePeriod_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sustainability-2018-05-10/TimePeriod)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sustainability-2018-05-10/TimePeriod)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sustainability-2018-05-10/TimePeriod)
