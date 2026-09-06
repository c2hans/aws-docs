---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containers-by-using-elastic-beanstalk.html
---

# Deploy containers by using Elastic Beanstalk
<a name="deploy-containers-by-using-elastic-beanstalk"></a>

*Thomas Scott and Jean-Baptiste Guillois, Amazon Web Services*

## Summary
<a name="deploy-containers-by-using-elastic-beanstalk-summary"></a>

On the Amazon Web Services (AWS) Cloud, AWS Elastic Beanstalk supports Docker as an available platform, so that containers can run with the created environment. This pattern shows how to deploy containers using the Elastic Beanstalk service. The deployment of this pattern will use the web server environment based on the Docker platform.

To use Elastic Beanstalk for deploying and scaling web applications and services, you upload your code and the deployment is automatically handled. Capacity provisioning, load balancing, automatic scaling, and application health monitoring are also included. When you use Elastic Beanstalk, you can take full control over the AWS resources that it creates on your behalf. There is no additional charge for Elastic Beanstalk. You pay only for the AWS resources that are used to store and run your applications.

This pattern includes instructions for deployment using the [AWS Elastic Beanstalk Command Line Interface (EB CLI)](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install-advanced.html) and the AWS Management Console.

**Use cases**

Use cases for Elastic Beanstalk include the following:
+ Deploy a prototype environment to demo a frontend application. (This pattern uses a Dockerfile** **as the example.)
+ Deploy an API to handle API requests for a given domain.
+ Deploy an orchestration solution using Docker-Compose (`docker-compose.yml` is** **not used as the practical example in this pattern).

## Prerequisites and limitations
<a name="deploy-containers-by-using-elastic-beanstalk-prereqs"></a>

**Prerequisites **
+ An AWS account
+ AWS EB CLI locally installed
+ Docker installed on a local machine

**Limitations **
+ There is a Docker pull limit of 100 pulls per 6 hours per IP address on the free plan.

## Architecture
<a name="deploy-containers-by-using-elastic-beanstalk-architecture"></a>

**Target technology stack **
+ Amazon Elastic Compute Cloud (Amazon EC2) instances
+ Security group
+ Application Load Balancer
+ Auto Scaling group

**Target architecture **

![Architecture for deploying containers with Elastic Beanstalk.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/dfabcdc2-747f-40e2-a603-08ea31ba71d3/images/1d17ff09-1aea-4c72-adb5-eaf741601428.png)

**Automation and scale**

AWS Elastic Beanstalk can automatically scale based on the number of requests made. AWS resources created for an environment include one Application Load Balancer, an Auto Scaling group, and one or more Amazon EC2 instances.

The load balancer sits in front of the Amazon EC2 instances, which are part of the Auto Scaling group. Amazon EC2 Auto Scaling automatically starts additional Amazon EC2 instances to accommodate increasing load on your application. If the load on your application decreases, Amazon EC2 Auto Scaling stops instances, but it keeps at least one instance running.

**Automatic scaling triggers**

The Auto Scaling group in your Elastic Beanstalk environment uses two Amazon CloudWatch alarms to initiate scaling operations. The default triggers scale when the average outbound network traffic from each instance is higher than 6 MB or lower than 2 MB over a period of five minutes. To use Amazon EC2 Auto Scaling effectively, configure triggers that are appropriate for your application, instance type, and service requirements. You can scale based on several statistics including latency, disk I/O, CPU utilization, and request count. For more information, see [Auto Scaling triggers](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-autoscaling-triggers.html).

## Tools
<a name="deploy-containers-by-using-elastic-beanstalk-tools"></a>

**AWS services**
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open-source tool that helps you interact with AWS services through commands in your command-line shell.
+ [AWS EB Command Line Interface (EB CLI)](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install.html) is a command-line client that you can use to create, configure, and manage Elastic Beanstalk environments.
+ [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) distributes incoming application or network traffic across multiple targets. For example, you can distribute traffic across Amazon Elastic Compute Cloud (Amazon EC2) instances, containers, and IP addresses in one or more Availability Zones.

**Other services**
+ [Docker](https://www.docker.com/) packages software into standardized units called containers that include libraries, system tools, code, and runtime.

**Code**

The code for this pattern is available in the GitHub [Cluster Sample Application](https://github.com/aws-samples/cluster-sample-app) repository.

## Epics
<a name="deploy-containers-by-using-elastic-beanstalk-epics"></a>

### Build with a Dockerfile
<a name="build-with-a-dockerfile"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the remote repository. | + To clone the repository, run the command `git clone https://github.com/aws-samples/cluster-sample-app.git`.< /p> | App developer, AWS administrator, AWS DevOps |
| Initialize the Elastic Beanstalk Docker project. | 1. Create a file called `aws.json` at the root.<br />2. In the `aws.json` file, add the following code.<pre>{<br />         "AWSEBDockerrunVersion":"1",<br />         "Image":{<br />            "Name":"cluster-sample-app"<br />         },<br />         "Ports":[<br />            {<br />               "ContainerPort":80,<br />               "HostPort":8080<br />            }<br />         ]<br />      }</pre><br />3. Run the command `eb init -p docker `at the root of the project. | App developer, AWS administrator, AWS DevOps |
| Test the project locally. | 1. Run the command `eb local run` at the root of the project.<br />2. Test the application by navigating to `http://localhost`. | App developer, AWS administrator, AWS DevOps |

### Deploy using EB CLI
<a name="deploy-using-eb-cli"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run deployment command | 1. Run the command `eb create docker-sample-cluster-app `at the root of the project. | App developer, AWS administrator, AWS DevOps |
| Access the deployed version. | After the deployment command has finished, access the project using the `eb open` command. | App developer, AWS administrator, AWS DevOps |

### Deploy using the console
<a name="deploy-using-the-console"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the application by using the browser. | 1. Open the console.<br />2. Navigate to the Elastic Beanstalk console.<br />3. Choose **Create Application.**<br />4. For the **Application Name**, enter **Cluster-Sample-App**.<br />5. Choose **Docker** as the platform.<br />6. Choose **Upload your code.**<br />7. Choose your local .zip file (in the root of the cloned project) or a public Amazon Simple Storage Service (Amazon S3) URL. | App developer, AWS administrator, AWS DevOps |
| Access the deployed version. | After deployment, access the deployed application, and choose the URL provided. | App developer, AWS administrator, AWS DevOps |

## Related resources
<a name="deploy-containers-by-using-elastic-beanstalk-resources"></a>
+ [Web server environments](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/concepts-webserver.html)
+ [Install the EB CLI on macOS](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install-osx.html)
+ [Manually install the EB CLI](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/eb-cli3-install-advanced.html)

## Additional information
<a name="deploy-containers-by-using-elastic-beanstalk-additional"></a>

**Advantages of using Elastic Beanstalk**
+ Automatic infrastructure provisioning
+ Automatic management of the underlying platform
+ Automatic patching and updates to support the application
+ Automatic scaling of the application
+ Ability to customize the number of nodes
+ Ability to access the infrastructure components if needed
+ Ease of deployment over other container deployment solutions
