---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ProtectedQueryOutput.html
---

# ProtectedQueryOutput
<a name="API_ProtectedQueryOutput"></a>

Contains details about the protected query output.

## Contents
<a name="API_ProtectedQueryOutput_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** distribute **   <a name="API-Type-ProtectedQueryOutput-distribute"></a>
Contains output information for protected queries that use a `distribute` output type. This output type lets you send query results to multiple locations - either to S3 or to collaboration members.
 You can only use the `distribute` output type with the Spark analytics engine.
Type: [ProtectedQueryDistributeOutput](API_ProtectedQueryDistributeOutput.md) object
Required: No

 ** memberList **   <a name="API-Type-ProtectedQueryOutput-memberList"></a>
The list of member AWS account(s) that received the results of the query.
Type: Array of [ProtectedQuerySingleMemberOutput](API_ProtectedQuerySingleMemberOutput.md) objects
Required: No

 ** s3 **   <a name="API-Type-ProtectedQueryOutput-s3"></a>
If present, the output for a protected query with an `S3` output type.
Type: [ProtectedQueryS3Output](API_ProtectedQueryS3Output.md) object
Required: No

## See Also
<a name="API_ProtectedQueryOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ProtectedQueryOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ProtectedQueryOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ProtectedQueryOutput)
