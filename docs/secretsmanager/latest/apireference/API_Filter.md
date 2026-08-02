---
source_url: https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_Filter.html
---

# Filter
<a name="API_Filter"></a>

Allows you to add filters when you use the search function in Secrets Manager. For more information, see [Find secrets in Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/manage_search-secret.html).

## Contents
<a name="API_Filter_Contents"></a>

 ** Key **   <a name="SecretsManager-Type-Filter-Key"></a>
The following are keys you can use:
+  **description**: Prefix match, not case-sensitive.
+  **name**: Prefix match, case-sensitive.
+  **tag-key**: Prefix match, case-sensitive.
+  **tag-value**: Prefix match, case-sensitive.
+  **primary-region**: Prefix match, case-sensitive.
+  **owning-service**: Prefix match, case-sensitive.
+  **all**: Breaks the filter value string into words and then searches all attributes for matches. Not case-sensitive.
Type: String
Valid Values: `description | name | tag-key | tag-value | primary-region | owning-service | all`
Required: No

 ** Values **   <a name="SecretsManager-Type-Filter-Values"></a>
The keyword to filter for.
You can prefix your search value with an exclamation mark (`!`) in order to perform negation filters.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Maximum length of 512.
Pattern: `^\!?[a-zA-Z0-9 :_@\/\+\=\.\-\!]*$`
Required: No

## See Also
<a name="API_Filter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/secretsmanager-2017-10-17/Filter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/secretsmanager-2017-10-17/Filter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/secretsmanager-2017-10-17/Filter)
