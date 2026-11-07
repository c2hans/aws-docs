---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DataQualityConfigurationV2.html
---

# DataQualityConfigurationV2
<a name="API_DataQualityConfigurationV2"></a>

The run configuration for a data quality result.

## Contents
<a name="API_DataQualityConfigurationV2_Contents"></a>

 ** ObservationMode **   <a name="Glue-Type-DataQualityConfigurationV2-ObservationMode"></a>
The observation mode for the run. Valid values are:
+  `SCHEDULED`
+  `FIXED`
Type: String
Valid Values: `SCHEDULED | FIXED`
Required: No

 ** ObservationsEnabled **   <a name="Glue-Type-DataQualityConfigurationV2-ObservationsEnabled"></a>
Whether observations are enabled for the run. Valid values are:
+  `ALL`
+  `NONE`
Type: String
Valid Values: `ALL | NONE`
Required: No

## See Also
<a name="API_DataQualityConfigurationV2_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DataQualityConfigurationV2)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DataQualityConfigurationV2)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DataQualityConfigurationV2)
