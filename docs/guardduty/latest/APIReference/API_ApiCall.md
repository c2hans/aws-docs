---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ApiCall.html
---

# ApiCall
<a name="API_ApiCall"></a>

Contains information about an API call that was observed as part of an activity.

## Contents
<a name="API_ApiCall_Contents"></a>

 ** error **   <a name="guardduty-Type-ApiCall-error"></a>
The error code that was returned, if the API call failed.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Required: No

 ** operation **   <a name="guardduty-Type-ApiCall-operation"></a>
The name of the API operation that was invoked.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Required: No

 ** service **   <a name="guardduty-Type-ApiCall-service"></a>
The service that the API operation was invoked against.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 512.
Required: No

 ** userAgent **   <a name="guardduty-Type-ApiCall-userAgent"></a>
User agent in the request to the API operation
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_ApiCall_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/ApiCall)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/ApiCall)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/ApiCall)
