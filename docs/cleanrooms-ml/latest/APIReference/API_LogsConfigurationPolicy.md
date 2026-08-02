---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_LogsConfigurationPolicy.html
---

# LogsConfigurationPolicy
<a name="API_LogsConfigurationPolicy"></a>

Provides the information necessary for a user to access the logs.

## Contents
<a name="API_LogsConfigurationPolicy_Contents"></a>

 ** allowedAccountIds **   <a name="API-Type-LogsConfigurationPolicy-allowedAccountIds"></a>
A list of account IDs that are allowed to access the logs.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 5 items.
Required: Yes

 ** filterPattern **   <a name="API-Type-LogsConfigurationPolicy-filterPattern"></a>
A regular expression pattern that is used to parse the logs and return information that matches the pattern.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** logRedactionConfiguration **   <a name="API-Type-LogsConfigurationPolicy-logRedactionConfiguration"></a>
Specifies the log redaction configuration for this policy.
Type: [LogRedactionConfiguration](API_LogRedactionConfiguration.md) object
Required: No

 ** logType **   <a name="API-Type-LogsConfigurationPolicy-logType"></a>
Specifies the type of log this policy applies to. The currently supported policies are ALL or ERROR\_SUMMARY.
Type: String
Valid Values: `ALL | ERROR_SUMMARY`
Required: No

## See Also
<a name="API_LogsConfigurationPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/LogsConfigurationPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/LogsConfigurationPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/LogsConfigurationPolicy)
