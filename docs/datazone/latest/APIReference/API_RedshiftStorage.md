---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_RedshiftStorage.html
---

# RedshiftStorage
<a name="API_RedshiftStorage"></a>

The details of the Amazon Redshift storage as part of the configuration of an Amazon Redshift data source run.

## Contents
<a name="API_RedshiftStorage_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** redshiftClusterSource **   <a name="datazone-Type-RedshiftStorage-redshiftClusterSource"></a>
The details of the Amazon Redshift cluster source.
Type: [RedshiftClusterStorage](API_RedshiftClusterStorage.md) object
Required: No

 ** redshiftServerlessSource **   <a name="datazone-Type-RedshiftStorage-redshiftServerlessSource"></a>
The details of the Amazon Redshift Serverless workgroup source.
Type: [RedshiftServerlessStorage](API_RedshiftServerlessStorage.md) object
Required: No

## See Also
<a name="API_RedshiftStorage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/RedshiftStorage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/RedshiftStorage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/RedshiftStorage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
