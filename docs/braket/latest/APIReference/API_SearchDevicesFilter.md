---
source_url: https://docs.aws.amazon.com/braket/latest/APIReference/API_SearchDevicesFilter.html
---

# SearchDevicesFilter
<a name="API_SearchDevicesFilter"></a>

The filter used to search for devices.

## Contents
<a name="API_SearchDevicesFilter_Contents"></a>

 ** name **   <a name="braket-Type-SearchDevicesFilter-name"></a>
The name of the device parameter to filter based on. Only `deviceArn` filter name is currently supported.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** values **   <a name="braket-Type-SearchDevicesFilter-values"></a>
The values used to filter devices based on the filter name.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_SearchDevicesFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/braket-2019-09-01/SearchDevicesFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/braket-2019-09-01/SearchDevicesFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/braket-2019-09-01/SearchDevicesFilter)
