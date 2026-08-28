---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_JobTemplateSummary.html
---

# JobTemplateSummary
<a name="API_JobTemplateSummary"></a>

An object that contains information about the job template.

## Contents
<a name="API_JobTemplateSummary_Contents"></a>

 ** createdAt **   <a name="iot-Type-JobTemplateSummary-createdAt"></a>
The time, in seconds since the epoch, when the job template was created.
Type: Timestamp
Required: No

 ** description **   <a name="iot-Type-JobTemplateSummary-description"></a>
A description of the job template.
Type: String
Length Constraints: Maximum length of 2028.
Pattern: `[^\p{C}]+`
Required: No

 ** jobTemplateArn **   <a name="iot-Type-JobTemplateSummary-jobTemplateArn"></a>
The ARN of the job template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:[!-~]+$`
Required: No

 ** jobTemplateId **   <a name="iot-Type-JobTemplateSummary-jobTemplateId"></a>
The unique identifier of the job template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: No

## See Also
<a name="API_JobTemplateSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/JobTemplateSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/JobTemplateSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/JobTemplateSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
