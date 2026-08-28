---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_CustomLogSourceResource.html
---

# CustomLogSourceResource
<a name="API_CustomLogSourceResource"></a>

Amazon Security Lake can collect logs and events from third-party custom sources.

## Contents
<a name="API_CustomLogSourceResource_Contents"></a>

 ** attributes **   <a name="securitylake-Type-CustomLogSourceResource-attributes"></a>
The attributes of a third-party custom source.
Type: [CustomLogSourceAttributes](API_CustomLogSourceAttributes.md) object
Required: No

 ** provider **   <a name="securitylake-Type-CustomLogSourceResource-provider"></a>
The details of the log provider for a third-party custom source.
Type: [CustomLogSourceProvider](API_CustomLogSourceProvider.md) object
Required: No

 ** sourceName **   <a name="securitylake-Type-CustomLogSourceResource-sourceName"></a>
The name for a third-party custom source. This must be a Regionally unique value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w\-\_\:\.]*`
Required: No

 ** sourceVersion **   <a name="securitylake-Type-CustomLogSourceResource-sourceVersion"></a>
The version for a third-party custom source. This must be a Regionally unique value.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `[A-Za-z0-9\-\.\_]*`
Required: No

## See Also
<a name="API_CustomLogSourceResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/CustomLogSourceResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/CustomLogSourceResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/CustomLogSourceResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Security Lake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query security-lake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
