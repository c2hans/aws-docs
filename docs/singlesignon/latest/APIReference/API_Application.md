---
source_url: https://docs.aws.amazon.com/singlesignon/latest/APIReference/API_Application.html
---

# Application
<a name="API_Application"></a>

A structure that describes an application that uses IAM Identity Center for access management.

## Contents
<a name="API_Application_Contents"></a>

 ** ApplicationAccount **   <a name="singlesignon-Type-Application-ApplicationAccount"></a>
The AWS account ID number of the application.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `\d{12}`
Required: No

 ** ApplicationArn **   <a name="singlesignon-Type-Application-ApplicationArn"></a>
The ARN of the application.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso::\d{12}:application/(sso)?ins-[a-zA-Z0-9-.]{16}/apl-[a-zA-Z0-9]{16}`
Required: No

 ** ApplicationProviderArn **   <a name="singlesignon-Type-Application-ApplicationProviderArn"></a>
The ARN of the application provider for this application.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso::aws:applicationProvider/[a-zA-Z0-9-/]+`
Required: No

 ** CreatedDate **   <a name="singlesignon-Type-Application-CreatedDate"></a>
The date and time when the application was originally created.
Type: Timestamp
Required: No

 ** CreatedFrom **   <a name="singlesignon-Type-Application-CreatedFrom"></a>
The AWS Region where the application was created in IAM Identity Center.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `([a-z]+-){2,3}\d`
Required: No

 ** Description **   <a name="singlesignon-Type-Application-Description"></a>
The description of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** IdentityStoreArn **   <a name="singlesignon-Type-Application-IdentityStoreArn"></a>
The ARN of the identity store that is connected to the instance of IAM Identity Center.
Type: String
Required: No

 ** InstanceArn **   <a name="singlesignon-Type-Application-InstanceArn"></a>
The ARN of the instance of IAM Identity Center that is configured with this application.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1224.
Pattern: `arn:aws(-[a-z]{1,5}){0,3}:sso:::instance/(sso)?ins-[a-zA-Z0-9-.]{16}`
Required: No

 ** Name **   <a name="singlesignon-Type-Application-Name"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\S\s]*`
Required: No

 ** PortalOptions **   <a name="singlesignon-Type-Application-PortalOptions"></a>
A structure that describes the options for the access portal associated with this application.
Type: [PortalOptions](API_PortalOptions.md) object
Required: No

 ** Status **   <a name="singlesignon-Type-Application-Status"></a>
The current status of the application in this instance of IAM Identity Center.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_Application_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sso-admin-2020-07-20/Application)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sso-admin-2020-07-20/Application)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sso-admin-2020-07-20/Application)
