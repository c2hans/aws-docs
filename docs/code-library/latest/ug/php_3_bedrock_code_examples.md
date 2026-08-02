---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/php_3_bedrock_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Amazon Bedrock examples using SDK for PHP
<a name="php_3_bedrock_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for PHP with Amazon Bedrock.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `ListFoundationModels`
<a name="bedrock_ListFoundationModels_php_3_topic"></a>

The following code example shows how to use `ListFoundationModels`.

**SDK for PHP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/bedrock#code-examples).
List the available Amazon Bedrock foundation models.

```
    public function listFoundationModels()
    {
        $bedrockClient = new BedrockClient([
            'region' => 'us-west-2',
            'profile' => 'default'
        ]);
        $response = $bedrockClient->listFoundationModels();
        return $response['modelSummaries'];
    }
```
+  For API details, see [ListFoundationModels](https://docs.aws.amazon.com/goto/SdkForPHPV3/bedrock-2023-04-20/ListFoundationModels) in *AWS SDK for PHP API Reference*.
