---
source_url: https://docs.aws.amazon.com/solutions/latest/clickstream-analytics-on-aws/data-management.html
---

# Data management
<a name="data-management"></a>

 Data Management helps you manage your clickstream data. This module provides the following features:

1. Matadata management. The guidance automatically scans the data in your clickstream database to generate metadata, allowing you to view names and descriptions of events, event parameters, and user attributes, as well as update their display names, descriptions, and data dictionaries.

1. Traffic source configuration. You can update the traffic source categorization rules in this tab.

## Access Data Management
<a name="access-data-management"></a>

 Follow below steps:

1.  Go to **Clickstream Analytics on AWS Console**, in the **Navigation Bar**, choose **Analytics Studio**.

1.  In the Analytics Studio page that opens, choose **Data Management** in the left navigation panel.

**Note**
 Only the user with Administrator or Analyst role can modify the metadata, such as display name, description.

## Metadata management
<a name="metadata-management"></a>

The guidance automatically scans clickstream data to generate metadata and then stored them in Redshift on a daily basis. There are three types of metadata:
+ **Event**: metadata describes clickstream events.
+ **Event Parameter**: metadata describes clickstream event parameters.
+ **User Attribute:** metadata describes user attributesBelow tables list all the dimensions included in each type of the metadata.

## Metadata dimensions
<a name="metadata-dimensions"></a>

 Below tables list all the dimensions included in each type of the metadata.

**Event**

|  **Dimension name**  |  **Description**  |
| --- | --- |
|  Event name  |  The name of the event reported from SDK  |
|  Display name  |  The display name of the event. By default, it is the same as Event name, user can customize the display name.  |
|  Description  |  The description name of the event reported from SDK. User can customize the display name. For the event automatically collected by the clickstream SDK, the guidance has pre-populated description  |
|  Source  |  Describe how the event was collected, Preset indicates the event is automatically collected by SDK, Custom indicates the event is defined and collected by app owner  |
|  Platform  |  Describe which platform the event was collected from, i.e., from Android, Web or iOS  |
|  Data volume last day  |  Describe how much data was collected in last day (in UTC timezone)  |
|  SDK version  |  Describe the version of the SDK that collected the event  |
|  Associate preset parameters  |  The preset event parameters associated with the event  |
|  Associate custom parameters  |  The custom event parameters associated with the event  |

** Event parameters **

|  **Dimension name**  |  **Description**  |
| --- | --- |
|  Parameter name  |  The name of the event event parameter reported from SDK  |
|  Display name  |  The display name of the event parameter. By default, it is the same as Parameter name, user can customize the display name.  |
|  Description  |  The description name of the event parameter reported from SDK. User can customize the display name. For the event automatically collected by the clickstream SDK, the guidance has pre-populated description  |
|  Source  |  Describe how the event parameter was collected, Preset indicates the event parameter is automatically collected by SDK, Custom indicates the event parameter is defined and collected by app owner  |
|  Data type  |  Describe the data type of the event parameter value, e.g., int, string,  |
|  Associate event  |  The event that the event parameters associated with.  |
|  Dictionary  |  The unique value for the event parameters, user can customize the display value.  |

** User attribute **

|  **Dimension name**  |  **Description**  |
| --- | --- |
|  Attribute name  |  The name of the user attribute reported from SDK  |
|  Display name  |  The display name of the user attribute. By default, it is the same as Attribute name, user can customize the display name.  |
|  Description  |  The description name of the user attribute reported from SDK. User can customize the display name. For the user attribute automatically collected by the clickstream SDK, the guidance has pre-populated description  |
|  Source  |  Describe how the event parameter was collected, Preset indicates the user attribute is automatically collected by SDK, Custom indicates the user attribute is defined and collected by app owner  |
|  Data type  |  Describe the data type of the user attribute value, e.g., int, string,  |

## Update event display name and description
<a name="update-event-display-name-and-description"></a>

1.  Click on the **Events** page, select any event, for example, view\_item.

1.  Click on the column labeled **Display Name**, enter a name, such as View Product Details, and then click confirm.

1.  Go back to Exploration, and in the filter dropdown, you can see view\_item now displayed as View Product Details.

 Follow the same steps to update display name and description for Event Parameters and User Attributes.

## Customize data dictionary for Event Parameter values
<a name="customize-data-dictionary-for-event-parameter-values"></a>

1.  Click on the **Event Properties** page, and in the search box, select an event parameter, such as \_entrances.

1.  The detailed information for the property should open automatically, choose the **Dictionary** page.

1.  Click on the column labeled **Display Value**, enter a new value, such as Non-First Entry for 0, and enter First Entry for 1, then click confirm.

1.  Go back to Exploration, and in the filter dropdown, you can see \_entrances displayed as Non-First Entry and First Entry.

 Follow the same steps to customize data dictionary for User Attributes values.

## Traffic source
<a name="traffic-source"></a>

Traffic source describes the channel through which the users arrive at your website or application, such as paid ads, marketing campaigns, search engines, and social networks. This article describes how the guidance collects and processes traffic-source data.

**Traffic-source data fields **

Traffic source includes the following key dimension to describe how the users arrives at your website or app.:

1. Source - where the traffic originates ( e.g., google, baidu, bing)

1. Medium - the methods by which users arrive at your site/app (medium, e.g., organic, cpc/ppc, email).

1. Campaign - the specific marketing efforts you use to drive that traffic (e.g., campaign, creative format, keywords).

1. Auto-tagged Click ID - the parameter generated and appended by ad platform automatically when ad are showed and clicked. (e.g., gclid).

   Clickstream Analytics on AWS uses below dimensions and fields to track traffic-source data when sending events.

|  **Dimension**  |  **Clickstream SDK preserved attributes** | **UTM parameters in page\_url (Web only)** | **Field in data schema** |
| --- | --- | --- | --- |
| Source  | \_traffic\_source\_source  | utm\_source  | traffic\_source\_source  |
| Medium  | \_traffic\_source\_medium  | utm\_medium  | traffic\_source\_medium  |
| Campaign Name  | \_traffic\_source\_campaign  | utm\_campaign  | traffic\_source\_campaign  |
| Campaign ID  | \_traffic\_source\_id  | utm\_id  | traffic\_source\_id  |
| Campaign Term  | \_traffic\_source\_term  | utm\_term  | traffic\_source\_term  |
| Campaign Content  | \_traffic\_source\_content  | utm\_content  | traffic\_source\_content  |
| Auto-tagged Click ID  | \_traffic\_source\_clid  | (\*)clid  | traffic\_source\_clid  |
| Auto-tagged Click ID Platform | \_traffic\_source\_clid\_platform  | N/A  | traffic\_source\_clid\_platform  |
| App Install Source  | \_app\_install\_channel | N/A  | app\_install\_source  |

Below two dimensions are enriched from above traffic-source data fields and added to each event

|  **Dimension**  |  **Field in data schema** | **Description** |
| --- | --- | --- |
| Source Category  | \_\_traffic\_source\_category | Categories based on traffic\_source\_source and referral domain, including Search, Social, Shopping, Video, and Internal |
| Channel Group  | \_traffic\_source\_channel\_group | A channel group is a set of channels, which are rule-based categories of your traffic sources, for example, paid search, paid social. |

## Processing
<a name="processing-1"></a>

During data processing, traffic-source field values are populated into dimension values for each event and attributed to users and sessions. Below describes the details steps.

**Step 1 - Extract traffic-source data **

1. If the preset traffic-source attributes are set with values, data process module will map their values them into corresponding traffic-source data fields. For example, map the value of \_traffic\_source\_source to traffic\_source\_source field.

1. (For web only) If the preset traffic-source attributes have no values, data processing module will map the utm\_parameters (e.g., utm\_source) and auto-tagged click id in the page\_url fields into corresponding traffic-source data fields. For example, map the value of utm\_source to traffic\_source\_source field.

1. (For web only) If the source dimension are still blank after above steps, data processing module will check if there is value in page\_view\_latest\_referrer field, and look up source value from the Source Category mapping table based on the domain of the referrer, if no source is matched, it will use the top-level domain name as the value of the traffic\_source\_source dimension.

**Step 2 - Derive source category**

Data processing module uses a Source Category mapping table (to classify the source into different categories (i.e., search, shopping, video, social). For example, source with values of "google" or "bing" will be classified into Search category.

**Step 3 - Derive channel group**

Data processing module uses a set of predefined rules to categorize the traffics into different groups (e.g., direct, paid search, organic search) based on the key traffic-source dimensions (mainly the source. medium, and campaign).

**Step 4 - Populate traffic source dimensions for user and session tables**

While process the traffic-source for each event, the data processing module populate traffic source dimension for each user and session.

1. **User:** If there are traffic-source data in the first meaningful events (e.g., first\_open, page\_view, app\_start, app\_end) for the first time user visit your website or apps, those traffic-source dimension will be assigned to corresponding user traffic-source attributes, i.e., first\_traffic\_source, first\_traffic\_medium.

1. **Session:** When user initiate a new session, the data processing module derives traffic-source dimension for the session from the traffic-source dimensions of the first meaningful events in the session (e.g., first\_open, page\_view, app\_start, app\_end).

## Configurations
<a name="configurations-1"></a>

Clickstream Analytics on AWS allows you to configure the channel group rules and source category mapping to customize the traffic source processing to meet your analytics needs.

**Channel group definitions and rules**

Below are the default channel groups and the rules that the guidance uses to categorize the traffic:

|  **Order**  |  **Channel** | **Description** | **Evaluation rules** |
| --- | --- | --- | --- |
| 1 | Direct | Direct is the channel by which users arrive at your site/app via a saved link or by entering your URL. | 1. traffic\_source\_category, traffic\_source\_source,traffic\_source\_medium,traffic\_source\_campaign,traffic\_source\_content,traffic\_source\_term/\\,traffic\_source\_campaign\_id,traffic\_source\_clid are all blank/(not set), (none) AND 2. latest\_referrer is blank |
| 2 | Paid Search | Paid Search is the channel by which users arrive at your site/app via ads on search-engine sites like Bing, Baidu, or Google. | 1. traffic\_source\_category is Search AND (2. traffic\_source\_medium matches regex ^(.cp.\|ppc\|retargeting\|paid.\*)$ OR clid is not none/blank). |
| 3 | Organic Search | Organic Search is the channel by which users arrive at your site/app via non-ad links in organic-search results. | 1. traffic\_source\_category is Search AND (2. medium is blank or none or exactly matches organic). |
| 4 | Paid Social | Paid Social is the channel by which users arrive at your site/app via ads on social sites like Facebook and Twitter. | 1. traffic\_source\_category is Social AND 2. traffic\_source\_medium matches regex ^(.*cp.*\|ppc\|retargeting\|paid.\*)$ OR clid is not none/blank. |
| 5 | Organic Social | Organic Social is the channel by which users arrive at your site/app via non-ad links on social sites like Facebook or Twitter. | 1. traffic\_source\_category is Social OR 2. traffic\_source\_medium is one of ("social", "social-network", "social-media", "sm", "social network", "social media") |
| 6 | Paid Video | Paid Video is the channel by which users arrive at your site/app via ads on video sites like TikTok, Vimeo, and YouTube. | 1. traffic\_source\_category is Video (i.e., traffic\_source\_source OR latest\_referrer\_host matches a list of video sites ) AND (2. traffic\_source\_medium matches regex ^(.*cp.*\|ppc\|retargeting\|paid.\*)$ OR clid is not none/blank). |
| 7 | Organic Video | Organic Video is the channel by which users arrive at your site/app via non-ad links on video sites like YouTube, TikTok, or Vimeo. | 1. traffic\_source\_category is Video OR 2. traffic\_source\_medium matches regex ^(.video.)$. |
| 8 | Paid Shopping | Paid Shopping is the channel by which users arrive at your site/app via paid ads on shopping sites like Amazon or ebay or on individual retailer sites. | 1. traffic\_source\_category is Shopping AND (2. traffic\_source\_medium matches regex ^(.*cp.*\|ppc\|retargeting\|paid.*)$*<br />*OR clid is not none/blank* *OR traffic\_source\_campaign matches regex ^(.*(([\\^a-df-z]\|^)shop\|shopping).\*)$). |
| 9 | Organic Shopping | Organic Shopping is the channel by which users arrive at your site/app via non-ad links on shopping sites like Amazon or ebay. | 1. traffic\_source\_category is Shopping OR 2. traffic\_source\_campaign matches regex ^(.*(([\\^a-df-z]\|^)shop\|shopping).*)$ . |
| 10 | Paid Other | Paid Other is the channel by which users arrive at your site/app via ads, but not through an ad identified as Search, Social, Shopping, or Video. | 1. traffic\_source\_category is none AND 2. traffic\_source\_medium matches regex ^(.*cp.*\|ppc\|retargeting\|paid.\*)$. |
| 11 | Email | Email is the channel by which users arrive at your site/app via links in email. | 1. traffic\_source\_source contains "mail" OR 2. traffic\_source\_medium contains "mail" OR 3. latest\_referrer\_host start with "mail". |
| 12 | SMS | SMS is the channel by which users arrive at your site/app via links from text messages. | 1. traffic\_source\_source exactly matches sms OR 2. traffic\_source\_medium exactly matches "sms" . |
| 13 | Audio | Audio is the channel by which users arrive at your site/app via ads on audio platforms (e.g., podcast platforms). | 1.traffic\_source\_medium exactly matches audio |
| 14 | Mobile Push Notifications | Mobile Push Notifications is the channel by which users arrive at your site/app via links in mobile-device messages when they're not actively using the app. | 1. traffic\_source\_medium ends with "push" OR 2.traffic\_source\_medium contains "mobile" or "notification" . |
| 15 | Referral | Referral is the channel by which users arrive at your site via non-ad links on other sites/apps (e.g., blogs, news sites). | 1. latest\_referrer is not none AND traffic\_source\_category is none AND 2. latest referrer\_host is not Internal Domain . |
| 16 | Internal | Traffic from specified internal domain. | 1. latest\_referrer\_host is one of the Internal domains. |
| 17 | Unassigned | Traffic that can not be assigned to a channel group. | All others |

To create and edit channel group, go to the Data Management > Traffic Source tab > Channel group.

1. Create a new group.
   + Click on the Add new group button.
   + Fill in the Group name, Description, and Condition.
   + Click on Reorder, adjust the evaluation sequence to by clicking on the Upper arrow or Down arrow, then click the Apply.

   2. Edit a channel group
   + Select a channel group
   + Click the action button, and select View details
   + Update the channel group then click on Confirm.
   + Click on the Reorder
   + Adjust the sequence of the channel group by clicking on the Upper arrow and Down arrow.
   + Click Apply to save the order.

**Source category mapping table**

Clickstream Analytics on AWS uses a source category mapping table to classify some known sources into the categories of Search, Social, Shopping, and Video. You can also add Internal category for the traffic source coming from internal source. Below are the description for the columns in the mapping table.

|  **Column**  |  **Description**  | Example |
| --- | --- | --- |
| Domain | The host name of the referral URL.  | google.com, baidu.com  |
| Source name | The name for the traffic source.  | google, baidu  |
| Category | Category for the source.  | Search, Shopping, Social, Video, and Internal  |
| Keyword pattern | The keyword parameter name in the referral url, only for Search domain.  | q, query, keyword  |

To create and edit source category, go to the Data Management > Traffic Source tab > Source category.

1. Create a new category.
   + Click on the Add new category button. Or you can select an existing category, then click on Action>Copy to new.
   + Fill in the Domain, Source name, and Category.
   + If it is Search, fill in keyword pattern, you can add multiple.
   + Click on Confirm

   2. Edit a channel group
   + Select a category record
   + Click the action button, and select View details
   + Update the record then click on Confirm.
