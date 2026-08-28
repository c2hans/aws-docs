---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/go_2_bedrock-runtime_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon Bedrock Runtime examples using SDK for Go V2
<a name="go_2_bedrock-runtime_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for Go V2 with Amazon Bedrock Runtime.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Get started](#get_started)
+ [Amazon Nova](#amazon_nova)
+ [Amazon Titan Image Generator](#amazon_titan_image_generator)
+ [Anthropic Claude](#anthropic_claude)

## Get started
<a name="get_started"></a>

### Hello Amazon Bedrock Runtime
<a name="bedrock-runtime_Hello_go_2_topic"></a>

The following code example shows how to get started using Amazon Bedrock Runtime.

**SDK for Go V2**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/bedrock-runtime#code-examples).

```
package main

import (
	"context"
	"flag"
	"fmt"
	"log"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/config"
	"github.com/aws/aws-sdk-go-v2/service/bedrockruntime"
	"github.com/aws/aws-sdk-go-v2/service/bedrockruntime/types"
)

// main uses the AWS SDK for Go (v2) to create an Amazon Bedrock Runtime client
// and invokes Anthropic Claude using the Converse API.
// This example uses the default settings specified in your shared credentials
// and config files.
func main() {

	region := flag.String("region", "us-east-1", "The AWS region")
	flag.Parse()

	fmt.Printf("Using AWS region: %s\n", *region)

	ctx := context.Background()
	sdkConfig, err := config.LoadDefaultConfig(ctx, config.WithRegion(*region))
	if err != nil {
		fmt.Println("Couldn't load default configuration. Have you set up your AWS account?")
		fmt.Println(err)
		return
	}

	client := bedrockruntime.NewFromConfig(sdkConfig)

	// Set the model ID, e.g., Claude Haiku.
	// The "global." prefix enables cross-region inference, allowing the request
	// to be routed to the nearest available region for the specified model.
	modelId := "global.anthropic.claude-haiku-4-5-20251001-v1:0"

	// Start a conversation with the user message.
	prompt := "Hello. In a short paragraph, explain what you can do."

	message := types.Message{
		Content: []types.ContentBlock{
			&types.ContentBlockMemberText{Value: prompt},
		},
		Role: types.ConversationRoleUser,
	}

	fmt.Printf("Model: %s\n", modelId)
	fmt.Printf("Prompt: %s\n\n", prompt)

	result, err := client.Converse(ctx, &bedrockruntime.ConverseInput{
		ModelId:  aws.String(modelId),
		Messages: []types.Message{message},
	})

	if err != nil {
		log.Fatalf("ERROR: Can't invoke '%s'. Reason: %v\n", modelId, err)
	}

	// Extract and print the response text.
	responseMessage, ok := result.Output.(*types.ConverseOutputMemberMessage)
	if !ok {
		log.Fatal("ERROR: Unexpected output type from Converse API")
	}
	responseContentBlock := responseMessage.Value.Content[0]
	text, ok := responseContentBlock.(*types.ContentBlockMemberText)
	if !ok {
		log.Fatal("ERROR: Unexpected content block type from Converse API")
	}
	fmt.Printf("Response: %s\n", text.Value)
}
```
+  For API details, see [Converse](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/bedrockruntime#Client.Converse) in *AWS SDK for Go API Reference*.

## Amazon Nova
<a name="amazon_nova"></a>

### Converse
<a name="bedrock-runtime_Converse_AmazonNovaText_go_2_topic"></a>

The following code example shows how to send a text message to Amazon Nova, using Bedrock's Converse API.

**SDK for Go V2**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/bedrock-runtime#code-examples).
Send a text message to Amazon Nova, using Bedrock's Converse API.

```
func (wrapper ConverseWrapper) ConverseNova(ctx context.Context, prompt string) (string, error) {
	var content = types.ContentBlockMemberText{
		Value: prompt,
	}
	var message = types.Message{
		Content: []types.ContentBlock{&content},
		Role:    "user",
	}
	modelId := "amazon.nova-lite-v1:0"
	var converseInput = bedrockruntime.ConverseInput{
		ModelId:  aws.String(modelId),
		Messages: []types.Message{message},
	}
	response, err := wrapper.BedrockRuntimeClient.Converse(ctx, &converseInput)
	if err != nil {
		ProcessError(err, modelId)
	}

	responseText, _ := response.Output.(*types.ConverseOutputMemberMessage)
	responseContentBlock := responseText.Value.Content[0]
	text, _ := responseContentBlock.(*types.ContentBlockMemberText)
	return text.Value, nil
}
```
+  For API details, see [Converse](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/bedrockruntime#Client.Converse) in *AWS SDK for Go API Reference*.

## Amazon Titan Image Generator
<a name="amazon_titan_image_generator"></a>

### InvokeModel
<a name="bedrock-runtime_InvokeModel_TitanImageGenerator_go_2_topic"></a>

The following code example shows how to invoke Amazon Titan Image on Amazon Bedrock to generate an image.

**SDK for Go V2**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/bedrock-runtime#code-examples).
Create an image with the Amazon Titan Image Generator.

```
import (
	"context"
	"encoding/json"
	"log"
	"strings"

	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/service/bedrockruntime"
)

// InvokeModelWrapper encapsulates Amazon Bedrock actions used in the examples.
// It contains a Bedrock Runtime client that is used to invoke foundation models.
type InvokeModelWrapper struct {
	BedrockRuntimeClient *bedrockruntime.Client
}

type TitanImageRequest struct {
	TaskType              string                `json:"taskType"`
	TextToImageParams     TextToImageParams     `json:"textToImageParams"`
	ImageGenerationConfig ImageGenerationConfig `json:"imageGenerationConfig"`
}
type TextToImageParams struct {
	Text string `json:"text"`
}
type ImageGenerationConfig struct {
	NumberOfImages int     `json:"numberOfImages"`
	Quality        string  `json:"quality"`
	CfgScale       float64 `json:"cfgScale"`
	Height         int     `json:"height"`
	Width          int     `json:"width"`
	Seed           int64   `json:"seed"`
}

type TitanImageResponse struct {
	Images []string `json:"images"`
}

// Invokes the Titan Image model to create an image using the input provided
// in the request body.
func (wrapper InvokeModelWrapper) InvokeTitanImage(ctx context.Context, prompt string, seed int64) (string, error) {
	modelId := "amazon.titan-image-generator-v2:0"

	body, err := json.Marshal(TitanImageRequest{
		TaskType: "TEXT_IMAGE",
		TextToImageParams: TextToImageParams{
			Text: prompt,
		},
		ImageGenerationConfig: ImageGenerationConfig{
			NumberOfImages: 1,
			Quality:        "standard",
			CfgScale:       8.0,
			Height:         512,
			Width:          512,
			Seed:           seed,
		},
	})

	if err != nil {
		log.Fatal("failed to marshal", err)
	}

	output, err := wrapper.BedrockRuntimeClient.InvokeModel(ctx, &bedrockruntime.InvokeModelInput{
		ModelId:     aws.String(modelId),
		ContentType: aws.String("application/json"),
		Body:        body,
	})

	if err != nil {
		ProcessError(err, modelId)
	}

	var response TitanImageResponse
	if err := json.Unmarshal(output.Body, &response); err != nil {
		log.Fatal("failed to unmarshal", err)
	}

	base64ImageData := response.Images[0]

	return base64ImageData, nil

}
```
+  For API details, see [InvokeModel](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/bedrockruntime#Client.InvokeModel) in *AWS SDK for Go API Reference*.

## Anthropic Claude
<a name="anthropic_claude"></a>

### Converse
<a name="bedrock-runtime_Converse_AnthropicClaude_go_2_topic"></a>

The following code example shows how to send a text message to Anthropic Claude, using Bedrock's Converse API.

**SDK for Go V2**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/gov2/bedrock-runtime#code-examples).
Send a text message to Anthropic Claude, using Bedrock's Converse API.

```
import (
	"context"
	"github.com/aws/aws-sdk-go-v2/aws"
	"github.com/aws/aws-sdk-go-v2/service/bedrockruntime"
	"github.com/aws/aws-sdk-go-v2/service/bedrockruntime/types"
)

// ConverseWrapper encapsulates Amazon Bedrock actions used in the examples.
// It contains a Bedrock Runtime client that is used to invoke Bedrock.
type ConverseWrapper struct {
	BedrockRuntimeClient *bedrockruntime.Client
}

func (wrapper ConverseWrapper) ConverseClaude(ctx context.Context, prompt string) (string, error) {
	var content = types.ContentBlockMemberText{
		Value: prompt,
	}
	var message = types.Message{
		Content: []types.ContentBlock{&content},
		Role:    "user",
	}
	modelId := "anthropic.claude-3-haiku-20240307-v1:0"
	var converseInput = bedrockruntime.ConverseInput{
		ModelId:  aws.String(modelId),
		Messages: []types.Message{message},
	}
	response, err := wrapper.BedrockRuntimeClient.Converse(ctx, &converseInput)
	if err != nil {
		ProcessError(err, modelId)
	}

	responseText, _ := response.Output.(*types.ConverseOutputMemberMessage)
	responseContentBlock := responseText.Value.Content[0]
	text, _ := responseContentBlock.(*types.ContentBlockMemberText)
	return text.Value, nil

}
```
+  For API details, see [Converse](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/bedrockruntime#Client.Converse) in *AWS SDK for Go API Reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK Code Examples. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query code-library` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
