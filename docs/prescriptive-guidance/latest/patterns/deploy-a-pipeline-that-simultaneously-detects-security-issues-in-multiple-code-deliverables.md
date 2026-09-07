---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-a-pipeline-that-simultaneously-detects-security-issues-in-multiple-code-deliverables.html
---

# Deploy a pipeline that simultaneously detects security issues in multiple code deliverables
<a name="deploy-a-pipeline-that-simultaneously-detects-security-issues-in-multiple-code-deliverables"></a>

*Benjamin Morris, Tim Hahn, Sapeksh Madan, Dina Odum, and Isaiah Schisler, Amazon Web Services*

## Summary
<a name="deploy-a-pipeline-that-simultaneously-detects-security-issues-in-multiple-code-deliverables-summary"></a>

The [Simple Code Scanning Pipeline (SCSP)](https://github.com/awslabs/simple-code-scanning-pipeline) provides two-click creation of a code analysis pipeline that runs industry-standard open-source security tools in parallel. This enables developers to check the quality and security of their code without having to install tools or even understand how to run them. This helps you reduce vulnerabilities and misconfigurations in code deliverables. It also reduces the amount of time your organization spends installing, researching, and configuring security tools.

Before SCSP, scanning code using this particular suite of tools required developers to locate, manually install, and configure the software analysis tools. Even locally installed, all-in-one tools, such as Automated Security Helper (ASH), require configuring a Docker container in order to run. However, with SCSP, a suite of industry-standard code analysis tools runs automatically in the AWS Cloud. With this solution, you use Git to push your code deliverables, and then you receive a visual output with at-a-glance insights into which security checks failed.

## Prerequisites and limitations
<a name="deploy-a-pipeline-that-simultaneously-detects-security-issues-in-multiple-code-deliverables-prereqs"></a>
+ An active AWS account
+ One or more code deliverables that you want to scan for security issues
+ AWS Command Line Interface (AWS CLI), [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
+ Python version 3.0 or later and pip version 9.0.3 or later, [installed](https://www.python.org/downloads/windows/)
+ Git, [installed](https://github.com/git-guides/install-git)
+ Install [git-remote-codecommit](https://docs.aws.amazon.com/codecommit/latest/userguide/setting-up-git-remote-codecommit.html#setting-up-git-remote-codecommit-install) on your local workstation

## Architecture
<a name="deploy-a-pipeline-that-simultaneously-detects-security-issues-in-multiple-code-deliverables-architecture"></a>

**Target technology stack**
+ AWS CodeCommit repository
+ AWS CodeBuild project
+ AWS CodePipeline pipeline
+ Amazon Simple Storage Service (Amazon S3) bucket
+ AWS CloudFormation template

**Target architecture**

The SCSP for static code analysis is a DevOps project designed to give security feedback on deliverable code.

![The SCSP performing code analysis in an AWS Region.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/61fe4f99-7dfc-48a8-90e4-a25253cc140d/images/fbc13150-0970-48d6-87bc-84dfaed90d4b.png)

1. In the AWS Management Console, log into the target AWS account. Confirm that you are in the AWS Region where you want to deploy the pipeline.

1. Use the CloudFormation template in the code repository to deploy the SCSP stack. This creates a new CodeCommit repository and CodeBuild project.
**Note**
As an alternative deployment option, you can use an existing CodeCommit repo by providing the Amazon Resource Name (ARN) of the repository as a parameter during stack deployment.

1. Clone the repository to your local workstation, and then add any files to their respective folders in the cloned repository.

1. Use Git to add, commit, and push the files to the CodeCommit repository.

1. Pushing to the CodeCommit repository initiates a CodeBuild job. The CodeBuild project uses the security tools to scan the code deliverables.

1. Review the output of the pipeline. Security tools that found error-level issues will result in failed actions in the pipeline. Fix these errors or suppress them as false positives. Review details of the tool output in the **Action details** in CodePipeline or in the pipeline’s S3 bucket.

## Tools
<a name="deploy-a-pipeline-that-simultaneously-detects-security-issues-in-multiple-code-deliverables-tools"></a>

**AWS services**
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and Regions.
+ [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) is a fully managed build service that helps you compile source code, run unit tests, and produce artifacts that are ready to deploy.
+ [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) is a version control service that helps you privately store and manage Git repositories, without needing to manage your own source control system.

**Other tools**

For a complete list of tools that SCSP uses to scan code deliverables, see the [SCSP readme](https://github.com/awslabs/simple-code-scanning-pipeline/blob/main/README.md) in GitHub.

**Code repository**

The code for this pattern is available in the [Simple Code Scanning Pipeline (SCSP)](https://github.com/awslabs/simple-code-scanning-pipeline) repository in GitHub.

## Epics
<a name="deploy-a-pipeline-that-simultaneously-detects-security-issues-in-multiple-code-deliverables-epics"></a>

### Deploy the SCSP
<a name="deploy-the-scsp"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the CloudFormation stack. | 1. Sign in to the [AWS Management Console](https://console.aws.amazon.com/).<br />2. In the console, confirm that you're in the target Region where you want to deploy the solution. For more information, see [Choosing a Region](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/select-region.html).<br />3. Choose the following link. This opens the Quick create stack wizard in CloudFormation.<br />[https://console.aws.amazon.com/cloudformation/home?\#/stacks/create/review?templateURL=https://proservetools.s3.amazonaws.com/cft/scsp-pipeline-stack.template.json&stackName=SimpleCodeScanPipeline](https://console.aws.amazon.com/cloudformation/home?#/stacks/create/review?templateURL=https://proservetools.s3.amazonaws.com/cft/scsp-pipeline-stack.template.json&stackName=SimpleCodeScanPipeline)<br />4. On the **Quick create stack** wizard, review the parameter settings for your stack and make any modifications as needed for your use case.<br />5. Select **I acknowledge that AWS CloudFormation might create IAM resources**, and then choose **Create stack**.This creates a CodeCommit repository, a CodePipeline pipeline, several CodeBuild job definitions, and an S3 bucket. Build runs and scanning results are copied into this bucket. After the CloudFormation stack has been completely deployed, SCSP is ready to use. | AWS DevOps, AWS administrator |

### Use the pipeline
<a name="use-the-pipeline"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Examine the results of the scan. | 1. In the [Amazon S3 console](https://console.aws.amazon.com/s3/home), in **Buckets**, choose the **simplecodescanpipeline-deleteresourcespipelinereso** bucket.<br />2. Choose the **scan\_results** directory, and then choose the folder with the most recent scan date stamp.<br />3. Review the log files in this folder to review any issues detected by the security tools used in the pipeline. Security tools that found error-level issues will result in `failed` actions in the pipeline. These need to be fixed or suppressed if they are false positives.You can also view details of the tool output (for both passing and failing scans) in the CodePipeline console, in the **Action details** section. | App developer, AWS DevOps |

## Troubleshooting
<a name="deploy-a-pipeline-that-simultaneously-detects-security-issues-in-multiple-code-deliverables-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| HashiCorp Terraform or AWS CloudFormation files aren’t being scanned. | Make sure that Terraform (.tf) and CloudFormation (.yml, .yaml, or .json) files are placed in the appropriate folders in the cloned CodeCommit repository. |
| The `git clone` command is failing. | Make sure that you have installed `git-remote-codecommit` and that your CLI has access to AWS credentials that have permissions to read the CodeCommit repository. |
| A concurrency error, such as `Project-level concurrent build limit cannot exceed the account-level concurrent build limit of 1`. | Rerun the pipeline by choosing the **Release Change** button in the [CodePipeline console](https://console.aws.amazon.com/codesuite/codepipeline/home). This is a known issue that seems to be most common during the first few times that the pipeline runs. |

## Related resources
<a name="deploy-a-pipeline-that-simultaneously-detects-security-issues-in-multiple-code-deliverables-resources"></a>

[Provide feedback](https://github.com/awslabs/simple-code-scanning-pipeline/issues) on the SCSP project.

## Additional information
<a name="deploy-a-pipeline-that-simultaneously-detects-security-issues-in-multiple-code-deliverables-additional"></a>

**FAQ**

*Is the SCSP project the same as Automated Security Helper (ASH)?*

No. Use ASH when you want a CLI tool that runs code-scanning tools by using containers. [Automated Security Helper (ASH)](https://github.com/awslabs/automated-security-helper) is a tool that is designed to reduce the probability of a security violation in new code, infrastructure, or IAM resource configuration. ASH is a command-line utility that can be run locally. Local use requires a container environment be installed and operational on the system.

Use SCSP when you want an easier setup pipeline than ASH. SCSP requires no local installations. SCSP is designed to run checks individually in a pipeline and display results by tool. SCSP also avoids a lot of the overhead with setting up Docker, and it is operating system (OS) agnostic.

*Is SCSP just for security teams?*

No, anyone can deploy the pipeline to determine which parts of their code are failing security checks. For example, non-security users can use SCSP to check their code before reviewing with their security teams.

*Can I use SCSP if I’m working with another type of repository, such as GitLab, GitHub, or Bitbucket?*

You can configure a local git repository to point to two different remote repositories. For example, you could clone an existing GitLab repository, create a SCSP instance (specifying CloudFormation, Terraform, and AWS Config Rules Development Kit (AWS RDK) folders, if needed), and then use `git remote add upstream <SCSPGitLink>` to point the local repository at the SCSP CodeCommit repository as well. This allows for code changes to be sent to SCSP first, validated, then, after any additional updates are made to address findings, pushed to the GitLab, GitHub, or Bitbucket repository. For more information about multiple remotes, see [Push commits to an additional Git repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-mirror-repo-pushes.html) (AWS blog post).

**Note**
Be careful of drift, such as avoid making changes through web interfaces.

**Contributing and adding your own actions**

SCSP setup is maintained as a GitHub project, which contains the source code for the SCSP AWS Cloud Development Kit (AWS CDK) application. To add additional checks to the pipeline, the AWS CDK application needs to be updated and then synthesized or deployed into the target AWS account where the pipeline will run. To do this, start by cloning the SCSP [GitHub project](https://github.com/awslabs/simple-code-scanning-pipeline), and then find the stack definition file in the `lib` folder.

If there's an additional check you would like to add, the `StandardizedCodeBuildProject` class in the AWS CDK code makes it very straightforward to add actions. Provide the name, description, and `install` or `build` commands. AWS CDK creates the CodeBuild project by using sensible default values. In addition to creating the build project, you need to add it to the CodePipeline actions in the build stage. When designing a new check, the action should `FAIL` if the scanning tool detects problems or fails to run. The action should `PASS` if the scanning tool doesn't detect any problems. For an example of configuring a tool, review the code for the `Bandit` action.

For more information about expected input and outputs, see the [repository documentation](https://github.com/awslabs/simple-code-scanning-pipeline/blob/main/README.md).

If you add custom actions, you need to deploy SCSP by using `cdk deploy` or `cdk synth + CloudFormation deploy`. This is because the **Quick create stack** CloudFormation template is maintained by the repo owners.
