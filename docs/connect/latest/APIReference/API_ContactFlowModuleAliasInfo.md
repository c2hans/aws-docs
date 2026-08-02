---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ContactFlowModuleAliasInfo.html
---

# ContactFlowModuleAliasInfo
<a name="API_ContactFlowModuleAliasInfo"></a>

Contains information about an alias.

## Contents
<a name="API_ContactFlowModuleAliasInfo_Contents"></a>

 ** AliasId **   <a name="connect-Type-ContactFlowModuleAliasInfo-AliasId"></a>
The identifier of the alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([$0-9a-zA-Z][_-]?)+$`
Required: No

 ** ContactFlowModuleArn **   <a name="connect-Type-ContactFlowModuleAliasInfo-ContactFlowModuleArn"></a>
The Amazon Resource Name (ARN) of the flow module.
Type: String
Required: No

 ** ContactFlowModuleId **   <a name="connect-Type-ContactFlowModuleAliasInfo-ContactFlowModuleId"></a>
The identifier of the flow module.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: No

 ** Description **   <a name="connect-Type-ContactFlowModuleAliasInfo-Description"></a>
The description of the alias.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `.*\S.*`
Required: No

 ** LastModifiedRegion **   <a name="connect-Type-ContactFlowModuleAliasInfo-LastModifiedRegion"></a>
The Amazon Web Services Region where this resource was last modified.
Type: String
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`
Required: No

 ** LastModifiedTime **   <a name="connect-Type-ContactFlowModuleAliasInfo-LastModifiedTime"></a>
The timestamp when this resource was last modified.
Type: Timestamp
Required: No

 ** Name **   <a name="connect-Type-ContactFlowModuleAliasInfo-Name"></a>
The name of the alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([$0-9a-zA-Z][_-]?)+$`
Required: No

 ** Version **   <a name="connect-Type-ContactFlowModuleAliasInfo-Version"></a>
The version of the flow module.
Type: Long
Valid Range: Minimum value of 1.
Required: No

## See Also
<a name="API_ContactFlowModuleAliasInfo_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ContactFlowModuleAliasInfo)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ContactFlowModuleAliasInfo)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ContactFlowModuleAliasInfo)
