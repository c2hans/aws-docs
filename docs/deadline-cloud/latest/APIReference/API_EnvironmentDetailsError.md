---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_EnvironmentDetailsError.html
---

# EnvironmentDetailsError
<a name="API_EnvironmentDetailsError"></a>

The error details for the environment.

## Contents
<a name="API_EnvironmentDetailsError_Contents"></a>

 ** code **   <a name="deadlinecloud-Type-EnvironmentDetailsError-code"></a>
The error code.
Type: String
Valid Values: `AccessDeniedException | InternalServerException | ValidationException | ResourceNotFoundException | MaxPayloadSizeExceeded | ConflictException`
Required: Yes

 ** environmentId **   <a name="deadlinecloud-Type-EnvironmentDetailsError-environmentId"></a>
The environment ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(STEP:step-[0-9a-f]{32}:.*)|(JOB:job-[0-9a-f]{32}:.*)`
Required: Yes

 ** jobId **   <a name="deadlinecloud-Type-EnvironmentDetailsError-jobId"></a>
The job ID.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: Yes

 ** message **   <a name="deadlinecloud-Type-EnvironmentDetailsError-message"></a>
The error message detailing the error's cause.
Type: String
Required: Yes

## See Also
<a name="API_EnvironmentDetailsError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/EnvironmentDetailsError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/EnvironmentDetailsError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/EnvironmentDetailsError)
