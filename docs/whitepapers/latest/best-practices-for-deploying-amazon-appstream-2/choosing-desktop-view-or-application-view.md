---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/choosing-desktop-view-or-application-view.html
---

# Choosing Desktop View or Application View
<a name="choosing-desktop-view-or-application-view"></a>

 The determination for choosing an application view or desktop view has no impact on performance or cost. Only one view is accessible at any given time per WorkSpaces Applications fleet. You can change the **Stream view** option. Plan this change during off-peak business hours, as changing the stream view requires a restart of the fleet.

 There is no single best practice for stream view. The impact of stream view options is summarized through the following:
+  Detailed reporting for application usage through the **Usage Reports** feature for administrators
+  Overall experience and workflow for end users (for example, does a full desktop address the needs of the use case or will only viewing the applications be sufficient?).

## Desktop View
<a name="desktop-view"></a>

 For use cases where all the user’s workflow is performed in session, Desktop View simplifies the user experience by keeping all applications focused in one environment. Desktop View can give a more consistent user experience for deployments of more than 3-5 applications that require integration with the operating system (OS). Desktop View is effective when maintaining two separate and distinct environments. For example, a user can have concurrent access to both a production and pre-production desktop environment to validate changes to layout, configuration, and application access.

 WorkSpaces Applications Usage Reports creates a daily application report for Desktop View. The resulting output for application is simply ‘desktop’, mapping directly to the WorkSpaces Applications session. For more information, refer to the [**Monitoring user usage**](monitoring.md#monitoring-user-usage) section of this document.

## Applications Only view
<a name="applications-only-view"></a>

 The Applications Only view is also effective when the WorkSpaces Applications stack is intended to deliver a few applications that are intermittently required. In kiosk environments, a securely locked down delivery of applications is delivered through Application View. With Application View, WorkSpaces Applications replaces the default Windows shell with a custom shell. This custom shell presents only running applications, minimizing the attack surface of the OS.

 For use cases where WorkSpaces Applications is used to augment an existing organization’s desktop environment, the Applications Only view is preferred. Deploy the WorkSpaces Applications Windows Client in [* native application mode*](https://docs.aws.amazon.com/appstream2/latest/developerguide/client-system-requirements-feature-support.html#feature-support-native-application-mode) to minimize user confusion by allowing full use of keyboard shortcuts.

 Amazon WorkSpaces Applications Usage Reports creates a daily application report for application view. For more granular reporting of application and run use, consider a third-party solution to report at the operating system level. You can use Microsoft AppLocker in reporting mode, or consider solutions that are available in the AWS Marketplace, such as Liquidware’s [*Stratusphere UX*](https://aws.amazon.com/marketplace/pp/prodview-ghxb36werkone).

## AWS Identity and Access Management role configuration
<a name="identity-and-access-management-role-configuration"></a>

If a workload requires the WorkSpaces Applications end users to access other AWS services from within their session, it is a best practice to delegate access through the use of [AWS Identity and Access Management (IAM) roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html). IAM roles can be directly attached to your end user’s session through the [assignment at the fleet level](https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html#how-to-use-iam-role-with-streaming-instances). For additional best practices when using IAM roles with WorkSpaces Applications, see [this section of the administrator guide](https://docs.aws.amazon.com/appstream2/latest/developerguide/using-iam-roles-to-grant-permissions-to-applications-scripts-streaming-instances.html#best-practices-for-using-iam-role-with-streaming-instances).

### Using static credentials
<a name="using-static-credentials"></a>

Some workloads may require static inputs for the IAM access keys opposed to inheriting them from the attached role. There are two methods for receiving these credentials. The first method involves storing the access keys within an AWS service and then giving your end users explicit IAM access to pull that specific value from the service. Two examples of access keys storage mechanisms is using [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/tutorials_basic.html) or [AWS SSM Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-paramstore-su-create.html). The second method is to use the WorkSpaces Applications credential provider to access the attached role’s access keys. This can be done by invoking the credential provider and parsing the output for your access key and secret key. An example of how to perform this action within PowerShell follows.

```
$CMD = 'C:\Program Files\Amazon\Photon\PhotonRoleCredentialProvider\PhotonRoleCredentialProvider.exe'
$role = 'Machine'

$output = & $CMD --role=$role
$parsed = $output | ConvertFrom-Json

$access_key = $parsed.AccessKeyId
$secret_key = $parsed.SecretAccessKey
$session_token = $parsed.SessionToken
```

### Protecting your WorkSpaces Applications S3 bucket
<a name="protecting-appstream-bucket"></a>

If your WorkSpaces Applications workload is configured with Home Folder and/or Application Persistence, then it is a best practice to protect the Amazon S3 bucket that the persistent data is being stored in from unauthorized access or accidental deletion. The first layer of protection is to add an Amazon S3 bucket policy to [prevent accidental deletion of the bucket](https://docs.aws.amazon.com/appstream2/latest/developerguide/s3-iam-policy.html#s3-iam-policy-delete). The second layer of protection is to add a bucket policy that aligns to the principle of least privilege. Aligning to the principle can be done by only [allowing bucket access to the necessary parties](https://docs.aws.amazon.com/appstream2/latest/developerguide/s3-iam-policy.html#s3-iam-policy-restricted-access).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
