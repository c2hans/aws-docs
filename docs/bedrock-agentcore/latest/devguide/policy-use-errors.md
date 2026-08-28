---
source_url: https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/policy-use-errors.html
---

# Errors
<a name="policy-use-errors"></a>

Policy in AgentCore operations can return the following types of errors:

AuthorizationError
The policy engine denied the request.
HTTP Status Code: 403

AccessDeniedException
You don’t have permission to perform this operation.
HTTP Status Code: 403

ConflictException
The request conflicts with the current state of the resource. For example, the policy name already exists, or a request reused a policy session that was invalidated because a temporal policy on the engine was added or updated.
HTTP Status Code: 409

InternalServerException
An internal server error occurred.
HTTP Status Code: 500

ResourceNotFoundException
The specified policy or policy engine does not exist.
HTTP Status Code: 404

ServiceQuotaExceededException
You have exceeded the service quota for policies or policy engines.
HTTP Status Code: 402

ThrottlingException
The request was throttled due to too many requests.
HTTP Status Code: 429

ValidationException
The request contains invalid parameters or the policy statement contains syntax errors.
HTTP Status Code: 400

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Bedrock AgentCore. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query bedrock-agentcore` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
