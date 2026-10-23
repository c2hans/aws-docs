---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ContactFlowAliasSummary.html
---

# ContactFlowAliasSummary
<a name="API_ContactFlowAliasSummary"></a>

Contains summary information about a flow alias.

## Contents
<a name="API_ContactFlowAliasSummary_Contents"></a>

 ** AliasDescription **   <a name="connect-Type-ContactFlowAliasSummary-AliasDescription"></a>
The description of the alias.
Type: String
Required: No

 ** AliasId **   <a name="connect-Type-ContactFlowAliasSummary-AliasId"></a>
The identifier of the alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** AliasName **   <a name="connect-Type-ContactFlowAliasSummary-AliasName"></a>
The name of the alias.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** Arn **   <a name="connect-Type-ContactFlowAliasSummary-Arn"></a>
The Amazon Resource Name (ARN) of the flow alias.
Type: String
Required: No

 ** LastModifiedRegion **   <a name="connect-Type-ContactFlowAliasSummary-LastModifiedRegion"></a>
The AWS Region where this resource was last modified.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-ContactFlowAliasSummary-LastModifiedTime"></a>
The timestamp when this resource was last modified.
Type: Timestamp
Required: No

 ** Version **   <a name="connect-Type-ContactFlowAliasSummary-Version"></a>
The version of the flow.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_ContactFlowAliasSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ContactFlowAliasSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ContactFlowAliasSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ContactFlowAliasSummary)
