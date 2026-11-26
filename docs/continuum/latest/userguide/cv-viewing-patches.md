---
source_url: https://docs.aws.amazon.com/continuum/latest/userguide/cv-viewing-patches.html
---

# Viewing generated patches

Review generated patches to understand the proposed code changes before you apply them. You can download available patches in the AWS Continuum console and check their delivery to your code sources.

## Viewing and downloading a patch
<a name="cv-viewing-patches-console"></a>

Before you begin, your environment must have an issue with a generated patch. You can review the changes and download a patch file for a code source.

**To view and download patches**

1. Open the AWS Continuum console at [https://console.aws.amazon.com/continuum/](https://console.aws.amazon.com/continuum/).

1. In the navigation pane, choose **Environments**.

1. Choose the name of the environment that contains the issue.

1. Choose the **Issues** tab.

1. Choose the title of the issue that you want to review.

1. Choose **View patch** for your source to open its generated patch in **Patch details**.

1. To download the patch file, choose the source's **Download patch** icon, labeled **Download patch for {{source name}}**.

Your browser saves the downloaded patch as a `.patch` file.

## Checking patch delivery
<a name="cv-viewing-patches-delivery"></a>

When you select **Automatically deliver remediation patches** for an environment, AWS Continuum attempts to deliver generated patches to your code sources. For GitHub, AWS Continuum creates pull requests. For GitLab, AWS Continuum creates merge requests. For Amazon S3, AWS Continuum uploads the patch files under `continuum-patches/` in your bucket.

On the issue details page, you can check the delivery destination and status. For a GitHub source, choose **View pull request** when the console displays that link.

In **Patch details**, choose the source's information icon, labeled **Patch information for {{source name}}**. The popover shows **Destination** when available. For Amazon S3, this value identifies the bucket and patch object.

To check delivery status and failure details, choose the issue's **Patch delivery** status. You can download an available patch from the console even if delivery to your code source fails.

For instructions on configuring the Amazon S3 integration role's patch permissions, see [Granting access to the bucket](cv-getting-started.md#cv-getting-started-s3-role). For information about console permissions, see [Allowing users to access the AWS Continuum console](security_iam_id-based-policy-examples.md#security_iam_id-based-policy-examples-console).

## Tracking pull and merge requests
<a name="cv-viewing-patches-lifecycle"></a>

After delivering a patch, AWS Continuum tracks its GitHub pull request or GitLab merge request. Delivery success means that the request was created. Its subsequent state tells you what happened to the proposed fix:
+ `OPEN` – The request is still open.
+ `MERGED` – The request was merged.
+ `CLOSED` – The request was closed without being merged. This state alone doesn't show that the vulnerability was fixed.

AWS Continuum refreshes request states asynchronously when a scan of the environment is queued. To request a refresh after a merge, queue a manual scan or wait for the next scheduled scan. See [Triggering a scan](cv-triggering-scan.md). Requests already recorded as merged retain that state.

In the `GetCodeIssueArtifact` response, the patch's `delivery.changeRequest` contains the recorded state, `checkedAt`, and any available `mergedAt` and `closedAt` timestamps. Before AWS Continuum first reads the request state successfully, the response omits `delivery.changeRequest`. The response also omits this field for patches that AWS Continuum delivers to Amazon S3. If AWS Continuum can't read a request, it keeps the last recorded state. Check the request in your source provider for its current state, and verify the integration's repository access if refreshes fail.

### Issue closure after merging a fix
<a name="cv-viewing-patches-merge-closure"></a>

**Note**
Merge-based issue closure is supported only for GitHub pull requests and GitLab merge requests. It isn't supported for patches delivered to Amazon S3.

Merge-based closure requires every patch from the issue's latest remediation run to have a delivered request. AWS Continuum closes the issue to new findings only after it confirms that all those requests merged into their original target branches. For a fix that spans multiple repositories, all of its requests must meet this condition. A merged request from an earlier remediation run doesn't close the issue for a newer run.

An open request, a request closed without merging, or a merge into a different target branch doesn't trigger issue closure. Closure also waits if a current patch has no delivered request or no confirmed merge. Older requests without a recorded original target branch don't qualify for merge-based closure.

The issue's processing status remains unchanged by merge closure. For example, `COMPLETED` means that AWS Continuum finished processing the issue. This status doesn't mean that you merged its fix. These rules also apply to issues created from findings submitted through the `CreateCodeFinding` API.

If you revert a merged fix, the original issue stays closed to new findings. A later finding for the restored vulnerability can create a new issue and a new remediation attempt instead of reopening the original issue. This depends on the vulnerability being found again and selected for processing. For selection controls, see [Controlling which findings AWS Continuum pursues](cv-focus-mode-issue-budget.md).
