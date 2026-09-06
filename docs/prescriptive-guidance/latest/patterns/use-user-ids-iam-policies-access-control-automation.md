---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/use-user-ids-iam-policies-access-control-automation.html
---

# Use user IDs in IAM policies for access control and automation
<a name="use-user-ids-iam-policies-access-control-automation"></a>

*Srinivas Ananda Babu and Ram Kandaswamy, Amazon Web Services*

## Summary
<a name="use-user-ids-iam-policies-access-control-automation-summary"></a>

This pattern explains the potential pitfalls of using username-based policies in AWS Identity and Access Management (IAM), the benefits of using user IDs, and how to integrate this approach with AWS CloudFormation for automation.

In the AWS Cloud, the IAM service helps you manage user identities and access control with precision. However, reliance on usernames in IAM policy creation can lead to unforeseen security risks and access control issues. For example, consider this scenario: A new employee, John Doe, joins your team, and you create an IAM user account with the username `j.doe`, which grants them permissions through IAM policies that reference usernames. When John leaves the company, the account is deleted. The trouble begins when a new employee, Jane Doe, joins your team, and the `j.doe` username is recreated. The existing policies now grant Jane Doe the same permissions as John Doe. This creates a potential security and compliance nightmare.

Manually updating each policy to reflect new user details is a time-consuming, error-prone process, especially as your organization grows. The solution is to use a unique and immutable user ID. When you create an IAM user account, AWS assigns the IAM user a unique user ID (or principal ID). You can use these user IDs in your IAM policies to ensure consistent and reliable access control that isn't affected by username changes or reuse.

For example, an IAM policy that uses a user ID might look like this:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:ListBucket",
            "Resource": "arn:aws:s3:::example-bucket",
            "Principal": { "AWS": "arn:aws:iam::123456789012:user/abcdef01234567890" }
        }
      ]
}
```

The benefits of using user IDs in IAM policies include:
+ **Uniqueness.** User IDs are unique across all AWS accounts, so they provide correct and consistent permission application.
+ **Immutability.** User IDs cannot be changed, so they provide a stable identifier for referencing users in policies.
+ **Auditing and compliance.** AWS services often include user IDs in logs and audit trails, which makes it easy to trace actions back to specific users.
+ **Automation and integration.** Using user IDs in AWS APIs, SDKs, or automation scripts ensures that processes remain unaffected by username changes.
+ **Future-proofing.** Using user IDs in policies from the start can prevent potential access control issues or extensive policy updates.

**Automation**

When you use infrastructure as code (IaC) tools such as AWS CloudFormation, the pitfalls of username-based IAM policies can still cause issues. The IAM user resource returns the username when you call the `Ref` intrinsic function. As your organization's infrastructure evolves, the cycle of creating and deleting resources, including IAM user accounts, can lead to unintended access control issues if you reuse usernames.

To address this issue, we recommend that you incorporate user IDs into your CloudFormation templates. However, obtaining user IDs for this purpose can be challenging. This is where custom resources can be helpful. You can use CloudFormation custom resources to extend the service's functionality by integrating with AWS APIs or external services. By creating a custom resource that fetches the user ID for a given IAM user, you can make the user ID available within your CloudFormation templates. This approach streamlines the process of referencing user IDs and ensures that your automation workflows remain robust and future-proof.

## Prerequisites and limitations
<a name="use-user-ids-iam-policies-access-control-automation-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An IAM role for a cloud administrator to run the CloudFormation template

**Limitations**
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see the [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html) page, and choose the link for the service.

## Architecture
<a name="use-user-ids-iam-policies-access-control-automation-architecture"></a>

**Target architecture **

The following diagram shows how CloudFormation uses a custom resource backed by AWS Lambda to retrieve the IAM user ID.

![Getting the IAM user ID by using a CloudFormation custom resource.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/71698647-274e-4911-92f0-549e444b53f6/images/7e507df4-f597-499e-bd5b-6d7a55e64146.png)

**Automation and scale**

You can use the CloudFormation template multiple times for different AWS Regions and accounts. You need to run it only once in each Region or account.

## Tools
<a name="use-user-ids-iam-policies-access-control-automation-tools"></a>

**AWS services**
+ [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) – AWS Identity and Access Management (IAM) is a web service that helps you securely control access to AWS resources. You use IAM to control who is authenticated (signed in) and authorized (has permissions) to use resources.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) – AWS CloudFormation helps you model and set up your AWS resources so that you can spend less time managing those resources and more time focusing on your applications that run on AWS. You create a template that describes the AWS resources that you want, and CloudFormation takes care of provisioning and configuring those resources for you.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) – AWS Lambda is a compute service that supports running code without provisioning or managing servers. Lambda runs your code only when needed and scales automatically, from a few requests per day to thousands per second.

## Best practices
<a name="use-user-ids-iam-policies-access-control-automation-best-practices"></a>

If you're starting from scratch or planning a greenfield deployment, we strongly recommend that you use [AWS IAM Identity Center](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html) for centralized user management. IAM Identity Center integrates with your existing identity providers (such as Active Directory or Okta) to federate user identities on AWS, which eliminates the need to create and manage IAM users directly. This approach not only ensures consistent access control but also simplifies user lifecycle management and helps enhance security and compliance across your AWS environment.

## Epics
<a name="use-user-ids-iam-policies-access-control-automation-epics"></a>

### Validate permissions
<a name="validate-permissions"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Validate your AWS account and IAM role. | Confirm that you have an IAM role with permissions to deploy CloudFormation templates in your AWS account.<br />If you're planning to use the AWS CLI instead of the CloudFormation console to deploy the template in the last step of this procedure, you should also set up temporary credentials to run AWS CLI commands. For instructions, see the [IAM documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html#using-temp-creds-sdk-cli). | Cloud architect |

### Build a CloudFormation template
<a name="build-a-cfnshort-template"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a CloudFormation template. | 1. Create a CloudFormation template by following the [instructions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-guide.html) in the CloudFormation documentation. You can use either JSON or YAML format. This pattern assumes that you're using YAML format.<br />2. Save the template with the name `get_unique_user_id.yaml`. | AWS DevOps, Cloud architect |
| Add an input parameter for the username. | Add the following code to the `Parameters` section of the CloudFormation template:<pre>Parameters:<br />  NewIamUserName:<br />    Type: String<br />    Description: Unique username for the new IAM user<br /></pre><br />This parameter prompts the user for the username. | AWS DevOps, Cloud architect |
| Add a custom resource to create an IAM user. | Add the following code to the `Resources` section of the CloudFormation template:<pre>Resources:<br />  rNewIamUser:<br />    Type: 'AWS::IAM::User'<br />    Properties:<br />      UserName: !Ref NewIamUserName<br /></pre><br />This code adds a CloudFormation resource that creates an IAM user with the name provided by the `NewIamUserName` parameter. | AWS DevOps, Cloud architect |
| Add an execution role for the Lambda function. | In this step, you  create an IAM role that grants an AWS Lambda function permission to get the IAM `UserId`. Specify the following minimum required permissions for Lambda to run:+ `logs:CreateLogStream`<br />+ `logs:PutLogEvents`<br />+ `CreateLogGroup`<br />+ `iam:GetUser`<br />+ `AssumeRole` for `lambda.amazonaws.com`<br />For instructions on creating an execution role, see the [Lambda documentation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-intro-execution-role.html). You will reference this role in the next step, when you create the Lambda function. | AWS administrator, Cloud architect |
| Add a Lambda function to get the unique IAM `UserId`. | In this step, you define a Lambda function with a Python runtime to get the unique IAM `UserId`. To do this, add the following code to the `Resources` section of the CloudFormation template. Replace `<<ROLENAME>>` with the name of the execution role that you created in the last step.<pre>  GetUserLambdaFunction:<br />    Type: 'AWS::Lambda::Function'<br />    Properties:<br />      Handler: index.handler<br />      Role: <<ROLENAME>><br />      Timeout: 30<br />      Runtime: python3.11<br />      Code:<br />        ZipFile: |<br />          import cfnresponse, boto3<br />          def handler(event, context):<br />            try:<br />              print(event)<br />              user = boto3.client('iam').get_user(UserName=event['ResourceProperties']['NewIamUserName'])['User']<br />              cfnresponse.send(event, context, cfnresponse.SUCCESS, {'NewIamUserId': user['UserId'], 'NewIamUserPath': user['Path'], 'NewIamUserArn': user['Arn']})<br />            except Exception as e:<br />              cfnresponse.send(event, context, cfnresponse.FAILED, {'NewIamUser': str(e)})<br /></pre> | AWS DevOps, Cloud architect |
| Add a custom resource. | Add the  following code to the `Resources` section of the CloudFormation template:<pre>  rCustomGetUniqueUserId:<br />    Type: 'Custom::rCustomGetUniqueUserIdWithLambda'<br />    Properties:<br />      ServiceToken: !GetAtt GetUserLambdaFunction.Arn<br />      NewIamUserName: !Ref NewIamUserName<br /></pre><br />This custom resource calls the Lambda function to get the IAM `UserID`. | AWS DevOps, Cloud architect |
| Define CloudFormation outputs. | Add the following code to the `Outputs` section of the CloudFormation template:<pre>Outputs:<br />  NewIamUserId:<br />    Value: !GetAtt rCustomGetUniqueUserId.NewIamUserId<br /></pre><br />This displays the IAM `UserID` for the new IAM user. | AWS DevOps, Cloud architect |
| Save the template. | Save your changes to the CloudFormation template. | AWS DevOps, Cloud architect |

### Deploy the CloudFormation template
<a name="deploy-the-cfnshort-template"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the CloudFormation template. | To deploy the `get_unique_user_id.yaml` template by using the CloudFormation console, follow the instructions in the [CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html).<br />Alternatively, you can run the following AWS CLI command to deploy the template:<pre>aws cloudformation create-stack \<br />--stack-name DemoNewUser \<br />--template-body file://get_unique_user_id.yaml \<br />--parameters ParameterKey=NewIamUserName,ParameterValue=demouser \<br />--capabilities CAPABILITY_NAMED_IAM</pre> | AWS DevOps, Cloud architect |

## Related resources
<a name="use-user-ids-iam-policies-access-control-automation-resources"></a>
+ [Create a stack from the CloudFormation console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) (CloudFormation documentation)
+ [Lambda-backed custom resources](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/template-custom-resources-lambda.html) (CloudFormation documentation)
+ [Unique identifiers](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_identifiers.html#identifiers-unique-ids) (IAM documentation)
+ [Use temporary credentials with AWS resources](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_temp_use-resources.html) (IAM documentation)
