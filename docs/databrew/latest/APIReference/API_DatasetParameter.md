---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_DatasetParameter.html
---

# DatasetParameter
<a name="API_DatasetParameter"></a>

Represents a dataset parameter that defines type and conditions for a parameter in the Amazon S3 path of the dataset.

## Contents
<a name="API_DatasetParameter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Name **   <a name="databrew-Type-DatasetParameter-Name"></a>
The name of the parameter that is used in the dataset's Amazon S3 path.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** Type **   <a name="databrew-Type-DatasetParameter-Type"></a>
The type of the dataset parameter, can be one of a 'String', 'Number' or 'Datetime'.
Type: String
Valid Values: `Datetime | Number | String`
Required: Yes

 ** CreateColumn **   <a name="databrew-Type-DatasetParameter-CreateColumn"></a>
Optional boolean value that defines whether the captured value of this parameter should be used to create a new column in a dataset.
Type: Boolean
Required: No

 ** DatetimeOptions **   <a name="databrew-Type-DatasetParameter-DatetimeOptions"></a>
Additional parameter options such as a format and a timezone. Required for datetime parameters.
Type: [DatetimeOptions](API_DatetimeOptions.md) object
Required: No

 ** Filter **   <a name="databrew-Type-DatasetParameter-Filter"></a>
The optional filter expression structure to apply additional matching criteria to the parameter.
Type: [FilterExpression](API_FilterExpression.md) object
Required: No

## See Also
<a name="API_DatasetParameter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/DatasetParameter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/DatasetParameter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/DatasetParameter)
