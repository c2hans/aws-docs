---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_NetworkCardInfo.html
---

# NetworkCardInfo
<a name="API_NetworkCardInfo"></a>

Describes the network card support of the instance type.

## Contents
<a name="API_NetworkCardInfo_Contents"></a>

 ** additionalFlexibleNetworkInterfaces **
The number of additional network interfaces that can be attached to an instance when using flexible Elastic Network Adapter (ENA) queues. This number is in addition to the base number specified by `maximumNetworkInterfaces`.
Type: Integer
Required: No

 ** baselineBandwidthInGbps **
The baseline network performance of the network card, in Gbps.
Type: Double
Required: No

 ** defaultEnaQueueCountPerInterface **
The default number of the ENA queues for each interface.
Type: Integer
Required: No

 ** maximumEnaQueueCount **
The maximum number of the ENA queues.
Type: Integer
Required: No

 ** maximumEnaQueueCountPerInterface **
The maximum number of the ENA queues for each interface.
Type: Integer
Required: No

 ** maximumNetworkInterfaces **
The maximum number of network interfaces for the network card.
Type: Integer
Required: No

 ** networkCardIndex **
The index of the network card.
Type: Integer
Required: No

 ** networkPerformance **
The network performance of the network card.
Type: String
Required: No

 ** peakBandwidthInGbps **
The peak (burst) network performance of the network card, in Gbps.
Type: Double
Required: No

## See Also
<a name="API_NetworkCardInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/NetworkCardInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/NetworkCardInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/NetworkCardInfo)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
