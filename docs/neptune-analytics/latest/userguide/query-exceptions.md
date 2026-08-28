---
source_url: https://docs.aws.amazon.com/neptune-analytics/latest/userguide/query-exceptions.html
---

# Exceptions
<a name="query-exceptions"></a>

The following table lists query-side exceptions that could be encountered while using a query.

| Neptune Analytics error code | HTTP status | Retriable | Description |
| --- | --- | --- | --- |
| Validation Exception | 400 | No | Something is wrong with the required information - Eg. a malformed query. |
| AccessDeniedException | 403 | No | User is not authorized to perform the requested operation. |
| ResourceNotFoundException | 404 | No | Requested resource is not available. |
| ThrottlingException | 429 | Yes | The server has received too many concurrent requests. |
| InternalServerErrorException | 500 | Yes | The server failed to process the request for an unknown reason. |
| UnprocessableException | 422 | No | Request cannot be processed due to known reasons - Eg. The query timed out. |
| ConflictException | 409 | Yes | Concurrently running queries attempted to modify resources or data records concurrently and the conflict could not be resolved automatically. Please retry with an exponential back-off strategy. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Neptune Analytics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query neptune-analytics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
