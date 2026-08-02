---
source_url: https://docs.aws.amazon.com/solutions/latest/guidance-for-multi-omics-and-multi-modal-data-integration-and-analysis-on-aws/uninstall-this-solution.html
---

# Uninstall this guidance
<a name="uninstall-this-solution"></a>

 You can uninstall Guidance for Multi-Omics and Multi-Modal Data Integration and Analysis on AWS using the AWS Management Console, the AWS Command Line Interface (AWS CLI), or manually.

**Note**
Uninstalling this guidance deletes the Amazon Simple Storage Service (Amazon S3) buckets and the data in those buckets; AWS CodeCommit repositories and the code in them; the Quick dataset; AWS CodeCommit repositories and the code in them; the AWS Glue jobs, crawlers, triggers, and data; and the Amazon SageMaker AI notebook instance.

## Using the AWS Management console
<a name="using-the-aws-management-console"></a>

1.  Sign in to the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/home?).

1.  Select your installation stack that was launched first and typically has a name ending in `-Setup`. All other guidance stacks will be deleted automatically.

1.  Choose **Delete**.

## Using AWS CLI
<a name="using-aws-cli"></a>

 Determine whether AWS CLI is available in your environment. For installation instructions, see [What Is the AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) in the *AWS CLI User Guide*. After confirming the AWS CLI is available, run the following command.

```
$ aws cloudformation delete-stack --stack-name {{<installation-stack-name>}}
```

### Uninstall manually
<a name="uninstall-manually"></a>

 To manually uninstall this solution, you must delete the related AWS CloudFormation stacks using the following procedure, in the specified order.

1.  Delete all {{<project-name>}}`-*bucket` Amazon S3 bucket contents.

1.  Delete the {{<project-name>}}`-Quicksight` stack.
**Important**
Wait for deletion to complete successfully before proceeding.

1.  Delete the {{<project-name>}}`-Imaging` stack.
**Important**
Wait for deletion to complete successfully before proceeding.

1.  Delete the {{<project-name>}}`-Omics` stack.
**Important**
Wait for deletion to complete successfully before proceeding. If Omics stack deletion fails, manually delete the {{variants}}, {{annotation}} and {{reference}} stores using the Amazon Omics console or API, followed by a re-attempt to delete the Omics stack.

1. Delete the {{<project-name>}}`-Genomics` stack.
**Important**
Wait for deletion to complete successfully before proceeding.

1.  Delete the {{<project-name>}}`-Pipeline` stack.
**Important**
Wait for deletion to complete successfully before proceeding.

1.  Delete the {{<project-name>}}`-LandingZone` stack.
**Important**
Wait for deletion to complete successfully before proceeding.

1.  Delete the installation stack.

1.  Delete the {{<project-name>}} AWS CodeCommit repository.

1.  Delete the {{<project-name>}}`-Pipe` AWS CodeCommit repository.

1.  [Cancel your Quick subscription](https://docs.aws.amazon.com/quicksight/latest/user/closing-account.html).
