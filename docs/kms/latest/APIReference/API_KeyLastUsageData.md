---
source_url: https://docs.aws.amazon.com/kms/latest/APIReference/API_KeyLastUsageData.html
---

# KeyLastUsageData
<a name="API_KeyLastUsageData"></a>

Contains usage information about the last time the KMS key was used for a successful cryptographic operation.

## Contents
<a name="API_KeyLastUsageData_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** CloudTrailEventId **   <a name="KMS-Type-KeyLastUsageData-CloudTrailEventId"></a>
The CloudTrail `eventId` associated with the last successful cryptographic operation. Absent if the key has not been used since AWS KMS began tracking.
Type: String
Required: No

 ** KmsRequestId **   <a name="KMS-Type-KeyLastUsageData-KmsRequestId"></a>
The AWS KMS request ID associated with the last successful cryptographic operation. Absent if the key has not been used since AWS KMS began tracking.
Type: String
Required: No

 ** Operation **   <a name="KMS-Type-KeyLastUsageData-Operation"></a>
The last successful cryptographic operation the KMS key was used for. Absent if the key has not been used since AWS KMS began tracking.
Type: String
Valid Values: `Decrypt | DeriveSharedSecret | Encrypt | GenerateDataKey | GenerateDataKeyPair | GenerateDataKeyPairWithoutPlaintext | GenerateDataKeyWithoutPlaintext | GenerateMac | ReEncrypt | Sign | Verify | VerifyMac`
Required: No

 ** Timestamp **   <a name="KMS-Type-KeyLastUsageData-Timestamp"></a>
The date and time when the KMS key was most recently used for a successful cryptographic operation. Absent if the key has not been used since AWS KMS began tracking.
Type: Timestamp
Required: No

## See Also
<a name="API_KeyLastUsageData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kms-2014-11-01/KeyLastUsageData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kms-2014-11-01/KeyLastUsageData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kms-2014-11-01/KeyLastUsageData)
