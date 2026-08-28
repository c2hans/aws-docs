---
source_url: https://docs.aws.amazon.com/elemental-live/latest/ug/step-a-prepare-the-overlay-asset.html
---

# Step A: Prepare the overlay asset
<a name="step-a-prepare-the-overlay-asset"></a>

1. Create a file with the following characteristics:
   + File type: A BMP, PNG, or TGA file.
   + Aspect ratio: The overlay can have any aspect ratio. It does not have to match the aspect ratio of the underlying video.
   + Size, in pixels: The overlay can be any size up to the same size as the underlying video. The overlay cannot be positioned so that part of the overlay runs beyond the right edge or bottom edge of the underlying video.
     + If you set up an overlay so that it is too big or it overruns an edge, if Elemental Live can identify this error at event creation time, an error message will appear then.
     + If Elemental Live cannot identify the error in advance, an error message will appear while the event is running. The event will not stop but the insertion request will fail.

1. Place the prepared file in a location accessible to the Elemental Live node. You can specify the location in one of the following ways:
   + Local to the Elemental Live appliance. E.g. `/data/assets/overlay.mov`
   + A remote server via a mount point. E.g. `/data/mnt/assets/overlay.mov`
   + An S3 bucket, using SSL. E.g. `s3ssl://company.test/sample_bucket/overlay.mov`
   + An S3 bucket, without SSL. E.g. `s3://company.test/sample_bucket/overlay.mov`

   Use sse=true to enable S3 Server Side Encryption (SSE) and rrs=true to enable Reduced Redundancy Storage (RRS). Default values for RRS and SSE are false.

   Example: `s3://<hostname>/sample_bucket/ encrypted?rrs=true&sse=true`

1. Make a note of the location.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Live. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-live` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
