---
source_url: https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/how-to-tag-associated-repository-view-cli.html
---

As of November 7, 2025, you can't create new repository associations in Amazon CodeGuru Reviewer. To learn about services with capabilities similar to CodeGuru Reviewer, see [Amazon CodeGuru Reviewer availability change](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/codeguru-reviewer-availability-change.html).

# View tags for a CodeGuru Reviewer associated repository (AWS CLI)
<a name="how-to-tag-associated-repository-view-cli"></a>

Follow these steps to use the AWS CLI to view the AWS tags for an associated repository. If no tags have been added, the returned tags list in the response is empty (`"Tags": {}`).

**To view tags for an associated repository**

1. Make sure that you have configured the AWS CLI with the AWS Region in which you want to create your code reviews. To verify the Region, run the following command at the command line or terminal and review the information for the default name.

   ```
   aws configure
   ```

   The default Region name must match the AWS Region for the repository in CodeCommit.

1. Run the **describe-repository-association** command and specify the Amazon Resource Name (ARN) of the associated repository.

   ```
   aws codeguru-reviewer describe-repository-association /
     --association-arn arn:aws:codeguru-reviewer:{{us-west-2}}:{{123456789012}}:association:{{repository-association-uuid}}
   ```

1. If successful, this command outputs a [`RepositoryAssociation`](https://docs.aws.amazon.com/codeguru/latest/reviewer-api/API_RepositoryAssociation.html) object that includes an array with its tags.

   ```
   {
       "RepositoryAssociation": {
           "AssociationId": "repository-association-uuid",
           "Name": "{{my-codecommit-repo}}",
           "LastUpdatedTimeStamp": 1595634764.029,
           "ProviderType": "CodeCommit",
           "CreatedTimeStamp": 1595634764.029,
           "Owner": "123456789012",
           "State": "Associating",
           "StateReason": "Pending Repository Association",
           "AssociationArn": "arn:aws:codeguru-reviewer:us-west-2:123456789012:association:repository-association-uuid",
       },
       "Tags": {
           "owner": "admin",
           "status": "beta",
           "value-1": "key-1",
       }
   }
   ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon CodeGuru. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query codeguru` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
