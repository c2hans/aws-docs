---
source_url: https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_ListConnectors.html
---

# ListConnectors
<a name="API_ListConnectors"></a>

Lists the connectors belonging to your AWS account.

## Request Syntax
<a name="API_ListConnectors_RequestSyntax"></a>

```
GET /connectors?MaxResults={{MaxResults}}&NextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListConnectors_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_ListConnectors_RequestSyntax) **   <a name="pcaconnectorscep-ListConnectors-request-uri-MaxResults"></a>
The maximum number of objects that you want Connector for SCEP to return for this request. If more objects are available, in the response, Connector for SCEP provides a `NextToken` value that you can use in a subsequent call to get the next batch of objects.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListConnectors_RequestSyntax) **   <a name="pcaconnectorscep-ListConnectors-request-uri-NextToken"></a>
When you request a list of objects with a `MaxResults` setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Connector for SCEP returns a `NextToken` value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `(?:[A-Za-z0-9_-]{4})*(?:[A-Za-z0-9_-]{2}==|[A-Za-z0-9_-]{3}=)?`

## Request Body
<a name="API_ListConnectors_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListConnectors_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Connectors": [
      {
         "Arn": "string",
         "CertificateAuthorityArn": "string",
         "CreatedAt": number,
         "Endpoint": "string",
         "MobileDeviceManagement": { ... },
         "OpenIdConfiguration": {
            "Audience": "string",
            "Issuer": "string",
            "Subject": "string"
         },
         "Status": "string",
         "StatusReason": "string",
         "Type": "string",
         "UpdatedAt": number
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListConnectors_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Connectors](#API_ListConnectors_ResponseSyntax) **   <a name="pcaconnectorscep-ListConnectors-response-Connectors"></a>
The connectors belonging to your AWS account.
Type: Array of [ConnectorSummary](API_ConnectorSummary.md) objects

 ** [NextToken](#API_ListConnectors_ResponseSyntax) **   <a name="pcaconnectorscep-ListConnectors-response-NextToken"></a>
When you request a list of objects with a `MaxResults` setting, if the number of objects that are still available for retrieval exceeds the maximum you requested, Connector for SCEP returns a `NextToken` value in the response. To retrieve the next batch of objects, use the token returned from the prior request in your next request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `(?:[A-Za-z0-9_-]{4})*(?:[A-Za-z0-9_-]{2}==|[A-Za-z0-9_-]{3}=)?`

## Errors
<a name="API_ListConnectors_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You can receive this error if you attempt to perform an operation and you don't have the required permissions. This can be caused by insufficient permissions in policies attached to your AWS Identity and Access Management (IAM) principal. It can also happen because of restrictions in place from an AWS Organizations service control policy (SCP) that affects your AWS account.
HTTP Status Code: 403

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure with an internal server.
HTTP Status Code: 500

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
An input validation error occurred. For example, invalid characters in a name tag, or an invalid pagination token.
 ** Reason **
The reason for the validation error, if available. The service doesn't return a reason for every validation exception.
HTTP Status Code: 400

## See Also
<a name="API_ListConnectors_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pca-connector-scep-2018-05-10/ListConnectors)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pca-connector-scep-2018-05-10/ListConnectors)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-scep-2018-05-10/ListConnectors)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pca-connector-scep-2018-05-10/ListConnectors)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-scep-2018-05-10/ListConnectors)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pca-connector-scep-2018-05-10/ListConnectors)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pca-connector-scep-2018-05-10/ListConnectors)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pca-connector-scep-2018-05-10/ListConnectors)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pca-connector-scep-2018-05-10/ListConnectors)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-scep-2018-05-10/ListConnectors)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA Connector for SCEP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pca-connector-scep` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
