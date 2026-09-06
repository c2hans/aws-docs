---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_IamPolicyConstraints.html
---

# IamPolicyConstraints
<a name="API_IamPolicyConstraints"></a>

Use this parameter to specify a supported global condition key that is added to the IAM policy.

## Contents
<a name="API_IamPolicyConstraints_Contents"></a>

 ** SourceIp **   <a name="sagemaker-Type-IamPolicyConstraints-SourceIp"></a>
When `SourceIp` is `Enabled` the worker's IP address when a task is rendered in the worker portal is added to the IAM policy as a `Condition` used to generate the Amazon S3 presigned URL. This IP address is checked by Amazon S3 and must match in order for the Amazon S3 resource to be rendered in the worker portal.
Type: String
Valid Values: `Enabled | Disabled`
Required: No

 ** VpcSourceIp **   <a name="sagemaker-Type-IamPolicyConstraints-VpcSourceIp"></a>
When `VpcSourceIp` is `Enabled` the worker's IP address when a task is rendered in private worker portal inside the VPC is added to the IAM policy as a `Condition` used to generate the Amazon S3 presigned URL. To render the task successfully Amazon S3 checks that the presigned URL is being accessed over an Amazon S3 VPC Endpoint, and that the worker's IP address matches the IP address in the IAM policy. To learn more about configuring private worker portal, see [Use Amazon VPC mode from a private worker portal](https://docs.aws.amazon.com/sagemaker/latest/dg/samurai-vpc-worker-portal.html).
Type: String
Valid Values: `Enabled | Disabled`
Required: No

## See Also
<a name="API_IamPolicyConstraints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/IamPolicyConstraints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/IamPolicyConstraints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/IamPolicyConstraints)
