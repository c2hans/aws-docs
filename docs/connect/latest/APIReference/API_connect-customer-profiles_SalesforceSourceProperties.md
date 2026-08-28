---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_SalesforceSourceProperties.html
---

# SalesforceSourceProperties
<a name="API_connect-customer-profiles_SalesforceSourceProperties"></a>

The properties that are applied when Salesforce is being used as a source.

## Contents
<a name="API_connect-customer-profiles_SalesforceSourceProperties_Contents"></a>

 ** Object **   <a name="connect-Type-connect-customer-profiles_SalesforceSourceProperties-Object"></a>
The object specified in the Salesforce flow source.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `\S+`
Required: Yes

 ** EnableDynamicFieldUpdate **   <a name="connect-Type-connect-customer-profiles_SalesforceSourceProperties-EnableDynamicFieldUpdate"></a>
The flag that enables dynamic fetching of new (recently added) fields in the Salesforce objects while running a flow.
Type: Boolean
Required: No

 ** IncludeDeletedRecords **   <a name="connect-Type-connect-customer-profiles_SalesforceSourceProperties-IncludeDeletedRecords"></a>
Indicates whether Amazon AppFlow includes deleted files in the flow run.
Type: Boolean
Required: No

## See Also
<a name="API_connect-customer-profiles_SalesforceSourceProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/SalesforceSourceProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/SalesforceSourceProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/SalesforceSourceProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
