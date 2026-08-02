---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_ProtectedQueryDistributeOutput.html
---

# ProtectedQueryDistributeOutput
<a name="API_ProtectedQueryDistributeOutput"></a>

 Contains the output information for a protected query with a distribute output configuration.

 This output type allows query results to be distributed to multiple receivers, including S3 and collaboration members. It is only available for queries using the Spark analytics engine.

## Contents
<a name="API_ProtectedQueryDistributeOutput_Contents"></a>

 ** memberList **   <a name="API-Type-ProtectedQueryDistributeOutput-memberList"></a>
 Contains the output results for each member location specified in the distribute output configuration. Each entry provides details about the result distribution to a specific collaboration member.
Type: Array of [ProtectedQuerySingleMemberOutput](API_ProtectedQuerySingleMemberOutput.md) objects
Required: No

 ** s3 **   <a name="API-Type-ProtectedQueryDistributeOutput-s3"></a>
Contains output information for protected queries with an S3 output type.
Type: [ProtectedQueryS3Output](API_ProtectedQueryS3Output.md) object
Required: No

## See Also
<a name="API_ProtectedQueryDistributeOutput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/ProtectedQueryDistributeOutput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/ProtectedQueryDistributeOutput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/ProtectedQueryDistributeOutput)
