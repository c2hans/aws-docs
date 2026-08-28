---
source_url: https://docs.aws.amazon.com/toolkit-for-jetbrains/latest/userguide/creating-service-apprunner.html
---

# Creating App Runner services
<a name="creating-service-apprunner"></a>

You can create an App Runner service in AWS Toolkit for JetBrains by using the **Create App Runner Service** dialog box. You can use its interface to select a source repository and configure the service instance where your application runs.

Before creating an App Runner service, make sure that you completed all the [prerequisites](using-apprunner.md#apprunner-prereqs). Included is providing the relevant IAM permissions and taking note of the specific information about the source repository that you want to deploy.<a name="create-service"></a>

# To create an App Runner service
<a name="create-service"></a>

1. Open AWS Explorer, if it isn't already open.

1. Right-click the **App Runner** node and choose **Create Service**.

   The **Create App Runner Service** dialog box is displayed.

1. Enter your unique **Service name**.

1. Choose your source type (**ECR**, **ECR public** or **Source code repository**) and configure the relevant settings:

------
#### [ ECR/ECR public ]

   If you're using a private registry, choose the **Deployment type**:
   + **Manual**: Use manual deployment if you want to explicitly initiate each deployment to your service.
   + **Automatic**: Use automatic deployment if you want implement continuous integration and deployment (CI/CD) behavior for your service. If you choose this option, it means that whenever you push a new image version to your image repository or a new commit to your code repository, App Runner automatically deploys it to your service without further action required from you.

   For **Container image URI**, enter the URI of the image repository that you copied from your Amazon ECR private registry or Amazon ECR Public Gallery.

   For **Start Command**, enter the command to start the service process.

   For **Port**, enter the IP port that's used by the service.

   If you're using an Amazon ECR private registry, select the required **ECR access role** and choose **Create**.
   + The **Create IAM Role** dialog box displays the **Name**, **Managed Policies**, and **Trust Relationships** for the IAM role. Choose **Create**.

------
#### [ Source code repository ]

   Choose the **Deployment type**:
   + **Manual**: Use manual deployment if you want to explicitly initiate each deployment to your service.
   + **Automatic**: Use automatic deployment if you want implement continuous integration and deployment (CI/CD) behavior for your service. If you choose this option, it means that whenever you push a new image version to your image repository, or a new commit to your code repository, App Runner automatically deploys it to your service without further action required from you.

   For **Connections**, select a connection that's available from the list on **GitHub connections** page.

   For **Repository URL**, enter the link to remote repository that's hosted on GitHub.

   For **Branch**, indicate which Git branch of your source code that you want to deploy.

   For **Configuration**, specify how you want to specify your runtime configuration:
   + **Configure all settings here**: Choose this option if you want to specify the following settings for the runtime environment of your application:
     + **Runtime**: Choose **Python 3** or **Nodejs 12**.
     + **Port**: Enter the IP port that your service uses.
     + **Build command**: Enter the command to build your application in the runtime environment of your service instance.
     + **Start command**: Enter the command to start your application in the runtime environment of your service instance.
   + **Provide a configuration file settings here**: Choose this option to use the settings that are defined by the `apprunner.yaml` configuration file. This file is in the root directory of your application’s repository.

------

1. Specify values to define the runtime configuration of the App Runner service instance:
   + **CPU**: The number of CPU units that are reserved for each instance of your App Runner service (Default: `1 vCPU`).
   + **Memory:** The amount of memory that's reserved for each instance of your App Runner service (Default: `2 GB`)
   + **Environmental variables**: Optional environment variables that you use to customize behavior in your service instance. Create environmental variables by defining a key and a value.

1. Choose **Create**

   When your service is being created, its status changes from **Operation in progress** to **Running**.

1. After your service starts running, right-click it and choose **Copy Service URL**.

1. To access your deployed application, paste the copied URL into the address bar of your web browser.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Toolkit for JetBrains. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query toolkit-for-jetbrains` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
