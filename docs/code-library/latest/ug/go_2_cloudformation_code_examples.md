---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/go_2_cloudformation_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# CloudFormation examples using SDK for Go V2
<a name="go_2_cloudformation_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Go V2 with CloudFormation.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `DescribeStacks`
<a name="cloudformation_DescribeStacks_go_2_topic"></a>

The following code example shows how to use `DescribeStacks`.

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
