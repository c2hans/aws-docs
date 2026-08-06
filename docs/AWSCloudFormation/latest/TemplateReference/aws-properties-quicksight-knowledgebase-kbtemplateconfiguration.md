---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-quicksight-knowledgebase-kbtemplateconfiguration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::QuickSight::KnowledgeBase KbTemplateConfiguration
<a name="aws-properties-quicksight-knowledgebase-kbtemplateconfiguration"></a>

The template configuration for a knowledge base. This object contains connector-specific configuration that defines how data is crawled and indexed.

## Syntax
<a name="aws-properties-quicksight-knowledgebase-kbtemplateconfiguration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-quicksight-knowledgebase-kbtemplateconfiguration-syntax.json"></a>

```
{
  "[Template](#cfn-quicksight-knowledgebase-kbtemplateconfiguration-template)" : {{}}
}
```

### YAML
<a name="aws-properties-quicksight-knowledgebase-kbtemplateconfiguration-syntax.yaml"></a>

```
  [Template](#cfn-quicksight-knowledgebase-kbtemplateconfiguration-template): {{
    }}
```

## Properties
<a name="aws-properties-quicksight-knowledgebase-kbtemplateconfiguration-properties"></a>

`Template`  <a name="cfn-quicksight-knowledgebase-kbtemplateconfiguration-template"></a>
The connector configuration for the knowledge base data source. The structure depends on the connector type of the data source referenced by `DataSourceArn`.
The template must be a JSON object. The required fields vary by connector type:
+ **Amazon S3** (`S3V2`) – Requires `connectionConfiguration` with `bucketName`. Supports `filterConfiguration` for inclusion and exclusion prefixes and patterns. Supports `accessControlConfiguration` and `deletionProtectionConfiguration`.
+ **Google Drive** (`GOOGLEDRIVEV3`) – Requires `connectionConfiguration` with `authType` set to `SERVICE_ACCOUNT`. Supports `dataEntityConfiguration` with `crawlMyDrive`, `crawlSharedWithMe`, and `crawlSharedDrives`.
+ **OneDrive** (`ONEDRIVEV3`) – Requires `authType` at the template root level set to `TWO_LEGGED_OAUTH`. Requires `connectionConfiguration` with `tenantId` in UUID format. Supports `dataEntityConfiguration` with `crawlPersonalDrives` and `crawlSharedWithMe`.
+ **SharePoint** (`SHAREPOINTV3`) – Requires `connectionConfiguration` with `tenantId` in UUID format. Supports `dataEntityConfiguration` with `siteUrls`, `crawlFiles`, and `crawlPages`.
+ **Web Crawler** (`WEBCRAWLERV3`) – Requires `connectionConfiguration` with `seedUrls` or `siteMapUrls` (mutually exclusive) and `authType`. Supports `crawlConfiguration` for crawl depth, rate limits, and scope. Supports `filterConfiguration` for file size limits and URL patterns. Valid values for `authType`: `NO_AUTH`, `BASIC_AUTH`, `FORM`, `SAML`.
The optional `deletionProtectionConfiguration` object is supported by all connector types. It contains `enableDeletionProtection` and `deletionProtectionThreshold`.
*Required*: No
*Type*:
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)
