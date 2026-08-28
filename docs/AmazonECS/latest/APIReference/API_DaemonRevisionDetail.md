---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_DaemonRevisionDetail.html
---

# DaemonRevisionDetail
<a name="API_DaemonRevisionDetail"></a>

Details about a daemon revision, including the running task counts per capacity provider.

## Contents
<a name="API_DaemonRevisionDetail_Contents"></a>

 ** arn **   <a name="ECS-Type-DaemonRevisionDetail-arn"></a>
The Amazon Resource Name (ARN) of the daemon revision.
Type: String
Required: No

 ** capacityProviders **   <a name="ECS-Type-DaemonRevisionDetail-capacityProviders"></a>
The capacity providers associated with this daemon revision.
Type: Array of [DaemonCapacityProvider](API_DaemonCapacityProvider.md) objects
Required: No

 ** totalRunningCount **   <a name="ECS-Type-DaemonRevisionDetail-totalRunningCount"></a>
The total number of daemon tasks running for this revision.
Type: Integer
Required: No

## See Also
<a name="API_DaemonRevisionDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/DaemonRevisionDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/DaemonRevisionDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/DaemonRevisionDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Elastic Container Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonECS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
