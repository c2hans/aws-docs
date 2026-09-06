---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_SessionChainingConfig.html
---

# SessionChainingConfig
<a name="API_SessionChainingConfig"></a>

Contains information about attribute-based access control (ABAC) for a training job. The session chaining configuration uses Amazon Security Token Service (STS) for your training job to request temporary, limited-privilege credentials to tenants. For more information, see [Attribute-based access control (ABAC) for multi-tenancy training](https://docs.aws.amazon.com/sagemaker/latest/dg/model-access-training-data.html#model-access-training-data-abac).

## Contents
<a name="API_SessionChainingConfig_Contents"></a>

 ** EnableSessionTagChaining **   <a name="sagemaker-Type-SessionChainingConfig-EnableSessionTagChaining"></a>
Set to `True` to allow SageMaker to extract session tags from a training job creation role and reuse these tags when assuming the training job execution role.
Type: Boolean
Required: No

## See Also
<a name="API_SessionChainingConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/SessionChainingConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/SessionChainingConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/SessionChainingConfig)
