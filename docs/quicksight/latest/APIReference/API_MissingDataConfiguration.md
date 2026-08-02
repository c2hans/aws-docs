---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_MissingDataConfiguration.html
---

# MissingDataConfiguration
<a name="API_MissingDataConfiguration"></a>

The configuration options that determine how missing data is treated during the rendering of a line chart.

## Contents
<a name="API_MissingDataConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** TreatmentOption **   <a name="QS-Type-MissingDataConfiguration-TreatmentOption"></a>
The treatment option that determines how missing data should be rendered. Choose from the following options:
+  `INTERPOLATE`: Interpolate missing values between the prior and the next known value.
+  `SHOW_AS_ZERO`: Show missing values as the value `0`.
+  `SHOW_AS_BLANK`: Display a blank space when rendering missing data.
Type: String
Valid Values: `INTERPOLATE | SHOW_AS_ZERO | SHOW_AS_BLANK`
Required: No

## See Also
<a name="API_MissingDataConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/MissingDataConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/MissingDataConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/MissingDataConfiguration)
