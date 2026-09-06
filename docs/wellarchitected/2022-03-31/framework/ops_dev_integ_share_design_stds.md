---
source_url: https://docs.aws.amazon.com/wellarchitected/2022-03-31/framework/ops_dev_integ_share_design_stds.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS05-BP06 Share design standards
<a name="ops_dev_integ_share_design_stds"></a>

 Share best practices across teams to increase awareness and maximize the benefits of development efforts.

 On AWS, application, compute, infrastructure, and operations can be defined and managed using code methodologies. This allows for easy release, sharing, and adoption.

 Many AWS services and resources are designed to be shared across accounts, enabling you to share created assets and learnings across your teams. For example, you can share [CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/cross-account.html) repositories, [Lambda](https://docs.aws.amazon.com/lambda/latest/dg/lambda-permissions.html) functions, [Amazon S3 buckets](https://aws.amazon.com/premiumsupport/knowledge-center/cross-account-access-s3/), and [AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-explicit.html) to specific accounts.

 When you publish new resources or updates, use Amazon SNS to provide [cross account notifications](https://docs.aws.amazon.com/lambda/latest/dg/with-sns-example.html). Subscribers can use Lambda to get new versions.

 If shared standards are enforced in your organization, it’s critical that mechanisms exist to request additions, changes, and exceptions to standards in support of teams’ activities. Without this option, standards become a constraint on innovation.

 **Common anti-patterns:**
+  You have created your own user authentication mechanism, as have each of the other development teams in your organization. Your users have to maintain a separate set of credentials for each part of the system they want to access.
+  You have created your own user authentication mechanism, as have each of the other development teams in your organization. Your organization is given a new compliance requirement that must be met. Every individual development team must now invest the resources to implement the new requirement.
+  You have created your own screen layout, as have each of the other development teams in your organization. Your users are complaining about the difficulty of navigating the inconsistent interfaces.

 **Benefits of establishing this best practice:** Use shared standards to support the adoption of best practices and to maximizes the benefits of development efforts where standards satisfy requirements for multiple applications or organizations.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>
+  Share design standards: Share existing best practices, design standards, checklists, operating procedures, and guidance and governance requirements across teams to reduce complexity and maximize the benefits from development efforts. Ensure that procedures exist to request changes, additions, and exceptions to design standards to support continual improvement and innovation. Ensure that teams are aware of published content so that they can take advantage of content, and limit rework and wasted effort.
  +  [Delegating access to your AWS environment](https://www.youtube.com/watch?v=0zJuULHFS6A&t=849s)
  +  [Share an AWS CodeCommit repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-share-repository.html)
  +  [Easy authorization of AWS Lambda functions](https://aws.amazon.com/blogs/compute/easy-authorization-of-aws-lambda-functions/)
  +  [Sharing an AMI with specific AWS accounts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-explicit.html)
  +  [Speed template sharing with an AWS CloudFormation designer URL](https://aws.amazon.com/blogs/devops/speed-template-sharing-with-an-aws-cloudformation-designer-url/)
  +  [Using AWS Lambda with Amazon SNS](https://docs.aws.amazon.com/lambda/latest/dg/with-sns-example.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Easy authorization of AWS Lambda functions](https://aws.amazon.com/blogs/compute/easy-authorization-of-aws-lambda-functions/)
+  [Share an AWS CodeCommit repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-share-repository.html)
+  [Sharing an AMI with specific AWS accounts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-explicit.html)
+  [Speed template sharing with an AWS CloudFormation designer URL](https://aws.amazon.com/blogs/devops/speed-template-sharing-with-an-aws-cloudformation-designer-url/)
+  [Using AWS Lambda with Amazon SNS](https://docs.aws.amazon.com/lambda/latest/dg/with-sns-example.html)

 **Related videos:**
+  [Delegating access to your AWS environment](https://www.youtube.com/watch?v=0zJuULHFS6A&t=849s)
