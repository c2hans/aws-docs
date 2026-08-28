---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_RevisionDestinationEntry.html
---

# RevisionDestinationEntry
<a name="API_RevisionDestinationEntry"></a>

The destination where the assets in the revision will be exported.

## Contents
<a name="API_RevisionDestinationEntry_Contents"></a>

 ** Bucket **   <a name="dataexchange-Type-RevisionDestinationEntry-Bucket"></a>
The Amazon S3 bucket that is the destination for the assets in the revision.
Type: String
Required: Yes

 ** RevisionId **   <a name="dataexchange-Type-RevisionDestinationEntry-RevisionId"></a>
The unique identifier for the revision.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** KeyPattern **   <a name="dataexchange-Type-RevisionDestinationEntry-KeyPattern"></a>
A string representing the pattern for generated names of the individual assets in the revision. For more information about key patterns, see [Key patterns when exporting revisions](https://docs.aws.amazon.com/data-exchange/latest/userguide/jobs.html#revision-export-keypatterns).
Type: String
Required: No

## See Also
<a name="API_RevisionDestinationEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/RevisionDestinationEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/RevisionDestinationEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/RevisionDestinationEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
