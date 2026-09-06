---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_UpdateTagCollectionFilter.html
---

# UpdateTagCollectionFilter
<a name="API_UpdateTagCollectionFilter"></a>

A new collection of AWS resources that are defined by an AWS tag or tag *key*/*value* pair.

## Contents
<a name="API_UpdateTagCollectionFilter_Contents"></a>

 ** AppBoundaryKey **   <a name="DevOpsGuru-Type-UpdateTagCollectionFilter-AppBoundaryKey"></a>
An AWS tag *key* that is used to identify the AWS resources that DevOps Guru analyzes. All AWS resources in your account and Region tagged with this *key* make up your DevOps Guru application and analysis boundary.
When you create a *key*, the case of characters in the *key* can be whatever you choose. After you create a *key*, it is case-sensitive. For example, DevOps Guru works with a *key* named `devops-guru-rds` and a *key* named `DevOps-Guru-RDS`, and these act as two different *keys*. Possible *key*/*value* pairs in your application might be `Devops-Guru-production-application/RDS` or `Devops-Guru-production-application/containers`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

 ** TagValues **   <a name="DevOpsGuru-Type-UpdateTagCollectionFilter-TagValues"></a>
The values in an AWS tag collection.
The tag's *value* is an optional field used to associate a string with the tag *key* (for example, `111122223333`, `Production`, or a team name). The *key* and *value* are the tag's *key* pair. Omitting the tag *value* is the same as using an empty string. Like tag *keys*, tag *values* are case-sensitive. You can specify a maximum of 256 characters for a tag value.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*|\*)$`
Required: Yes

## See Also
<a name="API_UpdateTagCollectionFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/UpdateTagCollectionFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/UpdateTagCollectionFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/UpdateTagCollectionFilter)
