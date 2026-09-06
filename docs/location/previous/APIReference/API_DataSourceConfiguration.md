---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_DataSourceConfiguration.html
---

# DataSourceConfiguration
<a name="API_DataSourceConfiguration"></a>

Specifies the data storage option chosen for requesting Places.

**Important**
When using Amazon Location Places:
If using HERE Technologies as a data provider, you can't store results for locations in Japan by setting `IntendedUse` to `Storage`. parameter.
Under the `MobileAssetTracking` or `MobilAssetManagement` pricing plan, you can't store results from your place index resources by setting `IntendedUse` to `Storage`. This returns a validation exception error.
For more information, see the [AWS Service Terms](https://aws.amazon.com/service-terms/) for Amazon Location Service.

## Contents
<a name="API_DataSourceConfiguration_Contents"></a>

 ** IntendedUse **   <a name="location-Type-DataSourceConfiguration-IntendedUse"></a>
Specifies how the results of an operation will be stored by the caller.
Valid values include:
+  `SingleUse` specifies that the results won't be stored.
+  `Storage` specifies that the result can be cached or stored in a database.
Default value: `SingleUse`
Type: String
Valid Values: `SingleUse | Storage`
Required: No

## See Also
<a name="API_DataSourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/DataSourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/DataSourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/DataSourceConfiguration)
