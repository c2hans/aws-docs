---
source_url: https://docs.aws.amazon.com/location/latest/developerguide/error-handling.html
---

# Error handling
<a name="error-handling"></a>

Jobs handle errors at both the job level and individual record level. Job-level errors prevent the entire job from completing and are reported through the job status. These include authentication failures, permission issues, and service errors.

Record-level errors affect individual records and are included in the output file with `ErrorType` and `ErrorMessage` fields, allowing you to identify and address problematic records while still processing valid ones. Common record-level errors include invalid input values or missing required fields.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
