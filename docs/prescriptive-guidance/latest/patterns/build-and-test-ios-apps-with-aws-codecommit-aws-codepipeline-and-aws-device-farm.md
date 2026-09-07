---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-and-test-ios-apps-with-aws-codecommit-aws-codepipeline-and-aws-device-farm.html
---

# Build and test iOS apps with AWS CodeCommit, AWS CodePipeline, and AWS Device Farm
<a name="build-and-test-ios-apps-with-aws-codecommit-aws-codepipeline-and-aws-device-farm"></a>

*Abdullahi Olaoye, Amazon Web Services*

## Summary
<a name="build-and-test-ios-apps-with-aws-codecommit-aws-codepipeline-and-aws-device-farm-summary"></a>

This pattern outlines the steps for creating a continuous integration and continuous delivery (CI/CD) pipeline that uses AWS CodePipeline to build and test iOS applications on real devices on AWS. The pattern uses AWS CodeCommit to store the application code, the Jenkins open-source tool to build the iOS application, and AWS Device Farm to test the built application on real devices. These three phases are orchestrated together in a pipeline by using AWS CodePipeline.

This pattern is based on the post [Building and testing iOS and iPadOS apps with AWS DevOps and mobile services](https://aws.amazon.com/blogs/devops/building-and-testing-ios-and-ipados-apps-with-aws-devops-and-mobile-services/) on the AWS DevOps blog. For detailed instructions, see the blog post.

## Prerequisites and limitations
<a name="build-and-test-ios-apps-with-aws-codecommit-aws-codepipeline-and-aws-device-farm-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ An Apple developer account
+ Build server (macOS)
+ [Xcode](https://developer.apple.com/xcode/) version 11.3 (installed and set up on the build server)
+ AWS Command Line Interface (AWS CLI) [installed](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv1.html) and [configured ](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)on the workstation
+ Basic knowledge of [Git](https://git-scm.com/docs)

**Limitations **
+ The application build server must be running macOS.
+ The build server must have a public IP address, so CodePipeline can connect to it remotely to initiate builds.

## Architecture
<a name="build-and-test-ios-apps-with-aws-codecommit-aws-codepipeline-and-aws-device-farm-architecture"></a>

**Source technology stack  **
+ An on-premises iOS application build process that involves using a simulator or manual test on physical devices

**Target technology stack  **
+ An AWS CodeCommit repository for storing application source code
+ A Jenkins server for application builds using Xcode
+ An AWS Device Farm device pool for testing applications on real devices

**Target architecture **

When a user commits changes to the source repository, the pipeline (AWS CodePipeline) fetches the code from the source repository, initiates a Jenkins build, and passes the application code to Jenkins. After the build, the pipeline retrieves the build artifact and starts an AWS Device Farm job to test the application against a device pool.

![CI/CD pipeline uses AWS CodePipeline to build and test iOS applications on real devices.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/06fbd82f-4aed-441c-818c-5f89f56af78e/images/0ae3d7b6-b40c-44ef-9580-8c8266c3d841.png)

## Tools
<a name="build-and-test-ios-apps-with-aws-codecommit-aws-codepipeline-and-aws-device-farm-tools"></a>
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) is a fully managed continuous delivery service that helps you automate your release pipelines for fast and reliable application and infrastructure updates. CodePipeline automates the build, test, and deploy phases of your release process every time there is a code change, based on the release model you define.
+ [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) is a fully managed source control service that hosts secure Git-based repositories. It makes it easy for teams to collaborate on code in a secure and highly scalable ecosystem. CodeCommit eliminates the need to operate your own source control system or worry about scaling its infrastructure.
+ [AWS Device Farm](https://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html) is an application testing service that lets you improve the quality of your web and mobile apps by testing them across an extensive range of desktop browsers and real mobile devices, without having to provision and manage any testing infrastructure.
+ [Jenkins](https://www.jenkins.io/) is an open-source automation server that enables developers to build, test, and deploy their software.

## Epics
<a name="build-and-test-ios-apps-with-aws-codecommit-aws-codepipeline-and-aws-device-farm-epics"></a>

### Set up the build environment
<a name="set-up-the-build-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install Jenkins on the build server that's running macOS. | Jenkins will be used for building the application, so you must first install it on the build server. To get detailed instructions for this and subsequent tasks, see the AWS blog post [Building and testing iOS and iPadOS apps with AWS DevOps and mobile services ](https://aws.amazon.com/blogs/devops/building-and-testing-ios-and-ipados-apps-with-aws-devops-and-mobile-services/)and other resources in the [Related resources](#build-and-test-ios-apps-with-aws-codecommit-aws-codepipeline-and-aws-device-farm-resources) section at the end of this pattern. | DevOps |
| Configure Jenkins. | Follow the on-screen instructions to configure Jenkins. | DevOps |
| Install the AWS CodePipeline plugin for Jenkins. | This plugin must be installed on the Jenkins server in order for Jenkins to interact with the AWS CodePipeline service. | DevOps |
| Create a Jenkins freestyle project. | In Jenkins, create a freestyle project. Configure the project to specify triggers and other build configuration options. | DevOps |

### Configure AWS Device Farm
<a name="configure-aws-device-farm"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a Device Farm project. | Open the AWS Device Farm console. Create a project and a device pool for testing. For instructions, see the blog post. | Developer |

### Configure the source repository
<a name="configure-the-source-repository"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a CodeCommit repository. | Create a repository where the source code will be stored. | DevOps |
| Commit your application code to the repository. | Connect to the CodeCommit repository you created. Push the code from your local machine to the repository. | DevOps |

### Configure the pipeline
<a name="configure-the-pipeline"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a pipeline in AWS CodePipeline. | Open the AWS CodePipeline console, and create a pipeline. The pipeline orchestrates all the phases of the CI/CD process. For instructions, see the AWS blog post [Building and testing iOS and iPadOS apps with AWS DevOps and mobile services](https://aws.amazon.com/blogs/devops/building-and-testing-ios-and-ipados-apps-with-aws-devops-and-mobile-services/). | DevOps |
| Add a test stage to the pipeline. | To add a test stage and integrate it with AWS Device Farm, edit the pipeline. | DevOps |
| Initiate the pipeline. | To start the pipeline and the CI/CD process, choose **Release change**. | DevOps |

### View application test results
<a name="view-application-test-results"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Review test results. | In the AWS Device Farm console, select the project you created, and review the results of the tests. The console will show the details of each test. | Developer |

## Related resources
<a name="build-and-test-ios-apps-with-aws-codecommit-aws-codepipeline-and-aws-device-farm-resources"></a>

**Step-by-step instructions for this pattern**
+ [Building and testing iOS and iPadOS apps with AWS DevOps and mobile services](https://aws.amazon.com/blogs/devops/building-and-testing-ios-and-ipados-apps-with-aws-devops-and-mobile-services/) (AWS DevOps blog post)

**Configure AWS Device Farm**
+ [AWS Device Farm console](https://console.aws.amazon.com/devicefarm)

**Configure the source repository**
+ [Create an AWS CodeCommit repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-create-repository.html)
+ [Connect to an AWS CodeCommit repository](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-connect.html)

**Configure the pipeline**
+ [AWS CodePipeline console](https://console.aws.amazon.com/codesuite/codepipeline/home)

**Additional resources**
+ [AWS CodePipeline documentation](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html)
+ [AWS CodeCommit documentation](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html)
+ [AWS Device Farm documentation](https://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html)
+ [Jenkins documentation](https://www.jenkins.io/doc/)
+ [Jenkins installation on macOS](https://www.jenkins.io/download/weekly/macos/)
+ [AWS CodePipeline plugin for Jenkins](https://plugins.jenkins.io/aws-codepipeline/)
+ [Xcode installation](https://developer.apple.com/xcode/)
+ AWS CLI [Installation](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv1.html) and [configuration](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
+ [Git documentation](https://git-scm.com/docs)
