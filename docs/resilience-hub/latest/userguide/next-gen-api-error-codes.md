---
source_url: https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-api-error-codes.html
---

# Error codes
<a name="next-gen-api-error-codes"></a>

The following table lists error codes returned by the next generation of Resilience Hub API.

| Error code | HTTP status | Description |
| --- | --- | --- |
| ValidationException | 400 | Request parameters are invalid. |
| ResourceNotFoundException | 404 | The specified resource does not exist. |
| ConflictException | 409 | Operation conflicts with current state (for example, an assessment is already running). |
| AccessDeniedException | 403 | Caller lacks required permissions. |
| ThrottlingException | 429 | Request rate exceeded. |
| InternalServerException | 500 | Internal service error. |
| ServiceQuotaExceededException | 402 | A service quota has been exceeded. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resilience Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resilience-hub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
