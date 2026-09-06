---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_RollbackConfig.html
---

# RollbackConfig
<a name="API_RollbackConfig"></a>

The rollback configuration for the cluster version rollback.

## Contents
<a name="API_RollbackConfig_Contents"></a>

 ** timeoutMinutes **   <a name="AmazonEKS-Type-RollbackConfig-timeoutMinutes"></a>
The length of time in minutes to wait before cancelling the update. Timeout is a minimum-bound property, meaning the timeout occurs no sooner than the time you specify, but can occur shortly thereafter. This value can be between 120 (2 hours) and 10080 (7 days). Default: `720` (12 hours) if not specified.
Type: Integer
Required: No

## See Also
<a name="API_RollbackConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/RollbackConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/RollbackConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/RollbackConfig)
