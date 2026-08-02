---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ContactFlowModule.html
---

# ContactFlowModule
<a name="API_ContactFlowModule"></a>

Contains information about a flow module.

## Contents
<a name="API_ContactFlowModule_Contents"></a>

 ** Arn **   <a name="connect-Type-ContactFlowModule-Arn"></a>
The Amazon Resource Name (ARN).
Type: String
Required: No

 ** Content **   <a name="connect-Type-ContactFlowModule-Content"></a>
The JSON string that represents the content of the flow. For an example, see [Example flow in Connect Customer Flow language](https://docs.aws.amazon.com/connect/latest/APIReference/flow-language-example.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256000.
Required: No

 ** Description **   <a name="connect-Type-ContactFlowModule-Description"></a>
The description of the flow module.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `.*\S.*`
Required: No

 ** ExternalInvocationConfiguration **   <a name="connect-Type-ContactFlowModule-ExternalInvocationConfiguration"></a>
The external invocation configuration for the flow module
Type: [ExternalInvocationConfiguration](API_ExternalInvocationConfiguration.md) object
Required: No

 ** FlowModuleContentSha256 **   <a name="connect-Type-ContactFlowModule-FlowModuleContentSha256"></a>
Hash of the module content for integrity verification.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9]{64}$`
Required: No

 ** Id **   <a name="connect-Type-ContactFlowModule-Id"></a>
The identifier of the flow module.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** Name **   <a name="connect-Type-ContactFlowModule-Name"></a>
The name of the flow module.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `.*\S.*`
Required: No

 ** Settings **   <a name="connect-Type-ContactFlowModule-Settings"></a>
The configuration settings for the flow module.
Type: String
Required: No

 ** State **   <a name="connect-Type-ContactFlowModule-State"></a>
The type of flow module.
Type: String
Valid Values: `ACTIVE | ARCHIVED`
Required: No

 ** Status **   <a name="connect-Type-ContactFlowModule-Status"></a>
The status of the flow module.
Type: String
Valid Values: `PUBLISHED | SAVED`
Required: No

 ** Tags **   <a name="connect-Type-ContactFlowModule-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** Version **   <a name="connect-Type-ContactFlowModule-Version"></a>
The version of the flow module.
Type: Long
Valid Range: Minimum value of 1.
Required: No

 ** VersionDescription **   <a name="connect-Type-ContactFlowModule-VersionDescription"></a>
Description of the version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_ContactFlowModule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ContactFlowModule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ContactFlowModule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ContactFlowModule)
