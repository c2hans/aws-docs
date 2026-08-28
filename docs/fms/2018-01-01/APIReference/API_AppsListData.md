---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_AppsListData.html
---

# AppsListData
<a name="API_AppsListData"></a>

An AWS Firewall Manager applications list.

## Contents
<a name="API_AppsListData_Contents"></a>

 ** AppsList **   <a name="fms-Type-AppsListData-AppsList"></a>
An array of applications in the AWS Firewall Manager applications list.
Type: Array of [App](API_App.md) objects
Required: Yes

 ** ListName **   <a name="fms-Type-AppsListData-ListName"></a>
The name of the AWS Firewall Manager applications list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: Yes

 ** CreateTime **   <a name="fms-Type-AppsListData-CreateTime"></a>
The time that the AWS Firewall Manager applications list was created.
Type: Timestamp
Required: No

 ** LastUpdateTime **   <a name="fms-Type-AppsListData-LastUpdateTime"></a>
The time that the AWS Firewall Manager applications list was last updated.
Type: Timestamp
Required: No

 ** ListId **   <a name="fms-Type-AppsListData-ListId"></a>
The ID of the AWS Firewall Manager applications list.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-z0-9A-Z-]{36}$`
Required: No

 ** ListUpdateToken **   <a name="fms-Type-AppsListData-ListUpdateToken"></a>
A unique identifier for each update to the list. When you update the list, the update token must match the token of the current version of the application list. You can retrieve the update token by getting the list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** PreviousAppsList **   <a name="fms-Type-AppsListData-PreviousAppsList"></a>
A map of previous version numbers to their corresponding `App` object arrays.
Type: String to array of [App](API_App.md) objects map
Key Length Constraints: Minimum length of 1. Maximum length of 2.
Key Pattern: `^\d{1,2}$`
Required: No

## See Also
<a name="API_AppsListData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/AppsListData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/AppsListData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/AppsListData)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for 1.0. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query fms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
