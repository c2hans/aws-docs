---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_NodeFromTemplateJob.html
---

# NodeFromTemplateJob
<a name="API_NodeFromTemplateJob"></a>

A job to create a camera stream node.

## Contents
<a name="API_NodeFromTemplateJob_Contents"></a>

 ** CreatedTime **   <a name="panorama-Type-NodeFromTemplateJob-CreatedTime"></a>
When the job was created.
Type: Timestamp
Required: No

 ** JobId **   <a name="panorama-Type-NodeFromTemplateJob-JobId"></a>
The job's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: No

 ** NodeName **   <a name="panorama-Type-NodeFromTemplateJob-NodeName"></a>
The node's name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: No

 ** Status **   <a name="panorama-Type-NodeFromTemplateJob-Status"></a>
The job's status.
Type: String
Valid Values: `PENDING | SUCCEEDED | FAILED`
Required: No

 ** StatusMessage **   <a name="panorama-Type-NodeFromTemplateJob-StatusMessage"></a>
The job's status message.
Type: String
Required: No

 ** TemplateType **   <a name="panorama-Type-NodeFromTemplateJob-TemplateType"></a>
The job's template type.
Type: String
Valid Values: `RTSP_CAMERA_STREAM`
Required: No

## See Also
<a name="API_NodeFromTemplateJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/NodeFromTemplateJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/NodeFromTemplateJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/NodeFromTemplateJob)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Panorama. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query panorama` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
