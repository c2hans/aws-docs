---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_KbTemplateConfiguration.html
---

# KbTemplateConfiguration
<a name="API_KbTemplateConfiguration"></a>

The template configuration for a knowledge base. This object contains connector-specific configuration that defines how data is crawled and indexed.

## Contents
<a name="API_KbTemplateConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** template **   <a name="QS-Type-KbTemplateConfiguration-template"></a>
The connector configuration for the knowledge base data source. The structure depends on the connector type of the data source referenced by `DataSourceArn`.
The template must be a JSON object. The required fields vary by connector type:
+  **Amazon S3** (`S3V2`) – Requires `connectionConfiguration` with `bucketName`. Supports `filterConfiguration` for inclusion and exclusion prefixes and patterns. Supports `accessControlConfiguration` and `deletionProtectionConfiguration`.
+  **Google Drive** (`GOOGLEDRIVEV3`) – Requires `connectionConfiguration` with `authType` set to `SERVICE_ACCOUNT`. Supports `dataEntityConfiguration` with `crawlMyDrive`, `crawlSharedWithMe`, and `crawlSharedDrives`.
+  **OneDrive** (`ONEDRIVEV3`) – Requires `authType` at the template root level set to `TWO_LEGGED_OAUTH`. Requires `connectionConfiguration` with `tenantId` in UUID format. Supports `dataEntityConfiguration` with `crawlPersonalDrives` and `crawlSharedWithMe`.
+  **SharePoint** (`SHAREPOINTV3`) – Requires `connectionConfiguration` with `tenantId` in UUID format. Supports `dataEntityConfiguration` with `siteUrls`, `crawlFiles`, and `crawlPages`.
+  **Web Crawler** (`WEBCRAWLERV3`) – Requires `connectionConfiguration` with `seedUrls` or `siteMapUrls` (mutually exclusive) and `authType`. Supports `crawlConfiguration` for crawl depth, rate limits, and scope. Supports `filterConfiguration` for file size limits and URL patterns. Valid values for `authType`: `NO_AUTH`, `BASIC_AUTH`, `FORM`, `SAML`.
The optional `deletionProtectionConfiguration` object is supported by all connector types. It contains `enableDeletionProtection` and `deletionProtectionThreshold`.
Type: JSON value
Required: No

## See Also
<a name="API_KbTemplateConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/KbTemplateConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/KbTemplateConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/KbTemplateConfiguration)
