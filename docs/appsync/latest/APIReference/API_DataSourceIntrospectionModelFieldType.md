---
source_url: https://docs.aws.amazon.com/appsync/latest/APIReference/API_DataSourceIntrospectionModelFieldType.html
---

# DataSourceIntrospectionModelFieldType
<a name="API_DataSourceIntrospectionModelFieldType"></a>

Represents the type data for each field retrieved from the introspection.

## Contents
<a name="API_DataSourceIntrospectionModelFieldType_Contents"></a>

 ** kind **   <a name="appsync-Type-DataSourceIntrospectionModelFieldType-kind"></a>
Specifies the classification of data. For example, this could be set to values like `Scalar` or `NonNull` to indicate a fundamental property of the field.
Valid values include:
+  `Scalar`: Indicates the value is a primitive type (scalar).
+  `NonNull`: Indicates the field cannot be `null`.
+  `List`: Indicates the field contains a list.
Type: String
Required: No

 ** name **   <a name="appsync-Type-DataSourceIntrospectionModelFieldType-name"></a>
The name of the data type that represents the field. For example, `String` is a valid `name` value.
Type: String
Required: No

 ** type **   <a name="appsync-Type-DataSourceIntrospectionModelFieldType-type"></a>
The `DataSourceIntrospectionModelFieldType` object data. The `type` is only present if `DataSourceIntrospectionModelFieldType.kind` is set to `NonNull` or `List`.
The `type` typically contains its own `kind` and `name` fields to represent the actual type data. For instance, `type` could contain a `kind` value of `Scalar` with a `name` value of `String`. The values `Scalar` and `String` will be collectively stored in the `values` field.
Type: [DataSourceIntrospectionModelFieldType](#API_DataSourceIntrospectionModelFieldType) object
Required: No

 ** values **   <a name="appsync-Type-DataSourceIntrospectionModelFieldType-values"></a>
The values of the `type` field. This field represents the AppSync data type equivalent of the introspected field.
Type: Array of strings
Required: No

## See Also
<a name="API_DataSourceIntrospectionModelFieldType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appsync-2017-07-25/DataSourceIntrospectionModelFieldType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appsync-2017-07-25/DataSourceIntrospectionModelFieldType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appsync-2017-07-25/DataSourceIntrospectionModelFieldType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AppSync. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appsync` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
