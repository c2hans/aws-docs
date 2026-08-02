---
source_url: https://docs.aws.amazon.com/outposts/latest/APIReference/API_BlockingInstance.html
---

# BlockingInstance
<a name="API_BlockingInstance"></a>

A running Amazon EC2 instance that can be stopped to free up capacity needed to run the capacity task.

## Contents
<a name="API_BlockingInstance_Contents"></a>

 ** AccountId **   <a name="outposts-Type-BlockingInstance-AccountId"></a>
The ID of the AWS account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** AwsServiceName **   <a name="outposts-Type-BlockingInstance-AwsServiceName"></a>
The AWS service name that owns the specified blocking instance.
Type: String
Valid Values: `AWS | EC2 | EKS | ELASTICACHE | ELB | RDS | ROUTE53`
Required: No

 ** InstanceId **   <a name="outposts-Type-BlockingInstance-InstanceId"></a>
The ID of the blocking instance.
Type: String
Length Constraints: Minimum length of 11. Maximum length of 32.
Pattern: `^i-[0-9a-z]+$`
Required: No

## See Also
<a name="API_BlockingInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/outposts-2019-12-03/BlockingInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/outposts-2019-12-03/BlockingInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/outposts-2019-12-03/BlockingInstance)
