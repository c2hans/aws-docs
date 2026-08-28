---
source_url: https://docs.aws.amazon.com/data-exchange/latest/userguide/revoking-revisions.html
---

# Revoking access to revisions in AWS Data Exchange
<a name="revoking-revisions"></a>

As a provider of data products in AWS Data Exchange, you can revoke subscriber access to a specific revision at any time. This action is typically done by providers for compliance reasons. Revoking a revision doesn't delete the underlying assets. After you have revoked the revision, all subscribers receive an Amazon EventBridge (formerly known as CloudWatch Events) notification that the revision has been revoked. Subscribers can then view the reason for the revoked revision on the AWS Data Exchange console. Subscribers can’t export or query the data within a revoked revision.

To be able to revoke revisions, providers who manage their own IAM policies must add `dataexchange:RevokeRevision` as a new action. Providers who use the [managed policies for AWS Data Exchange](security-iam-awsmanpol.md) don't need to make any changes.

After a revision is revoked, you can delete the assets of the revision by using the console or the AWS Data Exchange `DeleteAsset` API operation.

**Topics**
+ [Revoking access to an AWS Data Exchange asset revision (AWS CLI)](revoke-rev-sdk.md)
+ [Revoking access to a single AWS Data Exchange asset revision as a provider (console)](revoke-rev-single.md)
+ [Revoking multiple AWS Data Exchange asset revisions as a provider (console)](revoke-rev-multi.md)
+ [Editing an AWS Data Exchange asset revocation reason as a provider (console)](edit-revoked-rev.md)
+ [Viewing revoked revisions as a subscriber (console)](view-revoked-rev.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
