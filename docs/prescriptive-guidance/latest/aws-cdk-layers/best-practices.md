---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-cdk-layers/best-practices.html
---

# Best practices
<a name="best-practices"></a>

## L1 constructs
<a name="l1-constructs.947fecc2-63e3-5bec-bb45-a729e95f2e2a"></a>
+ You can't always avoid using L1 constructs directly, but you should avoid it whenever possible. If a specific L2 construct doesn't support your edge case, you can explore these two options instead of using the L1 construct directly:
+ **Access **`defaultChild`:** **If the CloudFormation property you need isn't available in an L2 construct, you can access the underlying L1 construct by using `L2Construct.node.defaultChild`. You can update any public properties of the L1 construct by accessing them through this property instead of going through the trouble of creating the L1 construct yourself.
+ **Use property overrides**: What if the property that you want to update isn't public? The ultimate escape hatch that allows the AWS CDK to do anything that a CloudFormation template can do is to use a method that's available in every L1 construct: [addPropertyOverride](https://docs.aws.amazon.com/cdk/v2/guide/cfn_layer.html). You can manipulate your stack at the CloudFormation template level by passing the CloudFormation property name and value directly to this method.

## L2 constructs
<a name="l2-constructs.462b1519-071c-5a93-912a-5d1d851173fe"></a>
+ Remember to take advantage of the helper methods that L2 constructs often offer. With layer 2, you don't have to pass every property upon instantiation. L2 helper methods can make resource provisioning exponentially more convenient, especially when conditional logic is needed. One of the most convenient helper methods is derived from the [Grant](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_iam.Grant.html) class. This class isn't used directly, but many L2 constructs use it to provide helper methods that make permissions much easier to implement. For example, if you want to give permission to an L2 Lambda function to access an L2 S3 bucket, you could call `s3Bucket.grantReadWrite(lambdaFunction)` instead of creating a new role and policy.

## L3 constructs
<a name="l3-constructs.46781bf3-c719-5c1e-a8ba-d81a31d3685e"></a>
+ Although L3 constructs can be very convenient when you want to make your stacks more reusable and customizable, we recommend that you use them carefully. Consider which type of L3 construct you need or whether you need an L3 construct at all:
  + If you aren't directly interacting with AWS resources, it's often more appropriate to make a helper class instead of extending the `Construct` class. This is because the `Construct` class performs many actions by default that are only needed if you're directly interacting with AWS resources. So if you don't need those actions performed, it's more efficient to avoid them.
  + If you determine that creating a new L3 construct is appropriate, in most cases you will want to extend the `Construct`class directly. Extend other L2 constructs only when you want to update the default properties of the construct. If other L2 constructs or custom logic are involved, extend `Construct` directly and instantiate all resources within the constructor.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
