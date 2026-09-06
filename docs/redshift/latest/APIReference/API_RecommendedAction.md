---
source_url: https://docs.aws.amazon.com/redshift/latest/APIReference/API_RecommendedAction.html
---

# RecommendedAction
<a name="API_RecommendedAction"></a>

The recommended action from the Amazon Redshift Advisor recommendation.

## Contents
<a name="API_RecommendedAction_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Command **
The command to run.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** Database **
The database name to perform the action on. Only applicable if the type of command is SQL.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** Text **
The specific instruction about the command.
Type: String
Length Constraints: Maximum length of 2147483647.
Required: No

 ** Type **
The type of command.
Type: String
Valid Values: `SQL | CLI`
Required: No

## See Also
<a name="API_RecommendedAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-2012-12-01/RecommendedAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-2012-12-01/RecommendedAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-2012-12-01/RecommendedAction)
