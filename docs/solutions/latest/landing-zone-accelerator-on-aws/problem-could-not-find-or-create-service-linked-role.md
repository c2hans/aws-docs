---
source_url: https://docs.aws.amazon.com/solutions/latest/landing-zone-accelerator-on-aws/problem-could-not-find-or-create-service-linked-role.html
---

# Problem: Couldn’t find or create service linked role
<a name="problem-could-not-find-or-create-service-linked-role"></a>

We updated this solution to make service linked role creation idempotent. When you create a new resource, the solution checks for existing service linked role. If no service linked role exists, the solution creates one. During cleanup, the `AWS::IAM::ServiceLinkedRole` resource might have been removed successfully, which can cause issues.

Example event from CodeBuild:

 `AWSAccelerator-OrganizationsStack-<account>-<region> | …​ | DELETE_IN_PROGRESS | AWS::IAM::ServiceLinkedRole | FirewallManagerServiceLinkedRole`

 `AWSAccelerator-OrganizationsStack-<account>-<region> | …​ | DELETE_COMPLETE | AWS::IAM::ServiceLinkedRole | FirewallManagerServiceLinkedRole`

## Resolution
<a name="resolution-8"></a>

 [Manually](https://docs.aws.amazon.com/codepipeline/latest/userguide/pipelines-rerun-manually.html) release the pipeline again. The service linked role will run on every pipeline. If no service linked role exists, the solution creates a new one in the account.
