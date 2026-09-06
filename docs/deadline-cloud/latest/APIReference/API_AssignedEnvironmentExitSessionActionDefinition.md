---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_AssignedEnvironmentExitSessionActionDefinition.html
---

# AssignedEnvironmentExitSessionActionDefinition
<a name="API_AssignedEnvironmentExitSessionActionDefinition"></a>

The assigned environment when a worker exits a session.

## Contents
<a name="API_AssignedEnvironmentExitSessionActionDefinition_Contents"></a>

 ** environmentId **   <a name="deadlinecloud-Type-AssignedEnvironmentExitSessionActionDefinition-environmentId"></a>
The environment ID of the assigned environment when exiting a session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `(STEP:step-[0-9a-f]{32}:.*)|(JOB:job-[0-9a-f]{32}:.*)`
Required: Yes

## See Also
<a name="API_AssignedEnvironmentExitSessionActionDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/AssignedEnvironmentExitSessionActionDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/AssignedEnvironmentExitSessionActionDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/AssignedEnvironmentExitSessionActionDefinition)
