---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_UpdateClone.html
---

# UpdateClone
<a name="API_UpdateClone"></a>

Manages a cloned blue/green upgrade that is in progress on a domain. Use it to shift a percentage of search traffic to the cloned cluster, to cut over to the cloned cluster or back to the primary cluster, or to change the retention period. Specify exactly one of `TrafficSplitOptions`, `CutoverOptions`, or `RetentionOptions` in each request.

## Request Syntax
<a name="API_UpdateClone_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/domain/{{DomainName}}/clone HTTP/1.1
Content-type: application/json

{
   "CutoverOptions": {
      "Target": "{{string}}"
   },
   "RetentionOptions": { ... },
   "TrafficSplitOptions": {
      "CloneReadTrafficPercent": {{number}},
      "Strategy": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateClone_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_UpdateClone_RequestSyntax) **   <a name="opensearchservice-UpdateClone-request-uri-DomainName"></a>
The name of the domain that has a cloned blue/green upgrade in progress.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

## Request Body
<a name="API_UpdateClone_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CutoverOptions](#API_UpdateClone_RequestSyntax) **   <a name="opensearchservice-UpdateClone-request-CutoverOptions"></a>
Cuts the domain over to the cloned cluster or back to the primary cluster.
Type: [CutoverRequestOptions](API_CutoverRequestOptions.md) object
Required: No

 ** [RetentionOptions](#API_UpdateClone_RequestSyntax) **   <a name="opensearchservice-UpdateClone-request-RetentionOptions"></a>
Changes the retention period, or ends it after cutover completes.
Type: [RetentionOptions](API_RetentionOptions.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [TrafficSplitOptions](#API_UpdateClone_RequestSyntax) **   <a name="opensearchservice-UpdateClone-request-TrafficSplitOptions"></a>
Shifts a percentage of search traffic from the primary cluster to the cloned cluster.
Type: [TrafficSplitRequestOptions](API_TrafficSplitRequestOptions.md) object
Required: No

## Response Syntax
<a name="API_UpdateClone_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ChangeId": "string",
   "CutoverOptions": {
      "Status": "string",
      "Target": "string"
   },
   "DomainName": "string",
   "RetentionOptions": { ... },
   "TrafficSplitOptions": {
      "Current": {
         "CloneReadTrafficPercent": number,
         "PrimaryReadTrafficPercent": number
      },
      "Status": "string",
      "Target": {
         "CloneReadTrafficPercent": number,
         "PrimaryReadTrafficPercent": number
      }
   }
}
```

## Response Elements
<a name="API_UpdateClone_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChangeId](#API_UpdateClone_ResponseSyntax) **   <a name="opensearchservice-UpdateClone-response-ChangeId"></a>
The unique identifier of the configuration change. Use it with `DescribeDomainChangeProgress` to track the change.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `\p{XDigit}{8}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{12}`

 ** [CutoverOptions](#API_UpdateClone_ResponseSyntax) **   <a name="opensearchservice-UpdateClone-response-CutoverOptions"></a>
The requested cutover target and the status of the cutover.
Type: [CutoverOptions](API_CutoverOptions.md) object

 ** [DomainName](#API_UpdateClone_ResponseSyntax) **   <a name="opensearchservice-UpdateClone-response-DomainName"></a>
The name of the domain.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`

 ** [RetentionOptions](#API_UpdateClone_ResponseSyntax) **   <a name="opensearchservice-UpdateClone-response-RetentionOptions"></a>
The retention settings for the upgrade.
Type: [RetentionOptions](API_RetentionOptions.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [TrafficSplitOptions](#API_UpdateClone_ResponseSyntax) **   <a name="opensearchservice-UpdateClone-response-TrafficSplitOptions"></a>
The current and requested traffic split, and the status of the traffic shift.
Type: [TrafficSplitOptions](API_TrafficSplitOptions.md) object

## Errors
<a name="API_UpdateClone_Errors"></a>

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
<a name="API_UpdateClone_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/UpdateClone)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/UpdateClone)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/UpdateClone)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/UpdateClone)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/UpdateClone)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/UpdateClone)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/UpdateClone)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/UpdateClone)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/UpdateClone)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/UpdateClone)
