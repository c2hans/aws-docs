---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_CodeRepositoryMetadata.html
---

# CodeRepositoryMetadata
<a name="API_CodeRepositoryMetadata"></a>

Contains metadata information about a code repository that is being scanned by Amazon Inspector.

## Contents
<a name="API_CodeRepositoryMetadata_Contents"></a>

 ** projectName **   <a name="inspector2-Type-CodeRepositoryMetadata-projectName"></a>
The name of the project in the code repository.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** providerType **   <a name="inspector2-Type-CodeRepositoryMetadata-providerType"></a>
The type of repository provider (such as GitHub, GitLab, etc.).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** providerTypeVisibility **   <a name="inspector2-Type-CodeRepositoryMetadata-providerTypeVisibility"></a>
The visibility setting of the repository (public or private).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** integrationArn **   <a name="inspector2-Type-CodeRepositoryMetadata-integrationArn"></a>
The Amazon Resource Name (ARN) of the code security integration associated with the repository.
Type: String
Pattern: `arn:(aws[a-zA-Z-]*)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:codesecurity-integration\/[a-f0-9-]{36}`
Required: No

 ** lastScannedCommitId **   <a name="inspector2-Type-CodeRepositoryMetadata-lastScannedCommitId"></a>
The ID of the last commit that was scanned in the repository.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 40.
Pattern: `([a-f0-9]{40})`
Required: No

 ** onDemandScan **   <a name="inspector2-Type-CodeRepositoryMetadata-onDemandScan"></a>
Information about on-demand scans performed on the repository.
Type: [CodeRepositoryOnDemandScan](API_CodeRepositoryOnDemandScan.md) object
Required: No

 ** scanConfiguration **   <a name="inspector2-Type-CodeRepositoryMetadata-scanConfiguration"></a>
The scan configuration settings applied to the code repository.
Type: [ProjectCodeSecurityScanConfiguration](API_ProjectCodeSecurityScanConfiguration.md) object
Required: No

## See Also
<a name="API_CodeRepositoryMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/CodeRepositoryMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/CodeRepositoryMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/CodeRepositoryMetadata)
