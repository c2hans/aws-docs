---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_SAPODataConnectorProfileProperties.html
---

# SAPODataConnectorProfileProperties
<a name="API_SAPODataConnectorProfileProperties"></a>

 The connector-specific profile properties required when using SAPOData.

## Contents
<a name="API_SAPODataConnectorProfileProperties_Contents"></a>

 ** applicationHostUrl **   <a name="appflow-Type-SAPODataConnectorProfileProperties-applicationHostUrl"></a>
 The location of the SAPOData resource.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `^(https?)://[-a-zA-Z0-9+&@#/%?=~_|!:,.;]*[-a-zA-Z0-9+&@#/%=~_|]`
Required: Yes

 ** applicationServicePath **   <a name="appflow-Type-SAPODataConnectorProfileProperties-applicationServicePath"></a>
 The application path to catalog service.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: Yes

 ** clientNumber **   <a name="appflow-Type-SAPODataConnectorProfileProperties-clientNumber"></a>
 The client number for the client creating the connection.
Type: String
Length Constraints: Fixed length of 3.
Pattern: `^\d{3}$`
Required: Yes

 ** portNumber **   <a name="appflow-Type-SAPODataConnectorProfileProperties-portNumber"></a>
 The port number of the SAPOData instance.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: Yes

 ** disableSSO **   <a name="appflow-Type-SAPODataConnectorProfileProperties-disableSSO"></a>
If you set this parameter to `true`, Amazon AppFlow bypasses the single sign-on (SSO) settings in your SAP account when it accesses your SAP OData instance.
Whether you need this option depends on the types of credentials that you applied to your SAP OData connection profile. If your profile uses basic authentication credentials, SAP SSO can prevent Amazon AppFlow from connecting to your account with your username and password. In this case, bypassing SSO makes it possible for Amazon AppFlow to connect successfully. However, if your profile uses OAuth credentials, this parameter has no affect.
Type: Boolean
Required: No

 ** logonLanguage **   <a name="appflow-Type-SAPODataConnectorProfileProperties-logonLanguage"></a>
 The logon language of SAPOData instance.
Type: String
Length Constraints: Maximum length of 2.
Pattern: `^[a-zA-Z0-9_]*$`
Required: No

 ** oAuthProperties **   <a name="appflow-Type-SAPODataConnectorProfileProperties-oAuthProperties"></a>
 The SAPOData OAuth properties required for OAuth type authentication.
Type: [OAuthProperties](API_OAuthProperties.md) object
Required: No

 ** privateLinkServiceName **   <a name="appflow-Type-SAPODataConnectorProfileProperties-privateLinkServiceName"></a>
 The SAPOData Private Link service name to be used for private data transfers.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `^$|com.amazonaws.vpce.[\w/!:@#.\-]+`
Required: No

## See Also
<a name="API_SAPODataConnectorProfileProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/SAPODataConnectorProfileProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/SAPODataConnectorProfileProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/SAPODataConnectorProfileProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
