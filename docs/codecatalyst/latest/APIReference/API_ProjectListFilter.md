---
source_url: https://docs.aws.amazon.com/codecatalyst/latest/APIReference/API_ProjectListFilter.html
---

# ProjectListFilter
<a name="API_ProjectListFilter"></a>

nformation about the filter used to narrow the results returned in a list of projects.

## Contents
<a name="API_ProjectListFilter_Contents"></a>

 ** key **   <a name="codecatalyst-Type-ProjectListFilter-key"></a>
A key that can be used to sort results.
Type: String
Valid Values: `hasAccessTo | name`
Required: Yes

 ** values **   <a name="codecatalyst-Type-ProjectListFilter-values"></a>
The values of the key.
Type: Array of strings
Required: Yes

 ** comparisonOperator **   <a name="codecatalyst-Type-ProjectListFilter-comparisonOperator"></a>
The operator used to compare the fields.
Type: String
Valid Values: `EQ | GT | GE | LT | LE | BEGINS_WITH`
Required: No

## See Also
<a name="API_ProjectListFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codecatalyst-2022-09-28/ProjectListFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codecatalyst-2022-09-28/ProjectListFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codecatalyst-2022-09-28/ProjectListFilter)
