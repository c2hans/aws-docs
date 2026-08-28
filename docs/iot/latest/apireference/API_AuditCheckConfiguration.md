---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_AuditCheckConfiguration.html
---

# AuditCheckConfiguration
<a name="API_AuditCheckConfiguration"></a>

Which audit checks are enabled and disabled for this account.

## Contents
<a name="API_AuditCheckConfiguration_Contents"></a>

 ** configuration **   <a name="iot-Type-AuditCheckConfiguration-configuration"></a>
A structure containing the configName and corresponding configValue for configuring audit checks.
Type: String to string map
Valid Keys: `CERT_AGE_THRESHOLD_IN_DAYS | CERT_EXPIRATION_THRESHOLD_IN_DAYS`
Value Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** enabled **   <a name="iot-Type-AuditCheckConfiguration-enabled"></a>
True if this audit check is enabled for this account.
Type: Boolean
Required: No

## See Also
<a name="API_AuditCheckConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/AuditCheckConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/AuditCheckConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/AuditCheckConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
