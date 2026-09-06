---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_KxClusterCodeDeploymentConfiguration.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# KxClusterCodeDeploymentConfiguration
<a name="API_KxClusterCodeDeploymentConfiguration"></a>

 The configuration that allows you to choose how you want to update code on a cluster. Depending on the option you choose, you can reduce the time it takes to update the cluster.

## Contents
<a name="API_KxClusterCodeDeploymentConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** deploymentStrategy **   <a name="finspace-Type-KxClusterCodeDeploymentConfiguration-deploymentStrategy"></a>
 The type of deployment that you want on a cluster.
+ ROLLING – This options updates the cluster by stopping the exiting q process and starting a new q process with updated configuration.
+ NO\_RESTART – This option updates the cluster without stopping the running q process. It is only available for `GP` type cluster. This option is quicker as it reduces the turn around time to update configuration on a cluster.

  With this deployment mode, you cannot update the `initializationScript` and `commandLineArguments` parameters.
+ FORCE – This option updates the cluster by immediately stopping all the running processes before starting up new ones with the updated configuration.
Type: String
Valid Values: `NO_RESTART | ROLLING | FORCE`
Required: Yes

## See Also
<a name="API_KxClusterCodeDeploymentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/KxClusterCodeDeploymentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/KxClusterCodeDeploymentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/KxClusterCodeDeploymentConfiguration)
