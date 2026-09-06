---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/apireference/getting-started.html
---

# Getting Started with MediaConvert Using the API
<a name="getting-started"></a>

This section shows you how to get started with the MediaConvert API to transcode media files using API calls.

**To get set up to use the AWS Elemental MediaConvert API**

1. Set up permissions:
   + **Permissions that the AWS Elemental MediaConvert service can assume on your behalf.** These allow access to your Amazon S3 buckets and to Amazon API Gateway. For instructions, see [Set Up IAM Permissions](https://docs.aws.amazon.com/mediaconvert/latest/ug/iam-role.html) in the *AWS Elemental MediaConvert User Guide*.
   + **Your [Signature Version 4](https://docs.aws.amazon.com/general/latest/gr/signature-version-4.html) authentication for the requests that you send to AWS.** When you use the AWS Command Line Interface (AWS CLI) or one of the AWS SDKs, these tools automatically sign the requests for you with the access key and secret key that you specify in your client configuration.

1. Set up S3 file locations.

   The service reads your input files from and saves your output files to Amazon S3 buckets. For instructions on creating these buckets, see [Create Storage for Files](https://docs.aws.amazon.com/mediaconvert/latest/ug/set-up-file-locations.html) in the *AWS Elemental MediaConvert User Guide*.

1.

**Send your transcoding requests.**

   Send your requests to manage transcoding jobs, queues, job templates, and presets. For more information, see the following:
   + For information about setting up your transcoding job, see the [Creating Your Job Specification](creating-your-json-job-specification.md) topic of this guide.
   + For general information about how the MediaConvert resources (jobs, queues, job templates, and output presets) work, see the [AWS Elemental MediaConvert User Guide](https://docs.aws.amazon.com/mediaconvert/latest/ug/what-is.html).
   + For information about interacting programmatically with each resource type, see the [Resources](https://docs.aws.amazon.com/mediaconvert/latest/apireference/resources.html) topic of this guide.
   + For detailed information about each transcoding setting, see the [Properties](https://docs.aws.amazon.com/mediaconvert/latest/apireference/jobs.html#jobs-properties) topic of the Jobs resource chapter of this guide. You might find it easiest to navigate to a particular setting in the Properties topic by following the links in the [Schemas](https://docs.aws.amazon.com/mediaconvert/latest/apireference/jobs.html#jobs-schemas) section.
   + To prevent duplicate jobs from being created, use client request tokens. For more information see [Preventing duplicate jobs](idempotency.md).
