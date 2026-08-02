---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_ServiceSyncConfig.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# ServiceSyncConfig
<a name="API_ServiceSyncConfig"></a>

Detailed data of the service sync configuration.

## Contents
<a name="API_ServiceSyncConfig_Contents"></a>

 ** branch **   <a name="proton-Type-ServiceSyncConfig-branch"></a>
The name of the code repository branch that holds the service code AWS Proton will sync with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 200.
Required: Yes

 ** filePath **   <a name="proton-Type-ServiceSyncConfig-filePath"></a>
The file path to the service sync configuration file.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: Yes

 ** repositoryName **   <a name="proton-Type-ServiceSyncConfig-repositoryName"></a>
The name of the code repository that holds the service code AWS Proton will sync with.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*[A-Za-z0-9_.-].*/[A-Za-z0-9_.-].*`
Required: Yes

 ** repositoryProvider **   <a name="proton-Type-ServiceSyncConfig-repositoryProvider"></a>
The name of the repository provider that holds the repository AWS Proton will sync with.
Type: String
Valid Values: `GITHUB | GITHUB_ENTERPRISE | BITBUCKET`
Required: Yes

 ** serviceName **   <a name="proton-Type-ServiceSyncConfig-serviceName"></a>
The name of the service that the service instance is added to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

## See Also
<a name="API_ServiceSyncConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/ServiceSyncConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/ServiceSyncConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/ServiceSyncConfig)
