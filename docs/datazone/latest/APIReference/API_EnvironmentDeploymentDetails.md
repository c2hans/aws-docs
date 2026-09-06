---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_EnvironmentDeploymentDetails.html
---

# EnvironmentDeploymentDetails
<a name="API_EnvironmentDeploymentDetails"></a>

The environment deployment details.

## Contents
<a name="API_EnvironmentDeploymentDetails_Contents"></a>

 ** environmentFailureReasons **   <a name="datazone-Type-EnvironmentDeploymentDetails-environmentFailureReasons"></a>
Environment failure reasons.
Type: String to array of [EnvironmentError](API_EnvironmentError.md) objects map
Required: No

 ** overallDeploymentStatus **   <a name="datazone-Type-EnvironmentDeploymentDetails-overallDeploymentStatus"></a>
The overall deployment status of the environment.
Type: String
Valid Values: `PENDING_DEPLOYMENT | IN_PROGRESS | SUCCESSFUL | FAILED_VALIDATION | FAILED_DEPLOYMENT`
Required: No

## See Also
<a name="API_EnvironmentDeploymentDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/EnvironmentDeploymentDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/EnvironmentDeploymentDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/EnvironmentDeploymentDetails)
