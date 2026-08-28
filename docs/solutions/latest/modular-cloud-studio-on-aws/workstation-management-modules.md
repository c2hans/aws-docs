---
source_url: https://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/workstation-management-modules.html
---

# Workstation Management modules
<a name="workstation-management-modules"></a>

Workstation Management modules create the necessary resources to provide virtual workstations to users in the post-production environment. This way, users can gain cloud performance by connecting remotely only from their local laptop, and handle auto-scaling based on policies.

The following Workstation Management modules are available in MCS after deployment:
+ Leostream Broker module - Manages assignment and auto scaling of workstations
+ Leostream Gateway module - Manages connections to workstations

**Note**
Modular Cloud Studio on AWS allows you to deploy and manage a scalable, secure, and global content production infrastructure in the cloud. This includes custom modules, developed by AWS Partners or other third parties, that you can choose to use ("Third-Party Modules"). AWS does not own or otherwise have any control over Third-Party Modules.
Your use of the Third-Party Modules is governed by any terms provided to you by the Third-Party Module providers when you acquired your license to use them (for example, their terms of service, license agreement, acceptable use policy, and privacy policy). You are responsible for ensuring that your use of the Third-Party Modules comply with any terms governing them, and any laws, rules, regulations, policies, or standards that apply to you.
You are also responsible for making your own independent assessment of the Third-Party Modules that you use. AWS does not make any representations, warranties, or guarantees regarding the Third-Party Modules, which are "Third-Party Content" under your agreement with AWS. Modular Cloud Studio on AWS is offered to you as "AWS Content" under your agreement with AWS.

## Leostream Broker module
<a name="leostream-broker-module"></a>

![leostream broker module](http://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/images/leostream-broker-module.png)

1. A privately [hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/route-53-concepts.html#route-53-concepts-hosted-zone) in [Amazon Route 53](https://aws.amazon.com/route53/) routes requests to an [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) that is accessible through a private subnet. This Application Load Balancer manages connections to an [Amazon EC2 Auto Scaling Group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html).

1. This module manages Leostream workstations on [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html).

1. An [Amazon EC2 Auto Scaling Group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html) maintains the necessary number of Leostream Broker instances on [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html).

1. The Leostream Broker EC2 instances use an [Amazon Relational Databases Service (Amazon RDS) for PostgreSQL](https://aws.amazon.com/rds/postgresql/) database.

   Database configuration:
   + A dedicated "leostream" user is provisioned with specific permissions
   + User can create, read, update, and delete databases and tables
   + Operates with restricted privileges compared to the default administrator account
   + Default admin user credentials are not exposed to or utilized by Leostream modules

1.  [Amazon EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html) is used upon deployment to build the AMI for the Leostream Broker EC2 instances along with both Windows and Linux AMIs that the Leostream Broker module uses.

## Spoke Leostream Broker module
<a name="spoke-leostream-broker-module"></a>

![spoke leostream broker module](http://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/images/spoke-leostream-broker-module.png)

1. The Leostream Broker cluster in the hub variant of this module manages workstations on [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html).

1. Workstations use the same AMIs built by the Leostream Broker module in the hub Region. The Spoke Leostream Broker module copies AMIs from the hub Region into the spoke Region.

## Leostream Gateway module
<a name="leostream-gateway-module"></a>

![leostream gateway module](http://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/images/leostream-gateway-module.png)

1. Optionally, when a certificate and hosted zone are configured, a [hosted zone](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/hosted-zones-working-with.html) on [Amazon Route 53](https://aws.amazon.com/route53) routes requests to [AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html).

1. The module deploys an [AWS Global Accelerator](https://docs.aws.amazon.com/global-accelerator/latest/dg/what-is-global-accelerator.html) and uses it to manage connections with Leostream Gateway to either a workstation or the Leostream Broker cluster.

1. The module uses the [Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) deployed by the Leostream Broker module which manages traffic to the [Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html) Group for Leostream Broker instances.

1.  [Amazon DCV](https://aws.amazon.com/hpc/dcv/) traffic is routed securely between the AWS Global Accelerator, Leostream Gateway, and workstations.

1. An [Auto Scaling Group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html) maintains the necessary number of Leostream Gateway instances on [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html).

1. Auto Scaling events invoke workflows in [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) via [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/) to manage Leostream Gateway registrations.

1. The AMI used by Leostream Gateway EC2 instances is built during deployment using [Amazon EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html).

## Spoke Leostream Gateway module
<a name="spoke-leostream-gateway-module"></a>

![spoke leostream gateway module](http://docs.aws.amazon.com/solutions/latest/modular-cloud-studio-on-aws/images/spoke-leostream-gateway-module.png)

1. Auto Scaling events invoke workflows in [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) via [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/) to manage Leostream Gateway registrations.

1.  [Amazon DCV](https://aws.amazon.com/hpc/dcv/) traffic is routed securely between the [AWS Global Accelerator](https://aws.amazon.com/global-accelerator/), Leostream Gateway, and workstations.

1. Workstations use the same AMIs built by the Leostream Broker module in the hub Region.

1. An [Auto Scaling Group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html) maintains the necessary number of Leostream Gateway instances on [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
