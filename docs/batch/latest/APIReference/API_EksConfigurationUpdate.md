---
source_url: https://docs.aws.amazon.com/batch/latest/APIReference/API_EksConfigurationUpdate.html
---

# EksConfigurationUpdate
<a name="API_EksConfigurationUpdate"></a>

An object that represents the attributes of an AWS Batch compute environment's Amazon EKS configuration that can be updated. Currently `accessEntry` is the only attribute that you can change after the compute environment is created. For more information, see [Amazon EKS access entry authentication](https://docs.aws.amazon.com/batch/latest/userguide/eks-access-entries.html) in the * AWS Batch User Guide*.

## Contents
<a name="API_EksConfigurationUpdate_Contents"></a>

 ** accessEntry **   <a name="Batch-Type-EksConfigurationUpdate-accessEntry"></a>
The updated access entry configuration for the compute environment. Set `desiredState` to declare whether AWS Batch will manage an access entry on the cluster. For the accepted values, see [`EksAccessEntry`](https://docs.aws.amazon.com/batch/latest/APIReference/API_EksAccessEntry.html).
Type: [EksAccessEntry](API_EksAccessEntry.md) object
Required: No

## See Also
<a name="API_EksConfigurationUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/batch-2016-08-10/EksConfigurationUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/batch-2016-08-10/EksConfigurationUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/batch-2016-08-10/EksConfigurationUpdate)
