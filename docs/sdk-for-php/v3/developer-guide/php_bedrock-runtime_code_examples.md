---
source_url: https://docs.aws.amazon.com/sdk-for-php/v3/developer-guide/php_bedrock-runtime_code_examples.html
---

# Amazon Bedrock Runtime examples using SDK for PHP
<a name="php_bedrock-runtime_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for PHP with Amazon Bedrock Runtime.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Amazon Nova](#amazon_nova)
+ [Stable Image Core](#stable_image_core)

## Amazon Nova
<a name="amazon_nova"></a>

### Converse
<a name="bedrock-runtime_Converse_AmazonNovaText_php_topic"></a>

The following code example shows how to send a text message to Amazon Nova, using Bedrock's Converse API.

**SDK for PHP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/bedrock-runtime#code-examples).
Send a text message to Amazon Nova, using Bedrock's Converse API.

```
// Use the Conversation API to send a text message to Amazon Nova.

use Aws\BedrockRuntime\BedrockRuntimeClient;
use Aws\Exception\AwsException;
use RuntimeException;

class Converse
{
    public function converse(): string
    {
        // Create a Bedrock Runtime client in the AWS Region you want to use.
        $client = new BedrockRuntimeClient([
            'region' => 'us-east-1',
            'profile' => 'default'
        ]);

        // Set the model ID, e.g., Amazon Nova Lite.
        $modelId = 'amazon.nova-lite-v1:0';

        // Start a conversation with the user message.
        $userMessage = "Describe the purpose of a 'hello world' program in one line.";
        $conversation = [
            [
                "role" => "user",
                "content" => [["text" => $userMessage]]
            ]
        ];

        try {
            // Send the message to the model, using a basic inference configuration.
            $response = $client->converse([
                'modelId' => $modelId,
                'messages' => $conversation,
                'inferenceConfig' => [
                    'maxTokens' => 512,
                    'temperature' => 0.5
                ]
            ]);

            // Extract and return the response text.
            $responseText = $response['output']['message']['content'][0]['text'];
            return $responseText;
        } catch (AwsException $e) {
            echo "ERROR: Can't invoke {$modelId}. Reason: {$e->getAwsErrorMessage()}";
            throw new RuntimeException("Failed to invoke model: " . $e->getAwsErrorMessage(), 0, $e);
        }
    }
}

$demo = new Converse();
echo $demo->converse();
```
+  For API details, see [Converse](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-runtime-2023-09-30/Converse) in *AWS SDK for PHP API Reference*.

## Stable Image Core
<a name="stable_image_core"></a>

### InvokeModel
<a name="bedrock-runtime_InvokeModel_StableDiffusion_php_topic"></a>

The following code example shows how to invoke Stability.ai Stable Image Core on Amazon Bedrock to generate an image.

**SDK for PHP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/bedrock-runtime#code-examples).
Create an image with Stable Diffusion.

```
    public function invokeStableDiffusion(string $prompt, int $seed = 0, string $aspect_ratio = '1:1')
    {
        // The different model providers have individual request and response formats.
        // For the format, ranges, and available parameters of Stable Diffusion models refer to:
        // https://docs.aws.amazon.com/bedrock/latest/userguide/model-parameters-stability-diffusion.html

        $base64_image_data = "";
        try {
            $modelId = 'stability.stable-image-core-v1:1';
            $body = [
                'prompt' => $prompt,
                'aspect_ratio' => $aspect_ratio,
                'seed' => $seed,
                'output_format' => 'png',
            ];

            $result = $this->bedrockRuntimeClient->invokeModel([
                'contentType' => 'application/json',
                'body' => json_encode($body),
                'modelId' => $modelId,
            ]);
            $response_body = json_decode($result['body']);
            $base64_image_data = $response_body->images[0];
        } catch (Exception $e) {
            echo "Error: ({$e->getCode()}) - {$e->getMessage()}\n";
        }

        return $base64_image_data;
    }
```
+  For API details, see [InvokeModel](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-runtime-2023-09-30/InvokeModel) in *AWS SDK for PHP API Reference*.
