---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_route53_alb.html
---

# aws-route53-alb
<a name="aws_route53_alb"></a>

![Stability:Experimental](https://img.shields.io/badge/stability-Experimental-important.svg?style=for-the-badge)

All classes are under active development and subject to non-backward compatible changes or removal in any future version. These are not subject to the [Semantic Versioning](https://semver.org/) model. This means that while you may use them, you may need to update your source code when upgrading to a newer version of this package.

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_route53_alb`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-route53-alb`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.route53alb`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an Amazon Route53 Hosted Zone routing to an Application Load Balancer

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { Route53ToAlb } from '@aws-solutions-constructs/aws-route53-alb';

// Note - all alb constructs turn on ELB logging by default, so require that an environment including account
// and region be provided when creating the stack
//
// new MyStack(app, 'id', {env: {account: '123456789012', region: 'us-east-1' }});
new Route53ToAlb(this, 'Route53ToAlbPattern', {
  privateHostedZoneProps: {
    zoneName: 'www.example.com',
  },
  publicApi: false,
});
```

```
from aws_solutions_constructs.aws_route53_alb import Route53ToAlb
from aws_cdk import (
    aws_route53 as route53,
    Stack
)
from constructs import Construct

# Note - all alb constructs turn on ELB logging by default, so require that an environment including account
# and region be provided when creating the stack
#
# MyStack(app, 'id', env=cdk.Environment(account='123456789012', region='us-east-1'))
Route53ToAlb(self, 'Route53ToAlbPattern',
                public_api=False,
                private_hosted_zone_props=route53.HostedZoneProps(
                    zone_name='www.example.com',
                )
                )
```

```
import software.constructs.Construct;

import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awscdk.services.route53.*;
import software.amazon.awsconstructs.services.route53alb.*;

// Note - all alb constructs turn on ELB logging by default, so require that an environment including account
// and region be provided when creating the stack
//
// new MyStack(app, "id", StackProps.builder()
//         .env(Environment.builder()
//                 .account("123456789012")
//                 .region("us-east-1")
//                 .build());
new Route53ToAlb(this, "Route53ToAlbPattern",
        new Route53ToAlbProps.Builder()
                .privateHostedZoneProps(new HostedZoneProps.Builder()
                        .zoneName("www.example.com")
                        .build())
                .publicApi(false)
                .build());
```

## Pattern Construct Props
<a name="_pattern_construct_props"></a>

This construct cannot create a new Public Hosted Zone, if you are creating a public API you must supply an existing Public Hosted Zone that will be reconfigured with a new Alias record. Public Hosted Zones are configured with public domain names and are not well suited to be launched and torn down dynamically, so this construct will only reconfigure existing Public Hosted Zones.

This construct can create Private Hosted Zones. If you want a Private Hosted Zone, then you can either provide an existing Private Hosted Zone or a privateHostedZoneProps value with at least the Domain Name defined.

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| privateHostedZoneProps? |  [route53.PrivateHostedZoneProps](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_route53.PrivateHostedZoneProps.html)  | Optional custom properties for a new Private Hosted Zone. Cannot be specified for a public API. Cannot specify a VPC, it will use the VPC in existingVpc or the VPC created by the construct. Providing both this and existingHostedZoneInterfacecauses an error. |
| existingHostedZoneInterface? |  [route53.IHostedZone](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_route53.IHostedZone.html)  | Existing Public or Private Hosted Zone (type must match publicApi setting). Specifying both this and privateHostedZoneProps causes an error. If this is a Private Hosted Zone, the associated VPC must be provided as the existingVpc property |
| loadBalancerProps? |  [elasticloadbalancingv2.ApplicationLoadBalancerProps](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_elasticloadbalancingv2.ApplicationLoadBalancerProps.html)  | Optional custom properties for a new loadBalancer. Providing both this and existingLoadBalancer causes an error. This cannot specify a VPC, it will use the VPC in existingVpc or the VPC created by the construct. |
| existingLoadBalancerObj? |  [elasticloadbalancingv2.ApplicationLoadBalancer](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_elasticloadbalancingv2.ApplicationLoadBalancer.html)  | Existing Application Load Balancer to incorporate into the construct architecture. Providing both this and loadBalancerProps causes an error. The VPC containing this loadBalancer must match the VPC provided in existingVpc. |
| vpcProps? |  [ec2.VpcProps](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.VpcProps.html)  | Optional custom properties for a VPC the construct will create. This VPC will be used by the new ALB and any Private Hosted Zone the construct creates (that’s why loadBalancerProps and privateHostedZoneProps can’t include a VPC). Providing both this and existingVpc causes an error. |
| existingVpc? |  [ec2.IVpc](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html)  | An existing VPC in which to deploy the construct. Providing both this and vpcProps causes an error. If the client provides an existing load balancer and/or existing Private Hosted Zone, those constructs must exist in this VPC. |
| logAlbAccessLogs? | boolean | Whether to turn on Access Logs for the Application Load Balancer. Uses an S3 bucket with associated storage costs.Enabling Access Logging is a best practice. default - true |
| albLoggingBucketProps? |  [s3.BucketProps](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_s3.BucketProps.html)  | Optional properties to customize the bucket used to store the ALB Access Logs. Supplying this and setting logAlbAccessLogs to false is an error. @default - none |

```
publicApi | boolean | Whether the construct is deploying a private or public API. This has implications for the Hosted Zone, VPC and ALB. |
```

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| hostedZone |  [route53.IHostedZone](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_route53.IHostedZone.html)  | The hosted zone used by the construct (whether created by the construct or providedb by the client) |
| vpc |  [ec2.IVpc](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_ec2.IVpc.html)  | The VPC used by the construct (whether created by the construct or providedb by the client) |
| loadBalancer |  [elasticloadbalancingv2.ApplicationLoadBalancer](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_elasticloadbalancingv2.ApplicationLoadBalancer.html)  | The Load Balancer used by the construct (whether created by the construct or providedb by the client) |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any override will set the following defaults:

### Amazon Route53
<a name="_amazon_route53"></a>
+ Adds an ALIAS record to the new or provided Hosted Zone that routes to the construct’s ALB

### Application Load Balancer
<a name="_application_load_balancer"></a>
+ Creates an Application Load Balancer with no Listener or target. The construct can incorporate an existing, fully configured ALB if provided.

## Architecture
<a name="_architecture"></a>

![Diagram showing the Route53 ALIAS record in an existing hosted zone and Application Load Balancer created by the construct](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-route53-alb.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-route53-alb) for this pattern to view the code, read/create issues and pull requests and more.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Solutions. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
