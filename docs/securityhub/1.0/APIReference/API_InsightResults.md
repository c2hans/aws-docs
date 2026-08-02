---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_InsightResults.html
---

# InsightResults
<a name="API_InsightResults"></a>

The insight results returned by the `GetInsightResults` operation.

## Contents
<a name="API_InsightResults_Contents"></a>

 ** GroupByAttribute **   <a name="securityhub-Type-InsightResults-GroupByAttribute"></a>
The attribute that the findings are grouped by for the insight whose results are returned by the `GetInsightResults` operation.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** InsightArn **   <a name="securityhub-Type-InsightResults-InsightArn"></a>
The ARN of the insight whose results are returned by the `GetInsightResults` operation.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** ResultValues **   <a name="securityhub-Type-InsightResults-ResultValues"></a>
The list of insight result values returned by the `GetInsightResults` operation.
Type: Array of [InsightResultValue](API_InsightResultValue.md) objects
Required: Yes

## See Also
<a name="API_InsightResults_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/InsightResults)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/InsightResults)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/InsightResults)
