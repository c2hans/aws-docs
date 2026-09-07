---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-cloudendure/prepare.html
---

# Preparing your environment
<a name="prepare"></a>

Before you use CloudEndure Migration, you have to make sure that your source and target environments are prepared and configured correctly. These preparations include setting a CloudEndure account, creating AWS credentials, defining network requirements, and opening the correct ports.

## Set up your CloudEndure account and users
<a name="account"></a>

Before you start your migration, follow these steps:

1. Subscribe to CloudEndure Migration in [AWS Marketplace](https://aws.amazon.com/marketplace/pp/B01MQCH96B?ref_=%22saas_products_all%22_B01MQCH96B_5), where it's available as a SaaS contract directly through your existing AWS account.

1. Create an account in CloudEndure. For instructions, see [Registering to CloudEndure Migration](https://docs.cloudendure.com/#Getting_Started_with_CloudEndure/Registering_to_CloudEndure_Migration/Registering_to_CloudEndure_Migration.htm) in the CloudEndure documentation.

1. Add users. The account owner and account administrators can manage users and projects in the CloudEndure User Console. For information about inviting and managing users, see [User Management](https://docs.cloudendure.com/Content/Getting_Started_with_CloudEndure/User_Management/User_Management.htm) in the CloudEndure documentation.

1. Create and configure a CloudEndure project. Log in to the [CloudEndure User Console](https://console.cloudendure.com/#/signIn) and follow the steps provided in [Working with Projects](https://docs.cloudendure.com/#Getting_Started_with_CloudEndure/Working_with_Projects/Working_with_Projects.htm) in the CloudEndure documentation.

For project type, select **Migration**.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-cloudendure/images/guide-img/bbb5871c-6fdf-4a96-872d-e22410dc477d/images/5e75b3ae-ba32-4c95-847f-1a072fd7d7e1.png)

**Note**
Make sure that you have sufficient [migration licenses](https://docs.cloudendure.com/#Getting_Started_with_CloudEndure/Understanding_CloudEndure_Basic_Concepts/Understanding_CloudEndure_Basic_Concepts.htm) for your project.

## Generate and use AWS Cloud credentials
<a name="credentials"></a>

Before you install CloudEndure Agents, you must create the AWS Identity and Access Management (IAM) credentials required to configure the CloudEndure User Console, and collect the access key and secret access key for the CloudEndure users in your organization. Follow these steps:

1. Sign in to your AWS account.

1. Create a policy for CloudEndure in your AWS account, using the code from [https://docs.cloudendure.com/Content/IAMPolicy.json](https://docs.cloudendure.com/Content/IAMPolicy.json). For more information about this step, see the [CloudEndure documentation](https://docs.cloudendure.com/#Generating_and_Using_Your_Credentials/Working_with_AWS_Credentials/Generating_the_Required_AWS_Credentials/Generating_the_Required_AWS_Credentials.htm).

1. Create a new IAM user and generate AWS credentials, which  consist of an access key ID and a secret access key. For more information, see the [CloudEndure documentation](https://docs.cloudendure.com/#Generating_and_Using_Your_Credentials/Working_with_AWS_Credentials/Generating_the_Required_AWS_Credentials/Generating_the_Required_AWS_Credentials.htm) and the [IAM documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_users_create.html).

1. In the CloudEndure User Console, choose **Setup & Info**, **AWS Credentials**.
![](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-cloudendure/images/guide-img/bbb5871c-6fdf-4a96-872d-e22410dc477d/images/31387e30-4c05-4743-88a9-f89e7a184f30.png)

1. Add the access key ID and secret access key you created in the previous step into the corresponding fields and save.

## Configure your source and target network
<a name="network"></a>

In the target environment on AWS, prepare a subnet to use as the CloudEndure staging area. Use a private subnet if you want to isolate your application. You can use an existing subnet or create a new one. This  subnet is used to launch the CloudEndure replication servers, which receive replicated data from the source machines.

In general, there are three points of contact between CloudEndure components and the external network:
+ The CloudEndure Agent needs to communicate with the CloudEndure Service Manager.
+ The CloudEndure Agent needs to communicate with the CloudEndure replication servers.
+ CloudEndure replication servers need to communicate with the CloudEndure Service Manager and Amazon Simple Storage Service (Amazon S3).

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-cloudendure/images/guide-img/bbb5871c-6fdf-4a96-872d-e22410dc477d/images/0db2de06-1b28-4ba8-8f08-139d16eac7c2.png)

### Network requirements
<a name="network-requirements.4888e3ec-6149-5b96-8ba0-18a6d2cdf8b6"></a>

|
|
| Client | Server | Description |
| --- |--- |--- |
| Agent | Outbound:  TCP 1500 | Replication server(s)  (private/public network) | Inbound:  TCP 1500 | Production instance status and data  (the actual data replication stream) |
| Agent | Outbound:  TCP 1500 | Management  (public network) |   | + REST APIs used during Agent installation<br />+ Agent monitoring<br />+ Statistics for Agents |
| Replication server(s) | Outbound:  TCP 443 | Management  (public network) |   | + Statistics for replication servers<br />+ Replication server logs<br />+ Replication server API |

To prepare your network for running CloudEndure's solutions, you need to set the following connectivity settings:
+ Communication over TCP port 443:
  + Between the source machines and CloudEndure Service Manager
  + Between the staging area and CloudEndure Service Manager
+ Communication over TCP port 1500:
  + Between the source machines and the staging area

**Note**
For information about replication from a private subnet or server behind a NAT gateway or instance, see the [CloudEndure documentation](https://docs.cloudendure.com/#FAQ/FAQ/Target_Related.htm).

### Communication over TCP port 443
<a name="communication-over-tcp-port-443.d881decf-3c19-53ad-8646-501b0c2afeca"></a>

Add the following IP addresses and URLs to your firewall:
+ CloudEndure Service Manager IP address (required for using CloudEndure software)
  + 52.72.172.158 (main service of console.cloudendure.com)
  + 52.53.92.136
+ Amazon S3 service URLs (required for downloading CloudEndure software)
  + s3.amazonaws.com
  + s3.us-west-1.amazonaws.com
  + s3.eu-west-1.amazonaws.com

## Proxy servers
<a name="proxy-servers"></a>

If you want to use proxy servers in your environment, follow this guidance for CloudEndure to operate effectively:
+ Make sure to set the proxy in replication settings,  either as an IP address or as a fully qualified domain name (FQDN).
+ Configure the proxy allow list for the CloudEndure Agent:
  + In Windows, the CloudEndure Agent runs as a system service, so make sure that the system account is part of the proxy allow list.
  + In Linux, the CloudEndure Agent creates a Linux user (named cloudendure) to run commands, so make sure that this user is part of the proxy allow list.
+ Set the proxy:
  + In Windows, open the Command Prompt window as an administrator, and run the command:

```
setx https_proxy https://<proxy-ip>:<proxy-port>/ /m
```
+ In Linux, change to **sudo **user and run the commands:

```
$ export http_proxy=http://server-ip:port/
$ export http_proxy=http://127.0.0.1:3128/
$ export http_proxy=http://proxy-server.mycorp.com:3128/
 (make sure to include the trailing slash "/")
```

Optionally, if you want to keep the environment variables for Windows, follow these steps:

1. In Windows Control Panel, choose **System and Security**, **System**, **Advanced system settings.**

1. In the **Advanced** tab of the **System Properties** dialog box, choose **Environment Variables**.

1. In the **System variables** section of the **Environment Variables** dialog box, choose **New** to add the `https_proxy` environment variable, or **Edit** if the variable already exists.

1. In the **Variable value** field of the `https_proxy` variable, enter `https://PROXY_ADDR:PROXY_PORT/` and then choose **OK**.

1. If the CloudEndure Agent was already installed, restart the service.
