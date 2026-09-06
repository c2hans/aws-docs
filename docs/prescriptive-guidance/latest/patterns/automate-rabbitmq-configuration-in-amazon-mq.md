---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-rabbitmq-configuration-in-amazon-mq.html
---

# Automate RabbitMQ configuration in Amazon MQ
<a name="automate-rabbitmq-configuration-in-amazon-mq"></a>

*Yogesh Bhatia and Afroz Khan, Amazon Web Services*

## Summary
<a name="automate-rabbitmq-configuration-in-amazon-mq-summary"></a>

[Amazon MQ](https://docs.aws.amazon.com/amazon-mq/) is a managed message broker service that provides compatibility with many popular message brokers. Using Amazon MQ with RabbitMQ provides a robust RabbitMQ cluster managed in the AWS Cloud with multiple brokers and configuration options. Amazon MQ provides a highly available, secure, and scalable infrastructure, and can process a large number of messages per second with ease. Multiple applications can use the infrastructure with different virtual hosts, queues, and exchanges. However, managing these configuration options or creating the infrastructure manually can require time and effort. This pattern describes a way to manage configurations for RabbitMQ in one step, through a single file. You can embed the code provided with this pattern within any continuous integration (CI) tool such as Jenkins or Bamboo.

You can use this pattern to configure any RabbitMQ cluster. All it requires is connectivity to the cluster. Although there are many other ways to manage RabbitMQ configurations, this solution creates entire application configurations in one step, so you can manage queues and other details easily.

## Prerequisites and limitations
<a name="automate-rabbitmq-configuration-in-amazon-mq-prereqs"></a>

**Prerequisites**
+ AWS Command Line Interface (AWS CLI) [installed and configured](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2-linux.html) to point to your AWS account
+ Ansible installed, so you can run playbooks to create the configuration
+ **rabbitmqadmin **installed (for instructions, see the [RabbitMQ documentation](https://www.rabbitmq.com/management-cli.html))
+ A RabbitMQ cluster in Amazon MQ, created with healthy Amazon CloudWatch metrics

**Additional requirements**
+ Make sure to create the configurations for virtual hosts and users separately and not as part of JSON.
+ Make sure that the configuration JSON is part of the repository and is version-controlled.
+ The version of the **rabbitmqadmin **CLI must be the same as the version of the RabbitMQ server, so the best option is to download the CLI from the RabbitMQ console.
+ As part of the pipeline, make sure that JSON syntax is validated before each run.

**Product versions**
+ AWS CLI version 2.0
+ Ansible version 2.9.13
+ **rabbitmqadmin **version 3.9.13 (must be the same as the RabbitMQ server version)

## Architecture
<a name="automate-rabbitmq-configuration-in-amazon-mq-architecture"></a>

**Source technology stack  **
+ An RabbitMQ cluster running on an existing on-premises virtual machine (VM) or a Kubernetes cluster (on premises or in the cloud)

**Target technology stack  **
+ Automated RabbitMQ configurations on Amazon MQ for RabbitMQ

**Target architecture **

There are many ways to configure RabbitMQ. This pattern uses the import configuration functionality, where a single JSON file contains all the configurations. This file applies all settings and can be managed by a version-control system such as Bitbucket or Git. This pattern uses Ansible to implement the configuration through the **rabbitmqadmin **CLI.

![Automating RabbitMQ configuration in Amazon MQ](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/294120b6-c95f-4cc5-bf85-5ad7e2abdad5/images/292e1284-5c9e-4c82-bb41-010fa84d8d74.png)

## Tools
<a name="automate-rabbitmq-configuration-in-amazon-mq-tools"></a>

**AWS services**
+ [Amazon MQ](https://docs.aws.amazon.com/amazon-mq/) is a managed message broker service that makes it easy to set up and operate message brokers in the cloud.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up your AWS infrastructure and speed up cloud provisioning with infrastructure as code.
+ [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) enables you to interact with AWS services by using commands in a command-line shell.

**Other tools**
+ [rabbitmqadmin](https://www.rabbitmq.com/management-cli.html) is a command-line tool for the RabbitMQ HTTP-based API. It is used to manage and monitor RabbitMQ nodes and clusters.
+ [Ansible](https://www.ansible.com/) is an open-source tool for automating applications and IT infrastructure.

**Code repository**

The JSON configuration file used in this pattern and a sample Ansible playbook are provided in the attachment.

## Epics
<a name="automate-rabbitmq-configuration-in-amazon-mq-epics"></a>

### Create your AWS infrastructure
<a name="create-your-aws-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a RabbitMQ cluster on AWS. | If you don't already have a RabbitMQ cluster, you can use [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) to create the stack on AWS. Or, you can use the [CloudFormation module in Ansible](https://docs.ansible.com/projects/ansible/latest/collections/amazon/aws/cloudformation_module.html) to create the stack. With the latter approach, you can use Ansible for both tasks: to create the RabbitMQ infrastructure and to manage configurations.  | General AWS, Ansible |

### Create the Amazon MQ for RabbitMQ configuration
<a name="create-the-amqlong-for-rabbitmq-configuration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a properties file. | Download the JSON configuration file (`rabbitmqconfig.json`) in the attachment, or export it from the RabbitMQ console.  Modify it to configure queues, exchanges, and bindings. This configuration file demonstrates the following:+ Creates two queues: `sample-queue1` and `sample-queue2` <br />+ Creates two exchanges: `sample-exchange1` and `sample-exchange2`<br />+ Implements the binding between the queues and exchanges<br />These configurations are performed under the root (/) virtual host, as required by **rabbitmqadmin**.  | JSON |
| Retrieve the details of the Amazon MQ for RabbitMQ infrastructure. | Retrieve the following details for the RabbitMQ infrastructure on AWS:+ Broker name<br />+ RabbitMQ host<br />+ RabbitMQ user name (the administrator user created during cluster creation)<br />+ RabbitMQ password<br />You can use the AWS Management Console or the AWS CLI to retrieve this information. These details enable the Ansible playbook to connect to your AWS account and use the RabbitMQ cluster to run commands.The computer that runs the Ansible playbook must be able to access your AWS account, and AWS CLI must already be configured, as described in the *Prerequisites* section. | General AWS |
| Create the `hosts_var` file. | Create the `hosts_var` file for Ansible and make sure that all the variables are defined in the file. Consider using Ansible Vault to store the password. You can configure the `hosts_var` file as follows (replace the asterisks with your information):<pre>RABBITMQ_HOST: "***********.mq.us-east-2.amazonaws.com"<br />RABBITMQ_VHOST: "/"<br />RABBITMQ_USERNAME: "admin"<br />RABBITMQ_PASSWORD: "*******"</pre> | Ansible |
| Create an Ansible playbook. | For a sample playbook, see `ansible-rabbit-config.yaml` in the attachment. Download and save this file. The Ansible playbook imports and manages all RabbitMQ configurations, such as queues, exchanges, and bindings, that applications require. <br />Follow best practices for Ansible playbooks, such as securing passwords. Use Ansible Vault for password encryption, and retrieve the RabbitMQ password from the encrypted file. | Ansible |

### Deploy the configuration
<a name="deploy-the-configuration"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run the playbook. | Run the Ansible playbook that you created in the previous epic.<pre>ansible-playbook ansible-rabbit-config.yaml</pre><br />You can verify the new configurations on the RabbitMQ console. | General AWS, RabbitMQ, Ansible |

## Related resources
<a name="automate-rabbitmq-configuration-in-amazon-mq-resources"></a>
+ [Migrating from RabbitMQ to Amazon MQ](https://aws.amazon.com/blogs/compute/migrating-from-rabbitmq-to-amazon-mq/) (AWS blog post)
+ [Management Command Line Tool](https://www.rabbitmq.com/management-cli.html) (RabbitMQ documentation)
+ [Create or delete an AWS CloudFormation stack](https://docs.ansible.com/ansible/latest/collections/amazon/aws/cloudformation_module.html) (Ansible documentation)
+ [Migrating message driven applications to Amazon MQ for RabbitMQ](https://aws.amazon.com/blogs/compute/migrating-message-driven-applications-to-amazon-mq-for-rabbitmq/) (AWS blog post)

## Attachments
<a name="attachments-294120b6-c95f-4cc5-bf85-5ad7e2abdad5"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/294120b6-c95f-4cc5-bf85-5ad7e2abdad5/attachments/attachment.zip)
