---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-dashboards.html
---

# Accessing OpenSearch Dashboards
<a name="serverless-dashboards"></a>

After you create a collection with the AWS Management Console, you can navigate to the collection's OpenSearch Dashboards URL. You can find the Dashboards URL by choosing **Collections** in the left navigation pane and selecting the collection to open its details page. The URL takes the format `https://dashboards.{{us-east-1}}.aoss.amazonaws.com/_login/?collectionId={{07tjusf2h91cunochc}}`. After you navigate to the URL, you automatically log in to Dashboards.

If you already have the OpenSearch Dashboards URL available but aren't on the AWS Management Console, calling the Dashboards URL from the browser will redirect to the console. After you enter your AWS credentials, you automatically log in to Dashboards. For information about accessing collections for SAML, see [Accessing OpenSearch Dashboards with SAML](serverless-saml.md#serverless-saml-dashboards).

The OpenSearch Dashboards console timeout is one hour and isn't configurable.

**Note**
On May 10, 2023, OpenSearch introduced a common global endpoint for OpenSearch Dashboards. You can now navigate to OpenSearch Dashboards in the browser with a URL that takes the format `https://dashboards.{{us-east-1}}.aoss.amazonaws.com/_login/?collectionId={{07tjusf2h91cunochc}}`. To ensure backward compatibility, OpenSearch continues to support the existing collection specific OpenSearch Dashboards endpoints with the format `https://{{07tjusf2h91cunochc}}.{{us-east-1}}.aoss.amazonaws.com/_dashboards`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
