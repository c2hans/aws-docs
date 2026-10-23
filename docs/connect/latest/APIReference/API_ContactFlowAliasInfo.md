---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ContactFlowAliasInfo.html
---

# ContactFlowAliasInfo
<a name="API_ContactFlowAliasInfo"></a>

Contains information about a flow alias.

## Contents
<a name="API_ContactFlowAliasInfo_Contents"></a>

 ** AliasId **   <a name="connect-Type-ContactFlowAliasInfo-AliasId"></a>
The identifier of the alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** ContactFlowArn **   <a name="connect-Type-ContactFlowAliasInfo-ContactFlowArn"></a>
The Amazon Resource Name (ARN) of the flow.
Type: String
Required: No

 ** ContactFlowId **   <a name="connect-Type-ContactFlowAliasInfo-ContactFlowId"></a>
The identifier of the flow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** Description **   <a name="connect-Type-ContactFlowAliasInfo-Description"></a>
The description of the alias.
Type: String
Required: No

 ** LastModifiedRegion **   <a name="connect-Type-ContactFlowAliasInfo-LastModifiedRegion"></a>
The AWS Region where this resource was last modified.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-ContactFlowAliasInfo-LastModifiedTime"></a>
The timestamp when this resource was last modified.
Type: Timestamp
Required: No

 ** Name **   <a name="connect-Type-ContactFlowAliasInfo-Name"></a>
The name of the alias.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** Version **   <a name="connect-Type-ContactFlowAliasInfo-Version"></a>
The version of the flow.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_ContactFlowAliasInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ContactFlowAliasInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ContactFlowAliasInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ContactFlowAliasInfo)
