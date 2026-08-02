---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_ResourceCollection.html
---

# ResourceCollection
<a name="API_ResourceCollection"></a>

 A collection of AWS resources supported by DevOps Guru. The two types of AWS resource collections supported are AWS CloudFormation stacks and AWS resources that contain the same AWS tag. DevOps Guru can be configured to analyze the AWS resources that are defined in the stacks or that are tagged using the same tag *key*. You can specify up to 1000 AWS CloudFormation stacks.

## Contents
<a name="API_ResourceCollection_Contents"></a>

 ** CloudFormation **   <a name="DevOpsGuru-Type-ResourceCollection-CloudFormation"></a>
 An array of the names of AWS CloudFormation stacks. The stacks define AWS resources that DevOps Guru analyzes. You can specify up to 1000 AWS CloudFormation stacks.
Type: [CloudFormationCollection](API_CloudFormationCollection.md) object
Required: No

 ** Tags **   <a name="DevOpsGuru-Type-ResourceCollection-Tags"></a>
The AWS tags that are used by resources in the resource collection.
Tags help you identify and organize your AWS resources. Many AWS services support tagging, so you can assign the same tag to resources from different services to indicate that the resources are related. For example, you can assign the same tag to an Amazon DynamoDB table resource that you assign to an AWS Lambda function. For more information about using tags, see the [Tagging best practices](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) whitepaper.
Each AWS tag has two parts.
+ A tag *key* (for example, `CostCenter`, `Environment`, `Project`, or `Secret`). Tag *keys* are case-sensitive.
+ An optional field known as a tag *value* (for example, `111122223333`, `Production`, or a team name). Omitting the tag *value* is the same as using an empty string. Like tag *keys*, tag *values* are case-sensitive.
Together these are known as *key*-*value* pairs.
When you create a *key*, the case of characters in the *key* can be whatever you choose. After you create a *key*, it is case-sensitive. For example, DevOps Guru works with a *key* named `devops-guru-rds` and a *key* named `DevOps-Guru-RDS`, and these act as two different *keys*. Possible *key*/*value* pairs in your application might be `Devops-Guru-production-application/RDS` or `Devops-Guru-production-application/containers`.
Type: Array of [TagCollection](API_TagCollection.md) objects
Required: No

## See Also
<a name="API_ResourceCollection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/ResourceCollection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/ResourceCollection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/ResourceCollection)
