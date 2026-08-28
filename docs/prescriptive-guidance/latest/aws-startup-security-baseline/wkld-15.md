---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/aws-startup-security-baseline/wkld-15.html
---

# WKLD.15 Define security controls in templates and deploy them by using CI/CD practices
<a name="wkld-15"></a>

*Infrastructure as code (IaC)* is the practice of defining your AWS resources and configurations in templates and code that you deploy by using continuous integration and continuous delivery (CI/CD) pipelines, the same pipelines used to deploy software applications. IaC tools, such as [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) and the [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html), support IAM identity-based and resource-based policies and integrate with AWS services, such as AWS WAF and Amazon VPC. Define your IAM policies, resource-based policies, and security service configurations as IaC templates. Commit the templates to a source code repository and deploy them by using CI/CD pipelines.

Commit application permission policies with application code in the same repository. Manage general resource policies and security service configurations in separate repositories and deployment pipelines. This separation reduces the risk of a single compromised repository affecting both application code and security configurations.

The following TypeScript AWS CDK stack demonstrates three foundational security controls from this document: an Amazon S3 bucket with `BlockPublicAccess` and server-side encryption ([ACCT.08](acct-08.md)), a CloudTrail trail with log file validation ([ACCT.07](acct-07.md)), and IAM Access Analyzer ([ACCT.11](acct-11.md)).

```
import * as cdk from "aws-cdk-lib";
import {
  aws_s3 as s3,
  aws_cloudtrail as cloudtrail,
  aws_accessanalyzer as accessanalyzer,
  aws_iam as iam,
  RemovalPolicy,
} from "aws-cdk-lib";
import { Construct } from "constructs";

export class SecurityBaselineStack extends cdk.Stack {
  constructor(scope: Construct, id: string, props?: cdk.StackProps) {
    super(scope, id, props);

    const accountId = cdk.Stack.of(this).account;
    const region = cdk.Stack.of(this).region;
    const trailName = "audit-trail";
    const trailArn = `arn:aws:cloudtrail:${region}:${accountId}:trail/${trailName}`;

    // -------------------------------------------------------
    // Tagging — applied to every resource in the stack
    // -------------------------------------------------------

    cdk.Tags.of(this).add("Environment", "production");
    cdk.Tags.of(this).add("Team", "platform");
    cdk.Tags.of(this).add("ManagedBy", "cdk");

    // -------------------------------------------------------
    // ACCT.08 — Block Public Access on S3
    // WKLD.08 — Encrypt data at rest (SSE-S3, AWS-managed)
    // -------------------------------------------------------
    const loggingBucket = new s3.Bucket(this, 'AccessLogsBucket', {
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
      encryption: s3.BucketEncryption.S3_MANAGED,
      enforceSSL: true,
      versioned: true,
      accessControl: s3.BucketAccessControl.LOG_DELIVERY_WRITE,
      lifecycleRules: [
        {
          id: "ArchiveAfter90Days",
          transitions: [
            {
              storageClass: s3.StorageClass.GLACIER,
              transitionAfter: cdk.Duration.days(90),
            },
          ],
        },
      ],
      removalPolicy: RemovalPolicy.RETAIN,
    });

    const auditLogsBucket = new s3.Bucket(this, "AuditLogsBucket", {
      blockPublicAccess: s3.BlockPublicAccess.BLOCK_ALL,
      encryption: s3.BucketEncryption.S3_MANAGED,
      enforceSSL: true,
      versioned: true,
      serverAccessLogsBucket: loggingBucket,
      serverAccessLogsPrefix: 'access-logs',
      lifecycleRules: [
        {
          id: "ArchiveAfter90Days",
          transitions: [
            {
              storageClass: s3.StorageClass.GLACIER,
              transitionAfter: cdk.Duration.days(90),
            },
          ],
        },
      ],
      removalPolicy: RemovalPolicy.RETAIN,
    });

    // -------------------------------------------------------
    // Bucket policy — CloudTrail access + account boundary
    //
    // Per AWS docs, CloudTrail needs two permissions:
    //   1. GetBucketAcl to verify bucket ownership
    //   2. PutObject to write log files
    // Both are scoped to this specific trail via aws:SourceArn.
    // -------------------------------------------------------

    auditLogsBucket.addToResourcePolicy(
      new iam.PolicyStatement({
        sid: "AWSCloudTrailAclCheck",
        effect: iam.Effect.ALLOW,
        principals: [new iam.ServicePrincipal("cloudtrail.amazonaws.com")],
        actions: ["s3:GetBucketAcl"],
        resources: [auditLogsBucket.bucketArn],
        conditions: {
          StringEquals: {
            "aws:SourceArn": trailArn,
          },
        },
      })
    );

    auditLogsBucket.addToResourcePolicy(
      new iam.PolicyStatement({
        sid: "AWSCloudTrailWrite",
        effect: iam.Effect.ALLOW,
        principals: [new iam.ServicePrincipal("cloudtrail.amazonaws.com")],
        actions: ["s3:PutObject"],
        resources: [
          `${auditLogsBucket.bucketArn}/cloudtrail/AWSLogs/${accountId}/*`,
        ],
        conditions: {
          StringEquals: {
            "s3:x-amz-acl": "bucket-owner-full-control",
            "aws:SourceArn": trailArn,
          },
        },
      })
    );

    auditLogsBucket.addToResourcePolicy(
      new iam.PolicyStatement({
        sid: "DenyExternalAccess",
        effect: iam.Effect.DENY,
        principals: [new iam.AnyPrincipal()],
        actions: ["s3:*"],
        resources: [
          auditLogsBucket.bucketArn,
          `${auditLogsBucket.bucketArn}/*`,
        ],
        conditions: {
          StringNotEquals: {
            "aws:PrincipalAccount": accountId,
          },
          Bool: {
          "aws:PrincipalIsAWSService": "false",
          },
        },
      })
    );

    // -------------------------------------------------------
    // ACCT.07 — Deliver CloudTrail logs to a protected S3 bucket
    // -------------------------------------------------------

    const trail = new cloudtrail.Trail(this, "AuditTrail", {
      trailName: trailName,
      bucket: auditLogsBucket,
      s3KeyPrefix: "cloudtrail",
      isMultiRegionTrail: true,
      isOrganizationTrail: false,
      includeGlobalServiceEvents: true,
      enableFileValidation: true,

      // ACCT.07: Captures both read and write management events.
      // For production environments, consider filtering high-volume events
      // per the guidance in ACCT.07.
      managementEvents: cloudtrail.ReadWriteType.ALL,
    });

    // -------------------------------------------------------
    // ACCT.11 — Enable IAM Access Analyzer (account scope)
    // -------------------------------------------------------

    const analyzer = new accessanalyzer.CfnAnalyzer(this, "AccessAnalyzer", {
      analyzerName: "account-analyzer",
      type: "ACCOUNT",
    });

    // -------------------------------------------------------
    // Outputs
    // -------------------------------------------------------

    new cdk.CfnOutput(this, "AuditLogsBucketArn", {
      description: "ARN of the audit logs S3 bucket",
      value: auditLogsBucket.bucketArn,
    });

    new cdk.CfnOutput(this, "AuditTrailArn", {
      description: "ARN of the CloudTrail trail",
      value: trail.trailArn,
    });

    new cdk.CfnOutput(this, "AccessAnalyzerArn", {
      description: "ARN of the IAM Access Analyzer",
      value: analyzer.attrArn,
    });
  }
}
```

For more information about getting started with IaC on AWS, see [Getting started with the AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) in the AWS CDK documentation.

**Note**
AWS CloudFormation is available at no additional charge, and the AWS CDK is open source and also available at no charge. You pay only for the AWS resources that your stacks create.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
