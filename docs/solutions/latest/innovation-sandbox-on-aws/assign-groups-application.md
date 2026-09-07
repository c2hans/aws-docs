---
source_url: https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/assign-groups-application.html
---

# Assign groups to your application
<a name="assign-groups-application"></a>

**Note**
If you have configured your IAM Identity Center instance to use an external identity provider, you will need to manage user groups through that external provider instead of creating them directly in IAM Identity Center.

The IDC stack creates these three user groups in IAM Identity Center (where `NAMESPACE` is the namespace parameter passed to the stack):
+  `<NAMESPACE>_IsbUsersGroup`
+  `<NAMESPACE>_IsbManagersGroup`
+  `<NAMESPACE>_IsbAdminsGroup`

To assign groups to your application:

1. Sign in to the [AWS IAM Identity Center console](https://console.aws.amazon.com/singlesignon/).

1. From the left pane, under **Application assignments**, choose **Applications**.

1. On the Applications page, from the **Customer managed** tab, choose the application you created in the previous steps.

1. Choose **Assigned users and groups**, and choose the three groups. Manually enter the namespace to find the group, as they are not listed by default.

![Assign users and groups](https://docs.aws.amazon.com/solutions/latest/innovation-sandbox-on-aws/images/screenshots/assign-user-groups.png)

1. Choose **Done** to assign these groups to your application.
