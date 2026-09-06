---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_InsightResultValue.html
---

# InsightResultValue
<a name="API_InsightResultValue"></a>

The insight result values returned by the `GetInsightResults` operation.

## Contents
<a name="API_InsightResultValue_Contents"></a>

 ** Count **   <a name="securityhub-Type-InsightResultValue-Count"></a>
The number of findings returned for each `GroupByAttributeValue`.
Type: Integer
Required: Yes

 ** GroupByAttributeValue **   <a name="securityhub-Type-InsightResultValue-GroupByAttributeValue"></a>
The value of the attribute that the findings are grouped by for the insight whose results are returned by the `GetInsightResults` operation.
Type: String
Pattern: `.*\S.*`
Required: Yes

## See Also
<a name="API_InsightResultValue_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/InsightResultValue)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/InsightResultValue)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/InsightResultValue)
