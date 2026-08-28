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

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
