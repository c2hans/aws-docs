---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsServiceDeploymentControllerDetails.html
---

# AwsEcsServiceDeploymentControllerDetails
<a name="API_AwsEcsServiceDeploymentControllerDetails"></a>

Information about the deployment controller type that the service uses.

## Contents
<a name="API_AwsEcsServiceDeploymentControllerDetails_Contents"></a>

 ** Type **   <a name="securityhub-Type-AwsEcsServiceDeploymentControllerDetails-Type"></a>
The rolling update (`ECS`) deployment type replaces the current running version of the container with the latest version.
The blue/green (`CODE_DEPLOY`) deployment type uses the blue/green deployment model that is powered by AWS CodeDeploy. This deployment model a new deployment of a service can be verified before production traffic is sent to it.
The external (`EXTERNAL`) deployment type allows the use of any third-party deployment controller for full control over the deployment process for an Amazon ECS service.
Valid values: `ECS` \| `CODE_DEPLOY` \| `EXTERNAL`
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsEcsServiceDeploymentControllerDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsServiceDeploymentControllerDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsServiceDeploymentControllerDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsServiceDeploymentControllerDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
