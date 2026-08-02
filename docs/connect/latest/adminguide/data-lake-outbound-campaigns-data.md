---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/data-lake-outbound-campaigns-data.html
---

# Outbound campaigns data in the Connect Customer data lake
<a name="data-lake-outbound-campaigns-data"></a>

This topic details the content in the Connect Customer data lake outbound campaign events table. The table lists the column, type, and description of the content.

There are two ways to access the analytics data lake and configure data to be shared:
+ [Option 1: Use the Connect Customer console](access-datalake.md#option1-configure-data-to-be-shared)
+ [Option 2: Use CLI or CloudShell](access-datalake.md#option2-configure-data-to-be-shared)

If you are unable to access the scheduling tables by using Option 1, try using Option 2.

## Outbound campaign events
<a name="data-lake-oc-events"></a>

**Table name:** `outbound_campaign_events`

**Description:** Records outbound campaign lifecycle events across voice, email, and SMS channels, including delivery attempts, campaign outcomes, and recipient interactions.

**Primary key:** `campaign_event_id, instance_id`

**Partition key:** `campaign_event_timestamp` (daily)

**Join keys:**
+ `instance_id` — Joins to all tables
+ `campaign_id` — Joins to Contact Record (as `campaign_Id`)
+ `profile_id` — Joins to Customer Profiles (external)

| **Column** | **Type** | **Nullable** | **Description** |
| --- | --- | --- | --- |
| account\_profile\_id | String |  Yes  | Specifies the profile identifier for an account-based profile in Customer Profiles. |
| instance\_id | String |  No  | The identifier of the Connect Customer instance. |
| instance\_arn | String |  Yes  | The ARN of the Connect Customer instance. |
| aws\_account\_id | String |  Yes  | The identifier of the AWS account that owns the outbound campaign.  |
| campaign\_id | String |  Yes  | The identifier for the outbound campaign. |
| campaign\_name | String |  Yes  | The name of the outbound campaign. |
| campaign\_initiation\_type | String |  Yes  | The campaign initiation method selected for the outbound campaign. For example: CUSTOMER\_SEGMENT, CUSTOMER\_EVENT. |
| campaign\_execution\_timestamp | Timestamp |  Yes  | The Timestamp indicating the start of each campaign execution. Multiple Timestamps can exist for campaigns that run repeatedly. |
| campaign\_event\_id | String |  No  | The unique identifier for each outbound campaign event. |
| campaign\_event\_category | String |  Yes  | The category of the outbound campaign event, used to group individual event types into higher-level classes such as delivery receipt, campaign send, orchestration, and campaign action events. |
| campaign\_event\_type | String |  Yes  | The specific outbound campaign event type.<br />*Campaign events:*[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/data-lake-outbound-campaigns-data.html)<br />*Email events:*[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/data-lake-outbound-campaigns-data.html)<br />*SMS events:*[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/data-lake-outbound-campaigns-data.html)<br />*Telephony events:*[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/data-lake-outbound-campaigns-data.html)<br />*WhatsApp events:*[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/data-lake-outbound-campaigns-data.html)<br />*Web notification events:*[See the AWS documentation website for more details](http://docs.aws.amazon.com/connect/latest/adminguide/data-lake-outbound-campaigns-data.html) |
| campaign\_event\_timestamp | Timestamp |  Yes  | The Timestamp indicating when the outbound campaign event occurred.  |
| delivery\_attempt\_id | String |  Yes  | The identifier for the outbound communication delivery attempt. |
| channel | String |  Yes  | The method used to contact your contact center. For example: VOICE, CHAT, EMAIL, NOTIFICATION. This field may be blank for campaign events when this value is not applicable. |
| subtype | String |  Yes  | The outbound campaign delivery mode used to contact the campaign recipient. For example: connect:Email, connect:SMS, connect:Telephony, connect:WhatsApp, connect:WebNotification. Note: Telephony includes both the Agent Assisted Voice, Automated Voice delivery modes. This field may be blank for campaign events when this value is not applicable.  |
| profile\_id | String |  Yes  | The unique identifier of an Connect Customer Customer Profile. Note: This attribute is only available when you use segmentation capabilities offered with Connect Customer Customer Profiles. |
| campaign\_segment\_arn | String |  Yes  | The ARN of a segment of users. Note: This attribute is only available when you use segmentation capabilities offered with Connect Customer Customer Profiles. |
| campaign\_url\_link\_click | String |  Yes  | The URL link clicked by the outbound campaign recipient. This attribute is applicable to email campaigns.  |
| web\_notification\_type | String |  No  | The type of web notification delivered to the recipient. This attribute is applicable to web notification campaigns. |
| device\_type | String |  No  | The type of device on which the recipient received the web notification (for example, desktop, mobile). This attribute is applicable to web notification campaigns. |
| device\_model | String |  No  | The model of the device on which the recipient received the web notification. This attribute is applicable to web notification campaigns. |
| browser\_name | String |  No  | The name of the browser in which the recipient received the web notification. This attribute is applicable to web notification campaigns. |
| campaign\_is\_final\_status | Boolean |  Yes  | Set to True if this is the final state of the message. There are intermediate message statuses and it can take up to 72 hours for the final state to be received. This attribute is applicable to SMS campaigns. |
| data\_lake\_last\_processed\_timestamp | Timestamp |  Yes  | The timestamp, which shows the last time the record was touched by the data lake. This can include transformation and backfill. This field cannot reliably be used to determine data freshness. |
| lambda\_function\_arn | String |  Yes  | The Lambda Function ARN invoked by Outbound Campaigns. |
| lambda\_invocation\_result | String |  Yes  | The result of the Lambda Function invocation attempt. Set to SUCCESS: Outbound Campaigns successfully invoked the Lambda function and received a response, including [function errors](https://docs.aws.amazon.com/lambda/latest/api/API_Invoke.html#API_Invoke_ResponseSyntax) and malformed responses. Set to ERROR: Outbound Campaigns failed to invoke the Lambda function or couldn't confirm successful invocation (e.g., timeout). |
| orchestration\_event\_context\_subtype | String |  Yes  | Provides additional granularity for outbound campaign events indicating the specific reason a target was not reached. |
