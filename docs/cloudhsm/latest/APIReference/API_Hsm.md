---
source_url: https://docs.aws.amazon.com/cloudhsm/latest/APIReference/API_Hsm.html
---

# Hsm
<a name="API_Hsm"></a>

Contains information about a hardware security module (HSM) in an AWS CloudHSM cluster.

## Contents
<a name="API_Hsm_Contents"></a>

 ** HsmId **   <a name="CloudHSMV2-Type-Hsm-HsmId"></a>
The HSM's identifier (ID).
Type: String
Pattern: `hsm-[2-7a-zA-Z]{11,16}`
Required: Yes

 ** AvailabilityZone **   <a name="CloudHSMV2-Type-Hsm-AvailabilityZone"></a>
The Availability Zone that contains the HSM.
Type: String
Pattern: `[a-z]{2}(-(gov))?-(east|west|north|south|central){1,2}-\d[a-z]`
Required: No

 ** ClusterId **   <a name="CloudHSMV2-Type-Hsm-ClusterId"></a>
The identifier (ID) of the cluster that contains the HSM.
Type: String
Pattern: `cluster-[2-7a-zA-Z]{11,16}`
Required: No

 ** EniId **   <a name="CloudHSMV2-Type-Hsm-EniId"></a>
The identifier (ID) of the HSM's elastic network interface (ENI).
Type: String
Pattern: `eni-[0-9a-fA-F]{8,17}`
Required: No

 ** EniIp **   <a name="CloudHSMV2-Type-Hsm-EniIp"></a>
The IP address of the HSM's elastic network interface (ENI).
Type: String
Pattern: `\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}`
Required: No

 ** EniIpV6 **   <a name="CloudHSMV2-Type-Hsm-EniIpV6"></a>
The IPv6 address (if any) of the HSM's elastic network interface (ENI).
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** HsmType **   <a name="CloudHSMV2-Type-Hsm-HsmType"></a>
The type of HSM.
Type: String
Length Constraints: Maximum length of 32.
Pattern: `((p|)hsm[0-9][a-z.]*\.[a-zA-Z]+)`
Required: No

 ** State **   <a name="CloudHSMV2-Type-Hsm-State"></a>
The HSM's state.
Type: String
Valid Values: `CREATE_IN_PROGRESS | ACTIVE | DEGRADED | DELETE_IN_PROGRESS | DELETED`
Required: No

 ** StateMessage **   <a name="CloudHSMV2-Type-Hsm-StateMessage"></a>
A description of the HSM's state.
Type: String
Required: No

 ** SubnetId **   <a name="CloudHSMV2-Type-Hsm-SubnetId"></a>
The subnet that contains the HSM's elastic network interface (ENI).
Type: String
Pattern: `subnet-[0-9a-fA-F]{8,17}`
Required: No

## See Also
<a name="API_Hsm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cloudhsmv2-2017-04-28/Hsm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cloudhsmv2-2017-04-28/Hsm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cloudhsmv2-2017-04-28/Hsm)
