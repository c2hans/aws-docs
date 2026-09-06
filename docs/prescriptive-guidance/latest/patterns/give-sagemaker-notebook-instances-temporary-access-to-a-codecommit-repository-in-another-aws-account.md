---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/give-sagemaker-notebook-instances-temporary-access-to-a-codecommit-repository-in-another-aws-account.html
---

# Give SageMaker notebook instances temporary access to a CodeCommit repository in another AWS account
<a name="give-sagemaker-notebook-instances-temporary-access-to-a-codecommit-repository-in-another-aws-account"></a>

*Helge Aufderheide, Amazon Web Services*

## Summary
<a name="give-sagemaker-notebook-instances-temporary-access-to-a-codecommit-repository-in-another-aws-account-summary"></a>

This pattern shows how to grant Amazon SageMaker notebook instances and users temporary access to an AWS CodeCommit repository that’s in another AWS account. This pattern also shows how you can grant granular permissions for specific actions each entity can perform on each repository.

Organizations often store CodeCommit repositories in a different AWS account than the account that hosts their development environment. This multi-account setup helps control access to the repositories and reduces the risk of their accidental deletion. To grant these cross-account permissions, it’s a best practice to use AWS Identity and Access Management (IAM) roles. Then, predefined IAM identities in each AWS account can temporarily assume the roles to create a controlled chain of trust across the accounts.

**Note**
You can apply a similar procedure to grant other IAM identities cross-account access to a CodeCommit repository. For more information, see [Configure cross-account access to an AWS CodeCommit repository using roles](https://docs.aws.amazon.com/codecommit/latest/userguide/cross-account.html) in the *AWS CodeCommit User Guide*.

## Prerequisites and limitations
<a name="give-sagemaker-notebook-instances-temporary-access-to-a-codecommit-repository-in-another-aws-account-prereqs"></a>

**Prerequisites**
+ An active AWS account with a CodeCommit repository (*account A*)
+ A second active AWS account with a SageMaker notebook instance (*account B*)
+ An AWS user with sufficient permissions to create and modify IAM roles in account A
+ A second AWS user with sufficient permissions to create and modify IAM roles in account B

## Architecture
<a name="give-sagemaker-notebook-instances-temporary-access-to-a-codecommit-repository-in-another-aws-account-architecture"></a>

The following diagram shows an example workflow for granting a SageMaker notebook instance and users in one AWS account cross-account access to a CodeCommit repository:

![Workflow for cross-account access to CodeCommit](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/54d0fdb3-6d25-4433-9f67-c87846633d61/images/97a799af-ce88-4495-a61c-d0cd22493ce2.png)

The diagram shows the following workflow:

1. The AWS user role and SageMaker notebook instance role in account B assume a [named profile](https://docs.aws.amazon.com/cli/latest/userguide/cli-configure-files.html#cli-configure-files-using-profiles).

1. The named profile’s permissions policy specifies a CodeCommit access role in account A that the profile then assumes.

1. The CodeCommit access role’s trust policy in account A allows the named profile in account B to assume the CodeCommit access role.

1. The CodeCommit repository’s IAM permissions policy in account A allows the CodeCommit access role to access the CodeCommit repository.

**Technology stack**
+ CodeCommit
+ Git
+ IAM
+ pip
+ SageMaker

## Tools
<a name="give-sagemaker-notebook-instances-temporary-access-to-a-codecommit-repository-in-another-aws-account-tools"></a>
+ [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) is a version control service that helps you privately store and manage Git repositories, without needing to manage your own source control system.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [Git](https://git-scm.com/) is a distributed version-control system for tracking changes in source code during software development.
+ [git-remote-codecommit](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-git-remote-codecommit.html) is a utility that helps you push and pull code from CodeCommit repositories by extending Git.
+ [pip](https://pypi.org/project/pip/) is the package installer for Python. You can use pip to install packages from the Python Package Index and other indexes.

## Best practices
<a name="give-sagemaker-notebook-instances-temporary-access-to-a-codecommit-repository-in-another-aws-account-best-practices"></a>

When you set permissions with IAM policies, make sure that you grant only the permissions required to perform a task. For more information, see [Apply least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege) in the IAM documentation.

When implementing this pattern, make sure that you do the following:
+ Confirm that IAM principles have only the permissions required to perform specific, needed actions within each repository. For example, it’s recommended to allow approved IAM principles to push and merge changes to specific repository branches, but only request merges to protected branches.
+ Confirm that IAM principles are assigned different IAM roles based on their respective roles and responsibilities for each project. For example, a developer will have different access permissions than a release manager or AWS Administrator.

## Epics
<a name="give-sagemaker-notebook-instances-temporary-access-to-a-codecommit-repository-in-another-aws-account-epics"></a>

### Configure the IAM roles
<a name="configure-the-iam-roles"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure the CodeCommit access role and permissions policy. | To automate the manual setup process documented in this epic,** **you can use an [AWS CloudFormation template](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html).In the account that contains the CodeCommit repository (*account A*), do the following:1. [Create an IAM role](https://docs.aws.amazon.com/codecommit/latest/userguide/cross-account-administrator-a.html#cross-account-create-role-a) that can be assumed by the SageMaker notebook instance role in account B.<br />2. [Create an IAM policy](https://docs.aws.amazon.com/codecommit/latest/userguide/cross-account-administrator-a.html#cross-account-create-policy-a) that grants access to the repository and [attach the policy to the role](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_manage-attach-detach.html#add-policies-console). For testing purposes only, choose the [AWSCodeCommitPowerUser](https://docs.aws.amazon.com/codecommit/latest/userguide/security-iam-awsmanpol.html#managed-policies-poweruser) AWS managed policy. This policy grants all [CodeCommit permissions](https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-permissions-reference.html) except the ability to delete resources.<br />3. [Modify the role’s trust policy](https://docs.aws.amazon.com/IAM/latest/UserGuide/roles-managingrole-editing-console.html#roles-managingrole_edit-trust-policy) so that account B is listed as a trusted entity.Before moving this setup into your production environment, it’s a best practice to write your own IAM policy that applies [least-privilege permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege). For more information, see the **Additional information** section of this pattern. | General AWS, AWS DevOps |
| Grant the SageMaker notebook instance's role in account B permissions to assume the CodeCommit access role in account A. | In the account that contains the SageMaker notebook instance’s IAM role (*account B),* do the following:1. Create an IAM policy that allows an IAM role or user to assume the CodeCommit access role in account A.<br />**Example IAM permissions policy that allows an IAM role or user to assume a cross-account role**<pre>{<br />  "Version": "2012-10-17",		 	 	 <br />  "Statement": [<br />      {<br />    "Sid": "VisualEditor0",<br />    "Effect": "Allow",<br />    "Action": "sts:AssumeRole",<br />    "Resource": "arn:aws:iam:::accountA_ID:role/accountArole_ID"<br />  }<br />}</pre><br />2. Attach the policy to your SageMaker notebook instance’s role in account B.<br />3. Have the SageMaker notebook instance’s role in account B assume the CodeCommit access role in account A.To view your repository’s Amazon Resource Name (ARN), see [View CodeCommit repository details](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-view-repository-details.html) in the *AWS CodeCommit User Guide*. | General AWS, AWS DevOps |

### Set up your SageMaker notebook instance in account B
<a name="set-up-your-sagemaker-notebook-instance-in-account-b"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up a user profile on the AWS SageMaker notebook instance to assume the role in account A.  | [Make sure that you have the latest version of the AWS Command Line Interface (AWS CLI) installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html).In the account that contains the SageMaker notebook instance (*account B),* do the following:1. Sign in to the AWS Management Console and open the [SageMaker console](https://console.aws.amazon.com/sagemaker/).<br />2. [Access your SageMaker notebook instance](https://docs.aws.amazon.com/sagemaker/latest/dg/howitworks-access-ws.html). The Jupyter interface opens.<br />3. Choose **New**, and then choose **Terminal**. [A new terminal window opens in your Jupyter environment](https://jupyterlab.readthedocs.io/en/stable/user/terminal.html).<br />4. Navigate to the SageMaker notebook instance’s **\~/.aws/config** file. Then, add a user profile to the file by entering the following statement:<pre>------.aws/config--------------<br />[profile remoterepouser]<br />role_arn = arn:aws:iam::<ID of Account A>:role/<rolename><br />role_session_name = remoteaccesssession<br />region = eu-west-1<br />credential_source  = Ec2InstanceMetadata<br />----------------------------------</pre> | General AWS, AWS DevOps |
| Install the git-remote-codecommit utility. | Follow the instructions in [Step 2: Install git-remote-codecommit](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-git-remote-codecommit.html#setting-up-git-remote-codecommit-install) in the *AWS CodeCommit User Guide*. | Data scientist |

### Access the repository
<a name="access-the-repository"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Access the CodeCommit repository by using Git commands or SageMaker. | **To use Git**<br />IAM principals that assume the SageMaker notebook instance’s role in account B can now run Git commands to access the CodeCommit repository in account A. For example, users can run commands such as `git clone`, `git pull`, and `git push`.<br />For instructions, see [Connect to an AWS CodeCommit repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-connect.html) in the *AWS CodeCommit User Guide*.<br />For information about how to use Git with CodeCommit, see [Getting started with AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/getting-started-cc.html) in the *AWS CodeCommit User Guide*.<br />**To use SageMaker**<br />To use Git from the SageMaker console, you must allow Git to retrieve credentials from your CodeCommit repository. For instructions, see [Associate a CodeCommit repository in a different AWS account with a notebook instance](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-git-cross.html) in the SageMaker documentation. | Git, bash console |

## Related resources
<a name="give-sagemaker-notebook-instances-temporary-access-to-a-codecommit-repository-in-another-aws-account-resources"></a>
+ [Configure cross-account access to an AWS CodeCommit repository using roles](https://docs.aws.amazon.com/codecommit/latest/userguide/cross-account.html) (AWS CodeCommit documentation)
+ [IAM tutorial: Delegate access across AWS accounts using IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial_cross-account-with-roles.html) (IAM documentation)

## Additional information
<a name="give-sagemaker-notebook-instances-temporary-access-to-a-codecommit-repository-in-another-aws-account-additional"></a>

**Restricting CodeCommit permissions to specific actions**

To restrict the actions that an IAM principal can take in the CodeCommit repository, modify the actions that are allowed in the CodeCommit access policy.

For more information about CodeCommit API operations, see [CodeCommit permissions reference](https://docs.aws.amazon.com/codecommit/latest/userguide/auth-and-access-control-permissions-reference.html) in the *AWS CodeCommit User Guide*.

**Note**
You can also edit the [AWSCodeCommitPowerUser](https://docs.aws.amazon.com/codecommit/latest/userguide/security-iam-awsmanpol.html#managed-policies-poweruser) AWS managed policy to fit your use case.

**Restricting CodeCommit permissions to specific repositories**

To create a multitenant environment where more than one code repository is accessible to only specific users, do the following:

1. Create multiple CodeCommit access roles in account A. Then, configure each access role’s trust policy to allow specific users in account B to assume the role.

1. Restrict what code repositories that each role can assume by adding a **"Resource"** condition to each CodeCommit access role’s policy.

**Example "Resource" condition that restricts an IAM principal’s access to a specific CodeCommit repository**

```
"Resource" : [<REPOSITORY_ARN>,<REPOSITORY_ARN> ]
```

**Note**
To help identify and differentiate multiple code repositories in the same AWS account, you can assign different prefixes to the repositories’ names. For example, you can name code repositories with prefixes that align to different developer groups, such as **myproject-subproject1-repo1** and **myproject-subproject2-repo1**. Then, you can create an IAM role for each developer group based on their assigned prefixes. For example, you could create a role named **myproject-subproject1-repoaccess** and grant it access to all of the code repositories that include the prefix **myproject-subproject1**.

**Example "Resource" condition that refers to a code repository ARN that includes a specific prefix**

```
"Resource" : arn:aws:codecommit:<region>:<account-id>:myproject-subproject1-*
```
