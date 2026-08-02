---
source_url: https://docs.aws.amazon.com/pca-connector-ad/latest/APIReference/API_SubjectNameFlagsV3.html
---

# SubjectNameFlagsV3
<a name="API_SubjectNameFlagsV3"></a>

Information to include in the subject name and alternate subject name of the certificate. The subject name can be common name, directory path, DNS as common name, or left blank. You can optionally include email to the subject name for user templates. If you leave the subject name blank then you must set a subject alternate name. The subject alternate name (SAN) can include globally unique identifier (GUID), DNS, domain DNS, email, service principal name (SPN), and user principal name (UPN). You can leave the SAN blank. If you leave the SAN blank, then you must set a subject name.

## Contents
<a name="API_SubjectNameFlagsV3_Contents"></a>

 ** RequireCommonName **   <a name="PcaConnectorAd-Type-SubjectNameFlagsV3-RequireCommonName"></a>
Include the common name in the subject name.
Type: Boolean
Required: No

 ** RequireDirectoryPath **   <a name="PcaConnectorAd-Type-SubjectNameFlagsV3-RequireDirectoryPath"></a>
Include the directory path in the subject name.
Type: Boolean
Required: No

 ** RequireDnsAsCn **   <a name="PcaConnectorAd-Type-SubjectNameFlagsV3-RequireDnsAsCn"></a>
Include the DNS as common name in the subject name.
Type: Boolean
Required: No

 ** RequireEmail **   <a name="PcaConnectorAd-Type-SubjectNameFlagsV3-RequireEmail"></a>
Include the subject's email in the subject name.
Type: Boolean
Required: No

 ** SanRequireDirectoryGuid **   <a name="PcaConnectorAd-Type-SubjectNameFlagsV3-SanRequireDirectoryGuid"></a>
Include the globally unique identifier (GUID) in the subject alternate name.
Type: Boolean
Required: No

 ** SanRequireDns **   <a name="PcaConnectorAd-Type-SubjectNameFlagsV3-SanRequireDns"></a>
Include the DNS in the subject alternate name.
Type: Boolean
Required: No

 ** SanRequireDomainDns **   <a name="PcaConnectorAd-Type-SubjectNameFlagsV3-SanRequireDomainDns"></a>
Include the domain DNS in the subject alternate name.
Type: Boolean
Required: No

 ** SanRequireEmail **   <a name="PcaConnectorAd-Type-SubjectNameFlagsV3-SanRequireEmail"></a>
Include the subject's email in the subject alternate name.
Type: Boolean
Required: No

 ** SanRequireSpn **   <a name="PcaConnectorAd-Type-SubjectNameFlagsV3-SanRequireSpn"></a>
Include the service principal name (SPN) in the subject alternate name.
Type: Boolean
Required: No

 ** SanRequireUpn **   <a name="PcaConnectorAd-Type-SubjectNameFlagsV3-SanRequireUpn"></a>
Include the user principal name (UPN) in the subject alternate name.
Type: Boolean
Required: No

## See Also
<a name="API_SubjectNameFlagsV3_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-ad-2018-05-10/SubjectNameFlagsV3)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-ad-2018-05-10/SubjectNameFlagsV3)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-ad-2018-05-10/SubjectNameFlagsV3)
