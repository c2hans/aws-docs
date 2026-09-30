---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_EnvironmentDetailsEntity.html
---

# EnvironmentDetailsEntity
<a name="API_EnvironmentDetailsEntity"></a>

The details of a specified environment.

## Contents
<a name="API_EnvironmentDetailsEntity_Contents"></a>

 ** environmentId **   <a name="deadlinecloud-Type-EnvironmentDetailsEntity-environmentId"></a>
The environment ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(STEP:step-[0-9a-f]{32}:.*)|(JOB:job-[0-9a-f]{32}:.*)`
Required: Yes

 ** jobId **   <a name="deadlinecloud-Type-EnvironmentDetailsEntity-jobId"></a>
The job ID.
Type: String
Pattern: `job-[0-9a-f]{32}`
Required: Yes

 ** schemaVersion **   <a name="deadlinecloud-Type-EnvironmentDetailsEntity-schemaVersion"></a>
The schema version in the environment.
Type: String
Required: Yes

 ** template **   <a name="deadlinecloud-Type-EnvironmentDetailsEntity-template"></a>
The template used for the environment.
Type: JSON value
Required: Yes

 ** extensions **   <a name="deadlinecloud-Type-EnvironmentDetailsEntity-extensions"></a>
The Open Job Description extensions that the environment uses. This value is used by the worker agent.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 32 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[A-Z][A-Z0-9_]*`
Required: No

 ** resolvedSymbolTable **   <a name="deadlinecloud-Type-EnvironmentDetailsEntity-resolvedSymbolTable"></a>
The resolved symbol table for the environment's expressions, serialized as JSON. This value is used by the worker agent.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000000.
Required: No

## See Also
<a name="API_EnvironmentDetailsEntity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/EnvironmentDetailsEntity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/EnvironmentDetailsEntity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/EnvironmentDetailsEntity)
