---
source_url: https://docs.aws.amazon.com/resilience-hub/v2/APIReference/API_ResolvedTargetResource.html
---

# ResolvedTargetResource
<a name="API_ResolvedTargetResource"></a>

A single AWS resource that AWS Fault Injection Service (AWS FIS) resolved as a target during a test run.

## Contents
<a name="API_ResolvedTargetResource_Contents"></a>

 ** resourceType **   <a name="ngresiliencehub-Type-ResolvedTargetResource-resourceType"></a>
The AWS FIS resource type the target belongs to, such as aws:ec2:instance, aws:ecs:task, or aws:eks:pod.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** targetInformation **   <a name="ngresiliencehub-Type-ResolvedTargetResource-targetInformation"></a>
The raw target information map as returned by AWS FIS.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: Yes

 ** targetName **   <a name="ngresiliencehub-Type-ResolvedTargetResource-targetName"></a>
The name of the target in the AWS FIS experiment template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_ResolvedTargetResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resiliencehubv2-2026-02-17/ResolvedTargetResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resiliencehubv2-2026-02-17/ResolvedTargetResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resiliencehubv2-2026-02-17/ResolvedTargetResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Next generation Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
