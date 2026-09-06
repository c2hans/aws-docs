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
