---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ResponseStream.html
---

# ResponseStream
<a name="API_ResponseStream"></a>

Contains the response, citation, and trace from the SiteWise Assistant.

## Contents
<a name="API_ResponseStream_Contents"></a>

 ** accessDeniedException **   <a name="iotsitewise-Type-ResponseStream-accessDeniedException"></a>
Access is denied.
Type: Exception
HTTP Status Code: 403
Required: No

 ** conflictingOperationException **   <a name="iotsitewise-Type-ResponseStream-conflictingOperationException"></a>
Your request has conflicting operations. This can occur if you're trying to perform more than one operation on the same resource at the same time.
Type: Exception
HTTP Status Code: 409
Required: No

 ** internalFailureException **   <a name="iotsitewise-Type-ResponseStream-internalFailureException"></a>
 AWS IoT SiteWise can't process your request right now. Try again later.
Type: Exception
HTTP Status Code: 500
Required: No

 ** invalidRequestException **   <a name="iotsitewise-Type-ResponseStream-invalidRequestException"></a>
The request isn't valid. This can occur if your request contains malformed JSON or unsupported characters. Check your request and try again.
Type: Exception
HTTP Status Code: 400
Required: No

 ** limitExceededException **   <a name="iotsitewise-Type-ResponseStream-limitExceededException"></a>
You've reached the quota for a resource. For example, this can occur if you're trying to associate more than the allowed number of child assets or attempting to create more than the allowed number of properties for an asset model.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
Type: Exception
HTTP Status Code: 410
Required: No

 ** output **   <a name="iotsitewise-Type-ResponseStream-output"></a>
Contains the SiteWise Assistant's response.
Type: [InvocationOutput](API_InvocationOutput.md) object
Required: No

 ** resourceNotFoundException **   <a name="iotsitewise-Type-ResponseStream-resourceNotFoundException"></a>
The requested resource can't be found.
Type: Exception
HTTP Status Code: 404
Required: No

 ** throttlingException **   <a name="iotsitewise-Type-ResponseStream-throttlingException"></a>
Your request exceeded a rate limit. For example, you might have exceeded the number of AWS IoT SiteWise assets that can be created per second, the allowed number of messages per second, and so on.
For more information, see [Quotas](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/quotas.html) in the * AWS IoT SiteWise User Guide*.
Type: Exception
HTTP Status Code: 429
Required: No

 ** trace **   <a name="iotsitewise-Type-ResponseStream-trace"></a>
Contains tracing information of the SiteWise Assistant's reasoning and data access.
Type: [Trace](API_Trace.md) object
Required: No

## See Also
<a name="API_ResponseStream_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ResponseStream)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ResponseStream)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ResponseStream)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
