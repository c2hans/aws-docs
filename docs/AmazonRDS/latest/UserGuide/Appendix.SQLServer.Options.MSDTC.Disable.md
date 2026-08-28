---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Appendix.SQLServer.Options.MSDTC.Disable.html
---

# Disabling MSDTC
<a name="Appendix.SQLServer.Options.MSDTC.Disable"></a>

To disable MSDTC, remove the `MSDTC` option from its option group.

## Console
<a name="Options.MSDTC.Disable.Console"></a>

**To remove the MSDTC option from its option group**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Option groups**.

1. Choose the option group with the `MSDTC` option (`msdtc-se-2016` in the previous examples).

1. Choose **Delete option**.

1. Under **Deletion options**, choose **MSDTC** for **Options to delete**.

1. Under **Apply immediately**, choose **Yes** to delete the option immediately, or **No** to delete it at the next maintenance window.

1. Choose **Delete**.

## CLI
<a name="Options.MSDTC.Disable.CLI"></a>

**To remove the MSDTC option from its option group**
+ Use one of the following commands.
**Example**

  For Linux, macOS, or Unix:

  ```
  aws rds remove-option-from-option-group \
      --option-group-name {{msdtc-se-2016}} \
      --options MSDTC \
      --apply-immediately
  ```

  For Windows:

  ```
  aws rds remove-option-from-option-group ^
      --option-group-name {{msdtc-se-2016}} ^
      --options MSDTC ^
      --apply-immediately
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
