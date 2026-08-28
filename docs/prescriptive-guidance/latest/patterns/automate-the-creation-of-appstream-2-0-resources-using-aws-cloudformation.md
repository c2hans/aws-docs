---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-the-creation-of-appstream-2-0-resources-using-aws-cloudformation.html
---

# Automate the creation of Amazon WorkSpaces Applications resources using AWS CloudFormation
<a name="automate-the-creation-of-appstream-2-0-resources-using-aws-cloudformation"></a>

*Ram Kandaswamy, Amazon Web Services*

## Summary
<a name="automate-the-creation-of-appstream-2-0-resources-using-aws-cloudformation-summary"></a>

This pattern provides code samples and steps to automate the creation of [Amazon WorkSpaces Applications](https://aws.amazon.com/workspaces/applications/) resources in the AWS Cloud by using an [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) template. The pattern shows you how to use a CloudFormation stack to automate the creation of your WorkSpaces Applications application resources, including an image builder, image, fleet instance, and stack. You can stream your WorkSpaces Applications application to end users on an HTML5-compliant browser by using either the desktop or application delivery mode.

## Prerequisites and limitations
<a name="automate-the-creation-of-appstream-2-0-resources-using-aws-cloudformation-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An acceptance of WorkSpaces Applications terms and conditions
+ Basic knowledge of WorkSpaces Applications resources, such as [fleets and stacks](https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-stacks-fleets.html) and [image builders](https://docs.aws.amazon.com/appstream2/latest/developerguide/managing-image-builders.html)

**Limitations**
+ You can’t modify the [AWS Identity and Access Management](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) (IAM) role associated with an WorkSpaces Applications instance after that instance is created.
+ You can’t modify properties (such as the [subnet](https://docs.aws.amazon.com/vpc/latest/userguide/configure-subnets.html#subnet-basics) or [security group](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-groups.html)) on the WorkSpaces Applications image builder instance after that image builder is created.

## Architecture
<a name="automate-the-creation-of-appstream-2-0-resources-using-aws-cloudformation-architecture"></a>

The following diagram shows you how to automate the creation of WorkSpaces Applications resources by using a CloudFormation template.

![Workflow for automatically creating WorkSpaces Applications resources.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/4f0205f5-5b91-4832-9f0f-2135ae866226/images/cb578939-d9af-4f60-93c9-286881df4c3a.png)

The diagram shows the following workflow:

1. You create a CloudFormation template based on the YAML code in the [Additional information](#automate-the-creation-of-appstream-2-0-resources-using-aws-cloudformation-additional) section of this pattern.

1. The CloudFormation template creates a CloudFormation test stack.

   1. (Optional) You create an image builder instance by using WorkSpaces Applications.

   1. (Optional) You create a Windows image by using your custom software.

1. The CloudFormation stack creates an WorkSpaces Applications fleet instance and stack.

1. You deploy your WorkSpaces Applications resources to end users on an HTML5-compliant browser.

## Tools
<a name="automate-the-creation-of-appstream-2-0-resources-using-aws-cloudformation-tools"></a>
+ [Amazon WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/what-is-appstream.html) is a fully managed application streaming service that provides you with instant access to your desktop applications from anywhere. WorkSpaces Applications manages the AWS resources required to host and run your applications, scales automatically, and provides access to your users on demand.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you model and set up your AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle. You can use a template to describe your resources and their dependencies, and launch and configure them together as a stack, instead of managing resources individually. You can manage and provision stacks across multiple AWS accounts and AWS Regions.

## Best practices
<a name="automate-the-creation-of-appstream-2-0-resources-using-aws-cloudformation-best-practices"></a>
+ **Configure network access for image builders correctly** – Launch image builders in virtual private cloud (VPC) subnets with proper internet access by using a NAT gateway for outbound-only internet access.

  Test network connectivity to required resources (such as application servers, databases, and licensing servers) before creating images. Verify that VPC route tables allow connections to all necessary network resources. For more information, see [Internet access](https://docs.aws.amazon.com/appstream2/latest/developerguide/internet-access.html) in the WorkSpaces Applications documentation.
+ **Monitor fleet capacity against service quotas proactively** – WorkSpaces Applications instance type and size quotas are per AWS account, per AWS Region. If you have multiple fleets in the same Region that use the same instance type and size, the total number of instances in all fleets in that Region must be less than or equal to the applicable quota. For more information, see [Troubleshooting Fleets](https://docs.aws.amazon.com/appstream2/latest/developerguide/troubleshooting-fleets.html) in the WorkSpaces Applications documentation.
+ **Test applications in Image Builder Test mode before fleet deployment** – Always validate applications in Image Builder Test mode before creating images and deploying to fleets. Test mode simulates the limited permissions that end users have on fleet instances. For more information, see [Troubleshooting Image Builders](https://docs.aws.amazon.com/appstream2/latest/developerguide/troubleshooting-image-builder.html#troubleshooting-07) in the WorkSpaces Applications documentation.

## Epics
<a name="automate-the-creation-of-appstream-2-0-resources-using-aws-cloudformation-epics"></a>

### (Optional) Create a WorkSpaces Applications image
<a name="optional-create-a-aas2-image"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install custom software and create an image. | 1. Launch[ image builder](https://docs.aws.amazon.com/appstream2/latest/developerguide/tutorial-image-builder-create.html) and choose the relevant instance types, subnet, security group, and so on.<br />2. Use admin mode while connecting to the instance.<br />3. Use the [Image assistant](https://docs.aws.amazon.com/appstream2/latest/developerguide/tutorial-image-builder.html) or a PowerShell script to create a new Windows image for your custom software.Consider using the Windows AppLocker feature to further lock down the image. | AWS DevOps, Cloud architect |

### Deploy the CloudFormation template
<a name="deploy-the-cfn-template"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Update the CloudFormation template. | 1. Use the code in the [Additional information](#automate-the-creation-of-appstream-2-0-resources-using-aws-cloudformation-additional) section of this pattern as a YAML file.<br />2. Update the YAML file with the required values for the parameters in your environment. | AWS systems administrator, Cloud administrator, Cloud architect, General AWS, AWS administrator |
| Create a CloudFormation stack by using the template. | 1. Sign in to the AWS Management Console and open the [CloudFormation console](https://console.aws.amazon.com/cloudformation/).<br />2. On the navigation pane, choose **Stacks**.<br />3. Choose **Create stack** and then choose **With new resources (standard)**.<br />4. In the **Prerequisite – Prepare template** section, choose **Template is ready**.<br />5. In the **Specify template** section, choose **Upload a template** **file**.<br />6. Choose **Choose file** and then choose your updated CloudFormation template.<br />7. Complete the rest of the steps in the wizard to create your stack. | App owner, AWS systems administrator, Windows Engineer |

## Troubleshooting
<a name="automate-the-creation-of-appstream-2-0-resources-using-aws-cloudformation-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Various issues | For more information, see [Troubleshooting](https://docs.aws.amazon.com/appstream2/latest/developerguide/troubleshooting.html) in the WorkSpaces Applications documentation. |

## Related resources
<a name="automate-the-creation-of-appstream-2-0-resources-using-aws-cloudformation-resources"></a>

**References**
+ [Get started with Amazon WorkSpaces Applications: Set up with sample applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/getting-started.html)
+ [Create an Amazon WorkSpaces Applications fleet and stack](https://docs.aws.amazon.com/appstream2/latest/developerguide/set-up-stacks-fleets.html)

**Tutorials and videos**
+ [Amazon WorkSpaces Applications User Workflow](https://www.youtube.com/watch?v=hVGQ87-Uhrc)
+ [How to Migrate a Legacy Windows Forms App to Amazon WorkSpaces Applications](https://www.youtube.com/watch?v=CIImtS2iVbg)
+ [AWS re:Invent 2018: Securely Deliver Desktop Applications with Amazon WorkSpaces Applications (BAP201)](https://www.youtube.com/watch?v=xNIyc_inOhM)

## Additional information
<a name="automate-the-creation-of-appstream-2-0-resources-using-aws-cloudformation-additional"></a>

The following code is an example of a CloudFormation template that you can use to automatically create WorkSpaces Applications resources.

```
AWSTemplateFormatVersion: 2010-09-09
Parameters:
  SubnetIds:
    Type: 'List<AWS::EC2::Subnet::Id>'
  testSecurityGroup:
    Type: 'AWS::EC2::SecurityGroup::Id'
  ImageName:
    Type: String
Resources:

  AppStreamFleet:
    Type: 'AWS::AppStream::Fleet'
    Properties:
      ComputeCapacity:
        DesiredInstances: 5
      InstanceType: stream.standard.medium
      Name: appstream-test-fleet
      DisconnectTimeoutInSeconds: 1200
      FleetType: ON_DEMAND
      IdleDisconnectTimeoutInSeconds: 1200
      ImageName: !Ref ImageName
      MaxUserDurationInSeconds: 345600
      VpcConfig:
        SecurityGroupIds:
          - !Ref testSecurityGroup
        SubnetIds: !Ref SubnetIds
  AppStreamStack:
    Type: 'AWS::AppStream::Stack'
    Properties:
      Description: AppStream stack for test
      DisplayName: AppStream test Stack
      Name: appstream-test-stack
      StorageConnectors:
        - ConnectorType: HOMEFOLDERS
      UserSettings:
        - Action: CLIPBOARD_COPY_FROM_LOCAL_DEVICE
          Permission: ENABLED
        - Action: CLIPBOARD_COPY_TO_LOCAL_DEVICE
          Permission: ENABLED
        - Action: FILE_DOWNLOAD
          Permission: ENABLED
        - Action: PRINTING_TO_LOCAL_DEVICE
          Permission: ENABLED
  AppStreamFleetAssociation:
    Type: 'AWS::AppStream::StackFleetAssociation'
    Properties:
      FleetName: appstream-test-fleet
      StackName: appstream-test-stack
    DependsOn:
      - AppStreamFleet
      - AppStreamStack
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
