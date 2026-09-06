---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_NetworkConfiguration.html
---

# NetworkConfiguration
<a name="API_NetworkConfiguration"></a>

The network configuration for jobs that are running on Fargate resources. Jobs that are running on Amazon EC2 resources must not specify this parameter.

## Contents
<a name="API_NetworkConfiguration_Contents"></a>

 ** assignPublicIp **   <a name="Batch-Type-NetworkConfiguration-assignPublicIp"></a>
Indicates whether the job has a public IP address. For a job that's running on Fargate resources in a private subnet to send outbound traffic to the internet (for example, to pull container images), the private subnet requires a NAT gateway be attached to route requests to the internet. For more information, see [Amazon ECS task networking](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task-networking.html) in the *Amazon Elastic Container Service Developer Guide*. The default value is "`DISABLED`".
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_NetworkConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/NetworkConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/NetworkConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/NetworkConfiguration)
