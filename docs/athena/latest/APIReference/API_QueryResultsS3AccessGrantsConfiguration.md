---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_QueryResultsS3AccessGrantsConfiguration.html
---

# QueryResultsS3AccessGrantsConfiguration
<a name="API_QueryResultsS3AccessGrantsConfiguration"></a>

Specifies whether Amazon S3 access grants are enabled for query results.

## Contents
<a name="API_QueryResultsS3AccessGrantsConfiguration_Contents"></a>

 ** AuthenticationType **   <a name="athena-Type-QueryResultsS3AccessGrantsConfiguration-AuthenticationType"></a>
The authentication type used for Amazon S3 access grants. Currently, only `DIRECTORY_IDENTITY` is supported.
Type: String
Valid Values: `DIRECTORY_IDENTITY`
Required: Yes

 ** EnableS3AccessGrants **   <a name="athena-Type-QueryResultsS3AccessGrantsConfiguration-EnableS3AccessGrants"></a>
Specifies whether Amazon S3 access grants are enabled for query results.
Type: Boolean
Required: Yes

 ** CreateUserLevelPrefix **   <a name="athena-Type-QueryResultsS3AccessGrantsConfiguration-CreateUserLevelPrefix"></a>
When enabled, appends the user ID as an Amazon S3 path prefix to the query result output location.
Type: Boolean
Required: No

## See Also
<a name="API_QueryResultsS3AccessGrantsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/QueryResultsS3AccessGrantsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/QueryResultsS3AccessGrantsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/QueryResultsS3AccessGrantsConfiguration)
