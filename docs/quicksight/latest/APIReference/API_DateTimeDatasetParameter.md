---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_DateTimeDatasetParameter.html
---

# DateTimeDatasetParameter
<a name="API_DateTimeDatasetParameter"></a>

A date time parameter for a dataset.

## Contents
<a name="API_DateTimeDatasetParameter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Id **   <a name="QS-Type-DateTimeDatasetParameter-Id"></a>
An identifier for the parameter that is created in the dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-zA-Z0-9-]+$`
Required: Yes

 ** Name **   <a name="QS-Type-DateTimeDatasetParameter-Name"></a>
The name of the date time parameter that is created in the dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^[a-zA-Z0-9]+$`
Required: Yes

 ** ValueType **   <a name="QS-Type-DateTimeDatasetParameter-ValueType"></a>
The value type of the dataset parameter. Valid values are `single value` or `multi value`.
Type: String
Valid Values: `MULTI_VALUED | SINGLE_VALUED`
Required: Yes

 ** DefaultValues **   <a name="QS-Type-DateTimeDatasetParameter-DefaultValues"></a>
A list of default values for a given date time parameter. This structure only accepts static values.
Type: [DateTimeDatasetParameterDefaultValues](API_DateTimeDatasetParameterDefaultValues.md) object
Required: No

 ** TimeGranularity **   <a name="QS-Type-DateTimeDatasetParameter-TimeGranularity"></a>
The time granularity of the date time parameter.
Type: String
Valid Values: `YEAR | QUARTER | MONTH | WEEK | DAY | HOUR | MINUTE | SECOND | MILLISECOND`
Required: No

## See Also
<a name="API_DateTimeDatasetParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/DateTimeDatasetParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/DateTimeDatasetParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/DateTimeDatasetParameter)
