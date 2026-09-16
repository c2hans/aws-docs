---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_GetUpgradeStatus.html
---

# GetUpgradeStatus
<a name="API_GetUpgradeStatus"></a>

Returns the most recent status of the last upgrade or upgrade eligibility check performed on an Amazon OpenSearch Service domain.

## Request Syntax
<a name="API_GetUpgradeStatus_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/upgradeDomain/{{DomainName}}/status HTTP/1.1
```

## URI Request Parameters
<a name="API_GetUpgradeStatus_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_GetUpgradeStatus_RequestSyntax) **   <a name="opensearchservice-GetUpgradeStatus-request-uri-DomainName"></a>
The domain of the domain to get upgrade status information for.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

## Request Body
<a name="API_GetUpgradeStatus_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetUpgradeStatus_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "StepStatus": "string",
   "UpgradeName": "string",
   "UpgradeStep": "string"
}
```

## Response Elements
<a name="API_GetUpgradeStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [StepStatus](#API_GetUpgradeStatus_ResponseSyntax) **   <a name="opensearchservice-GetUpgradeStatus-response-StepStatus"></a>
The status of the current step that an upgrade is on.
Type: String
Valid Values: `IN_PROGRESS | SUCCEEDED | SUCCEEDED_WITH_ISSUES | FAILED`

 ** [UpgradeName](#API_GetUpgradeStatus_ResponseSyntax) **   <a name="opensearchservice-GetUpgradeStatus-response-UpgradeName"></a>
A string that describes the update.
Type: String

 ** [UpgradeStep](#API_GetUpgradeStatus_ResponseSyntax) **   <a name="opensearchservice-GetUpgradeStatus-response-UpgradeStep"></a>
One of three steps that an upgrade or upgrade eligibility check goes through.
Type: String
Valid Values: `PRE_UPGRADE_CHECK | SNAPSHOT | UPGRADE`

## Errors
<a name="API_GetUpgradeStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## See Also
<a name="API_GetUpgradeStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/GetUpgradeStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/GetUpgradeStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/GetUpgradeStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/GetUpgradeStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/GetUpgradeStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/GetUpgradeStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/GetUpgradeStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/GetUpgradeStatus)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/GetUpgradeStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/GetUpgradeStatus)
