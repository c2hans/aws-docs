---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_BatchPutAssetPropertyError.html
---

# BatchPutAssetPropertyError
<a name="API_BatchPutAssetPropertyError"></a>

Contains error information from updating a batch of asset property values.

## Contents
<a name="API_BatchPutAssetPropertyError_Contents"></a>

 ** errorCode **   <a name="iotsitewise-Type-BatchPutAssetPropertyError-errorCode"></a>
The error code.
Type: String
Valid Values: `ResourceNotFoundException | InvalidRequestException | InternalFailureException | ServiceUnavailableException | ThrottlingException | LimitExceededException | ConflictingOperationException | TimestampOutOfRangeException | AccessDeniedException`
Required: Yes

 ** errorMessage **   <a name="iotsitewise-Type-BatchPutAssetPropertyError-errorMessage"></a>
The associated error message.
Type: String
Required: Yes

 ** timestamps **   <a name="iotsitewise-Type-BatchPutAssetPropertyError-timestamps"></a>
A list of timestamps for each error, if any.
Type: Array of [TimeInNanos](API_TimeInNanos.md) objects
Required: Yes

## See Also
<a name="API_BatchPutAssetPropertyError_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/BatchPutAssetPropertyError)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/BatchPutAssetPropertyError)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/BatchPutAssetPropertyError)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
