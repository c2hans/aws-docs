---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/update-aft-version.html
---

# Update the AFT version
<a name="update-aft-version"></a>

Sign in to the AWS Control Tower management account to initiate this AFT update.

You can update your deployed AFT version by pulling it in from the `main` repository branch:

```
terraform get -update
```

After the pull is complete, you can re-run the Terraform plan or run apply to update the AFT infrastructure with the latest changes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
