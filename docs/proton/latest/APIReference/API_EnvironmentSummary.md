---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_EnvironmentSummary.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# EnvironmentSummary
<a name="API_EnvironmentSummary"></a>

Summary data of an AWS Proton environment resource. An AWS Proton environment is a set of resources shared across AWS Proton services.

## Contents
<a name="API_EnvironmentSummary_Contents"></a>

 ** arn **   <a name="proton-Type-EnvironmentSummary-arn"></a>
The Amazon Resource Name (ARN) of the environment.
Type: String
Required: Yes

 ** createdAt **   <a name="proton-Type-EnvironmentSummary-createdAt"></a>
The time when the environment was created.
Type: Timestamp
Required: Yes

 ** deploymentStatus **   <a name="proton-Type-EnvironmentSummary-deploymentStatus"></a>
The environment deployment status.
Type: String
Valid Values: `IN_PROGRESS | FAILED | SUCCEEDED | DELETE_IN_PROGRESS | DELETE_FAILED | DELETE_COMPLETE | CANCELLING | CANCELLED`
Required: Yes

 ** lastDeploymentAttemptedAt **   <a name="proton-Type-EnvironmentSummary-lastDeploymentAttemptedAt"></a>
The time when a deployment of the environment was last attempted.
Type: Timestamp
Required: Yes

 ** lastDeploymentSucceededAt **   <a name="proton-Type-EnvironmentSummary-lastDeploymentSucceededAt"></a>
The time when the environment was last deployed successfully.
Type: Timestamp
Required: Yes

 ** name **   <a name="proton-Type-EnvironmentSummary-name"></a>
The name of the environment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** templateMajorVersion **   <a name="proton-Type-EnvironmentSummary-templateMajorVersion"></a>
The major version of the environment template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: Yes

 ** templateMinorVersion **   <a name="proton-Type-EnvironmentSummary-templateMinorVersion"></a>
The minor version of the environment template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: Yes

 ** templateName **   <a name="proton-Type-EnvironmentSummary-templateName"></a>
The name of the environment template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

 ** componentRoleArn **   <a name="proton-Type-EnvironmentSummary-componentRoleArn"></a>
The Amazon Resource Name (ARN) of the IAM service role that AWS Proton uses when provisioning directly defined components in this environment. It determines the scope of infrastructure that a component can provision.
The environment must have a `componentRoleArn` to allow directly defined components to be associated with the environment.
For more information about components, see [AWS Proton components](https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html) in the * AWS Proton User Guide*.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:(aws|aws-cn|aws-us-gov):[a-zA-Z0-9-]+:[a-zA-Z0-9-]*:\d{12}:([\w+=,.@-]+[/:])*[\w+=,.@-]+`
Required: No

 ** deploymentStatusMessage **   <a name="proton-Type-EnvironmentSummary-deploymentStatusMessage"></a>
An environment deployment status message.
Type: String
Required: No

 ** description **   <a name="proton-Type-EnvironmentSummary-description"></a>
The description of the environment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** environmentAccountConnectionId **   <a name="proton-Type-EnvironmentSummary-environmentAccountConnectionId"></a>
The ID of the environment account connection that the environment is associated with.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** environmentAccountId **   <a name="proton-Type-EnvironmentSummary-environmentAccountId"></a>
The ID of the environment account that the environment infrastructure resources are provisioned in.
Type: String
Pattern: `\d{12}`
Required: No

 ** lastAttemptedDeploymentId **   <a name="proton-Type-EnvironmentSummary-lastAttemptedDeploymentId"></a>
The ID of the last attempted deployment of this environment.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** lastSucceededDeploymentId **   <a name="proton-Type-EnvironmentSummary-lastSucceededDeploymentId"></a>
The ID of the last successful deployment of this environment.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** protonServiceRoleArn **   <a name="proton-Type-EnvironmentSummary-protonServiceRoleArn"></a>
The Amazon Resource Name (ARN) of the AWS Proton service role that allows AWS Proton to make calls to other services on your behalf.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Pattern: `arn:(aws|aws-cn|aws-us-gov):[a-zA-Z0-9-]+:[a-zA-Z0-9-]*:\d{12}:([\w+=,.@-]+[/:])*[\w+=,.@-]+`
Required: No

 ** provisioning **   <a name="proton-Type-EnvironmentSummary-provisioning"></a>
When included, indicates that the environment template is for customer provisioned and managed infrastructure.
Type: String
Valid Values: `CUSTOMER_MANAGED`
Required: No

## See Also
<a name="API_EnvironmentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/EnvironmentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/EnvironmentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/EnvironmentSummary)
