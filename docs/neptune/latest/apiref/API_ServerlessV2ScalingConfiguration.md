---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_ServerlessV2ScalingConfiguration.html
---

# ServerlessV2ScalingConfiguration
<a name="API_ServerlessV2ScalingConfiguration"></a>

Contains the scaling configuration of a Neptune Serverless DB cluster.

For more information, see [Using Amazon Neptune Serverless](https://docs.aws.amazon.com/neptune/latest/userguide/neptune-serverless-using.html) in the *Amazon Neptune User Guide*.

## Contents
<a name="API_ServerlessV2ScalingConfiguration_Contents"></a>

 ** MaxCapacity **
The maximum number of Neptune capacity units (NCUs) for a DB instance in a Neptune Serverless cluster. You can specify NCU values in half-step increments, such as 40, 40.5, 41, and so on.
Type: Double
Required: No

 ** MinCapacity **
The minimum number of Neptune capacity units (NCUs) for a DB instance in a Neptune Serverless cluster. You can specify NCU values in half-step increments, such as 8, 8.5, 9, and so on.
Type: Double
Required: No

## See Also
<a name="API_ServerlessV2ScalingConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/ServerlessV2ScalingConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/ServerlessV2ScalingConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/ServerlessV2ScalingConfiguration)
