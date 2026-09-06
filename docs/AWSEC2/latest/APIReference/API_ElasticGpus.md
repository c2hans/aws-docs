---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ElasticGpus.html
---

# ElasticGpus
<a name="API_ElasticGpus"></a>

**Note**
Amazon Elastic Graphics reached end of life on January 8, 2024.

Describes an Elastic Graphics accelerator.

## Contents
<a name="API_ElasticGpus_Contents"></a>

 ** availabilityZone **
The Availability Zone in the which the Elastic Graphics accelerator resides.
Type: String
Required: No

 ** elasticGpuHealth **
The status of the Elastic Graphics accelerator.
Type: [ElasticGpuHealth](API_ElasticGpuHealth.md) object
Required: No

 ** elasticGpuId **
The ID of the Elastic Graphics accelerator.
Type: String
Required: No

 ** elasticGpuState **
The state of the Elastic Graphics accelerator.
Type: String
Valid Values: `ATTACHED`
Required: No

 ** elasticGpuType **
The type of Elastic Graphics accelerator.
Type: String
Required: No

 ** instanceId **
The ID of the instance to which the Elastic Graphics accelerator is attached.
Type: String
Required: No

 ** TagSet.N **
The tags assigned to the Elastic Graphics accelerator.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_ElasticGpus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ElasticGpus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ElasticGpus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ElasticGpus)
