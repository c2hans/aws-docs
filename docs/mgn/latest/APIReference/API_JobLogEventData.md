---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_JobLogEventData.html
---

# JobLogEventData
<a name="API_JobLogEventData"></a>

Job log data

## Contents
<a name="API_JobLogEventData_Contents"></a>

 ** attemptCount **   <a name="mgn-Type-JobLogEventData-attemptCount"></a>
Retries for this operation.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** conversionServerID **   <a name="mgn-Type-JobLogEventData-conversionServerID"></a>
Job Event conversion Server ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `i-[0-9a-fA-F]{8,}`
Required: No

 ** maxAttemptsCount **   <a name="mgn-Type-JobLogEventData-maxAttemptsCount"></a>
The maximum number of retries that will be attempted if this operation failed.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** rawError **   <a name="mgn-Type-JobLogEventData-rawError"></a>
Job error.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 65536.
Required: No

 ** sourceServerID **   <a name="mgn-Type-JobLogEventData-sourceServerID"></a>
Job Event Source Server ID.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`
Required: No

 ** targetInstanceID **   <a name="mgn-Type-JobLogEventData-targetInstanceID"></a>
Job Event Target instance ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `i-[0-9a-fA-F]{8,}`
Required: No

## See Also
<a name="API_JobLogEventData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/JobLogEventData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/JobLogEventData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/JobLogEventData)
