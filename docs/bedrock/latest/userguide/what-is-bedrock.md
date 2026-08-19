---
source_url: https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html
---

# Overview
<a name="what-is-bedrock"></a>

Amazon Bedrock is a fully managed service that provides secure, enterprise-grade access to [high-performing foundation models](models.md) from leading AI companies, enabling you to build and scale generative AI applications.

## Quickstart
<a name="quickstart"></a>

Read the [Quickstart](getting-started.md) to write your first API call using Amazon Bedrock in under five minutes. For new applications, we recommend the `bedrock-runtime` endpoint.

------
#### [ Converse API ]

```
import boto3

client = boto3.client('bedrock-runtime', region_name='us-east-1')
response = client.converse(
    modelId='anthropic.claude-opus-4-7',
    messages=[
        {
            'role': 'user',
            'content': [{'text': 'Can you explain the features of Amazon Bedrock?'}]
        }
    ]
)
print(response)
```

------
#### [ Invoke API ]

```
import json
import boto3

client = boto3.client('bedrock-runtime', region_name='us-east-1')
response = client.invoke_model(
    modelId='anthropic.claude-opus-4-7',
    body=json.dumps({
            'anthropic_version': 'bedrock-2023-05-31',
            'messages': [{ 'role': 'user', 'content': 'Can you explain the features of Amazon Bedrock?'}],
            'max_tokens': 1024
    })
 )
 print(json.loads(response['body'].read()))
```

------
#### [ Responses API ]

```
from openai import OpenAI

client = OpenAI()

response = client.responses.create(
    model="openai.gpt-oss-120b",
    input="Can you explain the features of Amazon Bedrock?"
    )
print(response)
```

------
#### [ Chat Completions API ]

```
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="openai.gpt-oss-120b",
    messages=[{"role": "user", "content": "Can you explain the features of Amazon Bedrock?"}]
    )
print(response)
```

------
#### [ Messages API ]

```
import anthropic

client = anthropic.Anthropic()

response = client.messages.create(
    model="anthropic.claude-opus-4-7",
    max_tokens=1024,
    messages=[{"role": "user", "content": "Can you explain the features of Amazon Bedrock?"}]
)
print(response)
```

------

## Supported models
<a name="featured-models"></a>

Amazon Bedrock supports [100\+ foundation models](models.md) from industry-leading providers, including Amazon, Anthropic, DeepSeek, Moonshot AI, MiniMax, and OpenAI.

|  |  |  |  |  |  |
| --- |--- |--- |--- |--- |--- |
| ![Amazon logo with curved arrow from A to Z forming a smile.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/what-is/nova2pro.png)**Amazon Nova** | ![Orange rounded square icon with white radial loading spinner design.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/models/claude.png)**Claude** | ![DeepSeek logo.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/what-is/deepseek.png)**DeepSeek** | ![Spherical icon with horizontal stripes or segments across its surface.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/what-is/kimik2.5.png)**Kimi** | ![Red waveform icon representing audio or voice activity.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/what-is/minimax2.1.png)**MiniMax** | ![OpenAI logo.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/models/openai.png)**OpenAI** |

## What's new?
<a name="whats-new"></a>
+ [OpenAI GPT-5.6 Sol, Terra, and Luna now available in Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/07/openai-gpt-sol-terra/): A family of models from OpenAI that ranges from advanced reasoning to fast, cost-effective inference, now generally available through the Responses API on Amazon Bedrock. See the [GPT-5.6 Sol](model-card-openai-gpt-56-sol.md), [GPT-5.6 Terra](model-card-openai-gpt-56-terra.md), and [GPT-5.6 Luna](model-card-openai-gpt-56-luna.md) model cards for details.
+ [Claude Sonnet 5 now available in Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/06/claude-sonnet-5-now-available-on-aws/): The most capable Sonnet model from Anthropic to date, delivering strong performance across coding, agents, and everyday professional work at scale. See the [Claude Sonnet 5](model-card-anthropic-claude-sonnet-5.md) model card for details.
+ [Claude Opus 4.8 now available in Amazon Bedrock](https://aws.amazon.com/about-aws/whats-new/2026/05/claude-opus-4.8-aws/): The latest Opus model from Anthropic, delivering improvements across agentic coding, deep knowledge work, and multi-stage autonomous tasks. See the [Claude Opus 4.8](model-card-anthropic-claude-opus-4-8.md) model card for details.
+ [Claude Mythos Preview (Gated Research Preview)](https://aws.amazon.com/about-aws/whats-new/2026/04/amazon-bedrock-claude-mythos/): Anthropic's most advanced AI model with state-of-the-art capabilities across cybersecurity, software coding, and complex reasoning tasks. Available in gated preview in US East (N. Virginia).

## Start building
<a name="start-building"></a>

|  |  |
| --- |--- |
|  ![Cloud icon with bidirectional arrows indicating sync or data transfer.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/what-is/apis.jpg)  | Explore the [APIs supported by Amazon Bedrock](apis.md) and [Endpoints supported by Amazon Bedrock](endpoints.md) supported by Amazon Bedrock. |
|  ![Wrench and screwdriver icon on purple background.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/what-is/build.jpg)  | Build using the [Making inference requests](inference.md) operations provided by Amazon Bedrock. |
|  ![Amazon Bedrock model customization options including fine-tuning, continued pre-training, and distillation.](http://docs.aws.amazon.com/bedrock/latest/userguide/images/what-is/customize.png)  | Customize your models to improve performance and quality. [Customize your model to improve its performance for your use case](custom-models.md) |
