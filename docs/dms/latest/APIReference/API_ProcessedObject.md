---
source_url: https://docs.aws.amazon.com/dms/latest/APIReference/API_ProcessedObject.html
---

# ProcessedObject
<a name="API_ProcessedObject"></a>

The database object that the schema conversion operation currently uses.

## Contents
<a name="API_ProcessedObject_Contents"></a>

 ** EndpointType **   <a name="DMS-Type-ProcessedObject-EndpointType"></a>
The type of the data provider. This parameter can store one of the following values: `"SOURCE"` or `"TARGET"`.
Type: String
Required: No

 ** Name **   <a name="DMS-Type-ProcessedObject-Name"></a>
The name of the database object.
Type: String
Required: No

 ** Type **   <a name="DMS-Type-ProcessedObject-Type"></a>
The type of the database object. For example, a table, view, procedure, and so on.
Type: String
Required: No

## See Also
<a name="API_ProcessedObject_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dms-2016-01-01/ProcessedObject)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dms-2016-01-01/ProcessedObject)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dms-2016-01-01/ProcessedObject)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Database Migration Service (DMS) Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
