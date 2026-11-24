---
source_url: https://docs.aws.amazon.com/continuum/latest/userguide/cv-focus-mode-issue-budget.html
---

# Controlling which findings AWS Continuum pursues

Focus mode and an issue budget are two optional settings of an environment. They control which findings AWS Continuum *pursues*. When AWS Continuum pursues a finding, it validates whether the finding is exploitable, scores its severity, and, for a confirmed finding, creates an issue and prepares a remediation.
+ With focus mode, you choose which findings AWS Continuum pursues by the severity reported on each finding.
+ With an issue budget, you limit the number of new issues that each scan can create.

Use these settings to focus AWS Continuum on the findings that matter most to you and to manage your usage. Both settings reduce the work that AWS Continuum does after it discovers findings, such as validation and remediation, and so reduce the model inference that AWS Continuum uses. Discovery still runs on every scan, so scans continue to use inference to find vulnerabilities.

You can configure both settings in the AWS Continuum console or with the AWS Command Line Interface (AWS CLI).

## Focus mode options
<a name="cv-focus-mode"></a>

Focus mode has the following values:

**Comprehensive** (`COMPREHENSIVE`)
AWS Continuum pursues findings at every severity. This is the default value.

**Focused** (`FOCUSED`)
AWS Continuum pursues findings at every severity except `INFORMATIONAL`, `LOW`, and `MEDIUM`. This includes findings whose severity is `UNKNOWN` or `OTHER`.

In **Focused** mode, AWS Continuum doesn't validate, score, or remediate lower-severity findings, and creates no issues for them.

Focus mode also applies to findings that you submit with `CreateCodeFinding`. In **Focused** mode, a finding that you submit with `INFORMATIONAL`, `LOW`, or `MEDIUM` severity has the status `NOT_PURSUED` and the `notPursuedReason` `FOCUS_MODE`. The console shows its status as **Not pursued · Below focus mode**.

## Issue budget
<a name="cv-issue-budget"></a>

An issue budget (`issueBudget.maxIssuesPerScan`) sets the maximum number of new issues that one scan can create. You can set it to a number from 1 to 1000. By default, an environment has no issue budget.

When a scan produces more findings to pursue than the budget allows, AWS Continuum pursues the highest-ranked findings first after the scan completes. It ranks findings by severity, and then by CVSS base score. It creates no issues for the remaining findings.

The issue budget doesn't apply to findings that you submit with `CreateCodeFinding`.

An issue budget limits the number of issues, not your charges. To set cost and usage alerts, use AWS Budgets.

When you use focus mode and an issue budget together, AWS Continuum applies focus mode first. The issue budget then applies to the findings that focus mode doesn't exclude.

## When changes apply
<a name="cv-focus-budget-changes"></a>
+ A change to focus mode or the issue budget applies from the next scan that starts. A scan that is already running keeps the settings that were in effect when it started.
+ A change to focus mode applies immediately to findings that you submit with `CreateCodeFinding`.
+ A change doesn't apply to past scans or to findings that you already submitted. To apply new settings, run another scan, or submit the finding again with `CreateCodeFinding` and a new `clientToken`.

## Console configuration
<a name="cv-focus-budget-console"></a>

When you create an environment, the **Focus mode** section of **Create environment** contains both settings. For **Findings to pursue**, choose **Comprehensive** or **Focused**. For **Issues to pursue per scan**, enter a number from 1 to 1000, or leave it empty for no limit.

After you create an environment, you can change either setting at any time. For example, switch to **Focused** when you want AWS Continuum to spend less work on lower-severity findings.

You need an existing environment and permission to update it.

To change the settings for an existing environment, do the following.

1. Open the AWS Continuum console at [https://console.aws.amazon.com/continuum/](https://console.aws.amazon.com/continuum/).

1. In the navigation pane, choose **Environments**, and then choose the environment name.

1. Choose the **Configuration** tab.

1. In **Environment settings**, choose **Edit settings**.

1. For **Findings to pursue**, choose **Comprehensive** or **Focused**.

1. For **Issues to pursue per scan**, enter a number from 1 to 1000. To remove the limit, clear the value.

1. Choose **Save**.

The console shows **Environment settings updated.**, and **Environment settings** shows the new values in **Focus mode** and **Issues per scan**. The new values apply from the next scan.

## AWS CLI examples
<a name="cv-focus-budget-api"></a>

To configure the settings with the AWS CLI, set `focusMode` and `issueBudget` in the `environmentConfiguration` of an environment's code configuration.

The following AWS CLI command creates an environment that doesn't pursue lower-severity findings and creates at most 25 new issues for each scan. Replace {{my-environment}} with a name for the environment and {{integration-id}} with the ID of your Amazon S3 integration:

```bash
PROMPT> aws continuum create-environment \
    --name {{my-environment}} \
    --configuration '{
      "codeConfiguration": {
        "sourceConfiguration": {
          "s3Sources": [{"integrationId": "{{integration-id}}", "codePrefix": "code/"}]
        },
        "environmentConfiguration": {
          "focusMode": "FOCUSED",
          "issueBudget": {"maxIssuesPerScan": 25}
        }
      }
    }'
```

`UpdateEnvironment` is a partial update. Settings that you omit from `environmentConfiguration` keep their current values.

The following AWS CLI command changes only the issue budget. Replace {{environment-id}} with the ID of your environment:

```bash
PROMPT> aws continuum update-environment \
    --environment-id {{environment-id}} \
    --configuration '{"codeConfiguration": {"environmentConfiguration": {"issueBudget": {"maxIssuesPerScan": 50}}}}'
```

To remove the issue budget, set `maxIssuesPerScan` to `0`.

The following AWS CLI command removes the issue budget and switches the environment to `COMPREHENSIVE`. Replace {{environment-id}} with the ID of your environment:

```bash
PROMPT> aws continuum update-environment \
    --environment-id {{environment-id}} \
    --configuration '{"codeConfiguration": {"environmentConfiguration": {"focusMode": "COMPREHENSIVE", "issueBudget": {"maxIssuesPerScan": 0}}}}'
```

To view the current settings, call `GetEnvironment`. An environment with no issue budget doesn't return `issueBudget`.
