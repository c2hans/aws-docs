---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_RegionInfo.html
---

# RegionInfo
<a name="API_RegionInfo"></a>

Information about a AWS Region in your replication set.

## Contents
<a name="API_RegionInfo_Contents"></a>

 ** status **   <a name="IncidentManager-Type-RegionInfo-status"></a>
The status of the AWS Region in the replication set.
Type: String
Valid Values: `ACTIVE | CREATING | DELETING | FAILED`
Required: Yes

 ** statusUpdateDateTime **   <a name="IncidentManager-Type-RegionInfo-statusUpdateDateTime"></a>
The timestamp for when Incident Manager updated the status of the AWS Region.
Type: Timestamp
Required: Yes

 ** sseKmsKeyId **   <a name="IncidentManager-Type-RegionInfo-sseKmsKeyId"></a>
The ID of the KMS key used to encrypt the data in this AWS Region.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Required: No

 ** statusMessage **   <a name="IncidentManager-Type-RegionInfo-statusMessage"></a>
Information displayed about the status of the AWS Region.
Type: String
Required: No

## See Also
<a name="API_RegionInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/RegionInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/RegionInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/RegionInfo)
