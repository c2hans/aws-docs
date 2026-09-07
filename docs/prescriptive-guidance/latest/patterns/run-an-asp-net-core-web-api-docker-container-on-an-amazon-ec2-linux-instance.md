---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/run-an-asp-net-core-web-api-docker-container-on-an-amazon-ec2-linux-instance.html
---

# Run an ASP.NET Core web API Docker container on an Amazon EC2 Linux instance
<a name="run-an-asp-net-core-web-api-docker-container-on-an-amazon-ec2-linux-instance"></a>

*Vijai Anand Ramalingam and Sreelaxmi Pai, Amazon Web Services*

## Summary
<a name="run-an-asp-net-core-web-api-docker-container-on-an-amazon-ec2-linux-instance-summary"></a>

This pattern is for people who are starting to containerize their applications on the Amazon Web Services (AWS) Cloud. When you begin to containerize apps on cloud, usually there are no container orchestrating platforms set up. This pattern helps you quickly set up infrastructure on AWS to test your containerized applications without needing an elaborate container orchestrating infrastructure.

The first step in the modernization journey is to transform the application. If it's a legacy .NET Framework application, you must first change the runtime to ASP.NET Core. Then do the following:
+ Create the Docker container image
+ Run the Docker container using the built image
+ Validate the application before deploying it on any container orchestration platform, such as Amazon Elastic Container Service (Amazon ECS) or Amazon Elastic Kubernetes Service (Amazon EKS).

This pattern covers the build, run, and validate aspects of modern application development on an Amazon Elastic Compute Cloud (Amazon EC2) Linux instance.

## Prerequisites and limitations
<a name="run-an-asp-net-core-web-api-docker-container-on-an-amazon-ec2-linux-instance-prereqs"></a>

**Prerequisites **
+ An active [Amazon Web Services (AWS) account](https://aws.amazon.com/account/)
+ An [AWS Identity and Access Management (IAM) role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) with sufficient access to create AWS resources for this pattern
+ [Visual Studio Community 2022](https://visualstudio.microsoft.com/downloads/) or later downloaded and installed
+ A .NET Framework project modernized to ASP.NET Core
+ A GitHub repository

**Product versions**
+ Visual Studio Community 2022 or later

## Architecture
<a name="run-an-asp-net-core-web-api-docker-container-on-an-amazon-ec2-linux-instance-architecture"></a>

**Target architecture **

This pattern uses an [AWS CloudFormation template](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/new?stackName=SSM-SSH-Demo&templateURL=https://aws-quickstart.s3.amazonaws.com/quickstart-examples/samples/session-manager-ssh/session-manager-example.yaml) to create the highly available architecture shown in the following diagram. An Amazon EC2 Linux instance is launched in a private subnet. AWS Systems Manager Session Manager is used to access the private Amazon EC2 Linux instance and to test the API running in the Docker container.

![A user accessing the Amazon EC2 Linux instance and testing the API running in the Docker container.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/512e61b2-10ba-43be-bbd8-2bdc597c3de3/images/9c5206f6-32b1-47be-9037-360c0bff713c.png)

1. Access to the Linux instance through Session Manager

## Tools
<a name="run-an-asp-net-core-web-api-docker-container-on-an-amazon-ec2-linux-instance-tools"></a>

**AWS services**
+ [AWS Command Line Interface](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) – AWS Command Line Interface (AWS CLI) is an open source tool for interacting with AWS services through commands in your command line shell. With minimal configuration, you can run AWS CLI commands that implement functionality equivalent to that provided by the browser-based AWS Management Console.
+ [AWS Management Console](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/learn-whats-new.html) – The AWS Management Console is a web application that comprises and refers to a broad collection of service consoles for managing AWS resources. When you first sign in, you see the console home page. The home page provides access to each service console and offers a single place to access the information you need to perform your AWS related tasks.
+ [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) – Session Manager is a fully managed AWS Systems Manager capability. With Session Manager, you can manage your Amazon Elastic Compute Cloud (Amazon EC2) instances. Session Manager provides secure and auditable node management without the need to open inbound ports, maintain bastion hosts, or manage SSH keys.

**Other tools**
+ [Visual Studio 2022](https://visualstudio.microsoft.com/downloads/) – Visual Studio 2022 is an integrated development environment (IDE).
+ [Docker](https://www.docker.com/) – Docker is a set of platform as a service (PaaS) products that use virtualization at the operating-system level to deliver software in containers.

**Code**

```
FROM mcr.microsoft.com/dotnet/aspnet:5.0 AS base
 WORKDIR /app
EXPOSE 80
EXPOSE 443

FROM mcr.microsoft.com/dotnet/sdk:5.0 AS build
WORKDIR /src
COPY ["DemoNetCoreWebAPI/DemoNetCoreWebAPI.csproj", "DemoNetCoreWebAPI/"]
RUN dotnet restore "DemoNetCoreWebAPI/DemoNetCoreWebAPI.csproj"
COPY . .
WORKDIR "/src/DemoNetCoreWebAPI"
RUN dotnet build "DemoNetCoreWebAPI.csproj" -c Release -o /app/build

FROM build AS publish
RUN dotnet publish "DemoNetCoreWebAPI.csproj" -c Release -o /app/publish

FROM base AS final
WORKDIR /app
COPY --from=publish /app/publish .
ENTRYPOINT ["dotnet", "DemoNetCoreWebAPI.dll"]
```

## Epics
<a name="run-an-asp-net-core-web-api-docker-container-on-an-amazon-ec2-linux-instance-epics"></a>

### Develop the ASP.NET Core web API
<a name="develop-the-asp-net-core-web-api"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an example ASP.NET Core web API using Visual Studio. | To create an example ASP.NET Core web API, do the following:1. Open Visual Studio 2022.<br />2. Choose **Create a new project**.<br />3. Select the **ASP.NET Core Web API** project template, and choose **Next**.<br />4. For the project name, enter **DemoNetCoreWebAPI**, and choose **Next**.<br />5. Choose **Create**.<br />6. To run the project locally, press F5.<br />7. Verify that the default **WeatherForecast** API endpoint is returning the results using [Swagger](https://swagger.io/).<br />8. Open the command prompt, navigate to the .csproj project folder, and run the following commands to push the new web API to your GitHub repository. <pre>git add --all<br />git commit -m "Initial Version"<br />git push</pre> | App developer |
| Create a Dockerfile. | To create a Dockerfile, do one of the following:+ Create the Dockerfile manually using the sample Dockerfile in the *Code* section. Based on the requirements, select the appropriate .NET base image. For information about .NET and ASP.NET Core related images, see [Docker hub](https://hub.docker.com/_/microsoft-dotnet/). <br />+ Create the Dockerfile using Visual Studio and [Docker Desktop](https://www.docker.com/products/docker-desktop). In the solution explorer, right click on the project, choose **Add**->**Docker Support**. For **Target OS**, select **Linux**. Ensure that the new Dockerfile is in the same path as the solution file (.sln). <br />To push the changes to your GitHub repository, run the following command.<pre>git add --all<br />git commit -m "Dockerfile added"<br />git push</pre> | App developer |

### Set up the Amazon EC2 Linux instance
<a name="set-up-the-amazon-ec2-linux-instance"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the infrastructure. | Launch the [AWS CloudFormation template](https://console.aws.amazon.com/cloudformation/home?region=us-east-2#/stacks/new?stackName=SSM-SSH-Demo&templateURL=https://aws-quickstart.s3.amazonaws.com/quickstart-examples/samples/session-manager-ssh/session-manager-example.yaml) to create the infrastructure, which includes the following: + A virtual private cloud (VPC), using the [AWS VPC Quick Start](https://aws.amazon.com/quickstart/architecture/vpc/), with two public and two private subnets spanning two Availability Zones.<br />+ The required IAM role to enable AWS Systems Manager.<br />+ In one of the private subnets, an Amazon Linux 2 demo instance with the latest SSM Agent. Although this instance doesn’t have any direct connectivity from the internet, it can be accessed securely by using AWS Systems Manager Session Manager without requiring a bastion host.Amazon Linux 2 is nearing end of support. For more information, see the [Amazon Linux 2 FAQs](http://aws.amazon.com/amazon-linux-2/faqs/).<br />To learn more about accessing a private Amazon EC2 instance using Session Manager without requiring a bastion host, see the [Toward a bastion-less world](https://aws.amazon.com/blogs/infrastructure-and-automation/toward-a-bastion-less-world/) blog post. | App developer, AWS administrator, AWS DevOps |
| Log in to the Amazon EC2 Linux instance. | To connect to the Amazon EC2 Linux instance in the private subnet, do the following:1. Open the Amazon EC2 console.       <br />2. In the navigation pane, choose **Instances**.<br />3. Select the Amazon Linux 2 demo instance, and choose **Connect**.Amazon Linux 2 is nearing end of support. For more information, see the [Amazon Linux 2 FAQs](http://aws.amazon.com/amazon-linux-2/faqs/).<br />4. Choose **Session Manager**.<br />5. Choose **Connect** to open a new terminal window.<br />6. Run the following command.<pre> sudo su</pre> | App developer |
| Install and start Docker. | To install and start Docker in the Amazon EC2 Linux instance, do the following:1. To install Docker, run the following command.<pre>yum install -y docker</pre><br />2. To start the Docker service, run the following command.<pre> service docker start</pre><br />3. To verify Docker installation, run the following command.<pre>docker info</pre> | App developer, AWS administrator, AWS DevOps |
| Install Git and clone the repository. | To install Git on the Amazon EC2 Linux instance and clone the repository from GitHub, do the following.1. To install Git, run the following command.<pre>yum install git -y</pre><br />2. To clone the repository, run the following command.<pre>git clone https://github.com/<username>/<repo-name>.git</pre><br />3. To navigate to the Dockerfile, run the following command.<pre>cd <repo-name>/DemoNetCoreWebAPI/</pre> | App developer, AWS administrator, AWS DevOps |
| Build and run the Docker container. | To build the Docker image and run the container inside the Amazon EC2 Linux instance, do the following:1. To create the Docker image, run the following command.<pre>docker build -t aspnetcorewebapiimage -f Dockerfile .</pre><br />2. To view all the Docker images, run the following command.<pre>docker images</pre><br />3. To create and run the container, run the following command.<pre>docker run -d -p 80:80 --name aspnetcorewebapicontainer aspnetcorewebapiimage</pre> | App developer, AWS administrator, AWS DevOps |

### Test the web API
<a name="test-the-web-api"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Test the web API using the curl command. | To test the web API, run the following command.<pre>curl -X GET "http://localhost/WeatherForecast" -H  "accept: text/plain"</pre><br />Verify the API response.You can get the curl commands for each endpoint from Swagger when you are running it locally. | App developer |

### Clean up resources
<a name="clean-up-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Delete all resources. | Delete the stack to remove all the resources. This ensures that you aren’t charged for any services that you aren’t using. | AWS administrator, AWS DevOps |

## Related resources
<a name="run-an-asp-net-core-web-api-docker-container-on-an-amazon-ec2-linux-instance-resources"></a>
+ [Connect to your Linux instance from Windows using PuTTY](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/putty.html)
+ [Create a web API with ASP.NET Core](https://docs.microsoft.com/en-us/aspnet/core/tutorials/first-web-api?view=aspnetcore-5.0&tabs=visual-studio)
+ [Toward a bastion-less world](https://aws.amazon.com/blogs/infrastructure-and-automation/toward-a-bastion-less-world/)
