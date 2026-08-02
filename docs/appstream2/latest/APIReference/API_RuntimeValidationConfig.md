---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_RuntimeValidationConfig.html
---

# RuntimeValidationConfig
<a name="API_RuntimeValidationConfig"></a>

Configuration for runtime validation of imported images. This structure specifies the instance type to use for testing the imported image's streaming capabilities.

## Contents
<a name="API_RuntimeValidationConfig_Contents"></a>

 ** IntendedInstanceType **   <a name="WorkSpacesApplications-Type-RuntimeValidationConfig-IntendedInstanceType"></a>
The instance type to use for runtime validation testing. It's recommended to use the same instance type you plan to use for your fleet to ensure accurate validation results.
Type: String
Pattern: `^[a-zA-Z0-9-]+(\.[a-z0-9-]+)+\.(small|medium|large|xlarge|\d+xlarge|metal)$`
Required: No

## See Also
<a name="API_RuntimeValidationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/RuntimeValidationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/RuntimeValidationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/RuntimeValidationConfig)
