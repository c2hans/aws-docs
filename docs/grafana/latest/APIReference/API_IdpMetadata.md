---
source_url: https://docs.aws.amazon.com/grafana/latest/APIReference/API_IdpMetadata.html
---

# IdpMetadata
<a name="API_IdpMetadata"></a>

A structure containing the identity provider (IdP) metadata used to integrate the identity provider with this workspace. You can specify the metadata either by providing a URL to its location in the `url` parameter, or by specifying the full metadata in XML format in the `xml` parameter. Specifying both will cause an error.

## Contents
<a name="API_IdpMetadata_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** url **   <a name="ManagedGrafana-Type-IdpMetadata-url"></a>
The URL of the location containing the IdP metadata.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** xml **   <a name="ManagedGrafana-Type-IdpMetadata-xml"></a>
The full IdP metadata, in XML format.
Type: String
Required: No

## See Also
<a name="API_IdpMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/grafana-2020-08-18/IdpMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/grafana-2020-08-18/IdpMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/grafana-2020-08-18/IdpMetadata)
