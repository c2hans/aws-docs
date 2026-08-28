---
source_url: https://docs.aws.amazon.com/m2/latest/userguide/ba-runtime-error-codes-f.html
---

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

# AWS Transform for mainframe Runtime Error codes related to Files
<a name="ba-runtime-error-codes-f"></a>

Files error codes, prefixed with `BA-F`. These errors are related to files operations including ESDS and GDG (Generation Data Groups).

## GDG (Generation Data Groups)
<a name="gdg-errors"></a>

| Key | Severity | Text | Additional details |
| --- | --- | --- | --- |
| BA-F2000 | Error | Failed to process GDG deletion event. Verify the GDG file path is valid and the event queue is properly configured. |  |
| BA-F2001 | Warn | Cannot extract filename from path. Verify the GDG file path format is correct. |  |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Mainframe Modernization. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query m2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
