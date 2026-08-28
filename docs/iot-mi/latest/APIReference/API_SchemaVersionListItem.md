---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_SchemaVersionListItem.html
---

# SchemaVersionListItem
<a name="API_SchemaVersionListItem"></a>

List item describing a schema version.

## Contents
<a name="API_SchemaVersionListItem_Contents"></a>

 ** Description **   <a name="managedintegrations-Type-SchemaVersionListItem-Description"></a>
A description of the schema version.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 2048.
Pattern: `[a-zA-Z0-9.,/ -]+`
Required: No

 ** Namespace **   <a name="managedintegrations-Type-SchemaVersionListItem-Namespace"></a>
The name of the schema version.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 12.
Pattern: `[a-z0-9]+`
Required: No

 ** SchemaId **   <a name="managedintegrations-Type-SchemaVersionListItem-SchemaId"></a>
The identifier of the schema version.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `[a-zA-Z0-9.]+`
Required: No

 ** SemanticVersion **   <a name="managedintegrations-Type-SchemaVersionListItem-SemanticVersion"></a>
The schema version. If this is left blank, it defaults to the latest version.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 12.
Pattern: `(\d+\.\d+(\.\d+)?|\$latest)`
Required: No

 ** Type **   <a name="managedintegrations-Type-SchemaVersionListItem-Type"></a>
The type of schema version.
Type: String
Valid Values: `capability | definition`
Required: No

 ** Visibility **   <a name="managedintegrations-Type-SchemaVersionListItem-Visibility"></a>
The visibility of the schema version.
Type: String
Valid Values: `PUBLIC | PRIVATE`
Required: No

## See Also
<a name="API_SchemaVersionListItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/SchemaVersionListItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/SchemaVersionListItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/SchemaVersionListItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
