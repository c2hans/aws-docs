---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/opensearch-service-migration/functionality.html
---

# Functionality
<a name="functionality"></a>

The functionality focus area helps you ensure that you do not lose any functionality when you migrate to a target Amazon OpenSearch Service environment. We recommend paying close attention to the following aspects:
+ Current solution functionality
+ Amazon OpenSearch Service functionality
+ Packaged plugins

## Current solution functionality
<a name="current-functionality"></a>

We recommend that you analyze your current solution and determine the features, plugins, and APIs that you use in the current technology stack (for example, Elasticsearch, OpenSearch, or another solution). Determine what functionality is critical to your business, what can be modified, and what can be dropped during the migration.

## Amazon OpenSearch Service functionality
<a name="opensearch-service-functionality"></a>

To ensure that required functionality is available after migration, we recommend that you perform an analysis of the latest OpenSearch version supported by Amazon OpenSearch Service, including the features it offers, and the plugins that are available in Amazon OpenSearch Service. You want to confirm that the target platform supports the features you need (for example, index state management, which automates rolling over of the indexes, or machine learning features such as anomaly detection). Map the existing functionality of your current solution to features in Amazon OpenSearch Service that provide you with equivalent capability so that you can continue to support your workloads.

For more information about the functionality available within each supported version of the Elasticsearch or OpenSearch software, see the [Amazon OpenSearch Service documentation](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/features-by-version.html).

## Packaged plugins
<a name="licensed-plugins"></a>

Amazon OpenSearch Service supports a number of plugins that are part of the open-source OpenSearch project. If you are using any *licensed plugin* from the Elasticsearch suite that is part of X-Pack or otherwise, you might want to determine an equivalent plugin or native feature within the OpenSearch offerings. You might also want to capture that as a point to prove in the PoC stage.

OpenSearch has several plugins that provide enterprise-grade features equivalent to those licensed plugins. To determine the correct plugin and version for the target environment, review the OpenSearch Service documentation's list of [plugins by versions](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/supported-plugins.html). While Amazon OpenSearch Service supports a number of OpenSearch plugins out of the box, you might be using an open source OpenSearch plugin that isn't currently available within Amazon OpenSearch Service. To request adding the plugin to the Amazon OpenSearch Service future roadmap, [contact AWS](https://aws.amazon.com/contact-us/).

## Custom plugins
<a name="custom-plugins"></a>

At the time of writing this guide, custom plugins are not supported. Therefore, you will need to consider alternate ways to deliver the custom plugin function and experience. If your solution uses custom plugins, analyze the functionality to determine whether you can port the custom plugins to the target environment using Amazon OpenSearch Service supported plugins or native features within OpenSearch. We recommend testing and proving all plugin choices during the PoC stage. Migration is a good time to evaluate current solution functionality to determine whether it is critical to your business.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
