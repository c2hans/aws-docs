---
source_url: https://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/auto-session-revocation-module.html
---

# Auto session revocation module
<a name="auto-session-revocation-module"></a>

![Diagram of auto session revocation module: Detect compromised sessions workflow.](http://docs.aws.amazon.com/solutions/latest/secure-media-delivery-at-the-edge-on-aws/images/image7.png)

 The base and API module provide the ability to react when, through external analysis, you identified a compromised playback session, if it was confirmed that session was used through unallowed distribution channels. Alternatively, you can also deploy additional and optional modules which facilitate detecting sessions with a high probability of being compromised. As the process of detecting suspicious session is run regularly, the resulting session list is emitted to DynamoDB created under base module. These sessions are ordered and processed as explained in the [Base module: session revocation workflow](auto-session-revocation-1.md) section.

 The auto session revocation module design leverages AWS Step Functions to coordinate this entire multistep process. A predefined workflow is invoked periodically as specified in the created EventBridge rule. For ongoing video delivery streaming, set the period in the range of a few minutes to reduce the time it takes to detect and block suspicious sessions. Once workflow is initiated, the first step is to formulate the right SQL query based on the input parameters configured. The compiled SQL query is submitted as a job to Amazon Athena which initiates SQL query against the CloudFront distribution’s access logs. Bear in mind that for this process to work, session IDs must be issued for the viewers together with access tokens. Based on the provided SQL query, Athena job will eventually complete the query run, listing all the sessions that are above the acceptable suspicion score threshold, which is another input controlled by the solution’s operator. Multiple factors are taken into consideration when suspicion score level is evaluated, as explained in the Session Revocation Guide section, but put simply it is a measure of by how much request rate deviates from the median value and other signals indicative that multiple unique viewers are reusing the same session ID and token pair to watch the content simultaneously. When Athena job is completed and returned list of session is not empty, a Lambda function is invoked to ingest the session IDs with their suspicion scores and additional information, and put in DynamoDB table from the base module.

 Before using the auto revocation module, collection of access logs to Amazon S3 must be configured for each CloudFront distribution, the traffic of which should be analyzed through this process. You must also set up a database and a table in Athena referencing access logs in the S3 bucket.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Secure Media Delivery at the Edge on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
