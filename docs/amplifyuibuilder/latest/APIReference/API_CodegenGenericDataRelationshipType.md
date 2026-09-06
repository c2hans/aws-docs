---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_CodegenGenericDataRelationshipType.html
---

# CodegenGenericDataRelationshipType
<a name="API_CodegenGenericDataRelationshipType"></a>

Describes the relationship between generic data models.

## Contents
<a name="API_CodegenGenericDataRelationshipType_Contents"></a>

 ** relatedModelName **   <a name="amplifyuibuilder-Type-CodegenGenericDataRelationshipType-relatedModelName"></a>
The name of the related model in the data relationship.
Type: String
Required: Yes

 ** type **   <a name="amplifyuibuilder-Type-CodegenGenericDataRelationshipType-type"></a>
The data relationship type.
Type: String
Valid Values: `HAS_MANY | HAS_ONE | BELONGS_TO`
Required: Yes

 ** associatedFields **   <a name="amplifyuibuilder-Type-CodegenGenericDataRelationshipType-associatedFields"></a>
The associated fields of the data relationship.
Type: Array of strings
Required: No

 ** belongsToFieldOnRelatedModel **   <a name="amplifyuibuilder-Type-CodegenGenericDataRelationshipType-belongsToFieldOnRelatedModel"></a>
The value of the `belongsTo` field on the related data model.
Type: String
Required: No

 ** canUnlinkAssociatedModel **   <a name="amplifyuibuilder-Type-CodegenGenericDataRelationshipType-canUnlinkAssociatedModel"></a>
Specifies whether the relationship can unlink the associated model.
Type: Boolean
Required: No

 ** isHasManyIndex **   <a name="amplifyuibuilder-Type-CodegenGenericDataRelationshipType-isHasManyIndex"></a>
Specifies whether the `@index` directive is supported for a `hasMany` data relationship.
Type: Boolean
Required: No

 ** relatedJoinFieldName **   <a name="amplifyuibuilder-Type-CodegenGenericDataRelationshipType-relatedJoinFieldName"></a>
The name of the related join field in the data relationship.
Type: String
Required: No

 ** relatedJoinTableName **   <a name="amplifyuibuilder-Type-CodegenGenericDataRelationshipType-relatedJoinTableName"></a>
The name of the related join table in the data relationship.
Type: String
Required: No

 ** relatedModelFields **   <a name="amplifyuibuilder-Type-CodegenGenericDataRelationshipType-relatedModelFields"></a>
The related model fields in the data relationship.
Type: Array of strings
Required: No

## See Also
<a name="API_CodegenGenericDataRelationshipType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/CodegenGenericDataRelationshipType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/CodegenGenericDataRelationshipType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/CodegenGenericDataRelationshipType)
