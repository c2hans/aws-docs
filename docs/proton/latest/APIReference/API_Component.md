---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_Component.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# Component
<a name="API_Component"></a>

Detailed data of an AWS Proton component resource.

For more information about components, see [AWS Proton components](https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html) in the * AWS Proton User Guide*.

## Contents
<a name="API_Component_Contents"></a>

 ** arn **   <a name="proton-Type-Component-arn"></a>
The Amazon Resource Name (ARN) of the component.
Type: String
Required: Yes

 ** createdAt **   <a name="proton-Type-Component-createdAt"></a>
The time when the component was created.
Type: Timestamp
Required: Yes

 ** deploymentStatus **   <a name="proton-Type-Component-deploymentStatus"></a>
The component deployment status.
Type: String
Valid Values: `IN_PROGRESS | FAILED | SUCCEEDED | DELETE_IN_PROGRESS | DELETE_FAILED | DELETE_COMPLETE | CANCELLING | CANCELLED`
Required: Yes

 ** environmentName **   <a name="proton-Type-Component-environmentName"></a>
The name of the AWS Proton environment that this component is associated with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** lastModifiedAt **   <a name="proton-Type-Component-lastModifiedAt"></a>
The time when the component was last modified.
Type: Timestamp
Required: Yes

 ** name **   <a name="proton-Type-Component-name"></a>
The name of the component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** deploymentStatusMessage **   <a name="proton-Type-Component-deploymentStatusMessage"></a>
The message associated with the component deployment status.
Type: String
Required: No

 ** description **   <a name="proton-Type-Component-description"></a>
A description of the component.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** lastAttemptedDeploymentId **   <a name="proton-Type-Component-lastAttemptedDeploymentId"></a>
The ID of the last attempted deployment of this component.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** lastClientRequestToken **   <a name="proton-Type-Component-lastClientRequestToken"></a>
The last token the client requested.
Type: String
Required: No

 ** lastDeploymentAttemptedAt **   <a name="proton-Type-Component-lastDeploymentAttemptedAt"></a>
The time when a deployment of the component was last attempted.
Type: Timestamp
Required: No

 ** lastDeploymentSucceededAt **   <a name="proton-Type-Component-lastDeploymentSucceededAt"></a>
The time when the component was last deployed successfully.
Type: Timestamp
Required: No

 ** lastSucceededDeploymentId **   <a name="proton-Type-Component-lastSucceededDeploymentId"></a>
The ID of the last successful deployment of this component.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** serviceInstanceName **   <a name="proton-Type-Component-serviceInstanceName"></a>
The name of the service instance that this component is attached to. Provided when a component is attached to a service instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: No

 ** serviceName **   <a name="proton-Type-Component-serviceName"></a>
The name of the service that `serviceInstanceName` is associated with. Provided when a component is attached to a service instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: No

 ** serviceSpec **   <a name="proton-Type-Component-serviceSpec"></a>
The service spec that the component uses to access service inputs. Provided when a component is attached to a service instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Required: No

## See Also
<a name="API_Component_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/Component)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/Component)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/Component)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
