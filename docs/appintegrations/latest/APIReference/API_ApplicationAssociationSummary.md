---
source_url: https://docs.aws.amazon.com/appintegrations/latest/APIReference/API_ApplicationAssociationSummary.html
---

# ApplicationAssociationSummary
<a name="API_connect-app-integrations_ApplicationAssociationSummary"></a>

Summary information about the Application Association.

## Contents
<a name="API_connect-app-integrations_ApplicationAssociationSummary_Contents"></a>

 ** ApplicationArn **   <a name="connect-Type-connect-app-integrations_ApplicationAssociationSummary-ApplicationArn"></a>
The Amazon Resource Name (ARN) of the Application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: No

 ** ApplicationAssociationArn **   <a name="connect-Type-connect-app-integrations_ApplicationAssociationSummary-ApplicationAssociationArn"></a>
The Amazon Resource Name (ARN) of the Application Association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `^arn:aws:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: No

 ** ClientId **   <a name="connect-Type-connect-app-integrations_ApplicationAssociationSummary-ClientId"></a>
The identifier for the client that is associated with the Application Association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `.*`
Required: No

## See Also
<a name="API_connect-app-integrations_ApplicationAssociationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appintegrations-2020-07-29/ApplicationAssociationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appintegrations-2020-07-29/ApplicationAssociationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appintegrations-2020-07-29/ApplicationAssociationSummary)
