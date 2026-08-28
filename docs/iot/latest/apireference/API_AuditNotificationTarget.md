---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_AuditNotificationTarget.html
---

# AuditNotificationTarget
<a name="API_AuditNotificationTarget"></a>

Information about the targets to which audit notifications are sent.

## Contents
<a name="API_AuditNotificationTarget_Contents"></a>

 ** enabled **   <a name="iot-Type-AuditNotificationTarget-enabled"></a>
True if notifications to the target are enabled.
Type: Boolean
Required: No

 ** roleArn **   <a name="iot-Type-AuditNotificationTarget-roleArn"></a>
The ARN of the role that grants permission to send notifications to the target.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** targetArn **   <a name="iot-Type-AuditNotificationTarget-targetArn"></a>
The ARN of the target (SNS topic) to which audit notifications are sent.
Type: String
Length Constraints: Maximum length of 2048.
Required: No

## See Also
<a name="API_AuditNotificationTarget_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/AuditNotificationTarget)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/AuditNotificationTarget)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/AuditNotificationTarget)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
