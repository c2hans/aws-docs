---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_ReferenceLineDataConfiguration.html
---

# ReferenceLineDataConfiguration
<a name="API_ReferenceLineDataConfiguration"></a>

The data configuration of the reference line.

## Contents
<a name="API_ReferenceLineDataConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AxisBinding **   <a name="QS-Type-ReferenceLineDataConfiguration-AxisBinding"></a>
The axis binding type of the reference line. Choose one of the following options:
+  `PrimaryY`
+  `SecondaryY`
Type: String
Valid Values: `PRIMARY_YAXIS | SECONDARY_YAXIS`
Required: No

 ** DynamicConfiguration **   <a name="QS-Type-ReferenceLineDataConfiguration-DynamicConfiguration"></a>
The dynamic configuration of the reference line data configuration.
Type: [ReferenceLineDynamicDataConfiguration](API_ReferenceLineDynamicDataConfiguration.md) object
Required: No

 ** SeriesType **   <a name="QS-Type-ReferenceLineDataConfiguration-SeriesType"></a>
The series type of the reference line data configuration. Choose one of the following options:
+  `BAR`
+  `LINE`
Type: String
Valid Values: `BAR | LINE`
Required: No

 ** StaticConfiguration **   <a name="QS-Type-ReferenceLineDataConfiguration-StaticConfiguration"></a>
The static data configuration of the reference line data configuration.
Type: [ReferenceLineStaticDataConfiguration](API_ReferenceLineStaticDataConfiguration.md) object
Required: No

## See Also
<a name="API_ReferenceLineDataConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/ReferenceLineDataConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/ReferenceLineDataConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/ReferenceLineDataConfiguration)
