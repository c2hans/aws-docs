---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/diagnostics-pack.html
---

# Diagnostics pack
<a name="diagnostics-pack"></a>

The diagnostics pack tool is deployed when the installer stack of the solution is deployed with `Yes` as the value for the **Enable Diagnostics Pack** parameter. To create diagnostic reports and other configuration files, the diagnostics pack tool creates the `${ACCELERATOR_PREFIX}-Diagnostic` AWS Lambda function and the `${ACCELERATOR_PREFIX}-DiagnosticProject` AWS CodeBuild project.

To collect diagnostic reports, you can run the CodeBuild project manually. A diagnostic report will be stored in the installer’s S3 bucket under the prefix `$[ACCELERATOR_PREFIX]-Diagnostics-Pack`. You can also collect configuration files for Landing Zone Accelerator on AWS using the diagnostics tool. The diagnostic report along with configuration files will assist AWS Support in troubleshooting the failure. The diagnostic report can be reviewed to determine the root cause of the problem. As part of the CodeBuild project, the `DAYS_PIPELINE_IN_FAILED_STATUS` environment variable determines how long back logs will be retrieved by the tool.

Run the diagnostics tool AWS CodeBuild project by running the following AWS CLI command:

```
aws codebuild start-build --project-name $[ACCELERATOR_PREFIX]-DiagnosticProject
```

This command will override the default value for the `DAYS\_PIPELINE\_IN\_FAILED\_STATUS `variable for the run only, and will not update the CodeBuild project definition.

```
aws codebuild start-build --project-name $[ACCELERATOR_PREFIX]-DiagnosticProject --environment-variables-override name=DAYS_PIPELINE_IN_FAILED_STATUS,value=2
```

**Note**
We recommend that you review the diagnostic report and configuration files before providing them to AWS Support to ensure that no sensitive information is located within the logs or configuration files.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Landing Zone Accelerator on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
