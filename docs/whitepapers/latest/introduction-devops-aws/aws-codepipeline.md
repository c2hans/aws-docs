---
source_url: https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/aws-codepipeline.html
---

# AWS CodePipeline
<a name="aws-codepipeline"></a>

 [AWS CodePipeline](https://aws.amazon.com/codepipeline) is a continuous delivery service that you can use to model, visualize, and automate the steps required to release your software. With AWS CodePipeline, you model the full release process for building your code, deploying to pre-production environments, testing your application, and releasing it to production. AWS CodePipeline then builds, tests, and deploys your application according to the defined workflow every time there is a code change. You can integrate partner tools and your own custom tools into any stage of the release process to form an end-to-end continuous delivery solution.

AWS CodePipeline has several benefits that align with the DevOps principle of continuous deployment:
+ **Rapid delivery** — AWS CodePipeline automates your software release process, allowing you to rapidly release new features to your users. With CodePipeline, you can quickly iterate on feedback and get new features to your users faster.
+ **Improved quality** — By automating your build, test, and release processes, AWS CodePipeline enables you to increase the speed and quality of your software updates by running all new changes through a consistent set of quality checks.
+ **Easy to integrate** — AWS CodePipeline can easily be extended to adapt to your specific needs. You can use the pre-built plugins or your own custom plugins in any step of your release process. For example, you can pull your source code from GitHub, use your on-premises Jenkins build server, run load tests using a third-party service, or pass on deployment information to your custom operations dashboard.
+ **Configurable workflow** — AWS CodePipeline enables you to model the different stages of your software release process using the console interface, the AWS CLI, [CloudFormation](https://aws.amazon.com/cloudformation), or the AWS SDKs. You can easily specify the tests to run and customize the steps to deploy your application and its dependencies.
