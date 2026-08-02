---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_AppsListDataSummary.html
---

# AppsListDataSummary
<a name="API_AppsListDataSummary"></a>

Details of the AWS Firewall Manager applications list.

## Contents
<a name="API_AppsListDataSummary_Contents"></a>

 ** AppsList **   <a name="fms-Type-AppsListDataSummary-AppsList"></a>
An array of `App` objects in the AWS Firewall Manager applications list.
Type: Array of [App](API_App.md) objects
Required: No

 ** ListArn **   <a name="fms-Type-AppsListDataSummary-ListArn"></a>
The Amazon Resource Name (ARN) of the applications list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

 ** ListId **   <a name="fms-Type-AppsListDataSummary-ListId"></a>
The ID of the applications list.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^[a-z0-9A-Z-]{36}$`
Required: No

 ** ListName **   <a name="fms-Type-AppsListDataSummary-ListName"></a>
The name of the applications list.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`
Required: No

## See Also
<a name="API_AppsListDataSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/AppsListDataSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/AppsListDataSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/AppsListDataSummary)
