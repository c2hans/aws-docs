---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/go_2_bedrock_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon Bedrock examples using SDK for Go V2
<a name="go_2_bedrock_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Go V2 with Amazon Bedrock.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Get started](#get_started)
+ [Actions](#actions)

## Get started
<a name="get_started"></a>

### Hello Amazon Bedrock
<a name="bedrock_Hello_go_2_topic"></a>

The following code example shows how to get started using Amazon Bedrock.

**SDK for Go V2**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/bedrock#code-examples).

```
package main

import (
	"context"
	"fmt"

	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/bedrock"
)

const region = "us-east-1"

// main uses the AWS SDK for Go (v2) to create an Amazon Bedrock client and
// list the available foundation models in your account and the chosen region.
// This example uses the default settings specified in your shared credentials
// and config files.
func main() {
	ctx := context.Background()
	sdkConfig, err := config.LoadDefaultConfig(ctx, config.WithRegion(region))
	if err != nil {
		fmt.Println("Couldn't load default configuration. Have you set up your AWS account?")
		fmt.Println(err)
		return
	}
	bedrockClient := bedrock.NewFromConfig(sdkConfig)
	result, err := bedrockClient.ListFoundationModels(ctx, &bedrock.ListFoundationModelsInput{})
	if err != nil {
		fmt.Printf("Couldn't list foundation models. Here's why: %v\n", err)
		return
	}
	if len(result.ModelSummaries) == 0 {
		fmt.Println("There are no foundation models.")
	}
	for _, modelSummary := range result.ModelSummaries {
		fmt.Println(*modelSummary.ModelId)
	}
}
```
+  For API details, see [ListFoundationModels](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/bedrock#Client.ListFoundationModels) in *AWS SDK for Go API Reference*.

## Actions
<a name="actions"></a>

### `ListFoundationModels`
<a name="bedrock_ListFoundationModels_go_2_topic"></a>

The following code example shows how to use `ListFoundationModels`.

**SDK for Go V2**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/bedrock#code-examples).
List the available Bedrock foundation models.

```
import (
	"context"
	"log"

	"github.com/aws/aws-sdk-go-v2/service/bedrock"
	"github.com/aws/aws-sdk-go-v2/service/bedrock/types"
)

// FoundationModelWrapper encapsulates Amazon Bedrock actions used in the examples.
// It contains a Bedrock service client that is used to perform foundation model actions.
type FoundationModelWrapper struct {
	BedrockClient *bedrock.Client
}

// ListPolicies lists Bedrock foundation models that you can use.
func (wrapper FoundationModelWrapper) ListFoundationModels(ctx context.Context) ([]types.FoundationModelSummary, error) {

	var models []types.FoundationModelSummary

	result, err := wrapper.BedrockClient.ListFoundationModels(ctx, &bedrock.ListFoundationModelsInput{})

	if err != nil {
		log.Printf("Couldn't list foundation models. Here's why: %v\n", err)
	} else {
		models = result.ModelSummaries
	}
	return models, err
}
```
+  For API details, see [ListFoundationModels](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/bedrock#Client.ListFoundationModels) in *AWS SDK for Go API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
