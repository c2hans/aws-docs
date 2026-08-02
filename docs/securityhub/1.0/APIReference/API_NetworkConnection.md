---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_NetworkConnection.html
---

# NetworkConnection
<a name="API_NetworkConnection"></a>

 Contains information about the network connection involved in an Amazon GuardDuty Extended Threat Detection attack sequence. GuardDuty generates an attack sequence finding when multiple events align to a potentially suspicious activity. To receive GuardDuty attack sequence findings in AWS Security Hub CSPM, you must have GuardDuty enabled. For more information, see [GuardDuty Extended Threat Detection ](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty-extended-threat-detection.html) in the *Amazon GuardDuty User Guide*.

## Contents
<a name="API_NetworkConnection_Contents"></a>

 ** Direction **   <a name="securityhub-Type-NetworkConnection-Direction"></a>
 The direction in which the network traffic is flowing.
Type: String
Valid Values: `INBOUND | OUTBOUND`
Required: No

## See Also
<a name="API_NetworkConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/NetworkConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/NetworkConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/NetworkConnection)
