---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_ComponentSummary.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# ComponentSummary
<a name="API_ComponentSummary"></a>

Summary data of an AWS Proton component resource.

For more information about components, see [AWS Proton components](https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html) in the * AWS Proton User Guide*.

## Contents
<a name="API_ComponentSummary_Contents"></a>

 ** arn **   <a name="proton-Type-ComponentSummary-arn"></a>
The Amazon Resource Name (ARN) of the component.
Type: String
Required: Yes

 ** createdAt **   <a name="proton-Type-ComponentSummary-createdAt"></a>
The time when the component was created.
Type: Timestamp
Required: Yes

 ** deploymentStatus **   <a name="proton-Type-ComponentSummary-deploymentStatus"></a>
The component deployment status.
Type: String
Valid Values: `IN_PROGRESS | FAILED | SUCCEEDED | DELETE_IN_PROGRESS | DELETE_FAILED | DELETE_COMPLETE | CANCELLING | CANCELLED`
Required: Yes

 ** environmentName **   <a name="proton-Type-ComponentSummary-environmentName"></a>
The name of the AWS Proton environment that this component is associated with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** lastModifiedAt **   <a name="proton-Type-ComponentSummary-lastModifiedAt"></a>
The time when the component was last modified.
Type: Timestamp
Required: Yes

 ** name **   <a name="proton-Type-ComponentSummary-name"></a>
The name of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** deploymentStatusMessage **   <a name="proton-Type-ComponentSummary-deploymentStatusMessage"></a>
The message associated with the component deployment status.
Type: String
Required: No

 ** lastAttemptedDeploymentId **   <a name="proton-Type-ComponentSummary-lastAttemptedDeploymentId"></a>
The ID of the last attempted deployment of this component.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** lastDeploymentAttemptedAt **   <a name="proton-Type-ComponentSummary-lastDeploymentAttemptedAt"></a>
The time when a deployment of the component was last attempted.
Type: Timestamp
Required: No

 ** lastDeploymentSucceededAt **   <a name="proton-Type-ComponentSummary-lastDeploymentSucceededAt"></a>
The time when the component was last deployed successfully.
Type: Timestamp
Required: No

 ** lastSucceededDeploymentId **   <a name="proton-Type-ComponentSummary-lastSucceededDeploymentId"></a>
The ID of the last successful deployment of this component.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** serviceInstanceName **   <a name="proton-Type-ComponentSummary-serviceInstanceName"></a>
The name of the service instance that this component is attached to. Provided when a component is attached to a service instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: No

 ** serviceName **   <a name="proton-Type-ComponentSummary-serviceName"></a>
The name of the service that `serviceInstanceName` is associated with. Provided when a component is attached to a service instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: No

## See Also
<a name="API_ComponentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/ComponentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/ComponentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/ComponentSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
