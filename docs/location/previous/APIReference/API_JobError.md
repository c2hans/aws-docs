---
source_url: https://docs.aws.amazon.com/location/previous/APIReference/API_JobError.html
---

# JobError
<a name="API_JobError"></a>

Error information for failed jobs.

## Contents
<a name="API_JobError_Contents"></a>

 ** Code **   <a name="location-Type-JobError-Code"></a>
Error code indicating the type of error that occurred.
Type: String
Valid Values: `ValidationError | InternalServerError`
Required: Yes

 ** Messages **   <a name="location-Type-JobError-Messages"></a>
Error messages providing details about the failure.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 4 items.
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: No

## See Also
<a name="API_JobError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/location-2020-11-19/JobError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/location-2020-11-19/JobError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/location-2020-11-19/JobError)
