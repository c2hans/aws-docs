---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_JobEntry.html
---

# JobEntry
<a name="API_JobEntry"></a>

AWS Data Exchange Jobs are asynchronous import or export operations used to create or copy assets. A data set owner can both import and export as they see fit. Someone with an entitlement to a data set can only export. Jobs are deleted 90 days after they are created.

## Contents
<a name="API_JobEntry_Contents"></a>

 ** Arn **   <a name="dataexchange-Type-JobEntry-Arn"></a>
The ARN for the job.
Type: String
Required: Yes

 ** CreatedAt **   <a name="dataexchange-Type-JobEntry-CreatedAt"></a>
The date and time that the job was created, in ISO 8601 format.
Type: Timestamp
Required: Yes

 ** Details **   <a name="dataexchange-Type-JobEntry-Details"></a>
Details of the operation to be performed by the job, such as export destination details or import source details.
Type: [ResponseDetails](API_ResponseDetails.md) object
Required: Yes

 ** Id **   <a name="dataexchange-Type-JobEntry-Id"></a>
The unique identifier for the job.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

 ** State **   <a name="dataexchange-Type-JobEntry-State"></a>
The state of the job.
Type: String
Valid Values: `WAITING | IN_PROGRESS | ERROR | COMPLETED | CANCELLED | TIMED_OUT`
Required: Yes

 ** Type **   <a name="dataexchange-Type-JobEntry-Type"></a>
The job type.
Type: String
Valid Values: `IMPORT_ASSETS_FROM_S3 | IMPORT_ASSET_FROM_SIGNED_URL | EXPORT_ASSETS_TO_S3 | EXPORT_ASSET_TO_SIGNED_URL | EXPORT_REVISIONS_TO_S3 | IMPORT_ASSETS_FROM_REDSHIFT_DATA_SHARES | IMPORT_ASSET_FROM_API_GATEWAY_API | CREATE_S3_DATA_ACCESS_FROM_S3_BUCKET | IMPORT_ASSETS_FROM_LAKE_FORMATION_TAG_POLICY`
Required: Yes

 ** UpdatedAt **   <a name="dataexchange-Type-JobEntry-UpdatedAt"></a>
The date and time that the job was last updated, in ISO 8601 format.
Type: Timestamp
Required: Yes

 ** AssetConfiguration **   <a name="dataexchange-Type-JobEntry-AssetConfiguration"></a>
The configuration for the asset, including tags applied to assets created by the job.
Type: [AssetConfiguration](API_AssetConfiguration.md) object
Required: No

 ** Errors **   <a name="dataexchange-Type-JobEntry-Errors"></a>
Errors for jobs.
Type: Array of [JobError](API_JobError.md) objects
Required: No

## See Also
<a name="API_JobEntry_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/JobEntry)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/JobEntry)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/JobEntry)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
