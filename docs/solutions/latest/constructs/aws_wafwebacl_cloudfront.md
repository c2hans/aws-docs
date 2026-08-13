---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_wafwebacl_cloudfront.html
---

# aws-wafwebacl-cloudfront
<a name="aws_wafwebacl_cloudfront"></a>

![Stability:Stable](https://img.shields.io/badge/cfn—​resources-stable-success.svg?style=for-the-badge)

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_wafwebacl_cloudfront`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-wafwebacl-cloudfront`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.wafwebaclcloudfront`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an AWS WAF web ACL connected to Amazon CloudFront.

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from 'constructs';
import { Stack, StackProps } from 'aws-cdk-lib';
import { CloudFrontToS3 } from '@aws-solutions-constructs/aws-cloudfront-s3';
import { WafwebaclToCloudFront } from "@aws-solutions-constructs/aws-wafwebacl-cloudfront";

const cloudfrontToS3 = new CloudFrontToS3(this, 'test-cloudfront-s3', {});

// This construct can only be attached to a configured CloudFront.
new WafwebaclToCloudFront(this, 'test-wafwebacl-cloudfront', {
    existingCloudFrontWebDistribution: cloudfrontToS3.cloudFrontWebDistribution
});
```

```
from aws_solutions_constructs.aws_cloudfront_s3 import CloudFrontToS3
from aws_solutions_constructs.aws_wafwebacl_cloudfront import WafwebaclToCloudFront
from aws_cdk import Stack
from constructs import Construct

cloudfront_to_s3 = CloudFrontToS3(self, 'test_cloudfront_s3')

# This construct can only be attached to a configured CloudFront.
WafwebaclToCloudFront(self, 'test_wafwebacl_cloudfront',
                      existing_cloud_front_web_distribution=cloudfront_to_s3.cloud_front_web_distribution
                      )
```

```
import software.constructs.Construct;

import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awsconstructs.services.cloudfronts3.*;
import software.amazon.awsconstructs.services.wafwebaclcloudfront.*;

final CloudFrontToS3 cloudfrontToS3 = new CloudFrontToS3(this, "test-cloudfront-s3",
        new CloudFrontToS3Props.Builder()
                .build());

// This construct can only be attached to a configured CloudFront.
new WafwebaclToCloudFront(this, "test-wafwebacl-cloudfront", new WafwebaclToCloudFrontProps.Builder()
        .existingCloudFrontWebDistribution(cloudfrontToS3.getCloudFrontWebDistribution())
        .build());
```

## Pattern Construct Props
<a name="_pattern_construct_props"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| existingCloudFrontWebDistribution |  [`cloudfront.Distribution`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudfront.Distribution.html)  | The existing CloudFront instance that will be protected with the WAF web ACL. *Note that a WAF web ACL can only be added to a configured CloudFront, so this construct only accepts an existing Distribution and does not accept cloudfrontProps.*  |
| existingWebaclObj? |  [`waf.CfnWebACL`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_wafv2.CfnWebACL.html)  | Optional - existing instance of a WAF web ACL, providing both this and `webaclProps` causes an error. |
| webaclProps? |  [`waf.CfnWebACLProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_wafv2.CfnWebACLProps.html)  | Optional user-provided props to override the default props for the AWS WAF web ACL. Providing both this and existingWebaclObj causes an error. To use a different collection of managed rule sets, specify a new rules property. Use our [wrapManagedRuleSet(managedGroupName: string, vendorName: string, priority: number)](../core/lib/waf-defaults.ts) function from core to create an array entry from each desired managed rule set. |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| webacl |  [`waf.CfnWebACL`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_wafv2.CfnWebACL.html)  | Returns an instance of the waf.CfnWebACL created by the construct. |
| cloudFrontWebDistribution |  [`cloudfront.Distribution`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_cloudfront.Distribution.html)  | Returns an instance of cloudfront.Distribution created by the construct. |

## Default settings
<a name="_default_settings"></a>

Out of the box implementation of the Construct without any override will set the following defaults:

### AWS WAF
<a name="_aws_waf"></a>
+ Deploy a WAF web ACL with 7 [AWS managed rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-list.html).
  + AWSManagedRulesBotControlRuleSet
  + AWSManagedRulesKnownBadInputsRuleSet
  + AWSManagedRulesCommonRuleSet
  + AWSManagedRulesAnonymousIpList
  + AWSManagedRulesAmazonIpReputationList
  + AWSManagedRulesAdminProtectionRuleSet
  + AWSManagedRulesSQLiRuleSet

     *Note that the default rules can be replaced by specifying the rules property of CfnWebACLProps*
+ Send metrics to Amazon CloudWatch

### Amazon CloudFront
<a name="_amazon_cloudfront"></a>
+ User provided CloudFront object is used as-is

## Architecture
<a name="_architecture"></a>

![Diagram showing the WAF ACL, CloudFront distribution, CloudWatch log group and IAM role created by the construct](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-wafwebacl-cloudfront.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-wafwebacl-cloudfront) for this pattern to view the code, read/create issues and pull requests and more.
