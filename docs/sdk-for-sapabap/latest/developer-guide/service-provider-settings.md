---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/service-provider-settings.html
---

# Service provider settings
<a name="service-provider-settings"></a>

Basis administrators sometimes need to control certain features of the SDK across the entire system, from client `000`. This is a common scenario for hosting and service providers that operate systems in their own AWS account on behalf of their customers. AWS SDK for SAP ABAP supports Service Provider settings. These settings are configured in client `000`, and affect the SDK across all clients. Service Provider settings are not supported in SDK for SAP ABAP - BTP edition.

Service Provider settings are configured in transaction `/AWS1/IMG`, and must be configured in client `000`. Service Provider settings in other clients are ignored. The settings in client `000` take effect across all clients, and supercede other `IMG` settings in case of conflict.

Use the following steps to configure the Service Provider settings in client `000`.

1. Expand the **Service Provider Settings** branch in transaction `/AWS1/IMG`.

1. Choose **Service Provider Guardrails**

1. Select **New Entries**, and adjust the settings based on your business requirements.

   1. *Disable EC2 Metadata* – prevents the SDK from accessing EC2 instance metadata in all clients, even if an SDK Profile is configured to authenticate using EC2 instance metadata. The SDK raises an exception if an ABAP program attempts to access instance metadata using the SDK.

1. Select **Save**.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for SAP ABAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-sapabap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
