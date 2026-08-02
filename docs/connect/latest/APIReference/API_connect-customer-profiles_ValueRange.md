---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_ValueRange.html
---

# ValueRange
<a name="API_connect-customer-profiles_ValueRange"></a>

A structure letting customers specify a relative time window over which over which data is included in the Calculated Attribute. Use positive numbers to indicate that the endpoint is in the past, and negative numbers to indicate it is in the future. ValueRange overrides Value.

## Contents
<a name="API_connect-customer-profiles_ValueRange_Contents"></a>

 ** End **   <a name="connect-Type-connect-customer-profiles_ValueRange-End"></a>
The end time of when to include objects. Use positive numbers to indicate that the starting point is in the past, and negative numbers to indicate it is in the future.
Type: Integer
Required: Yes

 ** Start **   <a name="connect-Type-connect-customer-profiles_ValueRange-Start"></a>
The start time of when to include objects. Use positive numbers to indicate that the starting point is in the past, and negative numbers to indicate it is in the future.
Type: Integer
Required: Yes

## See Also
<a name="API_connect-customer-profiles_ValueRange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ValueRange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ValueRange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ValueRange)
