---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-aws-config-custom-rules-by-using-aws-cloudformation-guard-policies.html
---

# Create AWS Config custom rules by using AWS CloudFormation Guard policies
<a name="create-aws-config-custom-rules-by-using-aws-cloudformation-guard-policies"></a>

*Andrew Lok, Nicole Brown, Kailash Havildar, and Tanya Howell, Amazon Web Services*

## Summary
<a name="create-aws-config-custom-rules-by-using-aws-cloudformation-guard-policies-summary"></a>

[AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) rules help you evaluate your AWS resources and their target configuration state. There are two types of AWS Config rules: managed and custom. Your can create custom rules with AWS Lambda functions or with [AWS CloudFormation Guard](https://github.com/aws-cloudformation/cloudformation-guard) (GitHub), a policy-as-code language.

Rules created with Guard provide more granular control than managed rules, and they are typically easier to configure than fully custom Lambda rules. This approach provides engineers and architects the ability to build rules without needing to know Python, NodeJS, or Java, which are required to deploy custom rules through Lambda.

This pattern provides workable templates, code samples, and deployment approaches to help you adopt custom rules with Guard. By using this pattern, an administrator can use AWS Config to build custom compliance rules that have [configuration item](https://docs.aws.amazon.com/config/latest/developerguide/config-concepts.html#config-items) attributes. For example, developers can use Guard policies against AWS Config configuration items to continuously monitor the state of deployed AWS and non-AWS resources, detect rule violations, and automatically initiate remediation.

**Objectives**

After reading this pattern, you should be able to:
+ Understand how Guard policy code interacts with the AWS Config service.
+ Deploy *Scenario 1*, which is an AWS Config custom rule that uses Guard syntax to validate compliance for encrypted volumes. This rule verifies that the drive is in use and verifies that the drive type is [gp3](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/general-purpose.html#gp3-ebs-volume-type).
+ Deploy *Scenario 2*, which is an AWS Config custom rule that uses Guard syntax to validate Amazon GuardDuty compliance. This rule verifies that GuardDuty recorders have [Amazon Simple Storage Service (Amazon S3) Protection](https://docs.aws.amazon.com/guardduty/latest/ug/s3-protection.html) and [Amazon Elastic Kubernetes Service (Amazon EKS) Protection](https://docs.aws.amazon.com/guardduty/latest/ug/kubernetes-protection.html) enabled.

## Prerequisites and limitations
<a name="create-aws-config-custom-rules-by-using-aws-cloudformation-guard-policies-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ AWS Config, [set up](https://docs.aws.amazon.com/config/latest/developerguide/getting-started.html) in your AWS account

**Limitations**
+ Guard custom rules are only able to query key-value pairs in a target configuration item JSON record

## Architecture
<a name="create-aws-config-custom-rules-by-using-aws-cloudformation-guard-policies-architecture"></a>

You apply the Guard syntax to an AWS Config rule as a custom policy. AWS Config captures the hierarchical JSON of each of the resources specified. The JSON of the AWS Config configuration item contains key-value pairs. These attributes are used in the Guard syntax as variables that are assigned to their corresponding value.

The following is an explanation of the Guard syntax. The variables from the configuration item JSON are used and prepended with a `%` character.

```
# declare variable
let <variable name> = <'value'>

# create rule and assign condition and policy
    rule <rule name> when
        <CI json key> == <"CI json value"> {
            <top level CI json key>.<next level CI json key> == %<variable name>
        }
```

**Scenario 1: Amazon EBS volumes**

Scenario 1 deploys an AWS Config custom rule that uses Guard syntax to validate compliance for encrypted volumes. This rule verifies that the drive is in use and verifies that the drive type is gp3.

The following is an example of an AWS Config configuration item for scenario 1. There are three key-value pairs in this configuration item that used as variables in the Guard policy: `volumestatus`, `volumeencryptionstatus`, and `volumetype`. Also, the `resourceType` key is used as a filter in the Guard policy.

```
{
  "version": "1.3",
  "accountId": "111111111111",
  "configurationItemCaptureTime": "2023-01-15T19:04:45.402Z",
  "configurationItemStatus": "ResourceDiscovered",
  "configurationStateId": "4444444444444",
  "configurationItemMD5Hash": "",
  "arn": "arn:aws:ec2:us-west-2:111111111111:volume/vol-222222222222",
  "resourceType": "AWS::EC2::Volume",
  "resourceId": "vol-222222222222",
  "awsRegion": "us-west-2",
  "availabilityZone": "us-west-2b",
  "resourceCreationTime": "2023-01-15T19:03:22.247Z",
  "tags": {},
  "relatedEvents": [],
  "relationships": [
    {
      "resourceType": "AWS::EC2::Instance",
      "resourceId": "i-33333333333333333",
      "relationshipName": "Is attached to Instance"
    }
  ],
  "configuration": {
    "attachments": [
      {
        "attachTime": "2023-01-15T19:03:22.000Z",
        "device": "/dev/xvda",
        "instanceId": "i-33333333333333333",
        "state": "attached",
        "volumeId": "vol-222222222222",
        "deleteOnTermination": true,
        "associatedResource": null,
        "instanceOwningService": null
      }
    ],
    "availabilityZone": "us-west-2b",
    "createTime": "2023-01-15T19:03:22.247Z",
    "encrypted": false,
    "kmsKeyId": null,
    "outpostArn": null,
    "size": 8,
    "snapshotId": "snap-55555555555555555",
    "state": "in-use",
    "volumeId": "vol-222222222222",
    "iops": 100,
    "tags": [],
    "volumeType": "gp2",
    "fastRestored": null,
    "multiAttachEnabled": false,
    "throughput": null,
    "sseType": null
  },
  "supplementaryConfiguration": {}
}
```

The following is an example of using Guard syntax to define the variables and rules in scenario 1. In the following example:
+ The first three lines define the variables by using the `let` command.  They are assigned a name and value that is derived from the attributes of the configuration item.
+ The `compliancecheck` rule block adds a when conditional dependency that looks for a `resourceType` key-value pair that matches `AWS::EC2::Volume`. If a match is found, the rule proceeds through the rest of the JSON attributes and looks for matches on the following three conditions: `state`, `encrypted`, and `volumeType`.

```
let volumestatus = 'available'
let volumetype = 'gp3'
let volumeencryptionstatus = true

    rule compliancecheck when
        resourceType == "AWS::EC2::Volume" {
            configuration.state == %volumestatus
            configuration.encrypted == %volumeencryptionstatus
            configuration.volumeType == %volumetype
        }
```

For the complete Guard custom policy that implements this custom rule, see [awsconfig-guard-cft.yaml](https://github.com/aws-samples/aws-config-custom-rule-cloudformation-guard/blob/main/awsconfig-guard-cft.yaml) or [awsconfig-guard-tf-ec2vol.json](https://github.com/aws-samples/aws-config-custom-rule-cloudformation-guard/blob/main/awsconfig-guard-tf-ec2vol.json) in the GitHub code repository. For HashiCorp Terraform code that deploys this custom policy in Guard, see [awsconfig-guard-tf-example.json](https://github.com/aws-samples/aws-config-custom-rule-cloudformation-guard/blob/main/awsconfig-guard-tf-example.json) in the code repository.

**Scenario 2: GuardDuty compliance**

Scenario 2 deploys an AWS Config custom rule that uses Guard syntax to validate Amazon GuardDuty compliance. This rule verifies that GuardDuty recorders have Amazon S3 Protection and Amazon EKS Protection enabled. It also verifies that GuardDuty findings are published every 15 minutes. This scenario could be deployed across all AWS accounts and AWS Regions in an organization (in AWS Organizations).

The following is an example of an AWS Config configuration item for scenario 2. There are three key-value pairs in this configuration item that used as variables in the Guard policy: `FindingPublishingFrequency`, `S3Logs`, and `Kubernetes`. Also, the `resourceType` key is used as a filter in the policy.

```
{
  "version": "1.3",
  "accountId": "111111111111",
  "configurationItemCaptureTime": "2023-11-27T13:34:28.888Z",
  "configurationItemStatus": "OK",
  "configurationStateId": "7777777777777",
  "configurationItemMD5Hash": "",
  "arn": "arn:aws:guardduty:us-west-2:111111111111:detector/66666666666666666666666666666666",
  "resourceType": "AWS::GuardDuty::Detector",
  "resourceId": "66666666666666666666666666666666",
  "resourceName": "66666666666666666666666666666666",
  "awsRegion": "us-west-2",
  "availabilityZone": "Regional",
  "resourceCreationTime": "2020-02-17T02:48:04.511Z",
  "tags": {},
  "relatedEvents": [],
  "relationships": [],
  "configuration": {
    "Enable": true,
    "FindingPublishingFrequency": "FIFTEEN_MINUTES",
    "DataSources": {
      "S3Logs": {
        "Enable": true
      },
      "Kubernetes": {
        "AuditLogs": {
          "Enable": true
        }
      }
    },

    "Id": "66666666666666666666666666666666",
    "Tags": []
  },
  "supplementaryConfiguration": {
    "CreatedAt": "2020-02-17T02:48:04.511Z"
  }
}
```

The following is an example of using Guard syntax to define the variables and rules in scenario 2. In the following example:
+ The first three lines define the variables by using the `let` command.  They are assigned a name and value that is derived from the attributes of the configuration item.
+ The `compliancecheck` rule block adds a when conditional dependency that looks for a `resourceType` key-value pair that matches `AWS::GuardDuty::Detector`. If a match is found, the rule proceeds through the rest of the JSON attributes and looks for matches on the following three conditions: `S3Logs.Enable`, `Kubernetes.AuditLogs.Enable`, and `FindingPublishingFrequency`.

```
let s3protection = true
let kubernetesprotection = true
let publishfrequency = 'FIFTEEN_MINUTES'

    rule compliancecheck when
        resourceType == "AWS::GuardDuty::Detector" {
            configuration.DataSources.S3Logs.Enable == %s3protection
            configuration.DataSources.Kubernetes.AuditLogs.Enable == %kubernetesprotection
            configuration.FindingPublishingFrequency == %publishfrequency
        }
```

For the complete Guard custom policy that implements this custom rule, see [awsconfig-guard-cft-gd.yaml](https://github.com/aws-samples/aws-config-custom-rule-cloudformation-guard/blob/main/awsconfig-guard-cft-gd.yaml) in the GitHub code repository. For HashiCorp Terraform code that deploys this custom policy in Guard, see [awsconfig-guard-tf-gd.json](https://github.com/aws-samples/aws-config-custom-rule-cloudformation-guard/blob/main/awsconfig-guard-tf-gd.json) in the code repository.

## Tools
<a name="create-aws-config-custom-rules-by-using-aws-cloudformation-guard-policies-tools"></a>

**AWS services**
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and Regions.
+ [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/WhatIsConfig.html) provides a detailed view of the resources in your AWS account and how they’re configured. It helps you identify how resources are related to one another and how their configurations have changed over time.

**Other tools**
+ [HashiCorp Terraform](https://www.terraform.io/docs) is an infrastructure as code (IaC) tool that helps you use code to provision and manage cloud infrastructure and resources.

**Code repository**

The code for this pattern is available in the GitHub [AWS Config with AWS CloudFormation Guard](https://github.com/aws-samples/aws-config-custom-rule-cloudformation-guard/tree/main) repository. This code repository contains samples for both of the scenarios described in this pattern.

## Epics
<a name="create-aws-config-custom-rules-by-using-aws-cloudformation-guard-policies-epics"></a>

### Creating AWS Config custom rules
<a name="creating-cc-custom-rules"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| (Optional) Select key-value pairs for the rule. | Complete these steps if you are defining a custom Guard policy. If you are using one of the sample policies for scenario 1 or 2, skip these steps.1. Sign in to the AWS Management Console and open the [AWS Config console](https://console.aws.amazon.com/config/).<br />2. In the left navigation, choose **Resources**.<br />3. In the resource inventory, choose the type of resource that you want to create an AWS Config custom rule for.<br />4. Choose **View details**.<br />5. Choose **View Configuration Item (JSON)**. This section expands to show the configuration item in JSON format.<br />6. Identify the key-value pairs that you would like to build an AWS Config custom rule for. | AWS administrator, Security engineer |
| Create the custom rule. | Using the key-value pairs that you identified previously or using one of the provided sample Guard policies, follow the instructions in [Creating AWS Config Custom Policy Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules_cfn-guard.html#create-cfn-guard-rule-console) to create a custom rule. | AWS administrator, Security engineer |
| Validate the custom rule. | Do one of the following to validate the custom Guard rule:+ Enter the following command in the AWS Command Line Interface (AWS CLI).<pre>cfn-guard validate -r guard-s3.guard -d s3bucket-prod-pass.json</pre><br />+ Follow the instructions in *Detective mode* in [Evaluating Your Resources with AWS Config Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluating-your-resources.html) to deploy the rule in AWS Config. Confirm that the Guard syntax matches correctly to corresponding resources in the target account or file. | AWS administrator, Security engineer |

## Troubleshooting
<a name="create-aws-config-custom-rules-by-using-aws-cloudformation-guard-policies-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Test the Guard policy outside of AWS Config | Unit testing can be done on your local device or in an integrated development environment (IDE), such as an AWS Cloud9 IDE. To perform unit testing, do the following:1. Install the [AWS CloudFormation Guard CLI](https://github.com/aws-cloudformation/cloudformation-guard#guard-cli) and its dependencies.<br />2. Save a JSON-formatted CI sample to your workstation as a .json file.<br />3. Save the GuardDuty policy to your workstation as a .guard file.<br />4. In the Guard CLI, enter the following command to validate the sample JSON file by using the Guard policy.<pre>cfn-guard validate \<br />-r guard-s3.guard \<br />-d s3bucket-prod-pass.json</pre> |
| Debug an AWS Config custom rule | In your Guard policy, change the `EnableDebugLogDelivery` value to `true`. The default value is `false`. The log messages are stored in Amazon CloudWatch. |

## Related resources
<a name="create-aws-config-custom-rules-by-using-aws-cloudformation-guard-policies-resources"></a>

**AWS documentation**
+ [Creating AWS Config Custom Policy Rules](https://docs.aws.amazon.com/config/latest/developerguide/evaluate-config_develop-rules_cfn-guard.html) (AWS Config documentation)
+ [Writing AWS CloudFormation Guard rules](https://docs.aws.amazon.com/cfn-guard/latest/ug/writing-rules.html) (Guard documentation)

**AWS blog posts and workshops**
+ [Introducing AWS CloudFormation Guard 2.0](https://aws.amazon.com/blogs/mt/introducing-aws-cloudformation-guard-2-0/) (AWS blog post)

**Other resources**
+ [AWS CloudFormation Guard](https://github.com/aws-cloudformation/cloudformation-guard) (GitHub)
+ [AWS CloudFormation Guard CLI documentation](https://github.com/aws-cloudformation/cloudformation-guard#guard-cli) (GitHub)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
