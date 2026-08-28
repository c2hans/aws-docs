---
source_url: https://docs.aws.amazon.com/elemental-server/latest/ug/specifying-the-motion-overlay-location.html
---

This is version 2.18 of the AWS Elemental Server documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Conductor File and AWS Elemental Server Documentation](https://docs.aws.amazon.com/elemental-server/).

# Specifying the Motion Overlay File Location
<a name="specifying-the-motion-overlay-location"></a>

Specify one of the following valid locations for your overlay file:
+ Local to the AWS Elemental Server system.

  For example: `/data/assets/overlay_001.png`
+ A remote server via a mount point.

  For example: `/data/mnt/assets/overlay_001.png`
+ **AWS Elemental Server version 2.10 and later** An Amazon S3 bucket, using SSL.

   For example: `s3ssl://company.test/sample_bucket/overlay_001.png`
+ **AWS Elemental Server version 2.10 and later** An Amazon S3 bucket, without SSL.

   For example: `s3://company.test/sample_bucket/overlay_001.png`

For Amazon S3, use sse=true to enable S3 Server Side Encryption (SSE) and rrs=true to enable Reduced Redundancy Storage (RRS). Default values for RRS and SSE are false.

**Note**
If your motion overlay is a series of `.png` images, the way you specify it depends on the version of AWS Elemental Server you're running. In version 2.10 and later, include the full filename of the first image, as in the examples in the previous list. In version 2.9 and earlier, include the part of the filename that is common to all the images. For example, `/data/assets/overlay_`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Server. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-server` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
