---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_ControlError.html
---

# ControlError
<a name="API_ControlError"></a>

An error reported during the evaluation of a single control.

## Contents
<a name="API_ControlError_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Code **   <a name="AWSMarketplaceService-Type-ControlError-Code"></a>
The error code that identifies the type of error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[A-Z_]+$`
Required: No

 ** Message **   <a name="AWSMarketplaceService-Type-ControlError-Message"></a>
The message for the error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** Scope **   <a name="AWSMarketplaceService-Type-ControlError-Scope"></a>
The list of name-value pairs that identify the resource or attribute that the error applies to.
Type: Array of [ErrorScope](API_ErrorScope.md) objects
Required: No

## See Also
<a name="API_ControlError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/ControlError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/ControlError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/ControlError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
