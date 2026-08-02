---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_SourceConfiguration.html
---

# SourceConfiguration
<a name="API_amazon-q-connect_SourceConfiguration"></a>

Configuration information about the external data source.

## Contents
<a name="API_amazon-q-connect_SourceConfiguration_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** appIntegrations **   <a name="connect-Type-amazon-q-connect_SourceConfiguration-appIntegrations"></a>
Configuration information for Amazon AppIntegrations to automatically ingest content.
Type: [AppIntegrationsConfiguration](API_amazon-q-connect_AppIntegrationsConfiguration.md) object
Required: No

 ** managedSourceConfiguration **   <a name="connect-Type-amazon-q-connect_SourceConfiguration-managedSourceConfiguration"></a>
Source configuration for managed resources.
Type: [ManagedSourceConfiguration](API_amazon-q-connect_ManagedSourceConfiguration.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_amazon-q-connect_SourceConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/SourceConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/SourceConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/SourceConfiguration)
