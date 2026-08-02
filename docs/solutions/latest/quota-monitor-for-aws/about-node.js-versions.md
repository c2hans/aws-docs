---
source_url: https://docs.aws.amazon.com/solutions/latest/quota-monitor-for-aws/about-node.js-versions.html
---

# About Node.js versions
<a name="about-node.js-versions"></a>

Quota Monitor for AWS version 5.3.0 and earlier versions use the Node.js 8.10 runtime, which reached end-of-life on December 31, 2019. Lambda now blocks both the create operation and the `update` operation. For more information, refer to [Runtime Support Policy](https://docs.aws.amazon.com/lambda/latest/dg/runtime-support-policy.html) in the *AWS Lambda Developer Guide*. To continue using this solution with the latest features and improvements, update the stack as described in [Update the solution](update-the-solution.md).
