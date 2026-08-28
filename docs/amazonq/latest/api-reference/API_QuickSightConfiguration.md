---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_QuickSightConfiguration.html
---

# QuickSightConfiguration
<a name="API_QuickSightConfiguration"></a>

The Amazon Quick configuration for an Amazon Q Business application that uses Quick as the identity provider. For more information, see [Creating an Amazon Quick integrated application](https://docs.aws.amazon.com/amazonq/latest/qbusiness-ug/create-quicksight-integrated-application.html).

## Contents
<a name="API_QuickSightConfiguration_Contents"></a>

 ** clientNamespace **   <a name="qbusiness-Type-QuickSightConfiguration-clientNamespace"></a>
The Amazon Quick namespace that is used as the identity provider. For more information about Quick namespaces, see [Namespace operations](https://docs.aws.amazon.com/quicksight/latest/developerguide/namespace-operations.html).
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9._-]*`
Required: Yes

## See Also
<a name="API_QuickSightConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/QuickSightConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/QuickSightConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/QuickSightConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Q Business. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query amazonq` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
