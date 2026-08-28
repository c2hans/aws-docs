---
source_url: https://docs.aws.amazon.com/mediaconvert/latest/ug/setting-up-a-dolby-vision-job.html
---

# Configuring Dolby Vision
<a name="setting-up-a-dolby-vision-job"></a>

Use the following steps to set up a Dolby Vision job. For more information about jobs, see [Tutorial: Configuring job settings](setting-up-a-job.md).

1. For your input file or files, choose from the following:
   + MXF file, with frame-interleaved Dolby Vision metadata or an XML file.
   + IMF package (IMP) with frame-interleaved Dolby Vision metadata or an XML file. Also, specify a composition playlist (CPL) file for your input. If your CPL is from an incomplete IMP, choose **Supplemental IMPs** to specify the location of your supplemental IMPs.
   + Apple ProRes QuickTime MOV, with a Dolby Vision studio metadata XML file.
   + Any input with an HDR10 color space.
   + Any input with an SDR color space.

1. For each output that you want to process with Dolby Vision, do the following:

   1. Make sure that your output settings conform to the limitations listed in [Requirements](dolby-vision-job-limitations-and-requirements.md).

   1. Enable the **Dolby Vision** preprocessor.

   1. Specify a Dolby Vision **Profile** from one of the following choices:
      + **Profile 5**: Includes frame-interleaved Dolby Vision metadata in your output.
      + **Profile 8.1**: Includes both frame-interleaved Dolby Vision metadata and HDR10 metadata in your output.

1. Choose an on-demand queue. (Your default queue is on-demand.)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for MediaConvert. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconvert` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
