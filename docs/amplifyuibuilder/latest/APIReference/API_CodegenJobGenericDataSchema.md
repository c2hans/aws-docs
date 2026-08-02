---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_CodegenJobGenericDataSchema.html
---

# CodegenJobGenericDataSchema
<a name="API_CodegenJobGenericDataSchema"></a>

Describes the data schema for a code generation job.

## Contents
<a name="API_CodegenJobGenericDataSchema_Contents"></a>

 ** dataSourceType **   <a name="amplifyuibuilder-Type-CodegenJobGenericDataSchema-dataSourceType"></a>
The type of the data source for the schema. Currently, the only valid value is an Amplify `DataStore`.
Type: String
Valid Values: `DataStore`
Required: Yes

 ** enums **   <a name="amplifyuibuilder-Type-CodegenJobGenericDataSchema-enums"></a>
The name of a `CodegenGenericDataEnum`.
Type: String to [CodegenGenericDataEnum](API_CodegenGenericDataEnum.md) object map
Required: Yes

 ** models **   <a name="amplifyuibuilder-Type-CodegenJobGenericDataSchema-models"></a>
The name of a `CodegenGenericDataModel`.
Type: String to [CodegenGenericDataModel](API_CodegenGenericDataModel.md) object map
Required: Yes

 ** nonModels **   <a name="amplifyuibuilder-Type-CodegenJobGenericDataSchema-nonModels"></a>
The name of a `CodegenGenericDataNonModel`.
Type: String to [CodegenGenericDataNonModel](API_CodegenGenericDataNonModel.md) object map
Required: Yes

## See Also
<a name="API_CodegenJobGenericDataSchema_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/CodegenJobGenericDataSchema)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/CodegenJobGenericDataSchema)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/CodegenJobGenericDataSchema)
