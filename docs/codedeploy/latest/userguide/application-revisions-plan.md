---
source_url: https://docs.aws.amazon.com/codedeploy/latest/userguide/application-revisions-plan.html
---

# Plan a revision for CodeDeploy
<a name="application-revisions-plan"></a>

Good planning makes deploying revisions much easier.

For deployments to an AWS Lambda or an Amazon ECS compute platform, a revision is the same as the AppSpec file. The following information does not apply. For more information, see [Add an application specification file to a revision for CodeDeploy](application-revisions-appspec-file.md)

For deployments to an EC2/On-Premises compute platform, start by creating an empty root directory (folder) on the development machine. This is where you will store the source files (such as text and binary files, executables, packages, and so on) to be deployed to the instances or scripts to be run on the instances.

For example, at the `/tmp/` root folder in Linux, macOS, or Unix or the `c:\temp` root folder in Windows:

```
/tmp/ or c:\temp (root folder)
  |--content (subfolder)
  |    |--myTextFile.txt
  |    |--mySourceFile.rb
  |    |--myExecutableFile.exe
  |    |--myInstallerFile.msi
  |    |--myPackage.rpm
  |    |--myImageFile.png
  |--scripts (subfolder)
  |    |--myShellScript.sh
  |    |--myBatchScript.bat
  |    |--myPowerShellScript.ps1
  |--appspec.yml
```

The root folder should also include an application specification file (AppSpec file), as shown here. For more information, see [Add an application specification file to a revision for CodeDeploy](application-revisions-appspec-file.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CodeDeploy. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codedeploy` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
