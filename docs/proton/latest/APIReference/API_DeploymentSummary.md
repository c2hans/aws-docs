---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_DeploymentSummary.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# DeploymentSummary
<a name="API_DeploymentSummary"></a>

Summary data of the deployment.

## Contents
<a name="API_DeploymentSummary_Contents"></a>

 ** arn **   <a name="proton-Type-DeploymentSummary-arn"></a>
The Amazon Resource Name (ARN) of the deployment.
Type: String
Required: Yes

 ** createdAt **   <a name="proton-Type-DeploymentSummary-createdAt"></a>
The date and time the deployment was created.
Type: Timestamp
Required: Yes

 ** deploymentStatus **   <a name="proton-Type-DeploymentSummary-deploymentStatus"></a>
The current status of the deployment.
Type: String
Valid Values: `IN_PROGRESS | FAILED | SUCCEEDED | DELETE_IN_PROGRESS | DELETE_FAILED | DELETE_COMPLETE | CANCELLING | CANCELLED`
Required: Yes

 ** environmentName **   <a name="proton-Type-DeploymentSummary-environmentName"></a>
The name of the environment associated with the deployment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** id **   <a name="proton-Type-DeploymentSummary-id"></a>
The ID of the deployment.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** lastModifiedAt **   <a name="proton-Type-DeploymentSummary-lastModifiedAt"></a>
The date and time the deployment was last modified.
Type: Timestamp
Required: Yes

 ** targetArn **   <a name="proton-Type-DeploymentSummary-targetArn"></a>
The Amazon Resource Name (ARN) of the target of the deployment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:(aws|aws-cn|aws-us-gov):[a-zA-Z0-9-]+:[a-zA-Z0-9-]*:\d{12}:([\w+=,.@-]+[/:])*[\w+=,.@-]+`
Required: Yes

 ** targetResourceCreatedAt **   <a name="proton-Type-DeploymentSummary-targetResourceCreatedAt"></a>
The date and time the target resource was created.
Type: Timestamp
Required: Yes

 ** targetResourceType **   <a name="proton-Type-DeploymentSummary-targetResourceType"></a>
The resource type of the deployment target. It can be an environment, service, service instance, or component.
Type: String
Valid Values: `ENVIRONMENT | SERVICE_PIPELINE | SERVICE_INSTANCE | COMPONENT`
Required: Yes

 ** completedAt **   <a name="proton-Type-DeploymentSummary-completedAt"></a>
The date and time the deployment was completed.
Type: Timestamp
Required: No

 ** componentName **   <a name="proton-Type-DeploymentSummary-componentName"></a>
The name of the component associated with the deployment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: No

 ** lastAttemptedDeploymentId **   <a name="proton-Type-DeploymentSummary-lastAttemptedDeploymentId"></a>
The ID of the last attempted deployment.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** lastSucceededDeploymentId **   <a name="proton-Type-DeploymentSummary-lastSucceededDeploymentId"></a>
The ID of the last successful deployment.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** serviceInstanceName **   <a name="proton-Type-DeploymentSummary-serviceInstanceName"></a>
The name of the service instance associated with the deployment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: No

 ** serviceName **   <a name="proton-Type-DeploymentSummary-serviceName"></a>
The name of the service associated with the deployment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: No

## See Also
<a name="API_DeploymentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/DeploymentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/DeploymentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/DeploymentSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
