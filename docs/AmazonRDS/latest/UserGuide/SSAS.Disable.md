---
source_url: https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/SSAS.Disable.html
---

# Turning off SSAS
<a name="SSAS.Disable"></a>

To turn off SSAS, remove the `SSAS` option from its option group.

**Important**
Before you remove the `SSAS` option, delete your SSAS databases.
We highly recommend that you back up your SSAS databases before deleting them and removing the `SSAS` option.

## Console
<a name="SSAS.Disable.Console"></a>

**To remove the SSAS option from its option group**

1. Sign in to the AWS Management Console and open the Amazon RDS console at [https://console.aws.amazon.com/rds/](https://console.aws.amazon.com/rds/).

1. In the navigation pane, choose **Option groups**.

1. Choose the option group with the `SSAS` option that you want to remove (`ssas-se-2017` in the previous examples).

1. Choose **Delete option**.

1. Under **Deletion options**, choose **SSAS** for **Options to delete**.

1. Under **Apply immediately**, choose **Yes** to delete the option immediately, or **No** to delete it at the next maintenance window.

1. Choose **Delete**.

## AWS CLI
<a name="SSAS.Disable.CLI"></a>

**To remove the SSAS option from its option group**
+ Use one of the following commands.
**Example**

  For Linux, macOS, or Unix:

  ```
  aws rds remove-option-from-option-group \
      --option-group-name {{ssas-se-2017}} \
      --options SSAS \
      --apply-immediately
  ```

  For Windows:

  ```
  aws rds remove-option-from-option-group ^
      --option-group-name {{ssas-se-2017}} ^
      --options SSAS ^
      --apply-immediately
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon RDS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AmazonRDS` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
