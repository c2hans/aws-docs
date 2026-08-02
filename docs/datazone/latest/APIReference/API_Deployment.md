---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_Deployment.html
---

# Deployment
<a name="API_Deployment"></a>

The details of the last deployment of the environment.

## Contents
<a name="API_Deployment_Contents"></a>

 ** deploymentId **   <a name="datazone-Type-Deployment-deploymentId"></a>
The identifier of the last deployment of the environment.
Type: String
Required: No

 ** deploymentStatus **   <a name="datazone-Type-Deployment-deploymentStatus"></a>
The status of the last deployment of the environment.
Type: String
Valid Values: `IN_PROGRESS | SUCCESSFUL | FAILED | PENDING_DEPLOYMENT`
Required: No

 ** deploymentType **   <a name="datazone-Type-Deployment-deploymentType"></a>
The type of the last deployment of the environment.
Type: String
Valid Values: `CREATE | UPDATE | DELETE`
Required: No

 ** failureReason **   <a name="datazone-Type-Deployment-failureReason"></a>
The failure reason of the last deployment of the environment.
Type: [EnvironmentError](API_EnvironmentError.md) object
Required: No

 ** isDeploymentComplete **   <a name="datazone-Type-Deployment-isDeploymentComplete"></a>
Specifies whether the last deployment of the environment is complete.
Type: Boolean
Required: No

 ** messages **   <a name="datazone-Type-Deployment-messages"></a>
The messages of the last deployment of the environment.
Type: Array of strings
Required: No

## See Also
<a name="API_Deployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/Deployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/Deployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/Deployment)
