---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloudformation_example_cloudformation_DescribeStacks_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeStacks` with an AWS SDK or CLI
<a name="cloudformation_example_cloudformation_DescribeStacks_section"></a>

The following code examples show how to use `DescribeStacks`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples:
+  [Creating your first infrastructure stack](cloudformation_example_cloudformation_GettingStarted_021_section.md)
+  [Getting started with managed kubernetes clusters](cloudformation_example_eks_GettingStarted_034_section.md)

------
#### [ CLI ]

**AWS CLI**
**To describe AWS CloudFormation stacks**
The following `describe-stacks` command shows summary information for the `myteststack` stack:

```
aws cloudformation describe-stacks --stack-name {{myteststack}}
```
Output:

```
{
    "Stacks":  [
        {
            "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/myteststack/466df9e0-0dff-08e3-8e2f-5088487c4896",
            "Description": "AWS CloudFormation Sample Template S3_Bucket: Sample template showing how to create a publicly accessible S3 bucket. **WARNING** This template creates an S3 bucket. You will be billed for the AWS resources used if you create a stack from this template.",
            "Tags": [],
            "Outputs": [
                {
                    "Description": "Name of S3 bucket to hold website content",
                    "OutputKey": "BucketName",
                    "OutputValue": "myteststack-s3bucket-jssofi1zie2w"
                }
            ],
            "StackStatusReason": null,
            "CreationTime": "2013-08-23T01:02:15.422Z",
            "Capabilities": [],
            "StackName": "myteststack",
            "StackStatus": "CREATE_COMPLETE",
            "DisableRollback": false
        }
    ]
}
```
For more information, see Stacks in the *AWS CloudFormation User Guide*.
+  For API details, see [DescribeStacks](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/describe-stacks.html) in *AWS CLI Command Reference*.

------
#### [ Go ]

**SDK for Go V2**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/workflows/user_pools_and_lambda_triggers#code-examples).

```
import (
	"context"
	"log"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/service/cloudformation"
)

// StackOutputs defines a map of outputs from a specific stack.
type StackOutputs map[string]string

type CloudFormationActions struct {
	CfnClient *cloudformation.Client
}

// GetOutputs gets the outputs from a CloudFormation stack and puts them into a structured format.
func (actor CloudFormationActions) GetOutputs(ctx context.Context, stackName string) StackOutputs {
	output, err := actor.CfnClient.DescribeStacks(ctx, &cloudformation.DescribeStacksInput{
		StackName: aws.String(stackName),
	})
	if err != nil || len(output.Stacks) == 0 {
		log.Panicf("Couldn't find a CloudFormation stack named %v. Here's why: %v\n", stackName, err)
	}
	stackOutputs := StackOutputs{}
	for _, out := range output.Stacks[0].Outputs {
		stackOutputs[*out.OutputKey] = *out.OutputValue
	}
	return stackOutputs
}
```
+  For API details, see [DescribeStacks](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/cloudformation#Client.DescribeStacks) in *AWS SDK for Go API Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: Returns a collection of Stack instances describing all of the user's stacks.**

```
Get-CFNStack
```
**Example 2: Returns a Stack instance describing the specified stack**

```
Get-CFNStack -StackName "myStack"
```
+  For API details, see [DescribeStacks](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: Returns a collection of Stack instances describing all of the user's stacks.**

```
Get-CFNStack
```
**Example 2: Returns a Stack instance describing the specified stack**

```
Get-CFNStack -StackName "myStack"
```
+  For API details, see [DescribeStacks](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
