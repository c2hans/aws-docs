---
source_url: https://docs.aws.amazon.com/amazonq/latest/api-reference/API_Application.html
---

# Application
<a name="API_Application"></a>

Summary information for an Amazon Q Business application.

## Contents
<a name="API_Application_Contents"></a>

 ** applicationId **   <a name="qbusiness-Type-Application-applicationId"></a>
The identifier for the Amazon Q Business application.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9-]{35}`
Required: No

 ** createdAt **   <a name="qbusiness-Type-Application-createdAt"></a>
The Unix timestamp when the Amazon Q Business application was created.
Type: Timestamp
Required: No

 ** displayName **   <a name="qbusiness-Type-Application-displayName"></a>
The name of the Amazon Q Business application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: No

 ** identityType **   <a name="qbusiness-Type-Application-identityType"></a>
The authentication type being used by a Amazon Q Business application.
Type: String
Valid Values: `AWS_IAM_IDP_SAML | AWS_IAM_IDP_OIDC | AWS_IAM_IDC | AWS_QUICKSIGHT_IDP | ANONYMOUS`
Required: No

 ** quickSightConfiguration **   <a name="qbusiness-Type-Application-quickSightConfiguration"></a>
The Amazon Quick configuration for an Amazon Q Business application that uses Quick as the identity provider.
Type: [QuickSightConfiguration](API_QuickSightConfiguration.md) object
Required: No

 ** status **   <a name="qbusiness-Type-Application-status"></a>
The status of the Amazon Q Business application. The application is ready to use when the status is `ACTIVE`.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | FAILED | UPDATING`
Required: No

 ** updatedAt **   <a name="qbusiness-Type-Application-updatedAt"></a>
The Unix timestamp when the Amazon Q Business application was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_Application_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qbusiness-2023-11-27/Application)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qbusiness-2023-11-27/Application)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qbusiness-2023-11-27/Application)
