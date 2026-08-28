---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_KxDeploymentConfiguration.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# KxDeploymentConfiguration
<a name="API_KxDeploymentConfiguration"></a>

 The configuration that allows you to choose how you want to update the databases on a cluster. Depending on the option you choose, you can reduce the time it takes to update the cluster.

## Contents
<a name="API_KxDeploymentConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** deploymentStrategy **   <a name="finspace-Type-KxDeploymentConfiguration-deploymentStrategy"></a>
 The type of deployment that you want on a cluster.
+ ROLLING – This options updates the cluster by stopping the exiting q process and starting a new q process with updated configuration.
+ NO\_RESTART – This option updates the cluster without stopping the running q process. It is only available for `HDB` type cluster. This option is quicker as it reduces the turn around time to update configuration on a cluster.

  With this deployment mode, you cannot update the `initializationScript` and `commandLineArguments` parameters.
Type: String
Valid Values: `NO_RESTART | ROLLING`
Required: Yes

## See Also
<a name="API_KxDeploymentConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/KxDeploymentConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/KxDeploymentConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/KxDeploymentConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
