---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/integrate-a-bitbucket-repository-with-aws-amplify-using-aws-cloudformation.html
---

# Integrate a Bitbucket repository with AWS Amplify using AWS CloudFormation
<a name="integrate-a-bitbucket-repository-with-aws-amplify-using-aws-cloudformation"></a>

*Alwin Abraham, Amazon Web Services*

## Summary
<a name="integrate-a-bitbucket-repository-with-aws-amplify-using-aws-cloudformation-summary"></a>

AWS Amplify helps you to quickly deploy and test static websites without having to set up the infrastructure that is typically required. You can deploy this pattern's approach if your organization wants to use Bitbucket for source control, whether to migrate existing application code or build a new application. By using AWS CloudFormation to automatically set up Amplify, you provide visibility into the configurations that you use.

This pattern describes how to create a front-end continuous integration and continuous deployment (CI/CD) pipeline and deployment environment by using AWS CloudFormation to integrate a Bitbucket repository with AWS Amplify. The pattern's approach means that you can build an Amplify front-end pipeline for repeatable deployments.

## Prerequisites and limitations
<a name="integrate-a-bitbucket-repository-with-aws-amplify-using-aws-cloudformation-prereqs"></a>

**Prerequisites**** **
+ An active Amazon Web Services (AWS) account
+ An active Bitbucket account with administrator access
+ Access to a terminal that uses [cURL](https://curl.se/) or the [Postman](https://www.postman.com/) application
+ Familiarity with Amplify
+ Familiarity with AWS CloudFormation
+ Familiarity with YAML-formatted files

## Architecture
<a name="integrate-a-bitbucket-repository-with-aws-amplify-using-aws-cloudformation-architecture"></a>

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/24ae87ed-aa5d-4114-9c5d-bdcb4d40a78b/images/25d73a9d-d2ae-40bc-9ebc-57f9bd13884a.png)

**Technology stack  **
+ Amplify
+ AWS CloudFormation
+ Bitbucket

## Tools
<a name="integrate-a-bitbucket-repository-with-aws-amplify-using-aws-cloudformation-tools"></a>
+ [AWS Amplify](https://docs.aws.amazon.com/amplify/) – Amplify helps developers to develop and deploy cloud-powered mobile and web apps.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) – AWS CloudFormation is a service that helps you model and set up your AWS resources so that you can spend less time managing those resources and more time focusing on your applications that run in AWS.
+ [Bitbucket](https://bitbucket.org/) – Bitbucket is a Git repository management solution designed for professional teams. It gives you a central place to manage Git repositories, collaborate on your source code, and guide you through the development flow.

**Code **

The `bitbucket-amplify.yml` file (attached) contains the AWS CloudFormation template for this pattern.

## Epics
<a name="integrate-a-bitbucket-repository-with-aws-amplify-using-aws-cloudformation-epics"></a>

### Configure the Bitbucket repository
<a name="configure-the-bitbucket-repository"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| (Optional) Create a Bitbucket repository.  | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/integrate-a-bitbucket-repository-with-aws-amplify-using-aws-cloudformation.html)You can also use an existing Bitbucket repository. | DevOps engineer |
| Open the workspace settings. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/integrate-a-bitbucket-repository-with-aws-amplify-using-aws-cloudformation.html) | DevOps engineer |
| Create an OAuth consumer. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/integrate-a-bitbucket-repository-with-aws-amplify-using-aws-cloudformation.html) | DevOps engineer |
| Obtain OAuth access token.  | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/integrate-a-bitbucket-repository-with-aws-amplify-using-aws-cloudformation.html)`curl -X POST -u "KEY:SECRET" https://bitbucket.org/site/oauth2/access_token -d grant_type=client_credentials `Replace `KEY` and `SECRET` with the key and secret that you recorded earlier. <br />2. Record the access token without using the quotation marks. The token is only valid for a limited time and the default time is two hours. You must run the AWS CloudFormation template in this timeframe. | DevOps engineer |

### Create and deploy the AWS CloudFormation stack
<a name="create-and-deploy-the-aws-cloudformation-stack"></a>

| Task | Description | Skills required |
| --- | --- | --- |
|  Download the AWS CloudFormation template. | Download the `bitbucket-amplify.yml` AWS CloudFormation template (attached). This template creates the CI/CD pipeline in Amplify, in addition to the Amplify project and branch. |  |
| Create and deploy the AWS CloudFormation stack. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/integrate-a-bitbucket-repository-with-aws-amplify-using-aws-cloudformation.html)5. Choose **Next** and then choose **Create Stack**. | DevOps engineer |

### Test the CI/CD pipeline
<a name="test-the-ci-cd-pipeline"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the code to the branch in your repository. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/integrate-a-bitbucket-repository-with-aws-amplify-using-aws-cloudformation.html)For more information about this, see [Basic Git commands](https://confluence.atlassian.com/bitbucketserver/basic-git-commands-776639767.html) in the Bitbucket documentation.  | App developer |

## Related resources
<a name="integrate-a-bitbucket-repository-with-aws-amplify-using-aws-cloudformation-resources"></a>

[Authentication methods](https://developer.atlassian.com/bitbucket/api/2/reference/meta/authentication) (Atlassian documentation)

## Attachments
<a name="attachments-24ae87ed-aa5d-4114-9c5d-bdcb4d40a78b"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/24ae87ed-aa5d-4114-9c5d-bdcb4d40a78b/attachments/attachment.zip)
