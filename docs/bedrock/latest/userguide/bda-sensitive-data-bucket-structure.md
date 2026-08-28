---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/bda-sensitive-data-bucket-structure.html
---

# Sensitive data detection and redaction output bucket structure
<a name="bda-sensitive-data-bucket-structure"></a>

When you set the detection mode to DETECTION\_AND\_REDACTION, BDA creates a `redacted/` directory for redacted output files, as shown in the following example.

```
s3-bucket/
    ├── job-id/
       ├── job_metadata.json
       └── 0/
           └── standard_output/
               └── 0/
                   └── redacted/ # directory for redacted standard output
                              └── result.json
                   └── result.json # unredacted file with detected sensitive data
           └── custom_output/
               └── 0/
                   └── redacted/ # directory for redacted custom output
                              └── result.json
                   └── result.json # unredacted file with detected sensitive data
```

With DETECTION mode enabled, BDA does not create the `redacted/` directory. Instead, BDA includes the detected sensitive data within the existing `result.json`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
