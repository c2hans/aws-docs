---
source_url: https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/pipelines-for-multiple-teams-branches-and-aws-regions.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Pipelines for multiple teams, branches, and AWS Regions
<a name="pipelines-for-multiple-teams-branches-and-aws-regions"></a>

 For a large project, it’s not uncommon for multiple project teams to work on different components. If multiple teams use a single code repository, it can be mapped so that each team has its own branch. There should also be an integration or release branch for the final merge of the project. If a service-oriented or microservice architecture is used, each team could have its own code repository.

 In the first scenario, if a single pipeline is used it’s possible that one team could affect the other teams’ progress by blocking the pipeline. AWS recommends that you create specific pipelines for team branches and another release pipeline for the final product delivery.

## Pipeline integration with AWS CodeBuild
<a name="pipeline-integration-with-aws-codebuild"></a>

 AWS CodeBuild is designed to enable your organization to build a highly available build process with almost unlimited scale. AWS CodeBuild provides quickstart environments for a number of popular languages plus the ability to run any Docker container that you specify.

 With the advantages of tight integration with AWS CodeCommit, AWS CodePipeline, and AWS CodeDeploy, as well as Git and CodePipeline Lambda actions, the CodeBuild service is highly flexible.

 Software can be built through the inclusion of a buildspec.yml file that identifies each of the build steps, including pre- and post- build actions, or specified actions through the CodeBuild tool.

 You can view detailed history of each build using the CodeBuild dashboard. Events are stored as Amazon CloudWatch Logs log files.

![Screenshot showing CloudWatch Logs log files in AWS CodeBuild](http://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/images/cloudwatch-logs.png)

## Pipeline integration with Jenkins
<a name="pipeline-integration-with-jenkins"></a>

 You can use the Jenkins build tool [to create delivery pipelines](https://www.jenkins.io/doc/book/pipeline/getting-started/). These pipelines use standard jobs that define steps for implementing continuous delivery stages. However, this approach might not be optimal for larger projects because the current state of the pipeline doesn’t persist between Jenkins restarts, implementing manual approval is not straightforward, and tracking the state of a complex pipeline can be complicated.

 Instead, AWS recommends that you implement continuous delivery with Jenkins by using the [AWS Code Pipeline Plugin](https://wiki.jenkins-ci.org/display/JENKINS/AWS+CodePipeline+Plugin). This plugin allows complex workflows to be described using Groovy-like domain-specific language and can be used to orchestrate complex pipelines. The AWS Code Pipeline plugin’s functionality can be enhanced by the use of satellite plugins such as the [Pipeline Stage View Plugin](https://plugins.jenkins.io/aws-codepipeline/), which visualizes the current progress of stages defined in a pipeline, or [Pipeline Multibranch Plugin](https://plugins.jenkins.io/workflow-multibranch/), which groups builds from different branches.

 AWS recommends that you store your pipeline configuration in *Jenkinsfile* and have it checked into a source code repository. This allows for tracking changes to pipeline code and becomes even more important when working with the Pipeline Multibranch Plugin. AWS also recommends that you divide your pipeline into stages. This logically groups the pipeline steps and also enables the Pipeline Stage View Plugin to visualize the current state of the pipeline.

 The following figure shows a sample Jenkins pipeline, with four defined stages visualized by the Pipeline Stage View Plugin.

![Showing Defined stages of Jenkins pipeline visualized by the Pipeline Stage View Plugin](http://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/images/jenkins-pipeline-visual.png)
