---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/implement-controls-isolated-resource-environments.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Implement controls on isolated resource environments
<a name="implement-controls-isolated-resource-environments"></a>

Implementing controls on isolated resource environments provide cloud consumers the autonomy to build workloads to meet their business objectives while keeping the organization compliant to standards and regulations. Controls can take the form of either preventative or detective.

**Preventative controls** prevent events from occurring based on a variety of criteria, including the event type, action, resource, caller identity, and more. For example, a preventative control might deny all users from deleting a specific resource.

**Detective controls** are designed to detect, log, and alert after an event has occurred. These controls will not block actions from occurring, instead they can be used to provide notifications, generate incidents, or initiate automation to address the violation. Detective controls can be helpful in validating that preventative controls are working, auditing an environment, building automated responses to address violations, or measuring the success of process changes.

The sooner a guardrail can be evaluated in the deployment process the better. Implementing preventative guardrails in the deployment process allows compliance risks to be caught earlier and before an attempt to deploy resources even occurs. Identifying risk earlier also saves time during deployments. Building controls into the deployment workflows allows for the inspection of code against standards which can enforce guardrail compliance as resources are being provisioned.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
