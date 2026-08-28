---
source_url: https://docs.aws.amazon.com/res/archive/release-minus-1/ug/configuring-file-browser-access.html
---

# Configuring File browser access
<a name="configuring-file-browser-access"></a>

RES Administrators can toggle **Access data** on or off under **File browser permissions**. If **Access data** is turned off, users will not see **File Browser** navigation in their web portal and cannot upload or download data attached to their global file system. When **Access data** is enabled, users have access to **File Browser** navigation in their web portal which allows them to upload or download data that is attached to their global file system.

![environment boundaries](http://docs.aws.amazon.com/res/archive/release-minus-1/ug/images/permission-policy-ssh-disabled.png)

When the **Access data** feature is turned on and then later turned off, users who are already logged in to the web portal will be unable to upload or download files, even if they are on the corresponding page. Additionally, the navigation menu will disappear when they refresh the page.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Research and Engineering Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query res` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
