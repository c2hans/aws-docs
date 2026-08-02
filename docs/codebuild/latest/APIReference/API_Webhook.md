---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_Webhook.html
---

# Webhook
<a name="API_Webhook"></a>

Information about a webhook that connects repository events to a build project in AWS CodeBuild.

## Contents
<a name="API_Webhook_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** branchFilter **   <a name="CodeBuild-Type-Webhook-branchFilter"></a>
A regular expression used to determine which repository branches are built when a webhook is triggered. If the name of a branch matches the regular expression, then it is built. If `branchFilter` is empty, then all branches are built.
It is recommended that you use `filterGroups` instead of `branchFilter`.
Type: String
Required: No

 ** buildType **   <a name="CodeBuild-Type-Webhook-buildType"></a>
Specifies the type of build this webhook will trigger.
 `RUNNER_BUILDKITE_BUILD` is only available for `NO_SOURCE` source type projects configured for Buildkite runner builds. For more information about CodeBuild-hosted Buildkite runner builds, see [Tutorial: Configure a CodeBuild-hosted Buildkite runner](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-runner-buildkite.html) in the * AWS CodeBuild user guide*.
Type: String
Valid Values: `BUILD | BUILD_BATCH | RUNNER_BUILDKITE_BUILD`
Required: No

 ** filterGroups **   <a name="CodeBuild-Type-Webhook-filterGroups"></a>
An array of arrays of `WebhookFilter` objects used to determine which webhooks are triggered. At least one `WebhookFilter` in the array must specify `EVENT` as its `type`.
For a build to be triggered, at least one filter group in the `filterGroups` array must pass. For a filter group to pass, each of its filters must pass.
Type: Array of arrays of [WebhookFilter](API_WebhookFilter.md) objects
Required: No

 ** lastModifiedSecret **   <a name="CodeBuild-Type-Webhook-lastModifiedSecret"></a>
A timestamp that indicates the last time a repository's secret token was modified.
Type: Timestamp
Required: No

 ** manualCreation **   <a name="CodeBuild-Type-Webhook-manualCreation"></a>
If manualCreation is true, CodeBuild doesn't create a webhook in GitHub and instead returns `payloadUrl` and `secret` values for the webhook. The `payloadUrl` and `secret` values in the output can be used to manually create a webhook within GitHub.
manualCreation is only available for GitHub webhooks.
Type: Boolean
Required: No

 ** payloadUrl **   <a name="CodeBuild-Type-Webhook-payloadUrl"></a>
The AWS CodeBuild endpoint where webhook events are sent.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** pullRequestBuildPolicy **   <a name="CodeBuild-Type-Webhook-pullRequestBuildPolicy"></a>
A PullRequestBuildPolicy object that defines comment-based approval requirements for triggering builds on pull requests. This policy helps control when automated builds are executed based on contributor permissions and approval workflows.
Type: [PullRequestBuildPolicy](API_PullRequestBuildPolicy.md) object
Required: No

 ** scopeConfiguration **   <a name="CodeBuild-Type-Webhook-scopeConfiguration"></a>
The scope configuration for global or organization webhooks.
Global or organization webhooks are only available for GitHub and Github Enterprise webhooks.
Type: [ScopeConfiguration](API_ScopeConfiguration.md) object
Required: No

 ** secret **   <a name="CodeBuild-Type-Webhook-secret"></a>
The secret token of the associated repository.
A Bitbucket webhook does not support `secret`.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** status **   <a name="CodeBuild-Type-Webhook-status"></a>
The status of the webhook. Valid values include:
+  `CREATING`: The webhook is being created.
+  `CREATE_FAILED`: The webhook has failed to create.
+  `ACTIVE`: The webhook has succeeded and is active.
+  `DELETING`: The webhook is being deleted.
Type: String
Valid Values: `CREATING | CREATE_FAILED | ACTIVE | DELETING`
Required: No

 ** statusMessage **   <a name="CodeBuild-Type-Webhook-statusMessage"></a>
A message associated with the status of a webhook.
Type: String
Required: No

 ** url **   <a name="CodeBuild-Type-Webhook-url"></a>
The URL to the webhook.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_Webhook_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/Webhook)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/Webhook)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/Webhook)
