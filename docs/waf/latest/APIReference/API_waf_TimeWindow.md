---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_waf_TimeWindow.html
---

# TimeWindow
<a name="API_waf_TimeWindow"></a>

**Note**
 AWS WAF Classic support will end on September 30, 2025.
This is ** AWS WAF Classic** documentation. For more information, see [AWS WAF Classic](https://docs.aws.amazon.com/waf/latest/developerguide/classic-waf-chapter.html) in the developer guide.
 **For the latest version of AWS WAF **, use the AWS WAFV2 API and see the [AWS WAF Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html). With the latest version, AWS WAF has a single set of endpoints for regional and global use.

In a [GetSampledRequests](API_waf_GetSampledRequests.md) request, the `StartTime` and `EndTime` objects specify the time range for which you want AWS WAF to return a sample of web requests.

You must specify the times in Coordinated Universal Time (UTC) format. UTC format includes the special designator, `Z`. For example, `"2016-09-27T14:50Z"`.

In a [GetSampledRequests](API_waf_GetSampledRequests.md) response, the `StartTime` and `EndTime` objects specify the time range for which AWS WAF actually returned a sample of web requests. AWS WAF gets the specified number of requests from among the first 5,000 requests that your AWS resource receives during the specified time period. If your resource receives more than 5,000 requests during that period, AWS WAF stops sampling after the 5,000th request. In that case, `EndTime` is the time that AWS WAF received the 5,000th request.

## Contents
<a name="API_waf_TimeWindow_Contents"></a>

 ** EndTime **   <a name="WAF-Type-waf_TimeWindow-EndTime"></a>
The end of the time range from which you want `GetSampledRequests` to return a sample of the requests that your AWS resource received. You must specify the date and time in Coordinated Universal Time (UTC) format. UTC format includes the special designator, `Z`. For example, `"2016-09-27T14:50Z"`. You can specify any time range in the previous three hours.
Type: Timestamp
Required: Yes

 ** StartTime **   <a name="WAF-Type-waf_TimeWindow-StartTime"></a>
The beginning of the time range from which you want `GetSampledRequests` to return a sample of the requests that your AWS resource received. You must specify the date and time in Coordinated Universal Time (UTC) format. UTC format includes the special designator, `Z`. For example, `"2016-09-27T14:50Z"`. You can specify any time range in the previous three hours.
Type: Timestamp
Required: Yes

## See Also
<a name="API_waf_TimeWindow_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/waf-2015-08-24/TimeWindow)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/waf-2015-08-24/TimeWindow)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/waf-2015-08-24/TimeWindow)
