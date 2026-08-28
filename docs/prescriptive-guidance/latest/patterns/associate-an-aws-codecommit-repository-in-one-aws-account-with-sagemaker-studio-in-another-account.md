---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/associate-an-aws-codecommit-repository-in-one-aws-account-with-sagemaker-studio-in-another-account.html
---

# Associate an AWS CodeCommit repository in one AWS account with Amazon SageMaker AI Studio Classic in another account
<a name="associate-an-aws-codecommit-repository-in-one-aws-account-with-sagemaker-studio-in-another-account"></a>

*Laurens van der Maas and Aubrey Oosthuizen, Amazon Web Services*

## Summary
<a name="associate-an-aws-codecommit-repository-in-one-aws-account-with-sagemaker-studio-in-another-account-summary"></a>

This pattern provides instructions and code on how to associate an AWS CodeCommit repository in one AWS account (Account A) with Amazon SageMaker AI Studio Classic in another AWS account (Account B). To set up the association, you must create an AWS Identity and Access Management (IAM) policy and role in Account A and an IAM inline policy in Account B. Then, you use a shell script to clone the CodeCommit repository from Account A to Amazon SageMaker AI Classic in Account B.

## Prerequisites and limitations
<a name="associate-an-aws-codecommit-repository-in-one-aws-account-with-sagemaker-studio-in-another-account-prereqs"></a>

**Prerequisites **
+ Two [AWS accounts](https://aws.amazon.com/premiumsupport/knowledge-center/create-and-activate-aws-account/), one containing the CodeCommit repository and the other containing a SageMaker AI Domain with a user
+ Provisioned [SageMaker AI Domain and user](https://docs.aws.amazon.com/sagemaker/latest/dg/gs-studio-onboard.html), with internet access or access to CodeCommit and AWS Security Token Service (AWS STS) through virtual private network (VPC) endpoints
+ A basic understanding of [IAM](https://docs.aws.amazon.com/iam/?id=docs_gateway)
+ A basic understanding of [SageMaker AI Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/studio.html)
+ A basic understanding of [Git](https://git-scm.com/) and [CodeCommit ](https://docs.aws.amazon.com/codecommit/index.html)

**Limitations **

This pattern applies to SageMaker AI Studio Classic only, not to RStudio on Amazon SageMaker AI.

## Architecture
<a name="associate-an-aws-codecommit-repository-in-one-aws-account-with-sagemaker-studio-in-another-account-architecture"></a>

**Technology stack**
+ Amazon SageMaker AI
+ Amazon SageMaker AI Studio Classic
+ AWS CodeCommit
+ AWS Identity and Access Management (IAM)
+ Git

**Target architecture**

The following diagram shows an architecture that associates a CodeCommit repository from Account A to SageMaker AI Studio Classic in Account B.

![Architecture diagram for cross-account association](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/d40df9eb-6ee2-4cb8-8257-051fa624e52a/images/abb89a66-fc8f-4e72-8f45-f0f44c2ec6ce.png)

The diagram shows the following workflow:

1. A user assumes the `MyCrossAccountRepositoryContributorRole` role in Account A through the `sts:AssumeRole` role, while using the SageMaker AI execution role in SageMaker AI Studio Classic in Account B. The assumed role includes the CodeCommit permissions to clone and interact with the specified repository.

1. The user performs Git commands from the system terminal in SageMaker AI Studio Classic.

**Automation and scale**

This pattern consists of manual steps that can be automated by using the [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/?id=docs_gateway), [AWS CloudFormation](https://docs.aws.amazon.com/cloudformation/?id=docs_gateway), or [Terraform](https://www.terraform.io/).

## Tools
<a name="associate-an-aws-codecommit-repository-in-one-aws-account-with-sagemaker-studio-in-another-account-tools"></a>

**AWS tools**
+ [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/?id=docs_gateway) is a managed machine learning (ML) service that helps you build and train ML models and then deploy them into a production-ready hosted environment.
+ [Amazon SageMaker AI Studio Classic](https://docs.aws.amazon.com/sagemaker/latest/dg/studio.html) is a web-based, integrated development environment (IDE) for machine learning that lets you build, train, debug, deploy, and monitor your machine learning models.
+ [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) is a version control service that helps you privately store and manage Git repositories, without needing to manage your own source control system.

  **Notice**: AWS CodeCommit is no longer available to new customers. Existing customers of AWS CodeCommit can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-your-aws-codecommit-repository-to-another-git-provider/)
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.

**Other tools**
+ [Git](https://git-scm.com/) is a distributed version-control system for tracking changes in source code during software development.

## Epics
<a name="associate-an-aws-codecommit-repository-in-one-aws-account-with-sagemaker-studio-in-another-account-epics"></a>

### Create an IAM policy and IAM role in Account A
<a name="create-an-iam-policy-and-iam-role-in-account-a"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an IAM policy for repository access in Account A. | 1. Sign in to the AWS Management Console and open the [IAM console](https://console.aws.amazon.com/iam/).<br />2. In the navigation pane, choose **Policies**, and then choose **Create policy**.<br />3. Choose the **JSON **tab.<br />4. Copy the policy statement from *Example IAM policy* in the [Additional information](#associate-an-aws-codecommit-repository-in-one-aws-account-with-sagemaker-studio-in-another-account-additional) section of this pattern, and then paste the statement into the JSON editor. Make sure to replace all placeholder values in the policy.<br />5. Choose **Next:Tags**, and then choose **Next:Review**.<br />6. For **Name**, enter a name for the policy. **Note**: In this pattern, the IAM policy is referred to as `CrossAccountAccessForMySharedDemoRepo`, but you can choose whatever policy name that you prefer.<br />7. Choose **Create policy**.It's a best practice to restrict the scope of your IAM policies to the minimum required permissions for your use case. | AWS DevOps |
| Create an IAM role for repository access in Account A. | 1. In the navigation pane of the [IAM console](https://console.aws.amazon.com/iam/), choose **Roles**, and then choose **Create role**.<br />2. For **Trusted entity type**, select **AWS account**.<br />3. In the **AWS account** section, select **Another AWS account**.<br />4. For **Account ID**, enter the account ID for Account B.<br />5. On the **Add permissions** page, search for and choose the `CrossAccountAccessForMySharedDemoRepo` policy that you created earlier.<br />6. Choose **Next**.<br />7. For **Role name**, enter a name. **Note**: In this pattern, the IAM role name is referred to as `MyCrossAccountRepositoryContributorRole`, but you can choose whatever role name that you prefer.<br />8. Choose **Create role**, and then copy the Amazon Resource Name (ARN) of the new role. | AWS DevOps |

### Create an IAM inline policy in Account B
<a name="create-an-iam-inline-policy-in-account-b"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Attach an inline policy to the execution role that's attached to your SageMaker Domain user in Account B. | 1. In the navigation pane of the [IAM console](https://console.aws.amazon.com/iam/), choose **Roles**.<br />2. Search for and choose the execution role that's attached to your SageMaker AI Domain user in Account B.<br />3. Choose **Add permissions**, and then choose **Create inline policy**.<br />4. Choose the **JSON **tab.<br />5. Copy the following policy statement, and then paste it into the JSON editor.<pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />        {<br />            "Sid": "VisualEditor0",<br />            "Effect": "Allow",<br />            "Action": "sts:AssumeRole",<br />            "Resource": "arn:aws:iam::<Account_A_ID>:role/<Account_A_Role_Name>"<br />        }<br />    ]<br />}</pre><br />6. Replace `<Account_A_ID>` with the account ID for Account A. Replace `<Account_A_Role_Name>` with the name of the IAM role that you created earlier.<br />7. Choose **Review policy**.<br />8. For **Name**, enter a name for your inline policy.<br />9. Choose **Create policy**. | AWS DevOps |

### Clone the repository in SageMaker AI Studio Classic for Account B
<a name="clone-the-repository-in-sm-studio-classic-for-account-b"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the shell script in SageMaker AI Studio Classic in Account B. | 1. In the navigation pane of the [SageMaker console](https://console.aws.amazon.com/sagemaker/), choose **Studio**.<br />2. Select your user profile and then choose **Open Studio**.<br />3. In the **Home** section, choose **Open Launcher**.<br />4. In the **Utilities and files** section, choose **Text file**.<br />5. Copy the script from *Example SageMaker shell script* in the [Additional information](#associate-an-aws-codecommit-repository-in-one-aws-account-with-sagemaker-studio-in-another-account-additional) section of this pattern, and then paste the statement into the new file. Make sure to replace all placeholder values in the script.<br />6. Right-click the **untitled.txt** tab of your new file, and then choose **Rename Text**. For **New Name**, enter **cross\_account\_git\_clone.sh**, and then choose **Rename**. | AWS DevOps |
| Invoke the shell script from the system terminal. | 1. In the **Home** section of the [SageMaker console](https://console.aws.amazon.com/sagemaker/), choose **Open Launcher**.<br />2. In the **Utilities and files** section, choose **System terminal**.<br />3. In the terminal, run the following command:<pre>chmod u+x ./cross_account_git_clone.sh && ./cross_account_git_clone.sh</pre>You have cloned your CodeCommit repository in a SageMaker AI Studio cross-account. You can now perform all Git commands from the system terminal. | AWS DevOps |

## Additional information
<a name="associate-an-aws-codecommit-repository-in-one-aws-account-with-sagemaker-studio-in-another-account-additional"></a>

**Example IAM policy**

If you use this example policy, do the following:
+ Replace `<CodeCommit_Repository_Region>` with the AWS Region for the repository.
+ Replace `<Account_A_ID>` with the account ID for Account A.
+ Replace `<CodeCommit_Repository_Name>` with the name of your CodeCommit repository in Account A.

```
{
"Version": "2012-10-17",
"Statement": [
    {
        "Effect": "Allow",
        "Action": [
            "codecommit:BatchGet*",
            "codecommit:Create*",
            "codecommit:DeleteBranch",
            "codecommit:Get*",
            "codecommit:List*",
            "codecommit:Describe*",
            "codecommit:Put*",
            "codecommit:Post*",
            "codecommit:Merge*",
            "codecommit:Test*",
            "codecommit:Update*",
            "codecommit:GitPull",
            "codecommit:GitPush"
        ],
        "Resource": [
            "arn:aws:codecommit:<CodeCommit_Repository_Region>:<Account_A_ID>:<CodeCommit_Repository_Name>"
        ]
    }
]
}
```

**Example SageMaker AI shell script**

If you use this example script, do the following:
+ Replace `<Account_A_ID>` with the account ID for Account A.
+ Replace `<Account_A_Role_Name>` with the name of the IAM role that you created earlier.
+ Replace `<CodeCommit_Repository_Region>` with the AWS Region for the repository.
+ Replace `<CodeCommit_Repository_Name>` with the name of your CodeCommit repository in Account A.

```
#!/usr/bin/env bash
#Launch from system terminal
pip install --quiet git-remote-codecommit

mkdir -p ~/.aws
touch ~/.aws/config

echo "[profile CrossAccountAccessProfile]
region = <CodeCommit_Repository_Region>
credential_source=EcsContainer
role_arn = arn:aws:iam::<Account_A_ID>:role/<Account_A_Role_Name>
output = json" > ~/.aws/config

echo '[credential "https://git-codecommit.<CodeCommit_Repository_Region>.amazonaws.com"]
        helper = !aws codecommit credential-helper $@ --profile CrossAccountAccessProfile
        UseHttpPath = true' > ~/.gitconfig

git clone codecommit::<CodeCommit_Repository_Region>://CrossAccountAccessProfile@<CodeCommit_Repository_Name>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
