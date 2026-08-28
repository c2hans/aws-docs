---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_ListIntegrationItem.html
---

# ListIntegrationItem
<a name="API_connect-customer-profiles_ListIntegrationItem"></a>

An integration in list of integrations.

## Contents
<a name="API_connect-customer-profiles_ListIntegrationItem_Contents"></a>

 ** CreatedAt **   <a name="connect-Type-connect-customer-profiles_ListIntegrationItem-CreatedAt"></a>
The timestamp of when the domain was created.
Type: Timestamp
Required: Yes

 ** DomainName **   <a name="connect-Type-connect-customer-profiles_ListIntegrationItem-DomainName"></a>
The unique name of the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** LastUpdatedAt **   <a name="connect-Type-connect-customer-profiles_ListIntegrationItem-LastUpdatedAt"></a>
The timestamp of when the integration was most recently edited.
Type: Timestamp
Required: Yes

 ** Uri **   <a name="connect-Type-connect-customer-profiles_ListIntegrationItem-Uri"></a>
The URI of the S3 bucket or any other type of data source.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** EventTriggerNames **   <a name="connect-Type-connect-customer-profiles_ListIntegrationItem-EventTriggerNames"></a>
A list of unique names for active event triggers associated with the integration.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: No

 ** IsUnstructured **   <a name="connect-Type-connect-customer-profiles_ListIntegrationItem-IsUnstructured"></a>
Boolean that shows if the Flow that's associated with the Integration is created in Amazon Appflow, or with ObjectTypeName equals \_unstructured via API/CLI in flowDefinition.
Type: Boolean
Required: No

 ** ObjectTypeName **   <a name="connect-Type-connect-customer-profiles_ListIntegrationItem-ObjectTypeName"></a>
The name of the profile object type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
Required: No

 ** ObjectTypeNames **   <a name="connect-Type-connect-customer-profiles_ListIntegrationItem-ObjectTypeNames"></a>
A map in which each key is an event type from an external application such as Segment or Shopify, and each value is an `ObjectTypeName` (template) used to ingest the event. It supports the following event types: `SegmentIdentify`, `ShopifyCreateCustomers`, `ShopifyUpdateCustomers`, `ShopifyCreateDraftOrders`, `ShopifyUpdateDraftOrders`, `ShopifyCreateOrders`, and `ShopifyUpdatedOrders`.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 255.
Value Length Constraints: Minimum length of 1. Maximum length of 255.
Value Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
Required: No

 ** RoleArn **   <a name="connect-Type-connect-customer-profiles_ListIntegrationItem-RoleArn"></a>
The Amazon Resource Name (ARN) of the IAM role. The Integration uses this role to make Customer Profiles requests on your behalf.
Type: String
Length Constraints: Maximum length of 512.
Pattern: `arn:aws:iam:.*:[0-9]+:.*`
Required: No

 ** Scope **   <a name="connect-Type-connect-customer-profiles_ListIntegrationItem-Scope"></a>
The scope or boundary of the integration item's applicability.
Type: String
Valid Values: `PROFILE | DOMAIN`
Required: No

 ** Tags **   <a name="connect-Type-connect-customer-profiles_ListIntegrationItem-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

 ** WorkflowId **   <a name="connect-Type-connect-customer-profiles_ListIntegrationItem-WorkflowId"></a>
Unique identifier for the workflow.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

## See Also
<a name="API_connect-customer-profiles_ListIntegrationItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/ListIntegrationItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/ListIntegrationItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/ListIntegrationItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
