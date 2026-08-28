---
source_url: https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-creating-configuration-profile-feature-flags-editing-version.html
---

# Saving a previous feature flag version to a new version
<a name="appconfig-creating-configuration-profile-feature-flags-editing-version"></a>

When you update a feature flag, AWS AppConfig automatically saves your changes to a new version. If you want to use a previous feature flag version, you must copy it to a draft version and then save it. You can't edit and save changes to a previous flag version without saving it to a new version.

**To edit a previous feature flag version and save it to a new version**

1. Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/appconfig/](https://console.aws.amazon.com/systems-manager/appconfig/).

1. In the navigation pane, choose **Applications**, and then choose the application with the feature flag you want to edit and save to a new version.

1. On the **Configuration profiles and feature flags** tab, choose the configuration profile with the feature flag you want to edit and save to a new version.

1. On the **Feature flags** tab, use the **Version** list to choose the version you want to edit and save to a new version.

1. Choose **Copy to draft version**.

1. In the **Version label** field, enter a new label (optional, but recommended).

1. In the **Version description** field, enter a new description (optional, but recommended).

1. Choose **Save version**.

1. Choose **Start deployment** to deploy the new version.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
