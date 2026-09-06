---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_WebhookFilter.html
---

# WebhookFilter
<a name="API_WebhookFilter"></a>

A filter used to determine which webhooks trigger a build.

## Contents
<a name="API_WebhookFilter_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** pattern **   <a name="CodeBuild-Type-WebhookFilter-pattern"></a>
 For a `WebHookFilter` that uses `EVENT` type, a comma-separated string that specifies one or more events. For example, the webhook filter `PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED` allows all push, pull request created, and pull request updated events to trigger a build.
 For a `WebHookFilter` that uses any of the other filter types, a regular expression pattern. For example, a `WebHookFilter` that uses `HEAD_REF` for its `type` and the pattern `^refs/heads/` triggers a build when the head reference is a branch with a reference name `refs/heads/branch-name`.
 CodeBuild evaluates filter patterns using [RE2 regular expression syntax](https://github.com/google/re2/wiki/Syntax). RE2 does not support lookahead assertions (`(?=`, `(?!`), lookbehind assertions (`(?<=`, `(?<!`), or backreferences (`\1`). `CreateWebhook` and `UpdateWebhook` requests that include an unsupported pattern fail with an `InvalidInputException`. To trigger builds only on events that do not match a pattern, use a matching pattern with `excludeMatchedPattern` set to `true` instead of negative lookahead.
Type: String
Required: Yes

 ** type **   <a name="CodeBuild-Type-WebhookFilter-type"></a>
 The type of webhook filter. There are 11 webhook filter types: `EVENT`, `ACTOR_ACCOUNT_ID`, `HEAD_REF`, `BASE_REF`, `FILE_PATH`, `COMMIT_MESSAGE`, `TAG_NAME`, `RELEASE_NAME`, `REPOSITORY_NAME`, `ORGANIZATION_NAME`, and `WORKFLOW_NAME`.
+  EVENT
  +  A webhook event triggers a build when the provided `pattern` matches one of nine event types: `PUSH`, `PULL_REQUEST_CREATED`, `PULL_REQUEST_UPDATED`, `PULL_REQUEST_CLOSED`, `PULL_REQUEST_REOPENED`, `PULL_REQUEST_MERGED`, `RELEASED`, `PRERELEASED`, and `WORKFLOW_JOB_QUEUED`. The `EVENT` patterns are specified as a comma-separated string. For example, `PUSH, PULL_REQUEST_CREATED, PULL_REQUEST_UPDATED` filters all push, pull request created, and pull request updated events.
**Note**
 Types `PULL_REQUEST_REOPENED` and `WORKFLOW_JOB_QUEUED` work with GitHub and GitHub Enterprise only. Types `RELEASED` and `PRERELEASED` work with GitHub only.
+ ACTOR\_ACCOUNT\_ID
  +  A webhook event triggers a build when a GitHub, GitHub Enterprise, or Bitbucket account ID matches the regular expression `pattern`.
+ HEAD\_REF
  +  A webhook event triggers a build when the head reference matches the regular expression `pattern`. For example, `refs/heads/branch-name` and `refs/tags/tag-name`.
**Note**
 Works with GitHub and GitHub Enterprise push, GitHub and GitHub Enterprise pull request, Bitbucket push, and Bitbucket pull request events.
+ BASE\_REF
  +  A webhook event triggers a build when the base reference matches the regular expression `pattern`. For example, `refs/heads/branch-name`.
**Note**
 Works with pull request events only.
+ FILE\_PATH
  +  A webhook triggers a build when the path of a changed file matches the regular expression `pattern`.
**Note**
 Works with push and pull request events only.
+ COMMIT\_MESSAGE
  + A webhook triggers a build when the head commit message matches the regular expression `pattern`.
**Note**
 Works with push and pull request events only.
+ TAG\_NAME
  + A webhook triggers a build when the tag name of the release matches the regular expression `pattern`.
**Note**
 Works with `RELEASED` and `PRERELEASED` events only.
+ RELEASE\_NAME
  + A webhook triggers a build when the release name matches the regular expression `pattern`.
**Note**
 Works with `RELEASED` and `PRERELEASED` events only.
+ REPOSITORY\_NAME
  + A webhook triggers a build when the repository name matches the regular expression `pattern`.
**Note**
 Works with GitHub global or organization webhooks only.
+ ORGANIZATION\_NAME
  + A webhook triggers a build when the organization name matches the regular expression `pattern`.
**Note**
 Works with GitHub global webhooks only.
+ WORKFLOW\_NAME
  + A webhook triggers a build when the workflow name matches the regular expression `pattern`.
**Note**
 Works with `WORKFLOW_JOB_QUEUED` events only.
**Note**
For CodeBuild-hosted Buildkite runner builds, WORKFLOW\_NAME filters will filter by pipeline name.
Type: String
Valid Values: `EVENT | BASE_REF | HEAD_REF | ACTOR_ACCOUNT_ID | FILE_PATH | COMMIT_MESSAGE | WORKFLOW_NAME | TAG_NAME | RELEASE_NAME | REPOSITORY_NAME | ORGANIZATION_NAME`
Required: Yes

 ** excludeMatchedPattern **   <a name="CodeBuild-Type-WebhookFilter-excludeMatchedPattern"></a>
 Used to indicate that the `pattern` determines which webhook events do not trigger a build. If true, then a webhook event that does not match the `pattern` triggers a build. If false, then a webhook event that matches the `pattern` triggers a build.
Type: Boolean
Required: No

## See Also
<a name="API_WebhookFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/WebhookFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/WebhookFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/WebhookFilter)
