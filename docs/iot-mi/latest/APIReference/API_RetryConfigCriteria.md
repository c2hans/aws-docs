---
source_url: https://docs.aws.amazon.com/iot-mi/latest/APIReference/API_RetryConfigCriteria.html
---

# RetryConfigCriteria
<a name="API_RetryConfigCriteria"></a>

Structure representing one retry config criteria.

## Contents
<a name="API_RetryConfigCriteria_Contents"></a>

 ** FailureType **   <a name="managedintegrations-Type-RetryConfigCriteria-FailureType"></a>
Over-the-air (OTA) retry criteria failure type.
Type: String
Valid Values: `FAILED | TIMED_OUT | ALL`
Required: No

 ** MinNumberOfRetries **   <a name="managedintegrations-Type-RetryConfigCriteria-MinNumberOfRetries"></a>
The number of retries allowed for a failure type for the over-the-air (OTA) task.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 10.
Required: No

## See Also
<a name="API_RetryConfigCriteria_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-managed-integrations-2025-03-03/RetryConfigCriteria)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-managed-integrations-2025-03-03/RetryConfigCriteria)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-managed-integrations-2025-03-03/RetryConfigCriteria)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
