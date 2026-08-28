---
source_url: https://docs.aws.amazon.com/cdk/v2/guide/deploy-troubleshoot.html
---

This is the AWS CDK v2 Developer Guide. The older CDK v1 entered maintenance on June 1, 2022 and ended support on June 1, 2023.

# Troubleshoot AWS CDK deployments
<a name="deploy-troubleshoot"></a>

Troubleshoot common issues when deploying AWS Cloud Development Kit (AWS CDK) applications.

## Incorrect service principals are being created at deployment
<a name="deploy-troubleshoot-sp"></a>

When deploying CDK applications that contain AWS Identity and Access Management (IAM) roles with service principals, you find that incorrect domains for the service principals are being created.

The following is a basic example of creating an IAM role that can be assumed by Amazon CloudWatch Logs using its service principal:

```
import * as cdk from 'aws-cdk-lib';
import * as iam from 'aws-cdk-lib/aws-iam';
import { Construct } from 'constructs';

export class MyCdkProjectStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    // Create an IAM role for CloudWatch Logs to assume
    const cloudWatchLogsRole = new iam.Role(this, 'CloudWatchLogsRole', {
      assumedBy: new iam.ServicePrincipal('logs.amazonaws.com'), // This is for CloudWatch Logs
      managedPolicies: [
        iam.ManagedPolicy.fromAwsManagedPolicyName('service-role/AWSCloudWatchLogsFullAccess')
      ]
    });

    // You can then use this role in other constructs or configurations where CloudWatch Logs needs to assume a role
  }
}
```

When you deploy this stack, a service principal named `logs.amazonaws.com` should be created. In most cases, AWS services use the following naming for service principals: `<service>.amazonaws.com`.

### Common causes
<a name="deploy-troubleshoot-sp-causes"></a>

If you are using a version of the AWS CDK older than v2.150.0, you may encounter this bug. In older AWS CDK versions, the naming of service principals were not standardized, which could lead to the creation of service principals with incorrect domains.

In AWS CDK v2.51.0, a fix was implemented by standardizing all automatically created service principals to use `<service>.amazonaws.com` when possible. This fix was available by allowing the `@aws-cdk/aws-iam:standardizedServicePrincipals` feature flag.

Starting in AWS CDK v2.150.0, this became default behavior.

### Resolution
<a name="deploy-troubleshoot-sp-resolution"></a>

Upgrade to AWS CDK v2.150.0 or newer.

If you are unable to upgrade to AWS CDK v2.150.0 or newer, you must upgrade to at least v2.51.0 or newer. Then, allow the following feature flag in your `cdk.json` file: `@aws-cdk/aws-iam:standardizedServicePrincipals`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Cloud Development Kit. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
