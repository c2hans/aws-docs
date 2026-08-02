---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetails.html
---

# AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetails
<a name="API_AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetails"></a>

Determines whether a service deployment fails if a service cannot reach a steady state.

## Contents
<a name="API_AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetails_Contents"></a>

 ** Enable **   <a name="securityhub-Type-AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetails-Enable"></a>
Whether to enable the deployment circuit breaker logic for the service.
Type: Boolean
Required: No

 ** Rollback **   <a name="securityhub-Type-AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetails-Rollback"></a>
Whether to roll back the service if a service deployment fails. If rollback is enabled, when a service deployment fails, the service is rolled back to the last deployment that completed successfully.
Type: Boolean
Required: No

## See Also
<a name="API_AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetails)
