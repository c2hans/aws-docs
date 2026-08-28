---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_SourceConnectorProperties.html
---

# SourceConnectorProperties
<a name="API_connect-customer-profiles_SourceConnectorProperties"></a>

Specifies the information that is required to query a particular Amazon AppFlow connector. Customer Profiles supports Salesforce, Zendesk, Marketo, ServiceNow and Amazon S3.

## Contents
<a name="API_connect-customer-profiles_SourceConnectorProperties_Contents"></a>

 ** Marketo **   <a name="connect-Type-connect-customer-profiles_SourceConnectorProperties-Marketo"></a>
The properties that are applied when Marketo is being used as a source.
Type: [MarketoSourceProperties](API_connect-customer-profiles_MarketoSourceProperties.md) object
Required: No

 ** S3 **   <a name="connect-Type-connect-customer-profiles_SourceConnectorProperties-S3"></a>
The properties that are applied when Amazon S3 is being used as the flow source.
Type: [S3SourceProperties](API_connect-customer-profiles_S3SourceProperties.md) object
Required: No

 ** Salesforce **   <a name="connect-Type-connect-customer-profiles_SourceConnectorProperties-Salesforce"></a>
The properties that are applied when Salesforce is being used as a source.
Type: [SalesforceSourceProperties](API_connect-customer-profiles_SalesforceSourceProperties.md) object
Required: No

 ** ServiceNow **   <a name="connect-Type-connect-customer-profiles_SourceConnectorProperties-ServiceNow"></a>
The properties that are applied when ServiceNow is being used as a source.
Type: [ServiceNowSourceProperties](API_connect-customer-profiles_ServiceNowSourceProperties.md) object
Required: No

 ** Zendesk **   <a name="connect-Type-connect-customer-profiles_SourceConnectorProperties-Zendesk"></a>
The properties that are applied when using Zendesk as a flow source.
Type: [ZendeskSourceProperties](API_connect-customer-profiles_ZendeskSourceProperties.md) object
Required: No

## See Also
<a name="API_connect-customer-profiles_SourceConnectorProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/SourceConnectorProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/SourceConnectorProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/SourceConnectorProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
