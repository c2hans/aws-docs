---
source_url: https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/jamf-pro-source-config.html
---

# Source configuration for Jamf Pro
<a name="jamf-pro-source-config"></a>

## Integrating with Jamf Pro
<a name="jamf-pro-integration"></a>

CloudWatch Pipeline uses the Jamf Pro API to retrieve device inventory and management data. The API provides endpoints for querying computer, mobile device, and user information for security monitoring and compliance.

To integrate CloudWatch Pipelines with Jamf Pro, complete the following high-level steps:
+ Create an API Client in the Jamf Pro console with appropriate permissions.
+ Note the Client ID and Client Secret.
+ Store the credentials in AWS Secrets Manager.
+ Create a CloudWatch pipeline with Jamf Pro as the data source.
+ Verify that data is flowing into the pipeline.

## Prerequisites
<a name="jamf-pro-prerequisites"></a>

Before you begin, ensure you have the following:
+ An active Jamf Pro instance (cloud or on-premises)
+ An API Client configured with read permissions for computers, mobile devices, and users
+ An AWS account with permissions to create and manage CloudWatch Pipelines
+ An AWS account with permissions to create, retrieve, and update secrets in AWS Secrets Manager

## Authenticating with Jamf Pro
<a name="jamf-pro-authentication"></a>

Jamf Pro uses OAuth 2.0 Client Credentials for API authentication. The pipeline uses the Client ID and Client Secret to obtain access tokens for API requests.

## Configure Authentication for Jamf Pro
<a name="jamf-pro-configure-auth"></a>

To configure authentication credentials for the pipeline:

1. Log in to Jamf Pro and navigate to Settings > System > API Roles and Clients.

1. Create a new API Client with the required permissions (Read Computers, Read Mobile Devices, Read Users).

1. Note the Client ID and Client Secret provided.

1. Store the `client_id` and `client_secret` in AWS Secrets Manager.

## Configuring the CloudWatch Pipeline
<a name="jamf-pro-pipeline-config"></a>

To configure the pipeline, choose Jamf Pro as the data source. Provide the `hostname`, `client_id`, and `client_secret`. Once you create and activate the pipeline, device inventory data from Jamf Pro will begin flowing into the selected CloudWatch Logs log group.

## Supported Open Cybersecurity Schema Framework Event Classes
<a name="jamf-pro-ocsf-support"></a>

This integration supports the following OCSF event classes:
+ **Device Inventory Info [5001]** – Computer and mobile device inventory
