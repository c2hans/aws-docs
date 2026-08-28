---
source_url: https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_RecommenderSchemaSummary.html
---

# RecommenderSchemaSummary
<a name="API_connect-customer-profiles_RecommenderSchemaSummary"></a>

Provides a summary of a recommender schema's configuration and current state.

## Contents
<a name="API_connect-customer-profiles_RecommenderSchemaSummary_Contents"></a>

 ** CreatedAt **   <a name="connect-Type-connect-customer-profiles_RecommenderSchemaSummary-CreatedAt"></a>
The timestamp when the recommender schema was created.
Type: Timestamp
Required: Yes

 ** Fields **   <a name="connect-Type-connect-customer-profiles_RecommenderSchemaSummary-Fields"></a>
A map of dataset type to column definitions included in the schema.
Type: String to array of [RecommenderSchemaField](API_connect-customer-profiles_RecommenderSchemaField.md) objects map
Map Entries: Maximum number of 1 item.
Array Members: Minimum number of 1 item. Maximum number of 9 items.
Required: Yes

 ** RecommenderSchemaName **   <a name="connect-Type-connect-customer-profiles_RecommenderSchemaSummary-RecommenderSchemaName"></a>
The name of the recommender schema.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** Status **   <a name="connect-Type-connect-customer-profiles_RecommenderSchemaSummary-Status"></a>
The current operational status of the recommender schema.
Type: String
Valid Values: `ACTIVE | DELETING`
Required: Yes

## See Also
<a name="API_connect-customer-profiles_RecommenderSchemaSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/RecommenderSchemaSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/RecommenderSchemaSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/RecommenderSchemaSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
