---
source_url: https://docs.aws.amazon.com/amplifyuibuilder/latest/APIReference/API_Predicate.html
---

# Predicate
<a name="API_Predicate"></a>

Stores information for generating Amplify DataStore queries. Use a `Predicate` to retrieve a subset of the data in a collection.

## Contents
<a name="API_Predicate_Contents"></a>

 ** and **   <a name="amplifyuibuilder-Type-Predicate-and"></a>
A list of predicates to combine logically.
Type: Array of [Predicate](#API_Predicate) objects
Required: No

 ** field **   <a name="amplifyuibuilder-Type-Predicate-field"></a>
The field to query.
Type: String
Required: No

 ** operand **   <a name="amplifyuibuilder-Type-Predicate-operand"></a>
The value to use when performing the evaluation.
Type: String
Required: No

 ** operandType **   <a name="amplifyuibuilder-Type-Predicate-operandType"></a>
The type of value to use when performing the evaluation.
Type: String
Pattern: `boolean|string|number`
Required: No

 ** operator **   <a name="amplifyuibuilder-Type-Predicate-operator"></a>
The operator to use to perform the evaluation.
Type: String
Required: No

 ** or **   <a name="amplifyuibuilder-Type-Predicate-or"></a>
A list of predicates to combine logically.
Type: Array of [Predicate](#API_Predicate) objects
Required: No

## See Also
<a name="API_Predicate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/amplifyuibuilder-2021-08-11/Predicate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/amplifyuibuilder-2021-08-11/Predicate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/amplifyuibuilder-2021-08-11/Predicate)
