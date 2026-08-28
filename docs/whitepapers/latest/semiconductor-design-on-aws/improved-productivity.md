---
source_url: https://docs.aws.amazon.com/whitepapers/latest/semiconductor-design-on-aws/improved-productivity.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Improved productivity
<a name="improved-productivity"></a>

Organizations that move their workloads to the cloud can see a dramatic improvement in development productivity and time to market. AWS bills by the second for compute resources, so the cost of a batch of jobs is the same whether they run serially or in parallel. By scaling horizontally, a simulation regression can run all of its jobs in parallel, and complete in the time it takes to run the longest job. A check-in regression might complete in 5 minutes instead of 30 minutes, which reduces the time a developer needs to wait to verify a change.

Tape-outs are often gated by the time required to verify late changes. Sign-off verification can be completed in days instead of weeks, and compress the development schedule. The scalability of AWS improves productivity and reduces development time by reducing the time it takes to make changes, find bugs, synthesize logic, analyze timing, characterize libraries, and perform all the tasks required to complete a semiconductor design at no additional cost. These extreme levels of parallelism are common in the AWS Cloud in industries with large computing requirements.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
