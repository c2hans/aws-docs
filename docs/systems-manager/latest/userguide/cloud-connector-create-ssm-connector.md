---
source_url: https://docs.aws.amazon.com/systems-manager/latest/userguide/cloud-connector-create-ssm-connector.html
---

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html).

# Step 2: Create a Systems Manager Cloud Connector
<a name="cloud-connector-create-ssm-connector"></a>

After the AWS Config connector is set up, create the Systems Manager Cloud Connector. The Systems Manager Cloud Connector stores the Azure tenant and subscription configuration and links it to the AWS Config connector.

**To create a Systems Manager Cloud Connector**

1. Run the following command. Replace the placeholder values with your Azure tenant ID, the Systems Manager application (client) ID, subscription IDs, the Systems Manager Azure federation role ARN, and the AWS Config connector ARN from Step 1.

   ```
   aws ssm create-cloud-connector \
       --display-name "{{MyAzureConnector}}" \
       --configuration '{
           "AzureConfiguration": {
               "TenantId": "{{TENANT_ID}}",
               "ApplicationId": "{{SSM_APP_CLIENT_ID}}",
               "Targets": {
                   "Subscriptions": [
                       {"Id": "{{SUBSCRIPTION_ID}}"}
                   ]
               }
           }
       }' \
       --role-arn "arn:aws:iam::{{ACCOUNT_ID}}:role/service-role/SSM-AzureRole-{{CONNECTOR_NAME}}-{{ID8}}" \
       --config-connector-arn {{CONFIG_CONNECTOR_ARN}}
   ```

   To target all subscriptions in the tenant (tenant-level setup), omit the `Targets` field from the configuration.

   The response returns the `CloudConnectorId`. Note this value for future operations.

1. Verify the Cloud Connector was created successfully:

   ```
   aws ssm get-cloud-connector \
       --cloud-connector-id {{CLOUD_CONNECTOR_ID}}
   ```
