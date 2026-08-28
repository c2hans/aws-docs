---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_RedshiftPropertiesInput.html
---

# RedshiftPropertiesInput
<a name="API_RedshiftPropertiesInput"></a>

The Amazon Redshift properties.

## Contents
<a name="API_RedshiftPropertiesInput_Contents"></a>

 ** credentials **   <a name="datazone-Type-RedshiftPropertiesInput-credentials"></a>
The Amaon Redshift credentials.
Type: [RedshiftCredentials](API_RedshiftCredentials.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** databaseName **   <a name="datazone-Type-RedshiftPropertiesInput-databaseName"></a>
The Amazon Redshift database name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** host **   <a name="datazone-Type-RedshiftPropertiesInput-host"></a>
The Amazon Redshift host.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** lineageSync **   <a name="datazone-Type-RedshiftPropertiesInput-lineageSync"></a>
The lineage sync of the Amazon Redshift.
Type: [RedshiftLineageSyncConfigurationInput](API_RedshiftLineageSyncConfigurationInput.md) object
Required: No

 ** port **   <a name="datazone-Type-RedshiftPropertiesInput-port"></a>
The Amaon Redshift port.
Type: Integer
Required: No

 ** storage **   <a name="datazone-Type-RedshiftPropertiesInput-storage"></a>
The Amazon Redshift storage.
Type: [RedshiftStorageProperties](API_RedshiftStorageProperties.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## See Also
<a name="API_RedshiftPropertiesInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/RedshiftPropertiesInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/RedshiftPropertiesInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/RedshiftPropertiesInput)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
