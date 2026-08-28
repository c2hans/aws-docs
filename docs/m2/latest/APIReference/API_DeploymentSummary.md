---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_DeploymentSummary.html
---

# DeploymentSummary
<a name="API_DeploymentSummary"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

A subset of information about a specific deployment.

## Contents
<a name="API_DeploymentSummary_Contents"></a>

 ** applicationId **   <a name="m2-Type-DeploymentSummary-applicationId"></a>
The unique identifier of the application.
Type: String
Pattern: `\S{1,80}`
Required: Yes

 ** applicationVersion **   <a name="m2-Type-DeploymentSummary-applicationVersion"></a>
The version of the application.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 ** creationTime **   <a name="m2-Type-DeploymentSummary-creationTime"></a>
The timestamp when the deployment was created.
Type: Timestamp
Required: Yes

 ** deploymentId **   <a name="m2-Type-DeploymentSummary-deploymentId"></a>
The unique identifier of the deployment.
Type: String
Pattern: `\S{1,80}`
Required: Yes

 ** environmentId **   <a name="m2-Type-DeploymentSummary-environmentId"></a>
The unique identifier of the runtime environment.
Type: String
Pattern: `\S{1,80}`
Required: Yes

 ** status **   <a name="m2-Type-DeploymentSummary-status"></a>
The current status of the deployment.
Type: String
Valid Values: `Deploying | Succeeded | Failed | Updating Deployment`
Required: Yes

 ** statusReason **   <a name="m2-Type-DeploymentSummary-statusReason"></a>
The reason for the reported status.
Type: String
Required: No

## See Also
<a name="API_DeploymentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/DeploymentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/DeploymentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/DeploymentSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Mainframe Modernization. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query m2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
