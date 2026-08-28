---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_ConnectivityPropertiesPatch.html
---

# ConnectivityPropertiesPatch
<a name="API_ConnectivityPropertiesPatch"></a>

Contains the connectivity settings to update on an existing connection. Include only the fields you want to change.

## Contents
<a name="API_ConnectivityPropertiesPatch_Contents"></a>

 ** authenticationConfiguration **   <a name="datazone-Type-ConnectivityPropertiesPatch-authenticationConfiguration"></a>
The authentication settings to update.
Type: [AuthenticationConfigurationPatch](API_AuthenticationConfigurationPatch.md) object
Required: No

 ** connectionProperties **   <a name="datazone-Type-ConnectivityPropertiesPatch-connectionProperties"></a>
The connection properties to update.
Type: String to string map
Value Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** description **   <a name="datazone-Type-ConnectivityPropertiesPatch-description"></a>
A description of the connectivity properties update.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2048.
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_ConnectivityPropertiesPatch_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/ConnectivityPropertiesPatch)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/ConnectivityPropertiesPatch)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/ConnectivityPropertiesPatch)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
