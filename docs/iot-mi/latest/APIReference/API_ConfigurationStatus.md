---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_ConfigurationStatus.html
---

# ConfigurationStatus
<a name="API_ConfigurationStatus"></a>

Provides the status of the default encryption configuration for an AWS account.

## Contents
<a name="API_ConfigurationStatus_Contents"></a>

 ** state **   <a name="managedintegrations-Type-ConfigurationStatus-state"></a>
The status state describing the default encryption configuration update.
Type: String
Valid Values: `ENABLED | UPDATE_IN_PROGRESS | UPDATE_FAILED`
Required: Yes

 ** error **   <a name="managedintegrations-Type-ConfigurationStatus-error"></a>
The error details describing a failed default encryption configuration update.
Type: [ConfigurationError](API_ConfigurationError.md) object
Required: No

## See Also
<a name="API_ConfigurationStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/ConfigurationStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/ConfigurationStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/ConfigurationStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
