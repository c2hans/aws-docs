---
source_url: https://docs.aws.amazon.com/securityhub/latest/userguide/asff-resourcedetails-awscloudformation.html
---

# AwsCloudFormation resources in ASFF
<a name="asff-resourcedetails-awscloudformation"></a>

The following are examples of the AWS Security Finding Format (ASFF) syntax for `AwsCloudFormation` resources.

AWS Security Hub CSPM normalizes findings from various sources into ASFF. For background information about ASFF, see [AWS Security Finding Format (ASFF)](securityhub-findings-format.md).

## AwsCloudFormationStack
<a name="asff-resourcedetails-awscloudformationstack"></a>

The `AwsCloudFormationStack` object provides details about an AWS CloudFormation stack that is nested as a resource in a top-level template.

The following example shows the AWS Security Finding Format (ASFF) for the `AwsCloudFormationStack` object. To view descriptions of `AwsCloudFormationStack` attributes, see [AwsCloudFormationStackDetails](https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsCloudFormationStackDetails.html) in the *AWS Security Hub API Reference*.

**Example**

```
"AwsCloudFormationStack": {
	"Capabilities": [
		"CAPABILITY_IAM",
		"CAPABILITY_NAMED_IAM"
	],
	"CreationTime": "2022-02-18T15:31:53.161Z",
	"Description": "AWS CloudFormation Sample",
	"DisableRollback": true,
	"DriftInformation": {
		"StackDriftStatus": "DRIFTED"
	},
	"EnableTerminationProtection": false,
	"LastUpdatedTime": "2022-02-18T15:31:53.161Z",
	"NotificationArns": [
		"arn:aws:sns:us-east-1:978084797471:sample-sns-cfn"
	],
	"Outputs": [{
		"Description": "URL for newly created LAMP stack",
		"OutputKey": "WebsiteUrl",
		"OutputValue": "http://ec2-44-193-18-241.compute-1.amazonaws.com"
	}],
	"RoleArn": "arn:aws:iam::012345678910:role/exampleRole",
	"StackId": "arn:aws:cloudformation:us-east-1:978084797471:stack/sample-stack/e5d9f7e0-90cf-11ec-88c6-12ac1f91724b",
	"StackName": "sample-stack",
	"StackStatus": "CREATE_COMPLETE",
	"StackStatusReason": "Success",
	"TimeoutInMinutes": 1
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
