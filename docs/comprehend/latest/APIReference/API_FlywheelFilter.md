---
source_url: https://docs.aws.amazon.com/comprehend/latest/APIReference/API_FlywheelFilter.html
---

# FlywheelFilter
<a name="API_FlywheelFilter"></a>

Filter the flywheels based on creation time or flywheel status.

## Contents
<a name="API_FlywheelFilter_Contents"></a>

 ** CreationTimeAfter **   <a name="comprehend-Type-FlywheelFilter-CreationTimeAfter"></a>
Filter the flywheels to include flywheels created after the specified time.
Type: Timestamp
Required: No

 ** CreationTimeBefore **   <a name="comprehend-Type-FlywheelFilter-CreationTimeBefore"></a>
Filter the flywheels to include flywheels created before the specified time.
Type: Timestamp
Required: No

 ** Status **   <a name="comprehend-Type-FlywheelFilter-Status"></a>
Filter the flywheels based on the flywheel status.
Type: String
Valid Values: `CREATING | ACTIVE | UPDATING | DELETING | FAILED`
Required: No

## See Also
<a name="API_FlywheelFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/comprehend-2017-11-27/FlywheelFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/comprehend-2017-11-27/FlywheelFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/comprehend-2017-11-27/FlywheelFilter)
