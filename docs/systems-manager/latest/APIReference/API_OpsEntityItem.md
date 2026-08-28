---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_OpsEntityItem.html
---

# OpsEntityItem
<a name="API_OpsEntityItem"></a>

The OpsData summary.

## Contents
<a name="API_OpsEntityItem_Contents"></a>

 ** CaptureTime **   <a name="systemsmanager-Type-OpsEntityItem-CaptureTime"></a>
The time the OpsData was captured.
Type: String
Pattern: `^(20)[0-9][0-9]-(0[1-9]|1[012])-([12][0-9]|3[01]|0[1-9])(T)(2[0-3]|[0-1][0-9])(:[0-5][0-9])(:[0-5][0-9])(Z)$`
Required: No

 ** Content **   <a name="systemsmanager-Type-OpsEntityItem-Content"></a>
The details of an OpsData summary.
Type: Array of string to string maps
Array Members: Minimum number of 0 items. Maximum number of 10000 items.
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 64.
Value Length Constraints: Minimum length of 0. Maximum length of 4096.
Required: No

## See Also
<a name="API_OpsEntityItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/OpsEntityItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/OpsEntityItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/OpsEntityItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
