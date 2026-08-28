---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_DatasetSummary.html
---

# DatasetSummary
<a name="API_DatasetSummary"></a>

The summary details for the dataset.

## Contents
<a name="API_DatasetSummary_Contents"></a>

 ** arn **   <a name="iotsitewise-Type-DatasetSummary-arn"></a>
The [ARN](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference-arns.html) of the dataset. The format is `arn:${Partition}:iotsitewise:${Region}:${Account}:dataset/${DatasetId}`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`
Required: Yes

 ** creationDate **   <a name="iotsitewise-Type-DatasetSummary-creationDate"></a>
The dataset creation date, in Unix epoch time.
Type: Timestamp
Required: Yes

 ** description **   <a name="iotsitewise-Type-DatasetSummary-description"></a>
A description about the dataset, and its functionality.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[^\u0000-\u001F\u007F]+`
Required: Yes

 ** id **   <a name="iotsitewise-Type-DatasetSummary-id"></a>
The ID of the dataset.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `^(?!00000000-0000-0000-0000-000000000000)[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
Required: Yes

 ** lastUpdateDate **   <a name="iotsitewise-Type-DatasetSummary-lastUpdateDate"></a>
The date the dataset was last updated, in Unix epoch time.
Type: Timestamp
Required: Yes

 ** name **   <a name="iotsitewise-Type-DatasetSummary-name"></a>
The name of the dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z0-9 _\-#$*!@.]+$`
Required: Yes

 ** status **   <a name="iotsitewise-Type-DatasetSummary-status"></a>
The status of the dataset. This contains the state and any error messages. The state is `ACTIVE` when ready to use.
Type: [DatasetStatus](API_DatasetStatus.md) object
Required: Yes

 ** datasetType **   <a name="iotsitewise-Type-DatasetSummary-datasetType"></a>
The type of dataset: a session dataset, a curated dataset, or a connection to an external datasource.
Type: String
Valid Values: `SESSION | CURATED | EXTERNAL`
Required: No

 ** enrichmentStatus **   <a name="iotsitewise-Type-DatasetSummary-enrichmentStatus"></a>
The enrichment status of the dataset.
Type: [DatasetEnrichment](API_DatasetEnrichment.md) object
Required: No

 ** sourceType **   <a name="iotsitewise-Type-DatasetSummary-sourceType"></a>
The data source type of the dataset.
Type: String
Valid Values: `KENDRA | SITEWISE`
Required: No

## See Also
<a name="API_DatasetSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/DatasetSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/DatasetSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/DatasetSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
