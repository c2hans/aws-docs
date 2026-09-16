---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_WorkloadTypeConcurrency.html
---

# WorkloadTypeConcurrency
<a name="API_WorkloadTypeConcurrency"></a>

Defines the maximum number of contacts an agent can handle simultaneously for a specific channel and workload type combination.

## Contents
<a name="API_WorkloadTypeConcurrency_Contents"></a>

 ** Concurrency **   <a name="connect-Type-WorkloadTypeConcurrency-Concurrency"></a>
The maximum number of contacts an agent can handle simultaneously for a specific channel and workload type combination.
Valid Range for `VOICE`: Minimum value of 1. Maximum value of 1.
Valid Range for `CHAT`: Minimum value of 1. Maximum value of 10.
Valid Range for `TASK`: Minimum value of 1. Maximum value of 10.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: Yes

 ** WorkloadType **   <a name="connect-Type-WorkloadTypeConcurrency-WorkloadType"></a>
The value of the workload type.
Type: String
Required: Yes

 ** CrossChannelWorkloadBehavior **   <a name="connect-Type-WorkloadTypeConcurrency-CrossChannelWorkloadBehavior"></a>
Defines the cross-channel and workload type routing behavior for each channel and workload type combination that is enabled for this Routing Profile.
Type: [CrossChannelWorkloadBehavior](API_CrossChannelWorkloadBehavior.md) object
Required: No

## See Also
<a name="API_WorkloadTypeConcurrency_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/WorkloadTypeConcurrency)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/WorkloadTypeConcurrency)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/WorkloadTypeConcurrency)
