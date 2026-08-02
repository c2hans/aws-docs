---
source_url: https://docs.aws.amazon.com/access-analyzer/latest/APIReference/API_JobError.html
---

# JobError
<a name="API_JobError"></a>

Contains the details about the policy generation error.

## Contents
<a name="API_JobError_Contents"></a>

 ** code **   <a name="accessanalyzer-Type-JobError-code"></a>
The job error code.
Type: String
Valid Values: `AUTHORIZATION_ERROR | RESOURCE_NOT_FOUND_ERROR | SERVICE_QUOTA_EXCEEDED_ERROR | SERVICE_ERROR`
Required: Yes

 ** message **   <a name="accessanalyzer-Type-JobError-message"></a>
Specific information about the error. For example, which service quota was exceeded or which resource was not found.
Type: String
Required: Yes

## See Also
<a name="API_JobError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/accessanalyzer-2019-11-01/JobError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/accessanalyzer-2019-11-01/JobError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/accessanalyzer-2019-11-01/JobError)
