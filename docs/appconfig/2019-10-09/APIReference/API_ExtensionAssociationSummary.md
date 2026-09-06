---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_ExtensionAssociationSummary.html
---

# ExtensionAssociationSummary
<a name="API_ExtensionAssociationSummary"></a>

Information about an association between an extension and an AWS AppConfig resource such as an application, environment, or configuration profile. Call `GetExtensionAssociation` to get more information about an association.

## Contents
<a name="API_ExtensionAssociationSummary_Contents"></a>

 ** ExtensionArn **   <a name="appconfig-Type-ExtensionAssociationSummary-ExtensionArn"></a>
The system-generated Amazon Resource Name (ARN) for the extension.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:[a-z]+:((eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1})?:(\d{12})?:[a-zA-Z0-9-_/:.]+`
Required: No

 ** Id **   <a name="appconfig-Type-ExtensionAssociationSummary-Id"></a>
The extension association ID. This ID is used to call other `ExtensionAssociation` API actions such as `GetExtensionAssociation` or `DeleteExtensionAssociation`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** ResourceArn **   <a name="appconfig-Type-ExtensionAssociationSummary-ResourceArn"></a>
The ARNs of applications, configuration profiles, or environments defined in the association.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:[a-z]+:((eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1})?:(\d{12})?:[a-zA-Z0-9-_/:.]+`
Required: No

## See Also
<a name="API_ExtensionAssociationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/ExtensionAssociationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/ExtensionAssociationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/ExtensionAssociationSummary)
