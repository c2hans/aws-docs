---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_GcpProviderDetailUpdate.html
---

# GcpProviderDetailUpdate

The configuration details specific to Google Cloud Platform (GCP) for updating a connector, including the scan scope and locations to scan.

## Contents
<a name="API_GcpProviderDetailUpdate_Contents"></a>

 ** autoInstallVMScanner **   <a name="inspector2-Type-GcpProviderDetailUpdate-autoInstallVMScanner"></a>
Specifies whether to automatically install the VM scanner on connected GCP resources.
Type: Boolean
Required: No

 ** gcpRegions **   <a name="inspector2-Type-GcpProviderDetailUpdate-gcpRegions"></a>
The updated GCP locations to scan, such as regions, zones, multi-regions, or dual-regions. Specify `ALL` to scan all locations.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 256 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `(ALL|[a-z][a-z0-9-]*)`
Required: No

 ** scopeConfiguration **   <a name="inspector2-Type-GcpProviderDetailUpdate-scopeConfiguration"></a>
The updated scope configuration that defines which GCP resources to scan.
Type: [GcpScopeConfigurationInput](API_GcpScopeConfigurationInput.md) object
Required: No

## See Also
<a name="API_GcpProviderDetailUpdate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/GcpProviderDetailUpdate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/GcpProviderDetailUpdate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/GcpProviderDetailUpdate)
