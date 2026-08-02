---
source_url: https://docs.aws.amazon.com/detective/latest/APIReference/API_ImpossibleTravelDetail.html
---

# ImpossibleTravelDetail
<a name="API_ImpossibleTravelDetail"></a>

Contains information on unusual and impossible travel in an account.

## Contents
<a name="API_ImpossibleTravelDetail_Contents"></a>

 ** EndingIpAddress **   <a name="detective-Type-ImpossibleTravelDetail-EndingIpAddress"></a>
IP address where the resource was last used in the impossible travel.
Type: String
Required: No

 ** EndingLocation **   <a name="detective-Type-ImpossibleTravelDetail-EndingLocation"></a>
Location where the resource was last used in the impossible travel.
Type: String
Required: No

 ** HourlyTimeDelta **   <a name="detective-Type-ImpossibleTravelDetail-HourlyTimeDelta"></a>
Returns the time difference between the first and last timestamp the resource was used.
Type: Integer
Required: No

 ** StartingIpAddress **   <a name="detective-Type-ImpossibleTravelDetail-StartingIpAddress"></a>
IP address where the resource was first used in the impossible travel.
Type: String
Required: No

 ** StartingLocation **   <a name="detective-Type-ImpossibleTravelDetail-StartingLocation"></a>
Location where the resource was first used in the impossible travel.
Type: String
Required: No

## See Also
<a name="API_ImpossibleTravelDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/detective-2018-10-26/ImpossibleTravelDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/detective-2018-10-26/ImpossibleTravelDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/detective-2018-10-26/ImpossibleTravelDetail)
