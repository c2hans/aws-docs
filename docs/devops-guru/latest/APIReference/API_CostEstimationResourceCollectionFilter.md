---
source_url: https://docs.aws.amazon.com/devops-guru/latest/APIReference/API_CostEstimationResourceCollectionFilter.html
---

# CostEstimationResourceCollectionFilter
<a name="API_CostEstimationResourceCollectionFilter"></a>

Information about a filter used to specify which AWS resources are analyzed to create a monthly DevOps Guru cost estimate. For more information, see [Estimate your Amazon DevOps Guru costs](https://docs.aws.amazon.com/devops-guru/latest/userguide/cost-estimate.html) and [Amazon DevOps Guru pricing](http://aws.amazon.com/devops-guru/pricing/).

## Contents
<a name="API_CostEstimationResourceCollectionFilter_Contents"></a>

 ** CloudFormation **   <a name="DevOpsGuru-Type-CostEstimationResourceCollectionFilter-CloudFormation"></a>
An object that specifies the CloudFormation stack that defines the AWS resources used to create a monthly estimate for DevOps Guru.
Type: [CloudFormationCostEstimationResourceCollectionFilter](API_CloudFormationCostEstimationResourceCollectionFilter.md) object
Required: No

 ** Tags **   <a name="DevOpsGuru-Type-CostEstimationResourceCollectionFilter-Tags"></a>
The AWS tags used to filter the resource collection that is used for a cost estimate.
Tags help you identify and organize your AWS resources. Many AWS services support tagging, so you can assign the same tag to resources from different services to indicate that the resources are related. For example, you can assign the same tag to an Amazon DynamoDB table resource that you assign to an AWS Lambda function. For more information about using tags, see the [Tagging best practices](https://docs.aws.amazon.com/whitepapers/latest/tagging-best-practices/tagging-best-practices.html) whitepaper.
Each AWS tag has two parts.
+ A tag *key* (for example, `CostCenter`, `Environment`, `Project`, or `Secret`). Tag *keys* are case-sensitive.
+ An optional field known as a tag *value* (for example, `111122223333`, `Production`, or a team name). Omitting the tag *value* is the same as using an empty string. Like tag *keys*, tag *values* are case-sensitive.
Together these are known as *key*-*value* pairs.
When you create a *key*, the case of characters in the *key* can be whatever you choose. After you create a *key*, it is case-sensitive. For example, DevOps Guru works with a *key* named `devops-guru-rds` and a *key* named `DevOps-Guru-RDS`, and these act as two different *keys*. Possible *key*/*value* pairs in your application might be `Devops-Guru-production-application/RDS` or `Devops-Guru-production-application/containers`.
Type: Array of [TagCostEstimationResourceCollectionFilter](API_TagCostEstimationResourceCollectionFilter.md) objects
Required: No

## See Also
<a name="API_CostEstimationResourceCollectionFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devops-guru-2020-12-01/CostEstimationResourceCollectionFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devops-guru-2020-12-01/CostEstimationResourceCollectionFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devops-guru-2020-12-01/CostEstimationResourceCollectionFilter)
