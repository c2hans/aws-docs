---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_PardotConnectorProfileProperties.html
---

# PardotConnectorProfileProperties
<a name="API_PardotConnectorProfileProperties"></a>

The connector-specific profile properties required when using Salesforce Pardot.

## Contents
<a name="API_PardotConnectorProfileProperties_Contents"></a>

 ** businessUnitId **   <a name="appflow-Type-PardotConnectorProfileProperties-businessUnitId"></a>
The business unit id of Salesforce Pardot instance.
Type: String
Length Constraints: Maximum length of 18.
Pattern: `\S+`
Required: No

 ** instanceUrl **   <a name="appflow-Type-PardotConnectorProfileProperties-instanceUrl"></a>
The location of the Salesforce Pardot resource.
Type: String
Length Constraints: Maximum length of 256.
Pattern: `\S+`
Required: No

 ** isSandboxEnvironment **   <a name="appflow-Type-PardotConnectorProfileProperties-isSandboxEnvironment"></a>
Indicates whether the connector profile applies to a sandbox or production environment.
Type: Boolean
Required: No

## See Also
<a name="API_PardotConnectorProfileProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/PardotConnectorProfileProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/PardotConnectorProfileProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/PardotConnectorProfileProperties)
