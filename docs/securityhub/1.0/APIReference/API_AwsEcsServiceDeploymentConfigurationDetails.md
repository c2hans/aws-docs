---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsServiceDeploymentConfigurationDetails.html
---

# AwsEcsServiceDeploymentConfigurationDetails
<a name="API_AwsEcsServiceDeploymentConfigurationDetails"></a>

Optional deployment parameters for the service.

## Contents
<a name="API_AwsEcsServiceDeploymentConfigurationDetails_Contents"></a>

 ** DeploymentCircuitBreaker **   <a name="securityhub-Type-AwsEcsServiceDeploymentConfigurationDetails-DeploymentCircuitBreaker"></a>
Determines whether a service deployment fails if a service cannot reach a steady state.
Type: [AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetails](API_AwsEcsServiceDeploymentConfigurationDeploymentCircuitBreakerDetails.md) object
Required: No

 ** MaximumPercent **   <a name="securityhub-Type-AwsEcsServiceDeploymentConfigurationDetails-MaximumPercent"></a>
For a service that uses the rolling update (`ECS`) deployment type, the maximum number of tasks in a service that are allowed in the `RUNNING` or `PENDING` state during a deployment, and for tasks that use the EC2 launch type, when any container instances are in the `DRAINING` state. Provided as a percentage of the desired number of tasks. The default value is 200%.
For a service that uses the blue/green (`CODE_DEPLOY`) or `EXTERNAL` deployment types, and tasks that use the EC2 launch type, the maximum number of tasks in the service that remain in the `RUNNING` state while the container instances are in the `DRAINING` state.
For the Fargate launch type, the maximum percent value is not used.
Type: Integer
Required: No

 ** MinimumHealthyPercent **   <a name="securityhub-Type-AwsEcsServiceDeploymentConfigurationDetails-MinimumHealthyPercent"></a>
For a service that uses the rolling update (`ECS`) deployment type, the minimum number of tasks in a service that must remain in the `RUNNING` state during a deployment, and while any container instances are in the `DRAINING` state if the service contains tasks using the EC2 launch type. Expressed as a percentage of the desired number of tasks. The default value is 100%.
For a service that uses the blue/green (`CODE_DEPLOY`) or `EXTERNAL` deployment types and tasks that use the EC2 launch type, the minimum number of the tasks in the service that remain in the `RUNNING` state while the container instances are in the `DRAINING` state.
For the Fargate launch type, the minimum healthy percent value is not used.
Type: Integer
Required: No

## See Also
<a name="API_AwsEcsServiceDeploymentConfigurationDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsServiceDeploymentConfigurationDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsServiceDeploymentConfigurationDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsServiceDeploymentConfigurationDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
