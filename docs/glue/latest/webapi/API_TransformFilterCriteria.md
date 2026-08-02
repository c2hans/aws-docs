---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_TransformFilterCriteria.html
---

# TransformFilterCriteria
<a name="API_TransformFilterCriteria"></a>

The criteria used to filter the machine learning transforms.

## Contents
<a name="API_TransformFilterCriteria_Contents"></a>

 ** CreatedAfter **   <a name="Glue-Type-TransformFilterCriteria-CreatedAfter"></a>
The time and date after which the transforms were created.
Type: Timestamp
Required: No

 ** CreatedBefore **   <a name="Glue-Type-TransformFilterCriteria-CreatedBefore"></a>
The time and date before which the transforms were created.
Type: Timestamp
Required: No

 ** GlueVersion **   <a name="Glue-Type-TransformFilterCriteria-GlueVersion"></a>
This value determines which version of AWS Glue this machine learning transform is compatible with. Glue 1.0 is recommended for most customers. If the value is not set, the Glue compatibility defaults to Glue 0.9. For more information, see [AWS Glue Versions](https://docs.aws.amazon.com/glue/latest/dg/release-notes.html#release-notes-versions) in the developer guide.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^(\w+\.)+\w+$`
Required: No

 ** LastModifiedAfter **   <a name="Glue-Type-TransformFilterCriteria-LastModifiedAfter"></a>
Filter on transforms last modified after this date.
Type: Timestamp
Required: No

 ** LastModifiedBefore **   <a name="Glue-Type-TransformFilterCriteria-LastModifiedBefore"></a>
Filter on transforms last modified before this date.
Type: Timestamp
Required: No

 ** Name **   <a name="Glue-Type-TransformFilterCriteria-Name"></a>
A unique transform name that is used to filter the machine learning transforms.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** Schema **   <a name="Glue-Type-TransformFilterCriteria-Schema"></a>
Filters on datasets with a specific schema. The `Map<Column, Type>` object is an array of key-value pairs representing the schema this transform accepts, where `Column` is the name of a column, and `Type` is the type of the data such as an integer or string. Has an upper bound of 100 columns.
Type: Array of [SchemaColumn](API_SchemaColumn.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** Status **   <a name="Glue-Type-TransformFilterCriteria-Status"></a>
Filters the list of machine learning transforms by the last known status of the transforms (to indicate whether a transform can be used or not). One of "NOT\_READY", "READY", or "DELETING".
Type: String
Valid Values: `NOT_READY | READY | DELETING`
Required: No

 ** TransformType **   <a name="Glue-Type-TransformFilterCriteria-TransformType"></a>
The type of machine learning transform that is used to filter the machine learning transforms.
Type: String
Valid Values: `FIND_MATCHES`
Required: No

## See Also
<a name="API_TransformFilterCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/TransformFilterCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/TransformFilterCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/TransformFilterCriteria)
