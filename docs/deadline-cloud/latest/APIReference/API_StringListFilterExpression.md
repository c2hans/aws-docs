---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/APIReference/API_StringListFilterExpression.html
---

# StringListFilterExpression
<a name="API_StringListFilterExpression"></a>

Searches for a particular list of strings.

## Contents
<a name="API_StringListFilterExpression_Contents"></a>

 ** name **   <a name="deadlinecloud-Type-StringListFilterExpression-name"></a>
The field name to search.
Type: String
Required: Yes

 ** operator **   <a name="deadlinecloud-Type-StringListFilterExpression-operator"></a>
The type of comparison to use for this search.
Type: String
Valid Values: `EQUAL | NOT_EQUAL | GREATER_THAN_EQUAL_TO | GREATER_THAN | LESS_THAN_EQUAL_TO | LESS_THAN | ANY_EQUALS | ALL_NOT_EQUALS`
Required: Yes

 ** values **   <a name="deadlinecloud-Type-StringListFilterExpression-values"></a>
The list of string values to search for.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 16 items.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

## See Also
<a name="API_StringListFilterExpression_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/deadline-2023-10-12/StringListFilterExpression)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/deadline-2023-10-12/StringListFilterExpression)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/deadline-2023-10-12/StringListFilterExpression)
