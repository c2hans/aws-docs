---
source_url: https://docs.aws.amazon.com/rekognition/latest/dg/bulk-analysis-output-manifests.html
---

# Bulk analysis output manifests
<a name="bulk-analysis-output-manifests"></a>

**Note**
Streaming Video and Bulk Image Analysis is no longer available to new customers. For more information, see [Amazon Rekognition feature availability changes](rekognition-availability-changes.md).
**This change does not impact the availability of other Amazon Rekognition features.**

The bulk analysis job generates an output manifest file that contains the job results, as well as a manifest summary which contains statistics and details on any errors when processing the input manifest entries.

If duplicated entries were included in the input manifest, the job won’t attempt to filter out unique inputs, and will instead process all provided entries.

The output manifest file is formatted as follows:

```
// Output manifest for content moderation
{"source-ref":"s3://foo/bar/1.jpg", "detect-moderation-labels": {"ModerationLabels":[],"ModerationModelVersion":"7.0","ContentTypes":[{"Confidence":72.7257,"Name":"Animated"}]}}
```

The output manifest summary is formatted as follows:

```
{
    "version": "1.0",                # Schema version, 1.0 for GA.
    "statistics": {
        "total-json-lines": Number,  # Total number json lines (images) in the input manifest.
        "valid-json-lines": Number,  # Total number of JSON Lines (images) that contain references to valid images.
        "invalid-json-lines": Number # Total number of invalid JSON Lines. These lines were not handled.
    },
    "errors": [
        {
            "line-numer": Number,   # The number of the line in the manifest where the error occured.
            "source-ref": "String", # Optional. Name of the file if was parsed.
            "code": "String",       # Error code.
            "message": "String"     # Description of the error.
        }
     ]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Rekognition. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query rekognition` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
