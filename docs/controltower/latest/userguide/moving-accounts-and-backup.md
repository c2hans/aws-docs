---
source_url: https://docs.aws.amazon.com/controltower/latest/userguide/moving-accounts-and-backup.html
---

# Enable backup on moved accounts
<a name="moving-accounts-and-backup"></a>

If you move an account into an AWS Control Tower OU that has AWS Backup enabled, and the account is not enrolled in AWS Control Tower, your backup plan does not apply to the account automatically.

**Console:** To enable AWS Backup for an individual account from the AWS Control Tower console, you can choose **Update account** on the **Account details** page, or you can choose **Re-register OU** on the **OU detail**s page to update several accounts at the same time.

**API:** From the API, if you move an account into an OU that has the backup baseline enabled, you can call the `ResetEnabledBaseline` API on that OU, specifying the OU's `EnabledBaseline` resource as a target, to trigger backups on the account by inheritance from the OU.

Example command:

```
aws controltower reset-enabled-baseline --enabled-baseline-identifier arn:aws:controltower:{{REGION}}:{{NAMESPACE}}:enabledbaseline/XOSDORW8HDB5ZNWEE --region us-east-1
```

Example response:

```
{
        "operationIdentifier": "0bbdb587-c849-4152-95c6-7afa7664ee71"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Tower. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controltower` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
