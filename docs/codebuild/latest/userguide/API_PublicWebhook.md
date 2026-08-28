---
source_url: https://docs.aws.amazon.com/codebuild/latest/userguide/API_PublicWebhook.html
---

# PublicWebhook
<a name="API_PublicWebhook"></a>

**Note**
This API element is not contained in the AWS CLI or AWS SDKs.

## Contents
<a name="API_PublicWebhook_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 **branchFilter**   <a name="CodeBuild-Type-PublicWebhook-branchFilter"></a>
Type: String
Required: No

 **buildType**   <a name="CodeBuild-Type-PublicWebhook-buildType"></a>
Type: String
Required: No

 **filterGroups**   <a name="CodeBuild-Type-PublicWebhook-filterGroups"></a>
Type: Array of arrays of [WebhookFilter](https://docs.aws.amazon.com/codebuild/latest/APIReference/API_WebhookFilter.html) objects
Required: No

 **payloadUrl**   <a name="CodeBuild-Type-PublicWebhook-payloadUrl"></a>
Type: String
Length Constraints: Minimum length of 1.
Required: No

 **url**   <a name="CodeBuild-Type-PublicWebhook-url"></a>
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeBuild. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codebuild` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
