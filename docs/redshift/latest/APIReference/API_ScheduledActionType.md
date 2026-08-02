---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_ScheduledActionType.html
---

# ScheduledActionType
<a name="API_ScheduledActionType"></a>

The action type that specifies an Amazon Redshift API operation that is supported by the Amazon Redshift scheduler.

## Contents
<a name="API_ScheduledActionType_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** PauseCluster **
An action that runs a `PauseCluster` API operation.
Type: [PauseClusterMessage](API_PauseClusterMessage.md) object
Required: No

 ** ResizeCluster **
An action that runs a `ResizeCluster` API operation.
Type: [ResizeClusterMessage](API_ResizeClusterMessage.md) object
Required: No

 ** ResumeCluster **
An action that runs a `ResumeCluster` API operation.
Type: [ResumeClusterMessage](API_ResumeClusterMessage.md) object
Required: No

## See Also
<a name="API_ScheduledActionType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/ScheduledActionType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/ScheduledActionType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/ScheduledActionType)
