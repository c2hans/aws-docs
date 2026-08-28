---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_AssetItemAdditionalAttributes.html
---

# AssetItemAdditionalAttributes
<a name="API_AssetItemAdditionalAttributes"></a>

The additional attributes of an inventory asset.

## Contents
<a name="API_AssetItemAdditionalAttributes_Contents"></a>

 ** formsOutput **   <a name="datazone-Type-AssetItemAdditionalAttributes-formsOutput"></a>
The forms included in the additional attributes of an inventory asset.
Type: Array of [FormOutput](API_FormOutput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

 ** latestTimeSeriesDataPointFormsOutput **   <a name="datazone-Type-AssetItemAdditionalAttributes-latestTimeSeriesDataPointFormsOutput"></a>
The latest time series data points forms included in the additional attributes of an asset.
Type: Array of [TimeSeriesDataPointSummaryFormOutput](API_TimeSeriesDataPointSummaryFormOutput.md) objects
Required: No

 ** matchRationale **   <a name="datazone-Type-AssetItemAdditionalAttributes-matchRationale"></a>
List of rationales indicating why this item was matched by search.
Type: Array of [MatchRationaleItem](API_MatchRationaleItem.md) objects
Required: No

 ** readOnlyFormsOutput **   <a name="datazone-Type-AssetItemAdditionalAttributes-readOnlyFormsOutput"></a>
The read-only forms included in the additional attributes of an inventory asset.
Type: Array of [FormOutput](API_FormOutput.md) objects
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: No

## See Also
<a name="API_AssetItemAdditionalAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/AssetItemAdditionalAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/AssetItemAdditionalAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/AssetItemAdditionalAttributes)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
