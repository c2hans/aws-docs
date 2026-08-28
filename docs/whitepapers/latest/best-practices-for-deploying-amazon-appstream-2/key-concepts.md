---
source_url: https://docs.aws.amazon.com/whitepapers/latest/best-practices-for-deploying-amazon-appstream-2/key-concepts.html
---

# Key concepts
<a name="key-concepts"></a>

 To get the most out of WorkSpaces Applications, be familiar with the following concepts:
+  **Image** — An *image* is a pre-configured instance template*.* An image contains applications that you can stream to your users, and default Windows and application settings to enable your users to get started with their applications quickly. AWS provides base images that you can use to create images that include your own applications. After you create an image, you can't change it. To add other applications, update existing applications, or change image settings, you must create a new image. You can copy your images to other [*AWS Regions*](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/) or share them with other AWS accounts in the same Region.
+  **Image builder** — An *image builder* is a virtual machine that you use to create an image. You can launch and connect to an image builder using the WorkSpaces Applications console. After you connect to an image builder, you can install, add, and test your applications, and then use the image builder to create an image. You can launch new image builders by using private images that you own.
+  **Fleet** — A *fleet* consists of fleet instances (also known as streaming instances) that run the image that you specify. You can set the desired number of streaming instances for your fleet, and configure policies to scale your fleet automatically based on demand. Note that each user requires one instance.
+  **Stack** — A *stack* consists of an associated fleet, user access policies, and storage configurations. You set up a stack to start streaming applications to users.
+  **Streaming instance** — A *streaming instance* (also known as a *fleet instance*) is an [*Amazon Elastic Compute Cloud*](https://aws.amazon.com/ec2/) (Amazon EC2) instance that is made available to a single user for application streaming. After the user’s session completes, the instance is terminated by Amazon EC2.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
