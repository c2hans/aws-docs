---
source_url: https://docs.aws.amazon.com/emr-on-eks/latest/APIReference/API_ParametricConfigurationOverrides.html
---

# ParametricConfigurationOverrides
<a name="API_ParametricConfigurationOverrides"></a>

 A configuration specification to be used to override existing configurations. This data type allows job template parameters to be specified within.

## Contents
<a name="API_ParametricConfigurationOverrides_Contents"></a>

 ** applicationConfiguration **   <a name="emroneks-Type-ParametricConfigurationOverrides-applicationConfiguration"></a>
 The configurations for the application running by the job run.
Type: Array of [Configuration](API_Configuration.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** monitoringConfiguration **   <a name="emroneks-Type-ParametricConfigurationOverrides-monitoringConfiguration"></a>
 The configurations for monitoring.
Type: [ParametricMonitoringConfiguration](API_ParametricMonitoringConfiguration.md) object
Required: No

## See Also
<a name="API_ParametricConfigurationOverrides_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-containers-2020-10-01/ParametricConfigurationOverrides)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-containers-2020-10-01/ParametricConfigurationOverrides)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-containers-2020-10-01/ParametricConfigurationOverrides)
