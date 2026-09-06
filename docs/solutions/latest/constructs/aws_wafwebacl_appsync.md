---
source_url: https://docs.aws.amazon.com/solutions/latest/constructs/aws_wafwebacl_appsync.html
---

# aws-wafwebacl-appsync
<a name="aws_wafwebacl_appsync"></a>

![Stability:Stable](https://img.shields.io/badge/cfn—​resources-stable-success.svg?style=for-the-badge)

|  |  |
| --- |--- |
|  Reference Documentation: | https://docs.aws.amazon.com/solutions/latest/constructs/ |

|  **Language**  |  **Package**  |
| --- | --- |
|  ![Python Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/python32.png) Python |  `aws_solutions_constructs.aws_wafwebacl_appsync`  |
|  ![Typescript Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/typescript32.png) Typescript |  `@aws-solutions-constructs/aws-wafwebacl-appsync`  |
|  ![Java Logo](https://docs.aws.amazon.com/images/solutions/latest/constructs/images/java32.png) Java |  `software.amazon.awsconstructs.services.wafwebaclappsync`  |

## Overview
<a name="_overview"></a>

This AWS Solutions Construct implements an AWS WAF web ACL connected to an AWS AppSync API.

Here is a minimal deployable pattern definition:

**Example**

```
import { Construct } from "constructs";
import { Stack, StackProps } from "aws-cdk-lib";
import {
  WafwebaclToAppsyncProps,
  WafwebaclToAppsync,
} from "@aws-solutions-constructs/aws-wafwebacl-appsync";

// Use an existing AppSync GraphQL API
const existingGraphQLApi = previouslyCreatedApi;

// This construct can only be attached to a configured AWS AppSync API.
new WafwebaclToAppsync(this, "test-wafwebacl-appsync", {
  existingAppsyncApi: existingGraphQLApi,
});
```

```
from aws_solutions_constructs.aws_wafwebacl_appsync import WafwebaclToAppsyncProps, WafwebaclToAppsync
from aws_cdk import (
    aws_route53 as route53,
    Stack
)
from constructs import Construct

# Use an existing AppSync API
existingGraphQLApi = previouslyCreatedApi

# This construct can only be attached to a configured AWS AppSync API.
WafwebaclToAppsync(self, 'test_wafwebacl_appsync',
                existing_appsync_api=existingGraphQLApi
                )
```

```
import software.constructs.Construct;

import software.amazon.awscdk.Stack;
import software.amazon.awscdk.StackProps;
import software.amazon.awsconstructs.services.wafwebaclappsync.*;

// Use an existing AppSync API
final existingGraphQLApi = previouslyCreatedApi

// This construct can only be attached to a configured AWS AppSync API.
new WafwebaclToAppsync(this, "test-wafwebacl-appsync", new WafwebaclToAppsyncProps.Builder()
        .existingAppsyncApi(existingGraphQLApi)
        .build());
```

## Pattern Construct Props
<a name="_pattern_construct_props"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| existingAppsyncApi |  [`appsync.CfnGraphQLApi`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_appsync.CfnGraphQLApi.html)  | The existing Appsync CfnGraphQLApi object that will be protected with the WAF web ACL. *Note that a WAF web ACL can only be added to a configured AppSync API, so this construct only accepts an existing CfnGraphQLApi and does not accept CfnGraphQLApiProps.*  |
| existingWebaclObj? |  [`waf.CfnWebACL`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_waf.CfnWebACL.html)  | Optional - existing instance of a WAF web ACL, providing both this and `webaclProps` causes an error. |
| webaclProps? |  [`waf.CfnWebACLProps`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_waf.CfnWebACLProps.html)  | Optional user-provided props to override the default props for the AWS WAF web ACL. Providing both this and existingWebaclObj causes an error. To use a different collection of managed rule sets, specify a new rules property. Use our [wrapManagedRuleSet(managedGroupName: string, vendorName: string, priority: number)](../core/lib/waf-defaults.ts) function from core to create an array entry from each desired managed rule set. |

## Pattern Properties
<a name="_pattern_properties"></a>

|  **Name**  |  **Type**  |  **Description**  |
| --- | --- | --- |
| webacl |  [`waf.CfnWebACL`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_waf.CfnWebACL.html)  | Returns an instance of the waf.CfnWebACL created by the construct. |
| appsyncApi |  [`appsync.CfnGraphQLApi`](https://docs.aws.amazon.com/cdk/api/v2/docs/aws-cdk-lib.aws_appsync.CfnGraphQLApi.html)  | Returns an instance of the CfnGraphQLApi used by the pattern. |

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

### AppSync API
<a name="_appsync_api"></a>
+ User provided AppSync graphql API object is used as-is

## Architecture
<a name="_architecture"></a>

![Diagram showing the WAF ACL, AppSync api, CloudWatch log group and IAM role created by the construct](http://docs.aws.amazon.com/solutions/latest/constructs/images/aws-wafwebacl-appsync.png)

## Github
<a name="_github"></a>

Go to the [Github repo](https://github.com/awslabs/aws-solutions-constructs/tree/main/source/patterns/%40aws-solutions-constructs/aws-wafwebacl-appsync) for this pattern to view the code, read/create issues and pull requests and more.
