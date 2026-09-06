---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_FindingDetailsError.html
---

# FindingDetailsError
<a name="API_FindingDetailsError"></a>

Details about an error encountered when trying to return vulnerability data for a finding.

## Contents
<a name="API_FindingDetailsError_Contents"></a>

 ** errorCode **   <a name="inspector2-Type-FindingDetailsError-errorCode"></a>
The error code.
Type: String
Valid Values: `INTERNAL_ERROR | ACCESS_DENIED | FINDING_DETAILS_NOT_FOUND | INVALID_INPUT`
Required: Yes

 ** errorMessage **   <a name="inspector2-Type-FindingDetailsError-errorMessage"></a>
The error message.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** findingArn **   <a name="inspector2-Type-FindingDetailsError-findingArn"></a>
The finding ARN that returned an error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `arn:(aws[a-zA-Z-]*)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:finding/[a-f0-9]{32}`
Required: Yes

## See Also
<a name="API_FindingDetailsError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/FindingDetailsError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/FindingDetailsError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/FindingDetailsError)
