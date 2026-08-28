---
source_url: https://docs.aws.amazon.com/solutions/latest/security-automations-for-aws-waf/deployment-considerations.html
---

# Deployment considerations
<a name="deployment-considerations"></a>

The following sections provide constraints and considerations for implementing this solution.

## AWS WAF rules
<a name="aws-waf-rules"></a>

The web ACL that this solution generates is designed to offer comprehensive protection for web applications. The solution provides a set of AWS Managed Rules and custom rules that you can add to the web ACL. To include a rule, choose `yes` for the relevant parameters when launching the CloudFormation stack. See [Step 1. Launch the stack](step-1.-launch-the-stack.md) for the list of parameters.

**Note**
The out-of-box solution doesn’t support [AWS Firewall Manager](https://aws.amazon.com/firewall-manager). If you want to use the rules in Firewall Manager, we recommend that you to apply customizations to its [source code](https://github.com/aws-solutions/aws-waf-security-automations).

## Web ACL traffic logging
<a name="web-acl-traffic-logging"></a>

If you create the stack in an AWS Region other than US East (N. Virginia) and set the **Endpoint** as `CloudFront`, you must set **Activate HTTP Flood Protection** to `no` or `yes - AWS WAF rate based rule`.

The other two options (`yes - AWS Lambda log parser` and `yes - Amazon Athena log parser`) require activating AWS WAF logs on a web ACL that runs in all AWS edge locations, and this isn’t supported outside US East (N. Virginia). For more information about logging Web ACL traffic, refer to the [AWS WAF developer guide](https://docs.aws.amazon.com/waf/latest/developerguide/logging.html).

## Oversize handling for request components
<a name="oversize-handling-for-request-components"></a>

AWS WAF doesn’t support inspecting oversized content for the web request component’s body, headers, or cookies. When you write a rule statement that inspects one of these request component types, you can choose one of these options to tell AWS WAF what to do with these requests:
+  `yes` (continue) - Inspect the request component normally according to the rule inspection criteria. AWS WAF inspects the request component contents that are within the size limitations. This is the default option used in the solution.
+  `yes - MATCH` - Treat the web request as matching the rule statement. AWS WAF applies the rule action to the request without evaluating it against the rule’s inspection criteria. For a rule with `Block` action, this blocks the request with the oversize component.
+  `yes - NO_MATCH` - Treat the web request as not matching the rule statement, without evaluating it against the rule’s inspection criteria. AWS WAF continues its inspection of the web request by using the rest of the rules in the web ACL, like it would do for any non-matching rule.

For more information, refer to [Handling oversize web request components in AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-statement-oversize-handling.html).

## Multiple solution deployments
<a name="multiple-solution-deployments"></a>

You can deploy the solution multiple times in the same account and Region. You must use a unique CloudFormation stack name and Amazon S3 bucket name for each deployment. Each unique deployment incurs additional charges and is subject to the [AWS WAF quotas](https://docs.aws.amazon.com/waf/latest/developerguide/limits.html) per account, per Region.

## Minimum role permissions for deployment (Optional)
<a name="minimum-role-permissions"></a>

Customers can manually create an IAM role with the minimum required permissions for deployment:
+ WAF Permissions

```
        {
            "Effect": "Allow",
            "Action": [
                "wafv2:CreateWebACL",
                "wafv2:UpdateWebACL",
                "wafv2:DeleteWebACL",
                "wafv2:GetWebACL",
                "wafv2:ListWebACLs",
                "wafv2:CreateIPSet",
                "wafv2:UpdateIPSet",
                "wafv2:DeleteIPSet",
                "wafv2:GetIPSet",
                "wafv2:AssociateWebACL",
                "wafv2:DisassociateWebACL",
                "wafv2:PutLoggingConfiguration",
                "wafv2:DeleteLoggingConfiguration",
                "wafv2:ListWebACLs",
                "wafv2:ListIPSets",
                "wafv2:ListTagsForResource"
            ],
            "Resource": [
                "arn:aws:wafv2:*:*:regional/webacl/*",
                "arn:aws:wafv2:*:*:regional/ipset/*",
                "arn:aws:wafv2:*:*:global/webacl/*",
                "arn:aws:wafv2:*:*:global/ipset/*"
            ]
        }
```
+ Lambda Permissions

```
        {
            "Effect": "Allow",
            "Action": [
                "lambda:CreateFunction",
                "lambda:DeleteFunction",
                "lambda:GetFunction",
                "lambda:InvokeFunction",
                "lambda:UpdateFunctionCode",
                "lambda:UpdateFunctionConfiguration",
                "lambda:AddPermission",
                "lambda:RemovePermission"
            ],
            "Resource": "arn:aws:lambda:*:*:function:*"
        }
```
+ Firehose Permissions

```
        {
            "Effect": "Allow",
            "Action": [
                "firehose:CreateDeliveryStream",
                "firehose:DeleteDeliveryStream",
                "firehose:DescribeDeliveryStream",
                "firehose:StartDeliveryStreamEncryption",
                "firehose:StopDeliveryStreamEncryption",
                "firehose:UpdateDestination"
            ],
            "Resource": "arn:aws:firehose:*:*:deliverystream/*"
        }
```
+ S3 Permissions

```
        {
            "Effect": "Allow",
            "Action": [
                "s3:CreateBucket",
                "s3:DeleteBucketPolicy",
                "s3:GetBucketAcl",
                "s3:GetBucketPolicy",
                "s3:GetObject",
                "s3:PutBucketAcl",
                "s3:PutBucketPolicy",
                "s3:PutBucketPublicAccessBlock",
                "s3:PutBucketVersioning",
                "s3:PutEncryptionConfiguration",
                "s3:PutObject",
                "s3:PutBucketTagging",
                "s3:PutLifecycleConfiguration",
                "s3:AbortMultipartUpload",
                "s3:GetBucketLocation",
                "s3:ListBucket",
                "s3:ListBucketMultipartUploads",
                "s3:ListMultipartUploadParts",
                "s3:PutBucketLogging",
                "s3:GetBucketLogging"
            ],
            "Resource": "arn:aws:s3:::*"
        }
```
+ Athena Permissions

```
        {
            "Effect": "Allow",
            "Action": [
                "athena:CreateWorkGroup",
                "athena:DeleteWorkGroup",
                "athena:GetWorkGroup",
                "athena:UpdateWorkGroup",
                "athena:StartQueryExecution",
                "athena:GetQueryExecution",
                "athena:GetQueryResults",
                "athena:StopQueryExecution"
            ],
            "Resource": "arn:aws:athena:*:*:workgroup/WAF*"
        }
```
+ Glue Permissions

```
        {
            "Effect": "Allow",
            "Action": [
                "glue:CreateDatabase",
                "glue:DeleteDatabase",
                "glue:GetDatabase",
                "glue:GetDatabases",
                "glue:UpdateDatabase",
                "glue:CreateTable",
                "glue:DeleteTable",
                "glue:GetTable",
                "glue:GetTables",
                "glue:UpdateTable"
            ],
            "Resource": [
                "arn:aws:glue:*:*:catalog",
                "arn:aws:glue:*:*:database/*",
                "arn:aws:glue:*:*:table/*/*",
                "arn:aws:glue:*:*:userDefinedFunction/*"
            ]
        }
```
+ CloudWatch Logs Permissions

```
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents",
                "logs:DeleteLogGroup",
                "logs:DeleteLogStream",
                "logs:PutRetentionPolicy",
                "logs:DescribeLogGroups"
            ],
            "Resource": [
                "arn:aws:logs:*:*:log-group:/aws/lambda/*",
                "arn:aws:logs:*:*:log-group:*",
                "arn:aws:logs:*:*:log-group:/aws/kinesisfirehose/*"
            ]
        }
```
+ CloudWatch Permissions

```
        {
            "Effect": "Allow",
            "Action": [
                "cloudwatch:DeleteDashboards",
                "cloudwatch:GetDashboard",
                "cloudwatch:ListDashboards",
                "cloudwatch:PutDashboard",
                "cloudwatch:PutMetricData"
            ],
            "Resource": "*"
        }
```
+ SNS Permissions

```
        {
            "Effect": "Allow",
            "Action": [
                "sns:CreateTopic",
                "sns:DeleteTopic",
                "sns:Subscribe",
                "sns:Unsubscribe",
                "sns:SetTopicAttributes"
            ],
            "Resource": "arn:aws:sns:*:*:*"
        }
```
+ DynamoDB Permissions

```
        {
            "Effect": "Allow",
            "Action": [
                "dynamodb:CreateTable",
                "dynamodb:DeleteTable",
                "dynamodb:DescribeTable",
                "dynamodb:PutItem",
                "dynamodb:GetItem",
                "dynamodb:UpdateItem",
                "dynamodb:DeleteItem"
            ],
            "Resource": "arn:aws:dynamodb:*:*:table/*"
        }
```
+ CloudFormation Permissions

```
        {
            "Effect": "Allow",
            "Action": [
                "cloudformation:CreateStack",
                "cloudformation:DeleteStack",
                "cloudformation:DescribeStacks",
                "cloudformation:UpdateStack",
                "cloudformation:ListStacks"
            ],
            "Resource": "arn:aws:cloudformation:*:*:stack/*/*"
        }
```
+ Service Catalog App Registry Permissions

```
        {
            "Effect": "Allow",
            "Action": [
                "servicecatalog:CreateApplication",
                "servicecatalog:DeleteApplication",
                "servicecatalog:GetApplication",
                "servicecatalog:TagResource",
                "servicecatalog:CreateAttributeGroup",
                "servicecatalog:DeleteAttributeGroup",
                "servicecatalog:GetAttributeGroup",
                "servicecatalog:AssociateAttributeGroup",
                "servicecatalog:DisassociateAttributeGroup",
                "servicecatalog:AssociateResource",
                "servicecatalog:DisassociateResource"
            ],
            "Resource": "arn:aws:servicecatalog:*:*:*"
        }
```
+ X-Ray Permissions

```
        {
            "Effect": "Allow",
            "Action": [
                "xray:PutTraceSegments",
                "xray:PutTelemetryRecords"
            ],
            "Resource": "*"
        }
```
+ IAM Permissions

```
        {
            "Effect": "Allow",
            "Action": [
                "iam:AttachRolePolicy",
                "iam:CreatePolicy",
                "iam:CreateRole",
                "iam:DeleteRole",
                "iam:DeleteRolePolicy",
                "iam:DetachRolePolicy",
                "iam:GetRole",
                "iam:GetRolePolicy",
                "iam:ListRoles",
                "iam:PassRole",
                "iam:PutRolePolicy"
            ],
            "Resource": "arn:aws:iam::*:role/*"
        }
```
+ EventBridge Permissions

```
        {
            "Effect": "Allow",
            "Action": [
                "events:PutTargets",
                "events:RemoveTargets",
                "events:DescribeRule",
                "events:EnableRule",
                "events:ListRules",
                "events:PutRule",
                "events:DeleteRule",
                "events:ListEventSources",
                "events:DescribeEventSource",
                "events:ActivateEventSource",
                "events:DeactivateEventSource"
            ],
            "Resource": "arn:aws:events:*:*:rule/*"
        }
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Security Automations for AWS WAF. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
