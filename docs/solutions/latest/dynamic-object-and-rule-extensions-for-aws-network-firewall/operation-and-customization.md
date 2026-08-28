---
source_url: https://docs.aws.amazon.com/solutions/latest/dynamic-object-and-rule-extensions-for-aws-network-firewall/operation-and-customization.html
---

# Operation and customization
<a name="operation-and-customization"></a>

## Data backup and restore
<a name="data-backup-and-restore"></a>

 All DynamoDB tables have point-in-time recovery (PITR) activated by default. Perform these steps in a testing environment before applying to a production environment.

1.  Sign in to the [Amazon EventBridge console](https://console.aws.amazon.com/events/home), then select **Amazon EventBridge.**

1.  Select **Rules** and find the `FirewallObjectExtensionSo-autoconfigTriggerRule`\* rule.

1.  Select the rule and choose **Disable** to temporarily disable the rule. Refer to [Deleting or Disabling a CloudWatch Events Rule](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/Delete-or-Disable-Rule.html) for more information.

1.  Navigate to the [DynamoDB console](https://console.aws.amazon.com/dynamodbv2/home). Select **Backups** in the left navigation menu and find the target backup. For example, `rulesbackup`.

1.  Export backup table data into S3, refer to [Exporting and Importing DynamoDB Data Using AWS Data Pipeline](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBPipeline.html) for more information.

1.  For restore, import S3 data to the `RuleExtensionsRuleTable` solution table. Refer to [Exporting and Importing DynamoDB Data Using AWS Data Pipeline](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DynamoDBPipeline.html) for more information.

1.  Repeat steps 1 through to 6 until all tables are restored.

1.  Before restore, navigate to the [Amazon EventBridge console](https://console.aws.amazon.com/events/home). Select **Rules**, then select the `FirewallObjectExtensionSo-autoconfigTriggerRule`\* rule, and choose **Enable**.

 Allow the rules to be propagated to ANFW, then verify the ANFW rules number is correct. Also, verify the rule status by calling the solution’s API `rulebundles/<id>/rules`.

## AWS resources and service limitations
<a name="aws-resources-and-service-limitations"></a>

 The Dynamic Object and Rule Extensions for AWS Network Firewall solution leverages the following AWS services and is subject to their respective limitations.
+  AWS Identity & Access Management
+  Amazon Virtual Private Cloud
+  Amazon API Gateway
+  AWS Lambda
+  Amazon DynamoDB
+  Amazon CloudWatch Synthetics
+  Amazon CloudWatch
+  AWS Network Firewall
+  Amazon Elastic Container Service
+  AWS Config
+  AWS X-Ray

## API schema
<a name="api-schema"></a>

Visit our [GitHub repository](https://github.com/aws-solutions/dynamic-object-and-rule-extensions-for-anfw/) for the full schema and API documentation.

## Install JQ
<a name="install-jq"></a>

 JQ is used to parse command results from the CLI tool.

 To install on Amazon Linux 2:

```
sudo yum install jq
```

 To install on Mac OS X:

1.  Install [Homebrew](https://docs.brew.sh/Installation).

1.  Once Homebrew is installed, run the following command:

   ```
   brew install jq
   ```

## Install AWS curl
<a name="install-aws-curl"></a>

 AWS curl is used to call Sigv4 protected AWS API endpoints using AWS credentials.

 To install on Amazon Linux 2:

```
pip3 install --user awscurl
```

 To install on Mac OS X:

1.  Install [Homebrew](https://docs.brew.sh/Installation).

1.  Once Homebrew is installed, run the following command:

   ```
   brew install awscurl
   ```

### Install GNU Getopt
<a name="install-gnu-getopt"></a>

**Note**
GNU Getopt is not required on Amazon Linux 2.

 To install on Mac OS X:

1.  Install [Homebrew](https://docs.brew.sh/Installation).

1.  Once Homebrew is installed, run the following command:

   ```
   brew install gnu-getopt
   ```

1.  Set GNU\_GETOPT\_PATH for use by the CLI tool.

   ```
   export GNU_GETOPT_PATH=/usr/local/opt/gnu-getopt/bin/getopt
   ```

### Customize OPA policy
<a name="customize-opa-policy"></a>

1. Add a new OPA policy under `opa/packages/<folder>/, <folder>` could be objects or rules. In this example, the policy ID is `new_customer_policy`, and the new policy file is  `opa/packages/objects/object_new_customer_policy.rego`.

1. Register the new policy by using the following code:

   ```
   FF_CUSTOMER_REGISTERED_POLICIES := [{
       "level": "mandatory",
       "packageId": "objects",
       "policyId": "new_customer_policy_a",
       "parameters": {},
   }]
   availablePolicySet[p] {
       p := FF_CUSOMTER_REGISTERED_POLICIES
   }
   ```

1.  (Optional) We recommend adding OPA policy unit test for the newly added policy. Refer to our [GitHub repository](https://github.com/aws-solutions/dynamic-object-and-rule-extensions-for-anfw/) for an example of the test.

1.  Refer to the [README.md](https://github.com/aws-solutions/dynamic-object-and-rule-extensions-for-anfw/blob/main/README.md) file to build the bundle.

1.  Redeploy this solution.

### Create an EC2 instance
<a name="create-an-ec2-instance"></a>

 Create an Amazon EC2 instance to access the API Gateway endpoint in Amazon VPC.

1.  Sign in to the [EC2 console](https://console.aws.amazon.com/ec2/v2/home).

1.  On the Instances page, choose **Launch Instances**.

1.  Select the **Amazon Linux 2 AMI (HVM)**, **SSD Volume Type** instance.

1.  On the Choose an Instance Type page, select `t2.micro`, and then choose **Review and Launch**.

1.  Select **Edit instance details**, and choose the following configuration:

   ```
   Network: The VPC ID created by the solution.
   Subnet: FirewallObjectExtensionSolutionStack/object-extension-Vpc/PrivateSubnetASubnet2
   ```

1.  Choose **Review and Launch**.

1.  Review your Instance launch and choose **Launch**.

1.  In the Select an existing key pair or create a new key pair box, choose **Proceed without a key pair** and check the **I will not be able to connect to this instance unless you use EC2 Instance Connect or know the password built into the AMI** box.

1.  Choose **Launch Instances**.

### Troubleshooting
<a name="troubleshooting"></a>

 If you need to troubleshoot issues with the deployed solution in case unexpected network and/or infrastructure change occurs. The following are basic diagnosis and recovery steps for some common issues.

#### API gateway return 504 or 503 for all requests
<a name="api-gateway-return-504-or-503-for-all-requests"></a>

1.  Sign in to the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/), then select **Dashboards.**

1.  Select `RuleExtensionServiceDashboard`.

1.  Check the alarms. The alarm reason is listed in **Details**.

1.  Check **Synthetics canaries**. The logs section contains the error reasons in case of a failure.

1.  Navigate to the AWS Console, then select **API Gateway**.

1.  Select **Lambda**, then select **Monitor**.

1.  Check log for Lambda, search for log level ERROR.

1.  Get the `trace_id` from the ERROR log. For example, `trace_id` = `x_1123456`.

1.  Navigate to the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/), then select **Trace** and enter the trace\_id.

 The next page will point to the error where it occurs.

 Alternatively, if you cannot find trace\_id from examining the logs in step 5, you can query trace\_id by navigating to the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/), then select Trace and in the query section, enter:

```
service(id(name: "YOU_DEPLOYED_SERVICE_NAME" , type:
"AWS::Lambda::Function")) {fault = true}
```

#### Rule resolution failure
<a name="rule-resolution-failure"></a>

 If Rule resolution fails with the rule in failed status and displays a failure reason.

1.  Sign in to the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/), choose **Dashboards**, then select **RuleExtensionServiceDashboard**.

1.  Check the alarms. The reason of the alarm is listed under Details.

1.  Navigate to the [Lambda console](https://console.aws.amazon.com/lambda/home) and search `FirewallObjectExtensionSo-autoconfigapiautoConfig`.

1.  Navigate to the [API Gateway console](https://console.aws.amazon.com/apigateway/main) and choose **Lambda** then select **Monitor**.

1.  Check log for Lambda, search for log level ERROR.

1.  Get the `trace_id` from the ERROR log. For example, `trace_id` = `x_1123456`.

1.  Navigate to the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/) then select **Trace**, and enter the trace\_id.

#### Error: unauthorized access
<a name="error-unauthorized-access"></a>

 This is a common error, for example, `"User: arn:aws:iam::123456789012:user/mateojackson is not authorized to perform: networkfirewall:DescribeFirewall on resource: exampleFirewall"`

This is usually caused by an incorrect configuration of AWS Network Firewall rule group name. This solution can only access the pattern of AWS Network Firewall rule group name specified in the `networkFirewallRuleGroupNamePattern` configuration. Therefore, ensure the pattern is correct in respect to the actual name in AWS Network Firewall web console. Refer to [Update solution configuration](deployment.md#step-1.-update-solution-configuration) for more information.

#### Error: capacity exceeded
<a name="error-capacity-exceeded"></a>

 This is usually caused by an insufficient rule group capacity in respect to the number of rules defined in the system. Refer to [Performance](performance.md) for more information.

1.  Sign in to the [AWS Lambda console](https://console.aws.amazon.com/lambda/home) and search for `FirewallObjectExtensionSo-autoconfigautoConfigSche`. Stop the trigger Event bridge, so that the rule resolution stops.

1.  Navigate to the AWS Network Firewall console and select **Network Firewall rule groups,** then select your rule group.

1.  Delete the group in full capacity. Run the following command to use the `aoe.sh` script that comes with this solution.

   ```
   ./aoe.sh get-rule --rule-bundle-id <id> --rule-id <id>
   ```

1.  Create a new rule group with the same name but increase the capacity by 50% (recommended), or as appropriate.

1.  Restart event bridge that was stopped in step 1.

 For detailed troubleshooting steps for each AWS service used in this solution, refer to [Troubleshooting resources](https://docs.aws.amazon.com/awssupport/latest/user/troubleshooting.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Dynamic Object and Rule Extensions for AWS Network Firewall. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
