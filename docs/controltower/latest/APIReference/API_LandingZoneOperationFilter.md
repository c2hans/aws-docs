---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_LandingZoneOperationFilter.html
---

# LandingZoneOperationFilter
<a name="API_LandingZoneOperationFilter"></a>

A filter object that lets you call `ListLandingZoneOperations` with a specific filter.

## Contents
<a name="API_LandingZoneOperationFilter_Contents"></a>

 ** statuses **   <a name="controltower-Type-LandingZoneOperationFilter-statuses"></a>
The statuses of the set of landing zone operations selected by the filter.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `SUCCEEDED | FAILED | IN_PROGRESS`
Required: No

 ** types **   <a name="controltower-Type-LandingZoneOperationFilter-types"></a>
The set of landing zone operation types selected by the filter.
Type: Array of strings
Array Members: Fixed number of 1 item.
Valid Values: `DELETE | CREATE | UPDATE | RESET`
Required: No

## See Also
<a name="API_LandingZoneOperationFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/LandingZoneOperationFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/LandingZoneOperationFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/LandingZoneOperationFilter)
