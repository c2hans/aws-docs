---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_DeploymentSummary.html
---

# DeploymentSummary
<a name="API_DeploymentSummary"></a>

Summary information about a deployment.

## Contents
<a name="API_DeploymentSummary_Contents"></a>

 ** deploymentArn **   <a name="networksecuritymanager-Type-DeploymentSummary-deploymentArn"></a>
The Amazon Resource Name (ARN) of the deployment.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 1010.
Pattern: `arn(:[a-z0-9]+([.-][a-z0-9]+)*){2}(:([a-z0-9]+([.-][a-z0-9]+)*)?){2}:(.+)`
Required: Yes

 ** deploymentId **   <a name="networksecuritymanager-Type-DeploymentSummary-deploymentId"></a>
The service-generated id of the deployment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]{1,64}`
Required: Yes

 ** deploymentName **   <a name="networksecuritymanager-Type-DeploymentSummary-deploymentName"></a>
The name of the deployment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9 _.:/=+\-@]*`
Required: No

 ** hasPublishedVersion **   <a name="networksecuritymanager-Type-DeploymentSummary-hasPublishedVersion"></a>
Specifies whether a published version of the resource exists.
Type: Boolean
Required: No

 ** status **   <a name="networksecuritymanager-Type-DeploymentSummary-status"></a>
The current status of the resource: `DRAFT` (unpublished, editable), `ACTIVE` (published, in use), or `DISABLED` (deactivated; changes cannot be published until the resource is re-enabled).
Type: String
Valid Values: `DRAFT | ACTIVE | DISABLED`
Required: No

 ** updatedAt **   <a name="networksecuritymanager-Type-DeploymentSummary-updatedAt"></a>
The time when the resource was last updated. For a snapshot, this is the time when the snapshot was created.
Type: Timestamp
Required: No

 ** version **   <a name="networksecuritymanager-Type-DeploymentSummary-version"></a>
The version of the resource.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10.
Pattern: `[1-9][0-9]*`
Required: No

## See Also
<a name="API_DeploymentSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/DeploymentSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/DeploymentSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/DeploymentSummary)
