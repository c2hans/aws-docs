---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/studio-updated-idle-shutdown-update.html
---

# Update default idle shutdown settings
<a name="studio-updated-idle-shutdown-update"></a>

 You can update the default idle shutdown settings at either the domain or user profile level.

**Note**
If idle shutdown is set when applications are running, they must be restarted for idle shutdown settings to take effect.

## Update domain settings
<a name="studio-updated-idle-shutdown-update-domain"></a>

1.  Navigate to the domain.

1.  Choose the **App Configurations** tab.

1.  From the **App Configurations** tab, navigate to either the Code Editor or JupyterLab section.

1.  In the section for the application that you want to modify the idle shutdown time limit for, select **Edit**.

1.  Update the idle shutdown settings for the domain.

1.  Select **Save Changes**.

## Update user profile settings
<a name="studio-updated-idle-shutdown-update-userprofile"></a>

1.  Navigate to the domain.

1.  Choose the **User profiles** tab.

1.  From the **User profiles** tab, select the user profile to edit.

1.  From the **User profile** page, choose the **Applications** tab.

1.  On the **Applications** tab, navigate to either the Code Editor or JupyterLab section.

1.  In the section for the application that you want to modify the idle shutdown time limit for, select **Edit**.

1.  Update the idle shutdown settings for the user profile.

1.  Select **Save Changes**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
