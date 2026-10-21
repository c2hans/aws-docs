---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_NotificationConfig.html
---

# NotificationConfig
<a name="API_NotificationConfig"></a>

The notification configuration for a notebook run in Amazon SageMaker Unified Studio.

## Contents
<a name="API_NotificationConfig_Contents"></a>

 ** notifyOn **   <a name="datazone-Type-NotificationConfig-notifyOn"></a>
The notebook run states that trigger notifications. You can specify up to 7 states, and the ordering of the states is not significant.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 7 items.
Valid Values: `SUCCEEDED | FAILED | STOPPED | QUEUED | STARTING | RUNNING | STOPPING`
Required: Yes

## See Also
<a name="API_NotificationConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/NotificationConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/NotificationConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/NotificationConfig)
