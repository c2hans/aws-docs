---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_PackageConfiguration.html
---

# PackageConfiguration
<a name="API_PackageConfiguration"></a>

 The configuration parameters for a package.

## Contents
<a name="API_PackageConfiguration_Contents"></a>

 ** ConfigurationRequirement **   <a name="opensearchservice-Type-PackageConfiguration-ConfigurationRequirement"></a>
The configuration requirements for the package.
Type: String
Valid Values: `REQUIRED | OPTIONAL | NONE`
Required: Yes

 ** LicenseRequirement **   <a name="opensearchservice-Type-PackageConfiguration-LicenseRequirement"></a>
The license requirements for the package.
Type: String
Valid Values: `REQUIRED | OPTIONAL | NONE`
Required: Yes

 ** LicenseFilepath **   <a name="opensearchservice-Type-PackageConfiguration-LicenseFilepath"></a>
The relative file path for the license associated with the package.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^(?!.*\/\.{2,})(?!.*\.\.)[a-zA-Z0-9_.-]+(?:\/[a-zA-Z0-9_.-]+)*$`
Required: No

 ** RequiresRestartForConfigurationUpdate **   <a name="opensearchservice-Type-PackageConfiguration-RequiresRestartForConfigurationUpdate"></a>
This indicates whether a B/G deployment is required for updating the configuration that the plugin is prerequisite for.
Type: Boolean
Required: No

## See Also
<a name="API_PackageConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/PackageConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/PackageConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/PackageConfiguration)
