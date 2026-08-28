---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/transfer-of-log-files.html
---

# Transfer of log files
<a name="transfer-of-log-files"></a>

DataSync is configured to periodically (every hour on the half hour mark) to move the rotated and archived metric log files from EFS to an equivalent location in S3. For details, see the [Logging](logging.md) section. This period is set through Cron schedule by `DATASYNC_METRICS_SCHEDULE = "cron(30 * * * ? *)"` and `DATASYNC_LOGS_SCHEDULE = "cron(30 * * * ? *)"`. These parameters are available through the `source/infrastructure/prebid_server/stack_constants.py` file in the solution [source code](https://github.com/aws-solutions-library-samples/prebid-server-deployment-on-aws).

After each file is copied to S3 and verified, it is removed from the EFS file system through a Lambda function. Only actively written log files are retained on the EFS.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Deploying a Prebid Server on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
