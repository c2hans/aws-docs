---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_ServiceInstance.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# ServiceInstance
<a name="API_ServiceInstance"></a>

Detailed data of an AWS Proton service instance resource.

## Contents
<a name="API_ServiceInstance_Contents"></a>

 ** arn **   <a name="proton-Type-ServiceInstance-arn"></a>
The Amazon Resource Name (ARN) of the service instance.
Type: String
Required: Yes

 ** createdAt **   <a name="proton-Type-ServiceInstance-createdAt"></a>
The time when the service instance was created.
Type: Timestamp
Required: Yes

 ** deploymentStatus **   <a name="proton-Type-ServiceInstance-deploymentStatus"></a>
The service instance deployment status.
Type: String
Valid Values: `IN_PROGRESS | FAILED | SUCCEEDED | DELETE_IN_PROGRESS | DELETE_FAILED | DELETE_COMPLETE | CANCELLING | CANCELLED`
Required: Yes

 ** environmentName **   <a name="proton-Type-ServiceInstance-environmentName"></a>
The name of the environment that the service instance was deployed into.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** lastDeploymentAttemptedAt **   <a name="proton-Type-ServiceInstance-lastDeploymentAttemptedAt"></a>
The time when a deployment of the service instance was last attempted.
Type: Timestamp
Required: Yes

 ** lastDeploymentSucceededAt **   <a name="proton-Type-ServiceInstance-lastDeploymentSucceededAt"></a>
The time when the service instance was last deployed successfully.
Type: Timestamp
Required: Yes

 ** name **   <a name="proton-Type-ServiceInstance-name"></a>
The name of the service instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** serviceName **   <a name="proton-Type-ServiceInstance-serviceName"></a>
The name of the service that the service instance belongs to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** templateMajorVersion **   <a name="proton-Type-ServiceInstance-templateMajorVersion"></a>
The major version of the service template that was used to create the service instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: Yes

 ** templateMinorVersion **   <a name="proton-Type-ServiceInstance-templateMinorVersion"></a>
The minor version of the service template that was used to create the service instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: Yes

 ** templateName **   <a name="proton-Type-ServiceInstance-templateName"></a>
The name of the service template that was used to create the service instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** deploymentStatusMessage **   <a name="proton-Type-ServiceInstance-deploymentStatusMessage"></a>
The message associated with the service instance deployment status.
Type: String
Required: No

 ** lastAttemptedDeploymentId **   <a name="proton-Type-ServiceInstance-lastAttemptedDeploymentId"></a>
The ID of the last attempted deployment of this service instance.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** lastClientRequestToken **   <a name="proton-Type-ServiceInstance-lastClientRequestToken"></a>
The last client request token received.
Type: String
Required: No

 ** lastSucceededDeploymentId **   <a name="proton-Type-ServiceInstance-lastSucceededDeploymentId"></a>
The ID of the last successful deployment of this service instance.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** spec **   <a name="proton-Type-ServiceInstance-spec"></a>
The service spec that was used to create the service instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Required: No

## See Also
<a name="API_ServiceInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/ServiceInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/ServiceInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/ServiceInstance)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
