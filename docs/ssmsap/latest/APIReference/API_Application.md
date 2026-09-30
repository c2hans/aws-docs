---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_Application.html
---

# Application
<a name="API_Application"></a>

An SAP application registered with AWS Systems Manager for SAP.

## Contents
<a name="API_Application_Contents"></a>

 ** AppRegistryArn **   <a name="ssmsap-Type-Application-AppRegistryArn"></a>
The Amazon Resource Name (ARN) of the Application Registry. This member is deprecated; use applicationId or applicationArn instead.
Type: String
Pattern: `arn:aws:servicecatalog:[a-z0-9:\/-]+`
Required: No

 ** Arn **   <a name="ssmsap-Type-Application-Arn"></a>
The Amazon Resource Name (ARN) of the application.
Type: String
Pattern: `arn:(.+:){2,4}.+$|^arn:(.+:){1,3}.+\/.+`
Required: No

 ** AssociatedApplicationArns **   <a name="ssmsap-Type-Application-AssociatedApplicationArns"></a>
The Amazon Resource Names of the associated AWS Systems Manager for SAP applications.
Type: Array of strings
Pattern: `arn:(.+:){2,4}.+$|^arn:(.+:){1,3}.+\/.+`
Required: No

 ** Components **   <a name="ssmsap-Type-Application-Components"></a>
The components of the application.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[\w\d-]+`
Required: No

 ** DiscoveryStatus **   <a name="ssmsap-Type-Application-DiscoveryStatus"></a>
The latest discovery result for the application.
Type: String
Valid Values: `SUCCESS | REGISTRATION_FAILED | REFRESH_FAILED | REGISTERING | DELETING`
Required: No

 ** Id **   <a name="ssmsap-Type-Application-Id"></a>
The ID of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 60.
Pattern: `[\w\d\.-]+`
Required: No

 ** LastUpdated **   <a name="ssmsap-Type-Application-LastUpdated"></a>
The time at which the application was last updated.
Type: Timestamp
Required: No

 ** Status **   <a name="ssmsap-Type-Application-Status"></a>
The status of the application.
Type: String
Valid Values: `ACTIVATED | STARTING | STOPPED | STOPPING | FAILED | REGISTERING | DELETING | UNKNOWN`
Required: No

 ** StatusMessage **   <a name="ssmsap-Type-Application-StatusMessage"></a>
The status message.
Type: String
Required: No

 ** Type **   <a name="ssmsap-Type-Application-Type"></a>
The type of the application.
Type: String
Valid Values: `HANA | SAP_ABAP`
Required: No

## See Also
<a name="API_Application_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/Application)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/Application)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/Application)
