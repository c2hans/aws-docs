---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_UpdateWebhook.html
---

# UpdateWebhook
<a name="API_UpdateWebhook"></a>

 Updates the webhook associated with an AWS CodeBuild build project.

**Note**
 If you use Bitbucket for your repository, `rotateSecret` is ignored.

## Request Syntax
<a name="API_UpdateWebhook_RequestSyntax"></a>

```
{
   "branchFilter": "{{string}}",
   "buildType": "{{string}}",
   "filterGroups": [
      [
         {
            "excludeMatchedPattern": {{boolean}},
            "pattern": "{{string}}",
            "type": "{{string}}"
         }
      ]
   ],
   "projectName": "{{string}}",
   "pullRequestBuildPolicy": {
      "approverRoles": [ "{{string}}" ],
      "requiresCommentApproval": "{{string}}"
   },
   "rotateSecret": {{boolean}}
}
```

## Request Parameters
<a name="API_UpdateWebhook_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [projectName](#API_UpdateWebhook_RequestSyntax) **   <a name="CodeBuild-UpdateWebhook-request-projectName"></a>
The name of the AWS CodeBuild project.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 150.
Pattern: `[A-Za-z0-9][A-Za-z0-9\-_]{1,149}`
Required: Yes

 ** [branchFilter](#API_UpdateWebhook_RequestSyntax) **   <a name="CodeBuild-UpdateWebhook-request-branchFilter"></a>
A regular expression used to determine which repository branches are built when a webhook is triggered. If the name of a branch matches the regular expression, then it is built. If `branchFilter` is empty, then all branches are built.
 It is recommended that you use `filterGroups` instead of `branchFilter`.
Type: String
Required: No

 ** [buildType](#API_UpdateWebhook_RequestSyntax) **   <a name="CodeBuild-UpdateWebhook-request-buildType"></a>
Specifies the type of build this webhook will trigger.
 `RUNNER_BUILDKITE_BUILD` is only available for `NO_SOURCE` source type projects configured for Buildkite runner builds. For more information about CodeBuild-hosted Buildkite runner builds, see [Tutorial: Configure a CodeBuild-hosted Buildkite runner](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-runner-buildkite.html) in the * AWS CodeBuild user guide*.
Type: String
Valid Values: `BUILD | BUILD_BATCH | RUNNER_BUILDKITE_BUILD`
Required: No

 ** [filterGroups](#API_UpdateWebhook_RequestSyntax) **   <a name="CodeBuild-UpdateWebhook-request-filterGroups"></a>
 An array of arrays of `WebhookFilter` objects used to determine if a webhook event can trigger a build. A filter group must contain at least one `EVENT` `WebhookFilter`.
Type: Array of arrays of [WebhookFilter](API_WebhookFilter.md) objects
Required: No

 ** [pullRequestBuildPolicy](#API_UpdateWebhook_RequestSyntax) **   <a name="CodeBuild-UpdateWebhook-request-pullRequestBuildPolicy"></a>
A PullRequestBuildPolicy object that defines comment-based approval requirements for triggering builds on pull requests. This policy helps control when automated builds are executed based on contributor permissions and approval workflows.
Type: [PullRequestBuildPolicy](API_PullRequestBuildPolicy.md) object
Required: No

 ** [rotateSecret](#API_UpdateWebhook_RequestSyntax) **   <a name="CodeBuild-UpdateWebhook-request-rotateSecret"></a>
 A boolean value that specifies whether the associated GitHub repository's secret token should be updated. If you use Bitbucket for your repository, `rotateSecret` is ignored.
Type: Boolean
Required: No

## Response Syntax
<a name="API_UpdateWebhook_ResponseSyntax"></a>

```
{
   "webhook": {
      "branchFilter": "string",
      "buildType": "string",
      "filterGroups": [
         [
            {
               "excludeMatchedPattern": boolean,
               "pattern": "string",
               "type": "string"
            }
         ]
      ],
      "lastModifiedSecret": number,
      "manualCreation": boolean,
      "payloadUrl": "string",
      "pullRequestBuildPolicy": {
         "approverRoles": [ "string" ],
         "requiresCommentApproval": "string"
      },
      "scopeConfiguration": {
         "domain": "string",
         "name": "string",
         "scope": "string"
      },
      "secret": "string",
      "status": "string",
      "statusMessage": "string",
      "url": "string"
   }
}
```

## Response Elements
<a name="API_UpdateWebhook_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [webhook](#API_UpdateWebhook_ResponseSyntax) **   <a name="CodeBuild-UpdateWebhook-response-webhook"></a>
 Information about a repository's webhook that is associated with a project in AWS CodeBuild.
Type: [Webhook](API_Webhook.md) object

## Errors
<a name="API_UpdateWebhook_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

 ** OAuthProviderException **
There was a problem with the underlying OAuth provider.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified AWS resource cannot be found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateWebhook_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/UpdateWebhook)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/UpdateWebhook)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/UpdateWebhook)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/UpdateWebhook)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/UpdateWebhook)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/UpdateWebhook)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/UpdateWebhook)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/UpdateWebhook)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/UpdateWebhook)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/UpdateWebhook)
