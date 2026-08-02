---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_GetSendStatistics.html
---

# GetSendStatistics
<a name="API_GetSendStatistics"></a>

Provides sending statistics for the current AWS Region. The result is a list of data points, representing the last two weeks of sending activity. Each data point in the list contains statistics for a 15-minute period of time.

You can execute this operation no more than once per second.

## Response Elements
<a name="API_GetSendStatistics_ResponseElements"></a>

The following element is returned by the service.

 **SendDataPoints.member.N**
A list of data points, each of which represents 15 minutes of activity.
Type: Array of [SendDataPoint](API_SendDataPoint.md) objects

## Errors
<a name="API_GetSendStatistics_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetSendStatistics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/GetSendStatistics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/GetSendStatistics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/GetSendStatistics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/GetSendStatistics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/GetSendStatistics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/GetSendStatistics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/GetSendStatistics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/GetSendStatistics)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/GetSendStatistics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/GetSendStatistics)
