---
source_url: https://docs.aws.amazon.com/elemental-statmux/latest/upgradeguide/clean-install-sm-upg-restore.html
---

This is version 2.20 of the AWS Elemental Statmux documentation. This is the latest version. For prior versions, see the *Previous Versions* section of [AWS Elemental Statmux and AWS Elemental Live Documentation](https://docs.aws.amazon.com/elemental-live).

# Step C: Restore Copied Files
<a name="clean-install-sm-upg-restore"></a>

Now that your operating system is reinstalled, restore the files that you copied back onto the AWS Elemental Statmux hardware unit, to /home/elemental.

Enter this command to extract the database.

```
[elemental@hostname ~]$ tar -xvf elemental-db-backup_statmux_2.20.1.12345_2018-03-18_17-34-38.tar
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental Statmux. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elemental-statmux` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
