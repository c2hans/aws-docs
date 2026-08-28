---
source_url: https://docs.aws.amazon.com/whitepapers/latest/build-static-websites-aws/integration-with-your-continuous-deployment-process.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Integration with your continuous deployment process
<a name="integration-with-your-continuous-deployment-process"></a>

 Your website content should be managed using version control software (such as Git, Subversion, or Microsoft Team Foundation Server) to make it possible to revert to older versions of your files. (If version control software is not in use at your organization, one alternative approach is to look at the Amazon S3 object versioning feature for versioning your critical files. Note that object versioning introduces storage costs for each version, and requires you to programmatically manage the different versions. For more information, see [Using versioning in S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/dev/Versioning.html).)

 AWS offers a managed source control service called AWS CodeCommit that makes it easy to host secure and private Git repositories. Regardless of which version control system your team uses, consider tying it to a continuous build/integration tool so that your website automatically updates whenever the content changes.

 For example, if your team is using a Git-based repository for version control, a Git post-**commit hook can notify your continuous integration tool (for example, Jenkins) of any content updates. At that point, your continuous integration tool can perform the actual deployment to synchronize the content with Amazon S3 (using either the AWS CLI or the Amazon S3 API), and notify the user of the deployment status.

![A diagram that shows an example of continuous deployment process.](http://docs.aws.amazon.com/whitepapers/latest/build-static-websites-aws/images/continuous-deployment.png)

 If you don’t want to use version control, then be sure to periodically download your website and back up the snapshot. The AWS CLI lets you download your entire website with a single command:

```
    aws s3 sync s3://bucket /my_local_backup_directory
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
