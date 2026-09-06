---
source_url: https://docs.aws.amazon.com/databrew/latest/APIReference/API_DatabaseInputDefinition.html
---

# DatabaseInputDefinition
<a name="API_DatabaseInputDefinition"></a>

Connection information for dataset input files stored in a database.

## Contents
<a name="API_DatabaseInputDefinition_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** GlueConnectionName **   <a name="databrew-Type-DatabaseInputDefinition-GlueConnectionName"></a>
The AWS Glue Connection that stores the connection information for the target database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** DatabaseTableName **   <a name="databrew-Type-DatabaseInputDefinition-DatabaseTableName"></a>
The table within the target database.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: No

 ** QueryString **   <a name="databrew-Type-DatabaseInputDefinition-QueryString"></a>
Custom SQL to run against the provided AWS Glue connection. This SQL will be used as the input for DataBrew projects and jobs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10000.
Required: No

 ** TempDirectory **   <a name="databrew-Type-DatabaseInputDefinition-TempDirectory"></a>
Represents an Amazon S3 location (bucket name, bucket owner, and object key) where DataBrew can read input data, or write output from a job.
Type: [S3Location](API_S3Location.md) object
Required: No

## See Also
<a name="API_DatabaseInputDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/databrew-2017-07-25/DatabaseInputDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/databrew-2017-07-25/DatabaseInputDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/databrew-2017-07-25/DatabaseInputDefinition)
