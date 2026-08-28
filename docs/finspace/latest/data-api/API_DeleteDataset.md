---
source_url: https://docs.aws.amazon.com/finspace/latest/data-api/API_DeleteDataset.html
---

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/data-api/amazon-finspace-end-of-support.html).

# DeleteDataset
<a name="API_DeleteDataset"></a>

Deletes a FinSpace Dataset.

## Request Syntax
<a name="API_DeleteDataset_RequestSyntax"></a>

```
DELETE /datasetsv2/{{datasetId}}?clientToken={{clientToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteDataset_RequestParameters"></a>

The request uses the following URI parameters.

 ** [clientToken](#API_DeleteDataset_RequestSyntax) **   <a name="finspace-DeleteDataset-request-uri-clientToken"></a>
A token that ensures idempotency. This token expires in 10 minutes.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `.*\S.*`

 ** [datasetId](#API_DeleteDataset_RequestSyntax) **   <a name="finspace-DeleteDataset-request-uri-datasetId"></a>
The unique identifier of the Dataset to be deleted.
Length Constraints: Minimum length of 1. Maximum length of 26.
Required: Yes

## Request Body
<a name="API_DeleteDataset_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteDataset_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "datasetId": "string"
}
```

## Response Elements
<a name="API_DeleteDataset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [datasetId](#API_DeleteDataset_ResponseSyntax) **   <a name="finspace-DeleteDataset-response-datasetId"></a>
The unique identifier for the deleted Dataset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 26.

## Errors
<a name="API_DeleteDataset_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request conflicts with an existing resource.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** LimitExceededException **
A limit has exceeded.
HTTP Status Code: 400

 ** ResourceNotFoundException **
One or more resources can't be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_DeleteDataset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/finspace-2020-07-13/DeleteDataset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/finspace-2020-07-13/DeleteDataset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2020-07-13/DeleteDataset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/finspace-2020-07-13/DeleteDataset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2020-07-13/DeleteDataset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/finspace-2020-07-13/DeleteDataset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/finspace-2020-07-13/DeleteDataset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/finspace-2020-07-13/DeleteDataset)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/finspace-2020-07-13/DeleteDataset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2020-07-13/DeleteDataset)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
