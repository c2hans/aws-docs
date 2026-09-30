---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/apireference/creating-your-json-job-specification.html
---

# Creating Your AWS Elemental MediaConvert Job Specification
<a name="creating-your-json-job-specification"></a>

When you submit your MediaConvert jobs programmatically, you submit a payload with your job settings. When you use the SDK for Python (Boto) or the AWS CLI, you pass in your job settings directly as a JSON object. When you use the other AWS SDKs, translate the JSON job settings according to the SDK documentation.

This job specification must conform to validation by the transcoding engine. This validation is more complex than the schema exposed in this API reference. The transcoding engine validations represent complex dependencies among groups of settings and dependencies between your transcoding settings and properties of your input files. The MediaConvert console functions as a tool to build valid job settings specifications in JSON.

For examples of valid job settings specifications in JSON, see [Sample Job Settings Specifications in JSON](sample-json.md).

**Tip**
We recommend that you *don't* construct your production job settings specifications by starting from one of the samples in this chapter and then adding settings. This approach usually results in a series of validation errors that can be frustrating to resolve. Instead, use the MediaConvert console to set up and run your initial job. Export the JSON job object to use to programmatically submit future jobs.

**To construct your job specification using the MediaConvert console**

1. Open the MediaConvert console at [https://console.aws.amazon.com/mediaconvert/](https://console.aws.amazon.com/mediaconvert/).

1. Set up your job in the console. For more information, see [Setting Up a Job](https://docs.aws.amazon.com/mediaconvert/latest/ug/setting-up-a-job.html) in the *AWS Elemental MediaConvert User Guide*.

   Consider whether a MediaConvert system job template or output preset suits your workflow. For more information, see [Working with Job Templates](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-job-templates.html) and [Working with Output Presets](https://docs.aws.amazon.com/mediaconvert/latest/ug/working-with-presets.html) in the *AWS Elemental MediaConvert User Guide*.

1. On the **Create job** page, in the **Job** pane on the left, under **Job settings**, choose **Show job JSON**.

1. If you are using the SDK for Python (Boto) or the AWS CLI, copy the JSON object and save it as a file to submit with your `CreateJob` request.

   If you are using one of the other AWS SDKs, translate the JSON job settings according to the SDK documentation.
