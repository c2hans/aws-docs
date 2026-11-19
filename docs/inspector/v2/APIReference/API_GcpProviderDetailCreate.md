---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_GcpProviderDetailCreate.html
---

# GcpProviderDetailCreate

The configuration details specific to Google Cloud Platform (GCP) for creating a connector, including the AWS Config connector association, scan scope, and locations to scan.

## Contents
<a name="API_GcpProviderDetailCreate_Contents"></a>

 ** awsConfigConnectorArn **   <a name="inspector2-Type-GcpProviderDetailCreate-awsConfigConnectorArn"></a>
The ARN of the AWS Config connector to associate with this connector.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:([^:]+):config:([^:]+):([^:]+):connector/([^/]+)/([^/]+)/([^/:\s]+)`
Required: Yes

 ** gcpRegions **   <a name="inspector2-Type-GcpProviderDetailCreate-gcpRegions"></a>
The GCP locations to scan, such as regions, zones, multi-regions, or dual-regions. Specify `ALL` to scan all locations.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 256 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(ALL|[a-z][a-z0-9-]*)`
Required: Yes

 ** scopeConfiguration **   <a name="inspector2-Type-GcpProviderDetailCreate-scopeConfiguration"></a>
The scope configuration that defines which GCP resources to scan.
Type: [GcpScopeConfigurationInput](API_GcpScopeConfigurationInput.md) object
Required: Yes

 ** autoInstallVMScanner **   <a name="inspector2-Type-GcpProviderDetailCreate-autoInstallVMScanner"></a>
Specifies whether to automatically install the VM scanner on connected GCP resources. Defaults to `true`.
Type: Boolean
Required: No

## See Also
<a name="API_GcpProviderDetailCreate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/GcpProviderDetailCreate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/GcpProviderDetailCreate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/GcpProviderDetailCreate)
