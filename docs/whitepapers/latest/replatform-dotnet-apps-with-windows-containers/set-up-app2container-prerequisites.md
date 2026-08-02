---
source_url: https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/set-up-app2container-prerequisites.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Set up App2Container prerequisites
<a name="set-up-app2container-prerequisites"></a>

 App2Container needs access to AWS services to run most of its commands. There are two very different sets of permissions needed to run App2Container commands:
+  The General Purpose user or group can run all of the commands except commands that are run with the `--deploy` option.
+  For deployment, App2Container must be able to create or update AWS objects for container management services (Amazon ECR with Amazon ECS, Amazon EKS, or Fargate) and to create CI/CD pipelines with AWS CodePipeline. This requires elevated permissions that should only be used for deployment.

 AWS recommends that you create general purpose IAM resources, and if you plan to use App2Container to deploy your containers or create pipelines, that you create separate IAM resources for deployment which has elevated rights.

 For simplicity in this guide, you will create a user with Administrator rights so it can deploy a containerized application using the AWS services for deployment that are supported by App2Container.

 To create the user:

1.  Navigate to the IAM service in the AWS Management Console. In the left pane, choose **Users > Add user**.

1.  Select the **Programmatic access** type.

1.  Choose **Next: Permissions**.
![Screen showing Add User dialog](http://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/add-user.png)

1.  Set permissions for the App2container user by choosing **Attach existing policies directory**.

1.  Select **AdministratorAccess**, and choose **Next: Tags**.
**Note**
**AdministratorAccess** should be used only for demonstration purposes. Review the [official documentation](https://docs.aws.amazon.com/app2container/latest/UserGuide/iam-a2c.html) for real use cases.
![Screen showing the selection of AdministratorAccess](http://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/select-admin.png)

1.  Review and create your user. On the following screen, download the **access key ID** and **secret access key** to your local machine.
![Screen showing download of keys.](http://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/keys.jpg)

 App2Container uses AWS Secrets Manager to manage the credentials for connecting your worker machine to application servers to run remote commands. Secrets Manager encrypts your secrets for storage, and provides an [Amazon Resource Name](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) (ARN) for you to access the secret. When you run the remote configure command, you provide the secret ARN for App2Container to use to connect to your target server when running the remote command.

 To store a new secret:

1.  Navigate to AWS Secrets Manager in the AWS Management Console, and choose **Store a new secret**.
![Screen showing storing a new secret](http://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/secret-store.jpg)

1.  Choose **Other type of secrets** and add the following parameters. Choose **Next**.
![Screen showing adding parameters](http://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/secret-parms.jpg)

1.  In **Name and description**, enter a secret name and description. Choose **Next**.
![Screen showing entering secret name and description.](http://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/secret-name.jpg)

1.  On the next screen, leave the defaults in place, and choose **Next**.

1.  After you store the password, choose it from the **Secrets** list. This will take you to a screen with the secret details. Copy the secret ARN to your local machine, because you will need this later.
![Screen showing retrieval of secret ARN..](http://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/arn.jpg)

 Now that you have your IAM role and secret created, log in to your worker machine and configure the AWS CLI with these newly created access objects.

 To configure the AWS CLI:

1.  Go to the EC2 service in the AWS Management Console, choose your worker machine instance, and choose **Connect** in the upper right of the screen.
![Screen showing worker machine instance.](http://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/images/mach-instance.jpg)

1.  Follow the same steps as detailed earlier in the [*Connect to deployment*](connect-to-deployment.md) section to get the password for the worker machine. Copy that password to your local machine and use it to connect to the worker machine using Remote Desktop Connection.

1.  When you are connected to the worker machine, open PowerShell and run the following:

   ```
   aws configure

   AWS Access Key ID [None]: <<add AWS access key from previous steps>>
   AWS Secret Access Key [None]: <<add AWS secret access key from previous steps>>
   Default region name [None]: us-west-2
   Default output format [None]: [blank]
   ```

 With this step, you have set up your environment prerequisites, and are ready for App2Container installation on your environment. In the next section, you will install App2Container on your worker machine and set it up to start your containerization process.
