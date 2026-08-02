---
source_url: https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/implementing-continuous-integration-and-continuous-delivery.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Implementing continuous integration and continuous delivery
<a name="implementing-continuous-integration-and-continuous-delivery"></a>

 This section discusses the ways in which you can begin to implement a CI/CD model in your organization. This whitepaper doesn’t discuss how an organization with a mature DevOps and cloud transformation model builds and uses a CI/CD pipeline. To help you on your DevOps journey, AWS has a number of [certified DevOps Partners](https://aws.amazon.com/devops/partner-solutions/) who can provide resources and tooling. For more information on preparing for a move to the AWS Cloud, refer to the [Building a Cloud Operating Model](https://d1.awsstatic.com/whitepapers/building-a-cloud-operating-model.pdf).

## A pathway to continuous integration/continuous delivery
<a name="a-pathway-to-continuous-integrationcontinuous-delivery"></a>

CI/CD can be pictured as a workflow or pipeline (refer to the following figure), where new code is submitted on one end, tested over a series of stages (source, build, staging, and production), and then published as production-ready code. If your organization is new to CI/CD it can approach this pipeline in an iterative fashion. This means that you should start small, and iterate at each stage so that you can understand and develop your code in a way that will help your organization grow.

![Block diagram showing a CI/CD pipeline.](http://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/images/ci-cd-pipeline.png)

 Each stage of the CI/CD pipeline is structured as a logical unit in the delivery process. In addition, each stage acts as a gate that vets a certain aspect of the code. As the code progresses through the pipeline, the assumption is that the quality of the code is higher in the later stages because more aspects of it continue to be verified. Problems uncovered in an early stage stop the code from progressing through the pipeline. Results from the tests are immediately sent to the team, and all further builds and releases are stopped if software does not pass the stage.

 These stages are suggestions. You can adapt the stages based on your business need. Some stages can be repeated for multiple types of testing, security, and performance. Depending on the complexity of your project and the structure of your teams, some stages can be repeated several times at different levels. For example, the end product of one team can become a dependency in the project of the next team. This means that the first team’s end product is subsequently staged as an artifact in the next team’s project.

 The presence of a CI/CD pipeline will have a large impact on maturing the capabilities of your organization. The organization should start with small steps and not try to build a fully mature pipeline, with multiple environments, many testing phases, and automation in all stages at the start. Keep in mind that even organizations that have highly mature CI/CD environments still need to continuously improve their pipelines.

 Building a CI/CD-enabled organization is a journey, and there are many destinations along the way. The next section discusses a possible pathway that your organization could take, starting with continuous integration through the levels of continuous delivery.

### Continuous integration
<a name="continuous-integration-1"></a>

![Diagram showing continuous integration, source and build.](http://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/images/continuous-integration.png)

 The first phase in the CI/CD journey is to develop maturity in continuous integration. You should make sure that all of the developers regularly commit their code to a central repository (such as one hosted in CodeCatalyst, CodeCommit or GitHub) and merge all changes to a release branch for the application. No developer should be holding code in isolation. If a feature branch is needed for a certain period of time, it should be kept up to date by merging from upstream as often as possible. Frequent commits and merges with complete units of work are recommended for the team to develop discipline and are encouraged by the process. A developer who merges code early and often, will likely have fewer integration issues down the road.

 You should also encourage developers to create unit tests as early as possible for their applications and to run these tests before pushing the code to the central repository. Errors caught early in the software development process are the cheapest and easiest to fix.

 When the code is pushed to a branch in a source code repository, a workflow engine monitoring that branch will send a command to a builder tool to build the code and run the unit tests in a controlled environment. The build process should be sized appropriately to handle all activities, including pushes and tests that might happen during the commit stage, for fast feedback. Other quality checks, such as unit test coverage, style check, and static analysis, can happen at this stage as well. Finally, the builder tool creates one or more binary builds and other artifacts, like images, stylesheets, and documents for the application.

### Continuous delivery: creating a staging environment
<a name="continuous-delivery-creating-a-staging-environment"></a>

![Diagram showing continuous delivery, staging.](http://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/images/continuous-delivery.png)

 Continuous delivery (CD) is the next phase and entails deploying the application code in a staging environment, which is a replica of the production stack, and running more functional tests. The staging environment could be a static environment premade for testing, or you could provision and configure a dynamic environment with committed infrastructure and configuration code for testing and deploying the application code.

### Continuous delivery: creating a production environment
<a name="continuous-delivery-creating-a-production-environment"></a>

![Diagram showing continuous delivery, staging.](http://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/images/continuous-delivery-production.png)

 In the deployment/delivery pipeline sequence, after the staging environment, is the production environment, which is also built using infrastructure as code (IaC).

### Continuous deployment
<a name="continuous-deployment"></a>

![Diagram showing Continuous deployment.](http://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/images/continuous-deployment.png)

 The final phase in the CI/CD deployment pipeline is continuous deployment, which may include full automation of the entire software release process including deployment to the production environment. In a fully mature CI/CD environment, the path to the production environment is fully automated, which allows code to be deployed with high confidence.

### Maturity and beyond
<a name="maturity-and-beyond"></a>

 As your organization matures, it will continue to develop the CI/CD model to include more of the following improvements:
+  More staging environments for specific performance, compliance, security, and user interface (UI) tests
+  Unit tests of infrastructure and configuration code along with the application code
+  Integration with other systems and processes such as code review, issue tracking, and event notification
+  Integration with database schema migration (if applicable)
+  Additional steps for auditing and business approval

 Even the most mature organizations that have complex multi-environment CI/CD pipelines continue to look for improvements. DevOps is a journey, not a destination. Feedback about the pipeline is continuously collected and improvements in speed, scale, security, and reliability are achieved as a collaboration between the different parts of the development teams. Having a single place to collaborate across the teams for example, using Amazon CodeCatalyst, allows the teams to have visibility to build and deliver software products with confidence.

## Teams
<a name="teams"></a>

 AWS recommends organizing three developer teams for implementing a CI/CD environment: an application team, an infrastructure team, and a tools team (refer to the following figure). This organization represents a set of best practices that have been developed and applied in fast-moving startups, large enterprise organizations, and in Amazon itself.

![Diagram representing application, infrastructure, and tools teams](http://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/images/teams.jpeg)

### Application team
<a name="application-team"></a>

 The application team creates the application. Application developers own the backlog, stories, and unit tests, and they develop features based on a specified application target. This team’s organizational goal is to minimize the time these developers spend on non-core application tasks. Amazon CodeCatalyst allows the application team to maintain and manage issue tracking within the tool for collaboration.

 In addition to having functional programming skills in the application language, the application team should have platform skills and an understanding of system configuration. This will enable them to focus solely on developing features and hardening the application.

### Infrastructure team
<a name="infrastructure-team"></a>

 The infrastructure team writes the code that both creates and configures the infrastructure needed to run the application. The infrastructure team is responsible for specifying what resources are needed, and it works closely with the application team.

 The team should have skills in infrastructure provisioning methods, such as AWS CDK, AWS CloudFormation or HashiCorp Terraform. The team may also need to develop configuration automation skills with tools such as Ansible, and Puppet.

### Tools team
<a name="tools-team"></a>

 The tools team builds and manages the CI/CD pipeline. They are responsible for the infrastructure and tools that make up the pipeline. They create a tool that is used by the application and infrastructure teams in the organization. The organization needs to continuously mature its tools team, so that the tools team stays one step ahead of the maturing application and infrastructure teams.

 The tools team must be skilled in building and integrating all parts of the CI/CD pipeline. This includes building source control repositories, workflow engines, build environments, testing frameworks, and artifact repositories. This team may choose to implement a tool such as Amazon CodeCatalyst, and AWS CodePipeline as well as Jenkins, GitHub, or other similar tools. Some organizations might call this a DevOps team, but AWS discourages this and instead encourages thinking of DevOps as the sum of the people, processes, and tools in software delivery.
