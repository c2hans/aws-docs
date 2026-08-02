---
source_url: https://docs.aws.amazon.com/pinpoint-email/latest/APIReference/API_DedicatedIp.html
---

# DedicatedIp
<a name="API_DedicatedIp"></a>

Contains information about a dedicated IP address that is associated with your Amazon Pinpoint account.

## Contents
<a name="API_DedicatedIp_Contents"></a>

 ** Ip **   <a name="pinpoint-Type-DedicatedIp-Ip"></a>
An IP address that is reserved for use by your Amazon Pinpoint account.
Type: String
Required: Yes

 ** WarmupPercentage **   <a name="pinpoint-Type-DedicatedIp-WarmupPercentage"></a>
Indicates how complete the dedicated IP warm-up process is. When this value equals 1, the address has completed the warm-up process and is ready for use.
Type: Integer
Required: Yes

 ** WarmupStatus **   <a name="pinpoint-Type-DedicatedIp-WarmupStatus"></a>
The warm-up status of a dedicated IP address. The status can have one of the following values:
+  `IN_PROGRESS` – The IP address isn't ready to use because the dedicated IP warm-up process is ongoing.
+  `DONE` – The dedicated IP warm-up process is complete, and the IP address is ready to use.
Type: String
Valid Values: `IN_PROGRESS | DONE`
Required: Yes

 ** PoolName **   <a name="pinpoint-Type-DedicatedIp-PoolName"></a>
The name of the dedicated IP pool that the IP address is associated with.
Type: String
Required: No

## See Also
<a name="API_DedicatedIp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-email-2018-07-26/DedicatedIp)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-email-2018-07-26/DedicatedIp)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-email-2018-07-26/DedicatedIp)
