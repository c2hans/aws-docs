---
source_url: https://docs.aws.amazon.com/lightsail/2016-11-28/api-reference/API_RelationalDatabaseEvent.html
---

# RelationalDatabaseEvent
<a name="API_RelationalDatabaseEvent"></a>

Describes an event for a database.

## Contents
<a name="API_RelationalDatabaseEvent_Contents"></a>

 ** createdAt **   <a name="Lightsail-Type-RelationalDatabaseEvent-createdAt"></a>
The timestamp when the database event was created.
Type: Timestamp
Required: No

 ** eventCategories **   <a name="Lightsail-Type-RelationalDatabaseEvent-eventCategories"></a>
The category that the database event belongs to.
Type: Array of strings
Required: No

 ** message **   <a name="Lightsail-Type-RelationalDatabaseEvent-message"></a>
The message of the database event.
Type: String
Required: No

 ** resource **   <a name="Lightsail-Type-RelationalDatabaseEvent-resource"></a>
The database that the database event relates to.
Type: String
Pattern: `\w[\w\-]*\w`
Required: No

## See Also
<a name="API_RelationalDatabaseEvent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lightsail-2016-11-28/RelationalDatabaseEvent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lightsail-2016-11-28/RelationalDatabaseEvent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lightsail-2016-11-28/RelationalDatabaseEvent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lightsail. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lightsail` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
