---
source_url: https://docs.aws.amazon.com/agent-registry-control/latest/APIReference/API_ListPublisherAssociations.html
---

# ListPublisherAssociations

Lists the registry record associations that your account created. Specify `publisherArn` to list only the associations for that publisher, or omit it to list associations across all of your publishers. Results are eventually consistent, so an association that you just created or removed can take a few seconds to appear in or disappear from the list.

## Request Syntax
<a name="API_ListPublisherAssociations_RequestSyntax"></a>

```
GET /associations?maxResults={{maxResults}}&nextToken={{nextToken}}&publisherArn={{publisherArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListPublisherAssociations_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListPublisherAssociations_RequestSyntax) **   <a name="agentregistrycontrol-ListPublisherAssociations-request-uri-maxResults"></a>
The maximum number of results to return in a single call.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListPublisherAssociations_RequestSyntax) **   <a name="agentregistrycontrol-ListPublisherAssociations-request-uri-nextToken"></a>
The token for the next page of results. Use the value returned in the previous response.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S*`

 ** [publisherArn](#API_ListPublisherAssociations_RequestSyntax) **   <a name="agentregistrycontrol-ListPublisherAssociations-request-uri-publisherArn"></a>
The Amazon Resource Name (ARN) of a publisher. If you specify it, only the associations for this publisher are returned.
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `arn:(aws|aws-cn|aws-us-gov):[a-z0-9-]+::[0-9]{12}:[a-zA-Z0-9._/-]+`

## Request Body
<a name="API_ListPublisherAssociations_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListPublisherAssociations_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "publicIdentifier": "string",
         "publisher": "string",
         "recordArn": "string",
         "status": "string",
         "statusReason": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListPublisherAssociations_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListPublisherAssociations_ResponseSyntax) **   <a name="agentregistrycontrol-ListPublisherAssociations-response-items"></a>
The publisher associations on this page of results.
Type: Array of [PublisherAssociation](API_PublisherAssociation.md) objects

 ** [nextToken](#API_ListPublisherAssociations_ResponseSyntax) **   <a name="agentregistrycontrol-ListPublisherAssociations-response-nextToken"></a>
The token to use to get the next page of results. Absent when there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `\S*`

## Errors
<a name="API_ListPublisherAssociations_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The caller is not authorized to perform the requested action.
HTTP Status Code: 403

 ** InternalServerException **
The request failed due to an unexpected internal error; the caller may retry.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling; the caller may retry after a delay.
HTTP Status Code: 429

 ** ValidationException **
The request failed validation of one or more input fields.
 ** fieldList **
The list of input fields that failed validation.
 ** reason **
The reason the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_ListPublisherAssociations_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/agent-registry-control-2025-12-01/ListPublisherAssociations)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/agent-registry-control-2025-12-01/ListPublisherAssociations)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/agent-registry-control-2025-12-01/ListPublisherAssociations)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/agent-registry-control-2025-12-01/ListPublisherAssociations)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/agent-registry-control-2025-12-01/ListPublisherAssociations)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/agent-registry-control-2025-12-01/ListPublisherAssociations)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/agent-registry-control-2025-12-01/ListPublisherAssociations)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/agent-registry-control-2025-12-01/ListPublisherAssociations)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/agent-registry-control-2025-12-01/ListPublisherAssociations)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/agent-registry-control-2025-12-01/ListPublisherAssociations)
