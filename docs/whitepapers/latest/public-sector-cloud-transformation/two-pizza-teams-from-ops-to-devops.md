---
source_url: https://docs.aws.amazon.com/whitepapers/latest/public-sector-cloud-transformation/two-pizza-teams-from-ops-to-devops.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Two pizza teams, from Ops to DevOps
<a name="two-pizza-teams-from-ops-to-devops"></a>

One simple rule for maximizing team effectiveness. Former Amazon CEO Jeff Bezos has this rule: no team meeting should be so large that two pizzas can't feed the whole group. This is, of course, a shorthand method for ensuring that, as is often the case with big groups, no one's ideas get drowned out. Bezos believes that no matter how large your company gets, if you can’t feed a team with two pizzas, that team is too large. The reasoning behind it is quite straightforward. More people = more of everything. More coordination, more bureaucracy, more chaos – basically, everything that slows things down. Individual performance suffers and people become less engaged.

The smaller the team the better the collaboration. Collaboration is very important, as software releases are moving faster than ever. A team’s ability to deliver software can be a differentiating factor for your organization against your competition. Image a situation where a new product feature needs to be released or a bug needs to be fixed. You want this to happen as quickly as possible so you can have a smaller go-to-market timed. You don’t want the transformation to be a slow-moving process.

Communication between the teams is important as we move toward the shared responsibility model and start moving out of the siloed development approach. This brings the concept of ownership in the team and shifts their perspective to look at this as an end-to-end project. Your team should not think about your production environments as black boxes where they have no visibility.

Cultural transformation is important, as you may be building a common DevOps team. Another approach is that you have one or more DevOps-focused members on your team. Both of these approaches introduce shared responsibility in to the team.

DevOps is the combination of cultural, engineering practices and patterns, and tools that increase an organization's ability to deliver applications and services at high velocity and better quality. Over time, several essential practices have emerged when adopting DevOps: Continuous Integration, Continuous Delivery, Infrastructure as Code, and Monitoring and Logging.

This highlights AWS capabilities that help you accelerate your DevOps journey, and how AWS services can help remove the undifferentiated heavy lifting associated with DevOps adaptation. AWS also highlights how to build a continuous integration and delivery capability without managing servers or build nodes, and how to leverage Infrastructure as Code to provision and manage your cloud resources in a consistent and repeatable manner.
+  **Continuous Integration** is a software development practice where developers regularly merge their code changes into a central repository, after which automated builds and tests are run.
+  **Continuous Delivery** is a software development practice where code changes are automatically built, tested, and prepared for a release to production.
+  **Infrastructure as Code** is a practice in which infrastructure is provisioned and managed using code and software development techniques, such as version control, and continuous integration.
+  **Monitoring and Logging** enables organizations to see how application and infrastructure performance impacts the experience of their product’s end user.
+  **Communication and Collaboration** practices are established to bring the teams closer and by building workflows and distributing the responsibilities for DevOps.
+  **Security** should be a cross cutting concern. Your continuous integration and continuous delivery (CI/CD) pipelines and related services should be safeguarded and permissions of least privileges should be set up.

To make the journey to the cloud smooth, efficient, and effective, technology companies should embrace DevOps principles and practices. These principles are embedded in the AWS platform. They form the cornerstone of numerous AWS services, especially those in the deployment and monitoring offerings.
+  Begin by defining your infrastructure as code using the service AWS Cloud Formation or [AWS Cloud Development Kit (AWS CDK)](https://aws.amazon.com/cdk/).
+  Next, define the way in which your applications are going to use continuous deployment with the help of services like [AWS CodeBuild](https://aws.amazon.com/codebuild/), [AWS CodeDeploy](https://aws.amazon.com/codedeploy/), [AWS CodePipeline](https://aws.amazon.com/codepipeline/), and [AWS CodeCommit](https://aws.amazon.com/codecommit/).
+  At the application level, use containers like [AWS Elastic Beanstalk](https://aws.amazon.com/elasticbeanstalk/), [Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc&ecs-blogs.sort-by=item.additionalFields.createdDate&ecs-blogs.sort-order=desc), or [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/?whats-new-cards.sort-by=item.additionalFields.postDateTime&whats-new-cards.sort-order=desc&eks-blogs.sort-by=item.additionalFields.createdDate&eks-blogs.sort-order=desc), and [AWS OpsWorks](https://aws.amazon.com/opsworks/) to simplify the configuration of common architectures. Using these services also makes it easy to include other important services like Auto Scaling and Elastic Load Balancing.
+  Finally, use the Dev Ops strategy of monitoring such as [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), and solid security practices such as [IAM](https://aws.amazon.com/iam/). With AWS as your partner, your DevOps principles bring agility to your business and IT organization and accelerate your journey to the cloud.

   For more information, see the [https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/introduction-devops-aws.pdf#introduction](https://docs.aws.amazon.com/whitepapers/latest/introduction-devops-aws/introduction-devops-aws.pdf#introduction) whitepaper.
