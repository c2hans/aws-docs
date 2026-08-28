---
source_url: https://docs.aws.amazon.com/res/latest/ug/permission-profiles-desktop-sharing-profiles.html
---

# Desktop sharing profiles
<a name="permission-profiles-desktop-sharing-profiles"></a>

Administrators can create new profiles and customize them. These profiles can be accessed by all users and are used when sharing a session with others. The maximum permissions granted within these profiles cannot exceed the desktop permissions allowed globally.

**Create Profile**

Administrators can choose **Create profile** to create a new profile. Then they can enter a **Profile name**, a **Profile Description**, set the desired permissions, and **Save** their changes.

![desktop sharing profiles](http://docs.aws.amazon.com/res/latest/ug/images/desktop-sharing-profiles.png)

![profile definition and permissions](http://docs.aws.amazon.com/res/latest/ug/images/res-profile-definition.png)

**Edit Profile**

**To edit a profile:**

1. Select the desired profile.

1. Choose **Actions**, then select **Edit** to modify the profile.

1. Adjust the permissions as needed.

1. Choose **Save changes**.

Any changes made to the profile will be immediately applied to the current open sessions.

![desktop sharing profiles with testprofile_1 selected](http://docs.aws.amazon.com/res/latest/ug/images/res-desktop-sharing-profiles2.png)

![profile definition and permissions for testProfile_1](http://docs.aws.amazon.com/res/latest/ug/images/res-profile-definition2.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Research and Engineering Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query res` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
