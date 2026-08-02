---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_EnvironmentDetailsIdentifiers.html
---

# EnvironmentDetailsIdentifiers
<a name="API_EnvironmentDetailsIdentifiers"></a>

The IDs of the job and environment.

## Contents
<a name="API_EnvironmentDetailsIdentifiers_Contents"></a>

 ** environmentId **   <a name="deadlinecloud-Type-EnvironmentDetailsIdentifiers-environmentId"></a>
The environment ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(STEP:step-[0-9a-f]{32}:.*)|(JOB:job-[0-9a-f]{32}:.*)`
Required: Yes

 ** jobId **   <a name="deadlinecloud-Type-EnvironmentDetailsIdentifiers-jobId"></a>
The job ID.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: Yes

## See Also
<a name="API_EnvironmentDetailsIdentifiers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/EnvironmentDetailsIdentifiers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/EnvironmentDetailsIdentifiers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/EnvironmentDetailsIdentifiers)
