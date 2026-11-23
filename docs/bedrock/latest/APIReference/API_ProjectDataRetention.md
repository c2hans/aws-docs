---
source_url: https://docs.aws.amazon.com/bedrock/latest/APIReference/API_ProjectDataRetention.html
---

# ProjectDataRetention

A project's data-retention setting: the project-scope mode, which may be `inherit` to defer to the account scope or the model default. Uses the same mode space as the account-level data-retention operations; the effective mode for a request resolves project, then account, then model default.

## Contents
<a name="API_ProjectDataRetention_Contents"></a>

 ** mode **   <a name="bedrock-Type-ProjectDataRetention-mode"></a>
The project's data retention mode. Use `inherit` to defer to the account setting or model default.
Type: String
Valid Values: `default | none | aws_review | provider_data_share | inherit`
Required: Yes

## See Also
<a name="API_ProjectDataRetention_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bedrock-2023-04-20/ProjectDataRetention)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bedrock-2023-04-20/ProjectDataRetention)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bedrock-2023-04-20/ProjectDataRetention)
