---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_CapacityReservationFilter.html
---

# CapacityReservationFilter

A filter for the `ListCapacityReservations` operation. A reservation matches the filter when its value for `Name` equals any of the values in `Values`.

## Contents
<a name="API_CapacityReservationFilter_Contents"></a>

 ** Name **   <a name="sagemaker-Type-CapacityReservationFilter-Name"></a>
The name of the field to filter on. The only supported value is `Status`.
Type: String
Valid Values: `Status`
Required: Yes

 ** Values **   <a name="sagemaker-Type-CapacityReservationFilter-Values"></a>
The values to match. For the `Status` filter, valid values are `Scheduled`, `Active`, and `Expired`. Values are case sensitive. You can specify up to 10 values.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(Scheduled|Active|Expired)`
Required: Yes

## See Also
<a name="API_CapacityReservationFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/CapacityReservationFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/CapacityReservationFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/CapacityReservationFilter)
