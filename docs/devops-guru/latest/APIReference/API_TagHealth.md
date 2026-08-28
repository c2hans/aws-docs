---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_TagHealth.html
---

# TagHealth
<a name="API_TagHealth"></a>

 Information about the health of AWS resources in your account that are specified by an AWS tag *key*.

## Contents
<a name="API_TagHealth_Contents"></a>

 ** AnalyzedResourceCount **   <a name="DevOpsGuru-Type-TagHealth-AnalyzedResourceCount"></a>
 Number of resources that DevOps Guru is monitoring in your account that are specified by an AWS tag.
Type: Long
Required: No

 ** AppBoundaryKey **   <a name="DevOpsGuru-Type-TagHealth-AppBoundaryKey"></a>
An AWS tag *key* that is used to identify the AWS resources that DevOps Guru analyzes. All AWS resources in your account and Region tagged with this *key* make up your DevOps Guru application and analysis boundary.
When you create a *key*, the case of characters in the *key* can be whatever you choose. After you create a *key*, it is case-sensitive. For example, DevOps Guru works with a *key* named `devops-guru-rds` and a *key* named `DevOps-Guru-RDS`, and these act as two different *keys*. Possible *key*/*value* pairs in your application might be `Devops-Guru-production-application/RDS` or `Devops-Guru-production-application/containers`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** Insight **   <a name="DevOpsGuru-Type-TagHealth-Insight"></a>
Information about the health of the AWS resources in your account that are specified by an AWS tag, including the number of open proactive, open reactive insights, and the Mean Time to Recover (MTTR) of closed insights.
Type: [InsightHealth](API_InsightHealth.md) object
Required: No

 ** TagValue **   <a name="DevOpsGuru-Type-TagHealth-TagValue"></a>
The value in an AWS tag.
The tag's *value* is an optional field used to associate a string with the tag *key* (for example, `111122223333`, `Production`, or a team name). The *key* and *value* are the tag's *key* pair. Omitting the tag *value* is the same as using an empty string. Like tag *keys*, tag *values* are case-sensitive. You can specify a maximum of 256 characters for a tag value.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*|\*)$`
Required: No

## See Also
<a name="API_TagHealth_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/TagHealth)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/TagHealth)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/TagHealth)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
