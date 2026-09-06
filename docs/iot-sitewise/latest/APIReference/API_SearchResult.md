---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_SearchResult.html
---

# SearchResult
<a name="API_SearchResult"></a>

A single matching segment of time-series data returned by a search.

## Contents
<a name="API_SearchResult_Contents"></a>

 ** datasetId **   <a name="iotsitewise-Type-SearchResult-datasetId"></a>
The identifier of the dataset that contains the matching data.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** endTimestamp **   <a name="iotsitewise-Type-SearchResult-endTimestamp"></a>
The end of the matching time-series segment, in nanoseconds since the Unix epoch.
Type: [TimeInNanos](API_TimeInNanos.md) object
Required: Yes

 ** score **   <a name="iotsitewise-Type-SearchResult-score"></a>
The relevance score of this result. Higher scores indicate a stronger match.
Type: Float
Required: Yes

 ** searchId **   <a name="iotsitewise-Type-SearchResult-searchId"></a>
The identifier of the search that produced this result.
Type: String
Length Constraints: Minimum length of 23. Maximum length of 36.
Pattern: `[a-zA-Z0-9]+(-[a-zA-Z0-9]+)*`
Required: Yes

 ** startTimestamp **   <a name="iotsitewise-Type-SearchResult-startTimestamp"></a>
The start of the matching time-series segment, in nanoseconds since the Unix epoch.
Type: [TimeInNanos](API_TimeInNanos.md) object
Required: Yes

 ** timeSeriesId **   <a name="iotsitewise-Type-SearchResult-timeSeriesId"></a>
The identifier of the time series that contains the matching data.
Type: String
Length Constraints: Minimum length of 36. Maximum length of 73.
Required: Yes

 ** topTimestamp **   <a name="iotsitewise-Type-SearchResult-topTimestamp"></a>
The timestamp of the most relevant point within the matching segment, in nanoseconds since the Unix epoch.
Type: [TimeInNanos](API_TimeInNanos.md) object
Required: Yes

 ** workspaceName **   <a name="iotsitewise-Type-SearchResult-workspaceName"></a>
The name of the workspace the search ran against.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## See Also
<a name="API_SearchResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/SearchResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/SearchResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/SearchResult)
