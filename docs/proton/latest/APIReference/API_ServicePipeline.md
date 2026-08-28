---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_ServicePipeline.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# ServicePipeline
<a name="API_ServicePipeline"></a>

Detailed data of an AWS Proton service instance pipeline resource.

## Contents
<a name="API_ServicePipeline_Contents"></a>

 ** arn **   <a name="proton-Type-ServicePipeline-arn"></a>
The Amazon Resource Name (ARN) of the service pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:(aws|aws-cn|aws-us-gov):[a-zA-Z0-9-]+:[a-zA-Z0-9-]*:\d{12}:([\w+=,.@-]+[/:])*[\w+=,.@-]+`
Required: Yes

 ** createdAt **   <a name="proton-Type-ServicePipeline-createdAt"></a>
The time when the service pipeline was created.
Type: Timestamp
Required: Yes

 ** deploymentStatus **   <a name="proton-Type-ServicePipeline-deploymentStatus"></a>
The deployment status of the service pipeline.
Type: String
Valid Values: `IN_PROGRESS | FAILED | SUCCEEDED | DELETE_IN_PROGRESS | DELETE_FAILED | DELETE_COMPLETE | CANCELLING | CANCELLED`
Required: Yes

 ** lastDeploymentAttemptedAt **   <a name="proton-Type-ServicePipeline-lastDeploymentAttemptedAt"></a>
The time when a deployment of the service pipeline was last attempted.
Type: Timestamp
Required: Yes

 ** lastDeploymentSucceededAt **   <a name="proton-Type-ServicePipeline-lastDeploymentSucceededAt"></a>
The time when the service pipeline was last deployed successfully.
Type: Timestamp
Required: Yes

 ** templateMajorVersion **   <a name="proton-Type-ServicePipeline-templateMajorVersion"></a>
The major version of the service template that was used to create the service pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: Yes

 ** templateMinorVersion **   <a name="proton-Type-ServicePipeline-templateMinorVersion"></a>
The minor version of the service template that was used to create the service pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: Yes

 ** templateName **   <a name="proton-Type-ServicePipeline-templateName"></a>
The name of the service template that was used to create the service pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** deploymentStatusMessage **   <a name="proton-Type-ServicePipeline-deploymentStatusMessage"></a>
A service pipeline deployment status message.
Type: String
Required: No

 ** lastAttemptedDeploymentId **   <a name="proton-Type-ServicePipeline-lastAttemptedDeploymentId"></a>
The ID of the last attempted deployment of this service pipeline.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** lastSucceededDeploymentId **   <a name="proton-Type-ServicePipeline-lastSucceededDeploymentId"></a>
The ID of the last successful deployment of this service pipeline.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** spec **   <a name="proton-Type-ServicePipeline-spec"></a>
The service spec that was used to create the service pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 51200.
Required: No

## See Also
<a name="API_ServicePipeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/ServicePipeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/ServicePipeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/ServicePipeline)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Proton. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query proton` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
