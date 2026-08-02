---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_TagCollection.html
---

# TagCollection
<a name="API_TagCollection"></a>

A collection of AWS tags.

Tags help you identify and organize your AWS resources. Many AWS services support tagging, so you can assign the same tag to resources from different services to indicate that the resources are related. For example, you can assign the same tag to an Amazon DynamoDB table resource that you assign to an AWS Lambda function. For more information about using tags, see the [Tagging best practices](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) whitepaper.

Each AWS tag has two parts.
+ A tag *key* (for example, `CostCenter`, `Environment`, `Project`, or `Secret`). Tag *keys* are case-sensitive.
+ An optional field known as a tag *value* (for example, `111122223333`, `Production`, or a team name). Omitting the tag *value* is the same as using an empty string. Like tag *keys*, tag *values* are case-sensitive.

Together these are known as *key*-*value* pairs.

**Important**
When you create a *key*, the case of characters in the *key* can be whatever you choose. After you create a *key*, it is case-sensitive. For example, DevOps Guru works with a *key* named `devops-guru-rds` and a *key* named `DevOps-Guru-RDS`, and these act as two different *keys*. Possible *key*/*value* pairs in your application might be `Devops-Guru-production-application/RDS` or `Devops-Guru-production-application/containers`.

## Contents
<a name="API_TagCollection_Contents"></a>

 ** AppBoundaryKey **   <a name="DevOpsGuru-Type-TagCollection-AppBoundaryKey"></a>
An AWS tag *key* that is used to identify the AWS resources that DevOps Guru analyzes. All AWS resources in your account and Region tagged with this *key* make up your DevOps Guru application and analysis boundary.
When you create a *key*, the case of characters in the *key* can be whatever you choose. After you create a *key*, it is case-sensitive. For example, DevOps Guru works with a *key* named `devops-guru-rds` and a *key* named `DevOps-Guru-RDS`, and these act as two different *keys*. Possible *key*/*value* pairs in your application might be `Devops-Guru-production-application/RDS` or `Devops-Guru-production-application/containers`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

 ** TagValues **   <a name="DevOpsGuru-Type-TagCollection-TagValues"></a>
The values in an AWS tag collection.
The tag's *value* is an optional field used to associate a string with the tag *key* (for example, `111122223333`, `Production`, or a team name). The *key* and *value* are the tag's *key* pair. Omitting the tag *value* is the same as using an empty string. Like tag *keys*, tag *values* are case-sensitive. You can specify a maximum of 256 characters for a tag value.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*|\*)$`
Required: Yes

## See Also
<a name="API_TagCollection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/TagCollection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/TagCollection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/TagCollection)
