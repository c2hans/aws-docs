---
source_url: https://docs.aws.amazon.com/appstudio/latest/userguide/troubleshooting-preview.html
---

# Troubleshooting previewing apps
<a name="troubleshooting-preview"></a>

This topic contains information about troubleshooting issues when trying to preview apps.

## The preview fails to load with the following error: `Your app failed to build and cannot be previewed`
<a name="troubleshooting-preview-fails-to-load"></a>

**Problem:** Your app must build successfully to be previewed. This error occurs when there is a compilation error that prevents your app from building successfully.

**Solution:** Review and solve the errors by using the debug panel in the application studio.

## The preview is taking a long time to load
<a name="troubleshooting-preview-long-load"></a>

**Problem:** Certain types of app updates require a long time to compile and build.

**Solution:** Leave the tab open, and wait for the updates to be built. You should see **Saved** in the top-right corner of the application studio of the app, and the preview will reload.

## The preview doesn't reflect the latest changes
<a name="troubleshooting-preview-no-latest-changes"></a>

**Problem:** This can happen when your app editing session was taken over by another user, but you weren't notified. This can cause the app being edited to not match the preview environment.

**Solution:** Refresh the application studio browser tab and take over the editing session if needed.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstudio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
