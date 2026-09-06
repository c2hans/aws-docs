---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_RowFilterExpression.html
---

# RowFilterExpression
<a name="API_RowFilterExpression"></a>

The row filter expression.

## Contents
<a name="API_RowFilterExpression_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** equalTo **   <a name="datazone-Type-RowFilterExpression-equalTo"></a>
The 'equal to' clause of the row filter expression.
Type: [EqualToExpression](API_EqualToExpression.md) object
Required: No

 ** greaterThan **   <a name="datazone-Type-RowFilterExpression-greaterThan"></a>
The 'greater than' clause of the row filter expression.
Type: [GreaterThanExpression](API_GreaterThanExpression.md) object
Required: No

 ** greaterThanOrEqualTo **   <a name="datazone-Type-RowFilterExpression-greaterThanOrEqualTo"></a>
The 'greater than or equal to' clause of the filter expression.
Type: [GreaterThanOrEqualToExpression](API_GreaterThanOrEqualToExpression.md) object
Required: No

 ** in **   <a name="datazone-Type-RowFilterExpression-in"></a>
The 'in' clause of the row filter expression.
Type: [InExpression](API_InExpression.md) object
Required: No

 ** isNotNull **   <a name="datazone-Type-RowFilterExpression-isNotNull"></a>
The 'is not null' clause of the row filter expression.
Type: [IsNotNullExpression](API_IsNotNullExpression.md) object
Required: No

 ** isNull **   <a name="datazone-Type-RowFilterExpression-isNull"></a>
The 'is null' clause of the row filter expression.
Type: [IsNullExpression](API_IsNullExpression.md) object
Required: No

 ** lessThan **   <a name="datazone-Type-RowFilterExpression-lessThan"></a>
The 'less than' clause of the row filter expression.
Type: [LessThanExpression](API_LessThanExpression.md) object
Required: No

 ** lessThanOrEqualTo **   <a name="datazone-Type-RowFilterExpression-lessThanOrEqualTo"></a>
The 'less than or equal to' clause of the row filter expression.
Type: [LessThanOrEqualToExpression](API_LessThanOrEqualToExpression.md) object
Required: No

 ** like **   <a name="datazone-Type-RowFilterExpression-like"></a>
The 'like' clause of the row filter expression.
Type: [LikeExpression](API_LikeExpression.md) object
Required: No

 ** notEqualTo **   <a name="datazone-Type-RowFilterExpression-notEqualTo"></a>
The 'no equal to' clause of the row filter expression.
Type: [NotEqualToExpression](API_NotEqualToExpression.md) object
Required: No

 ** notIn **   <a name="datazone-Type-RowFilterExpression-notIn"></a>
The 'not in' clause of the row filter expression.
Type: [NotInExpression](API_NotInExpression.md) object
Required: No

 ** notLike **   <a name="datazone-Type-RowFilterExpression-notLike"></a>
The 'not like' clause of the row filter expression.
Type: [NotLikeExpression](API_NotLikeExpression.md) object
Required: No

## See Also
<a name="API_RowFilterExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/RowFilterExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/RowFilterExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/RowFilterExpression)
