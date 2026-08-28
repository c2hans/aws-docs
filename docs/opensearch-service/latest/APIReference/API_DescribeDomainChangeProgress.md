---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDomainChangeProgress.html
---

# DescribeDomainChangeProgress
<a name="API_DescribeDomainChangeProgress"></a>

Returns information about the current blue/green deployment happening on an Amazon OpenSearch Service domain. For more information, see [Making configuration changes in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/managedomains-configuration-changes.html).

## Request Syntax
<a name="API_DescribeDomainChangeProgress_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/domain/{{DomainName}}/progress?changeid={{ChangeId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeDomainChangeProgress_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ChangeId](#API_DescribeDomainChangeProgress_RequestSyntax) **   <a name="opensearchservice-DescribeDomainChangeProgress-request-uri-ChangeId"></a>
The specific change ID for which you want to get progress information. If omitted, the request returns information about the most recent configuration change.
Length Constraints: Fixed length of 36.
Pattern: `\p{XDigit}{8}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{4}-\p{XDigit}{12}`

 ** [DomainName](#API_DescribeDomainChangeProgress_RequestSyntax) **   <a name="opensearchservice-DescribeDomainChangeProgress-request-uri-DomainName"></a>
The name of the domain to get progress information for.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

## Request Body
<a name="API_DescribeDomainChangeProgress_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeDomainChangeProgress_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ChangeProgressStatus": {
      "ChangeId": "string",
      "ChangeProgressStages": [
         {
            "Description": "string",
            "LastUpdated": number,
            "Name": "string",
            "Status": "string"
         }
      ],
      "CompletedProperties": [ "string" ],
      "ConfigChangeStatus": "string",
      "InitiatedBy": "string",
      "LastUpdatedTime": number,
      "PendingProperties": [ "string" ],
      "StartTime": number,
      "Status": "string",
      "TotalNumberOfStages": number
   }
}
```

## Response Elements
<a name="API_DescribeDomainChangeProgress_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ChangeProgressStatus](#API_DescribeDomainChangeProgress_ResponseSyntax) **   <a name="opensearchservice-DescribeDomainChangeProgress-response-ChangeProgressStatus"></a>
Container for information about the stages of a configuration change happening on a domain.
Type: [ChangeProgressStatusDetails](API_ChangeProgressStatusDetails.md) object

## Errors
<a name="API_DescribeDomainChangeProgress_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BaseException **
An error occurred while processing the request.
 ** message **
A description of the error.
HTTP Status Code: 400

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
<a name="API_DescribeDomainChangeProgress_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/DescribeDomainChangeProgress)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/DescribeDomainChangeProgress)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DescribeDomainChangeProgress)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/DescribeDomainChangeProgress)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DescribeDomainChangeProgress)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/DescribeDomainChangeProgress)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/DescribeDomainChangeProgress)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/DescribeDomainChangeProgress)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/DescribeDomainChangeProgress)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DescribeDomainChangeProgress)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon OpenSearch Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query opensearch-service` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
