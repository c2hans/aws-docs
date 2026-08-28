---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_ConnectorEntityField.html
---

# ConnectorEntityField
<a name="API_ConnectorEntityField"></a>

 Describes the data model of a connector field. For example, for an *account* entity, the fields would be *account name*, *account ID*, and so on.

## Contents
<a name="API_ConnectorEntityField_Contents"></a>

 ** identifier **   <a name="appflow-Type-ConnectorEntityField-identifier"></a>
 The unique identifier of the connector field.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `\S+`
Required: Yes

 ** customProperties **   <a name="appflow-Type-ConnectorEntityField-customProperties"></a>
A map that has specific properties related to the ConnectorEntityField.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `[\w]+`
Value Length Constraints: Maximum length of 2048.
Value Pattern: `\S+`
Required: No

 ** defaultValue **   <a name="appflow-Type-ConnectorEntityField-defaultValue"></a>
Default value that can be assigned to this field.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `.*`
Required: No

 ** description **   <a name="appflow-Type-ConnectorEntityField-description"></a>
 A description of the connector entity field.
Type: String
Length Constraints: Maximum length of 1024.
Pattern: `[\s\w/!@#+=.-]*`
Required: No

 ** destinationProperties **   <a name="appflow-Type-ConnectorEntityField-destinationProperties"></a>
 The properties applied to a field when the connector is being used as a destination.
Type: [DestinationFieldProperties](API_DestinationFieldProperties.md) object
Required: No

 ** isDeprecated **   <a name="appflow-Type-ConnectorEntityField-isDeprecated"></a>
Booelan value that indicates whether this field is deprecated or not.
Type: Boolean
Required: No

 ** isPrimaryKey **   <a name="appflow-Type-ConnectorEntityField-isPrimaryKey"></a>
Booelan value that indicates whether this field can be used as a primary key.
Type: Boolean
Required: No

 ** label **   <a name="appflow-Type-ConnectorEntityField-label"></a>
 The label applied to a connector entity field.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `.*`
Required: No

 ** parentIdentifier **   <a name="appflow-Type-ConnectorEntityField-parentIdentifier"></a>
The parent identifier of the connector field.
Type: String
Length Constraints: Maximum length of 128.
Pattern: `\S+`
Required: No

 ** sourceProperties **   <a name="appflow-Type-ConnectorEntityField-sourceProperties"></a>
 The properties that can be applied to a field when the connector is being used as a source.
Type: [SourceFieldProperties](API_SourceFieldProperties.md) object
Required: No

 ** supportedFieldTypeDetails **   <a name="appflow-Type-ConnectorEntityField-supportedFieldTypeDetails"></a>
 Contains details regarding the supported `FieldType`, including the corresponding `filterOperators` and `supportedValues`.
Type: [SupportedFieldTypeDetails](API_SupportedFieldTypeDetails.md) object
Required: No

## See Also
<a name="API_ConnectorEntityField_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/ConnectorEntityField)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/ConnectorEntityField)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/ConnectorEntityField)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
