---
source_url: https://docs.aws.amazon.com/codedeploy/latest/userguide/reference-cloudformation-templates.html
---

# CloudFormation templates for CodeDeploy reference
<a name="reference-cloudformation-templates"></a>

This section introduces the CloudFormation resources, transform, and hook designed to work with CodeDeploy deployments. For a walkthrough of creating a stack update managed by the CloudFormation hook for CodeDeploy, see [Create an Amazon ECS blue/green deployment through CloudFormation](deployments-create-ecs-cfn.md)

**Note**
CloudFormation hooks are part of the CloudFormation components for AWS and are different from CodeDeploy lifecycle event hooks.

In addition to the other methods available to you in CodeDeploy, you can use CloudFormation templates to perform the following tasks:
+ Create applications.
+ Create deployment groups and specify a target revision.
+ Create deployment configurations.
+ Create Amazon EC2 instances.

CloudFormation is a service that helps you model and set up your AWS resources using templates. An CloudFormation template is a text file whose format complies with the JSON standard. You create a template that describes all of the AWS resources you want, and CloudFormation takes care of provisioning and configuring those resources for you.

For more information, see [What is AWS CloudFormation?](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) and [Working with AWS CloudFormation templates](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html) in *AWS CloudFormation User Guide*.

If you plan to use CloudFormation templates that are compatible with CodeDeploy in your organization, as an administrator, you must grant access to CloudFormation and to the AWS services and actions on which CloudFormation depends. To grant permissions to create applications, deployment groups, and deployment configurations, add the following policy to the permission set of the users who will work with CloudFormation:

------
#### [ JSON ]

****

```
{
  "Version":"2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "cloudformation:*"
      ],
      "Resource": "*"
    }
  ]
}
```

------

For more information about policies, see the following topics:
+ To view the policy that must be added to the permission set of users who will create Amazon EC2 instances, see [Create an Amazon EC2 instance for CodeDeploy (CloudFormation template)](instances-ec2-create-cloudformation-template.md).
+ For information about adding policies to permission sets, see [Create a permission set](https://docs.aws.amazon.com/singlesignon/latest/userguide/howtocreatepermissionset.html) in the *IAM User Guide*.
+ To learn how to restrict users to a limited set of CodeDeploy actions and resources, see [AWS managed (predefined) policies for CodeDeploy](managed-policies.md).

The following table shows the actions a CloudFormation template can perform on your behalf and includes links to more information about the AWS resource types and their property types you can add to a CloudFormation template.

<table>
<thead>
  <tr><th>Action</th><th> CloudFormation reference </th><th>Reference type</th></tr>
</thead>
<tbody>
  <tr><td>Create a CodeDeploy application. </td><td>[AWS::CodeDeploy::application](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-application.html)</td><td>CloudFormation resource</td></tr>
  <tr><td>Create and specify the details for a deployment group to be used to deploy your application revisions. ¹</td><td>[AWS::CodeDeploy::DeploymentGroup](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentgroup.html)</td><td>CloudFormation resource</td></tr>
  <tr><td>Create a set of deployment rules, deployment success conditions, and deployment failure conditions that CodeDeploy will use during a deployment.</td><td>[AWS::CodeDeploy::DeploymentConfig](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-codedeploy-deploymentconfig.html)</td><td>CloudFormation resource</td></tr>
  <tr><td>Create an Amazon EC2 instance. ²</td><td>[AWS::EC2::instance](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-ec2-instance.html)</td><td>CloudFormation resource</td></tr>
  <tr><td rowspan="2">Use the CloudFormation AWS::CodeDeployBlueGreen transform and AWS::CodeDeploy::BlueGreen hook to manage stack updates, create resources, and shift traffic for CodeDeploy blue/green deployments.3</td><td>[AWS::CodeDeployBlueGreen](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/blue-green.html)</td><td>The AWS::CodeDeployBlueGreen transform is a macro hosted by CloudFormation </td></tr>
  <tr><td>[AWS::CodeDeploy::BlueGreen](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/blue-green.html)</td><td>The AWS::CodeDeploy::BlueGreen hook is structured as a Hook resource in CloudFormation. The hook includes parameters that take the place of your CodeDeploy AppSpec file by pointing to designated CodeDeploy lifecycle event hooks.</td></tr>
  <tr><td colspan="2">¹ If you specify the version of the application revision that you want to be deployed as part of the deployment group, your target revision will be deployed as soon as the provisioning process is complete. For more information about template configuration, see [CodeDeploy DeploymentGroup deployment revision S3Location](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-s3location.html) and [CodeDeploy DeploymentGroup deployment revision GitHubLocation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-codedeploy-deploymentgroup-deployment-revision-githublocation.html) in the *AWS CloudFormation User Guide*.<br />² We provide templates you can use to create Amazon EC2 instances in the Regions in which CodeDeploy is supported. For more information about using these templates, see [Create an Amazon EC2 instance for CodeDeploy (CloudFormation template)](instances-ec2-create-cloudformation-template.md). <br />3Only Amazon ECS blue/green deployments are supported by this deployment configuration. For more information about deployment configurations for Amazon ECS blue/green deployments through CloudFormation, see [Deployment configurations for CloudFormation blue/green deployments (Amazon ECS)](deployment-configurations.md#deployment-configuration-cfn-bg). For more information about Amazon ECS blue/green deployments through CloudFormation and how to view your deployment in CodeDeploy, see [Create an Amazon ECS blue/green deployment through CloudFormation](deployments-create-ecs-cfn.md).</td><td></td></tr>
</tbody>
</table>
