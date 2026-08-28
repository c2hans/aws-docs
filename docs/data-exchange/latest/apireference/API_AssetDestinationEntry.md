---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_AssetDestinationEntry.html
---

# AssetDestinationEntry
<a name="API_AssetDestinationEntry"></a>

The destination for the asset.

## Contents
<a name="API_AssetDestinationEntry_Contents"></a>

 ** AssetId **   <a name="dataexchange-Type-AssetDestinationEntry-AssetId"></a>
The unique identifier for the asset.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** Bucket **   <a name="dataexchange-Type-AssetDestinationEntry-Bucket"></a>
The Amazon S3 bucket that is the destination for the asset.
Type: String
Required: Yes

 ** Key **   <a name="dataexchange-Type-AssetDestinationEntry-Key"></a>
The name of the object in Amazon S3 for the asset.
Type: String
Required: No

## See Also
<a name="API_AssetDestinationEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/AssetDestinationEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/AssetDestinationEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/AssetDestinationEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
