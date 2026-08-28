---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_ResourceCollectionFilter.html
---

# ResourceCollectionFilter
<a name="API_ResourceCollectionFilter"></a>

 Information about a filter used to specify which AWS resources are analyzed for anomalous behavior by DevOps Guru.

## Contents
<a name="API_ResourceCollectionFilter_Contents"></a>

 ** CloudFormation **   <a name="DevOpsGuru-Type-ResourceCollectionFilter-CloudFormation"></a>
 Information about AWS CloudFormation stacks. You can use up to 1000 stacks to specify which AWS resources in your account to analyze. For more information, see [Stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/stacks.html) in the * AWS CloudFormation User Guide*.
Type: [CloudFormationCollectionFilter](API_CloudFormationCollectionFilter.md) object
Required: No

 ** Tags **   <a name="DevOpsGuru-Type-ResourceCollectionFilter-Tags"></a>
The AWS tags used to filter the resources in the resource collection.
Tags help you identify and organize your AWS resources. Many AWS services support tagging, so you can assign the same tag to resources from different services to indicate that the resources are related. For example, you can assign the same tag to an Amazon DynamoDB table resource that you assign to an AWS Lambda function. For more information about using tags, see the [Tagging best practices](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) whitepaper.
Each AWS tag has two parts.
+ A tag *key* (for example, `CostCenter`, `Environment`, `Project`, or `Secret`). Tag *keys* are case-sensitive.
+ An optional field known as a tag *value* (for example, `111122223333`, `Production`, or a team name). Omitting the tag *value* is the same as using an empty string. Like tag *keys*, tag *values* are case-sensitive.
Together these are known as *key*-*value* pairs.
When you create a *key*, the case of characters in the *key* can be whatever you choose. After you create a *key*, it is case-sensitive. For example, DevOps Guru works with a *key* named `devops-guru-rds` and a *key* named `DevOps-Guru-RDS`, and these act as two different *keys*. Possible *key*/*value* pairs in your application might be `Devops-Guru-production-application/RDS` or `Devops-Guru-production-application/containers`.
Type: Array of [TagCollectionFilter](API_TagCollectionFilter.md) objects
Required: No

## See Also
<a name="API_ResourceCollectionFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/ResourceCollectionFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/ResourceCollectionFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/ResourceCollectionFilter)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DevOps Guru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devops-guru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
