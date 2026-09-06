---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/configure-wave-planning-manager.html
---

# Step 9: Configure Wave Planning Manager
<a name="configure-wave-planning-manager"></a>

Wave Planning Manager (WPM) is an optional module that helps you organize and schedule your migration workloads in an optimal way. If you enabled it in [Launch the stack](launch-the-stack.md), review the following concepts.

## Prerequisites
<a name="prerequisites"></a>

### Bedrock available regions and model selection
<a name="bedrock-regions-model-selection"></a>

#### Generative AI support - Attribute mapping and rule creation
<a name="generative-ai-support"></a>

The Wave Planning Manager (WPM) module provides two optional features that utilize generative AI to streamline the user experience: automated header mapping; and intelligent rule creation.

If you choose to deploy WPM and want to enable these features, you will need to verify that [AWS Bedrock](https://aws.amazon.com/bedrock/) is available in your deployment Region. WPM will attempt to integrate with the following models, in preferential order:

1. (Anthropic) Claude Sonnet 4

1. Claude 3.7 Sonnet

1. Claude 3.5 Sonnet v2

1. Claude 3.5 Sonnet

1. Claude 3 Sonnet

1. (Amazon) Nova Pro

To use these features, you will need to [add access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access-modify.html) to the highest supported preferential model in your AWS Region.

**Note**
If none of these models are available, Bedrock is not available, or you do not wish to enable the highest supported preferred model, you can still enable WPM doing deployment. However, both features will not be available and users will need to manually map headers and define rules.

## Configure data source
<a name="configure-data-source"></a>

The WPM module enables many-to-many relationships during import. With this capability, applications can be deployed to many servers and a server can support many applications.

The import process is different, and requires the creation of a data source. For more information on how to create a data source, see [here](data-source-management.md#data-source-management-data-sources).

## Configure rules
<a name="configure-rules"></a>

Wave Planning Rules are a set of configurable guidelines that control how assets are processed during wave planning. WPM pre-defines a list of most frequently used rules as default rules, however you are also able to define your own custom rules based upon your data. To do this, see [this link](wave-planning-management.md#adding-planning-rules).
