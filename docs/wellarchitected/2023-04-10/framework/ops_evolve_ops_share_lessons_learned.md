---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/ops_evolve_ops_share_lessons_learned.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# OPS11-BP08 Document and share lessons learned
<a name="ops_evolve_ops_share_lessons_learned"></a>

 Document and share lessons learned from the operations activities so that you can use them internally and across teams.

 You should share what your teams learn to increase the benefit across your organization. You will want to share information and resources to prevent avoidable errors and ease development efforts. This will allow you to focus on delivering desired features.

 Use AWS Identity and Access Management (IAM) to define permissions permitting controlled access to the resources you wish to share within and across accounts. You should then use version-controlled AWS CodeCommit repositories to share application libraries, scripted procedures, procedure documentation, and other system documentation. Share your compute standards by sharing access to your AMIs and by authorizing the use of your Lambda functions across accounts. You should also share your infrastructure standards as AWS CloudFormation templates.

 Through the AWS APIs and SDKs, you can integrate external and third-party tools and repositories (for example, GitHub, BitBucket, and SourceForge). When sharing what you have learned and developed, be careful to structure permissions to ensure the integrity of shared repositories.

 **Common anti-patterns:**
+  You suffered an extended outage because of your use of a buggy library commonly used in your organization. You have since migrated to a reliable library. The other teams in your organization do not know they are at risk. Were you to document and share your experience with this library, they would be aware of the risk.
+  You have identified an edge case in an internally shared microservice that causes sessions to drop. You have updated your calls to the service to avoid this edge case. The other teams in your organization do not know that they are at risk. Were you to document and share your experience with this library, they would be aware of the risk.
+  You have found a way to significantly reduce the CPU utilization requirements for one of your microservices. You do not know if any other teams could take advantage of this technique. Were you to document and share your experience with this library, they would have the opportunity to do so.

 **Benefits of establishing this best practice:** Share lessons learned to support improvement and to maximize the benefits of experience.

 **Level of risk exposed if this best practice is not established:** Low

## Implementation guidance
<a name="implementation-guidance"></a>
+  Document and share lessons learned: Have procedures to document the lessons learned from the running of operations activities and retrospective analysis so that they can be used by other teams.
  +  Share learnings: Have procedures to share lessons learned and associated artifacts across teams. For example, share updated procedures, guidance, governance, and best practices through an accessible wiki. Share scripts, code, and libraries through a common repository.
    +  [Delegating access to your AWS environment](https://www.youtube.com/watch?v=0zJuULHFS6A&t=849s)
    +  [Share an AWS CodeCommit repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-share-repository.html)
    +  [Easy authorization of AWS Lambda functions](https://aws.amazon.com/blogs/compute/easy-authorization-of-aws-lambda-functions/)
    +  [Sharing an AMI with specific AWS Accounts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-explicit.html)
    +  [Speed template sharing with an AWS CloudFormation designer URL](https://aws.amazon.com/blogs/devops/speed-template-sharing-with-an-aws-cloudformation-designer-url/)
    +  [Using AWS Lambda with Amazon SNS](https://docs.aws.amazon.com/lambda/latest/dg/with-sns-example.html)

## Resources
<a name="resources"></a>

 **Related documents:**
+  [Easy authorization of AWS Lambda functions](https://aws.amazon.com/blogs/compute/easy-authorization-of-aws-lambda-functions/)
+  [Share an AWS CodeCommit repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-share-repository.html)
+  [Sharing an AMI with specific AWS Accounts](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/sharingamis-explicit.html)
+  [Speed template sharing with an AWS CloudFormation designer URL](https://aws.amazon.com/blogs/devops/speed-template-sharing-with-an-aws-cloudformation-designer-url/)
+  [Using AWS Lambda with Amazon SNS](https://docs.aws.amazon.com/lambda/latest/dg/with-sns-example.html)

 **Related videos:**
+  [Delegating access to your AWS environment](https://www.youtube.com/watch?v=0zJuULHFS6A&t=849s)
