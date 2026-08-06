---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_ProvisionedPollerConfig.html
---

# ProvisionedPollerConfig
<a name="API_ProvisionedPollerConfig"></a>

The [ provisioned mode](https://docs.aws.amazon.com/lambda/latest/dg/invocation-eventsourcemapping.html#invocation-eventsourcemapping-provisioned-mode) configuration for the event source. Use Provisioned Mode to customize the minimum and maximum number of event pollers for your event source.

## Contents
<a name="API_ProvisionedPollerConfig_Contents"></a>

 ** MaximumPollers **   <a name="lambda-Type-ProvisionedPollerConfig-MaximumPollers"></a>
The maximum number of event pollers this event source can scale up to. For Amazon SQS event source mappings, the accepted range is between 2 and 10,000, with a default of 200. For Amazon MSK and self-managed Apache Kafka event source mappings, the accepted range is between 1 and 2,000, with a default of 200.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 2000.
Required: No

 ** MinimumPollers **   <a name="lambda-Type-ProvisionedPollerConfig-MinimumPollers"></a>
The minimum number of event pollers this event source can scale down to. For Amazon SQS events source mappings, default is 2, and minimum 2 required. For Amazon MSK and self-managed Apache Kafka event source mappings, default is 1.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 200.
Required: No

 ** PollerGroupName **   <a name="lambda-Type-ProvisionedPollerConfig-PollerGroupName"></a>
(Amazon MSK and self-managed Apache Kafka) The name of the provisioned poller group. Use this option to group multiple ESMs within the event source's VPC to share Event Poller Unit (EPU) capacity. You can use this option to optimize Provisioned mode costs for your ESMs. You can group up to 100 ESMs per poller group and aggregate maximum pollers across all ESMs in a group cannot exceed 2000.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_]*`
Required: No

## See Also
<a name="API_ProvisionedPollerConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/ProvisionedPollerConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/ProvisionedPollerConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/ProvisionedPollerConfig)
