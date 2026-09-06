---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_ServiceAccountCredentials.html
---

# ServiceAccountCredentials
<a name="API_ServiceAccountCredentials"></a>

Describes the credentials for the service account used by the fleet or image builder to connect to the directory.

## Contents
<a name="API_ServiceAccountCredentials_Contents"></a>

 ** AccountName **   <a name="WorkSpacesApplications-Type-ServiceAccountCredentials-AccountName"></a>
The user name of the account. This account must have the following privileges: create computer objects, join computers to the domain, and change/reset the password on descendant computer objects for the organizational units specified.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** AccountPassword **   <a name="WorkSpacesApplications-Type-ServiceAccountCredentials-AccountPassword"></a>
The password for the account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 127.
Required: Yes

## See Also
<a name="API_ServiceAccountCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/ServiceAccountCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/ServiceAccountCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/ServiceAccountCredentials)
