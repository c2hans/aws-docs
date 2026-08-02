---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_RepositoryScanningConfiguration.html
---

# RepositoryScanningConfiguration
<a name="API_RepositoryScanningConfiguration"></a>

The details of the scanning configuration for a repository.

## Contents
<a name="API_RepositoryScanningConfiguration_Contents"></a>

 ** appliedScanFilters **   <a name="ECR-Type-RepositoryScanningConfiguration-appliedScanFilters"></a>
The scan filters applied to the repository.
Type: Array of [ScanningRepositoryFilter](API_ScanningRepositoryFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.
Required: No

 ** repositoryArn **   <a name="ECR-Type-RepositoryScanningConfiguration-repositoryArn"></a>
The ARN of the repository.
Type: String
Required: No

 ** repositoryName **   <a name="ECR-Type-RepositoryScanningConfiguration-repositoryName"></a>
The name of the repository.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 256.
Pattern: `[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*(\/[a-z0-9]+((\.|_|__|-+)[a-z0-9]+)*)*`
Required: No

 ** scanFrequency **   <a name="ECR-Type-RepositoryScanningConfiguration-scanFrequency"></a>
The scan frequency for the repository.
Type: String
Valid Values: `SCAN_ON_PUSH | CONTINUOUS_SCAN | MANUAL`
Required: No

 ** scanOnPush **   <a name="ECR-Type-RepositoryScanningConfiguration-scanOnPush"></a>
Whether or not scan on push is configured for the repository.
Type: Boolean
Required: No

## See Also
<a name="API_RepositoryScanningConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/RepositoryScanningConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/RepositoryScanningConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/RepositoryScanningConfiguration)
