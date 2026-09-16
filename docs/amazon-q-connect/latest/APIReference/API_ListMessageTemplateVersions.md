---
source_url: https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_ListMessageTemplateVersions.html
---

# ListMessageTemplateVersions
<a name="API_amazon-q-connect_ListMessageTemplateVersions"></a>

Lists all the available versions for the specified Amazon Q in Connect message template.

## Request Syntax
<a name="API_amazon-q-connect_ListMessageTemplateVersions_RequestSyntax"></a>

```
GET /knowledgeBases/{{knowledgeBaseId}}/messageTemplates/{{messageTemplateId}}/versions?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_amazon-q-connect_ListMessageTemplateVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [knowledgeBaseId](#API_amazon-q-connect_ListMessageTemplateVersions_RequestSyntax) **   <a name="connect-amazon-q-connect_ListMessageTemplateVersions-request-uri-knowledgeBaseId"></a>
The identifier of the knowledge base. Can be either the ID or the ARN. URLs cannot contain the ARN.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}`
Required: Yes

 ** [maxResults](#API_amazon-q-connect_ListMessageTemplateVersions_RequestSyntax) **   <a name="connect-amazon-q-connect_ListMessageTemplateVersions-request-uri-maxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [messageTemplateId](#API_amazon-q-connect_ListMessageTemplateVersions_RequestSyntax) **   <a name="connect-amazon-q-connect_ListMessageTemplateVersions-request-uri-messageTemplateId"></a>
The identifier of the message template. Can be either the ID or the ARN. It cannot contain any qualifier.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(:[A-Z0-9_$]+){0,1}$|^arn:[a-z-]*?:wisdom:[a-z0-9-]*?:[0-9]{12}:[a-z-]*?/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}(?:/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}){0,2}(:[A-Z0-9_$]+){0,1}`
Required: Yes

 ** [nextToken](#API_amazon-q-connect_ListMessageTemplateVersions_RequestSyntax) **   <a name="connect-amazon-q-connect_ListMessageTemplateVersions-request-uri-nextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Request Body
<a name="API_amazon-q-connect_ListMessageTemplateVersions_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_amazon-q-connect_ListMessageTemplateVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "messageTemplateVersionSummaries": [
      {
         "channel": "string",
         "channelSubtype": "string",
         "isActive": boolean,
         "knowledgeBaseArn": "string",
         "knowledgeBaseId": "string",
         "messageTemplateArn": "string",
         "messageTemplateId": "string",
         "name": "string",
         "versionNumber": number
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_amazon-q-connect_ListMessageTemplateVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [messageTemplateVersionSummaries](#API_amazon-q-connect_ListMessageTemplateVersions_ResponseSyntax) **   <a name="connect-amazon-q-connect_ListMessageTemplateVersions-response-messageTemplateVersionSummaries"></a>
Summary information about the versions of a message template.
Type: Array of [MessageTemplateVersionSummary](API_amazon-q-connect_MessageTemplateVersionSummary.md) objects

 ** [nextToken](#API_amazon-q-connect_ListMessageTemplateVersions_ResponseSyntax) **   <a name="connect-amazon-q-connect_ListMessageTemplateVersions-response-nextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_amazon-q-connect_ListMessageTemplateVersions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** resourceName **
The specified resource name.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by a service.
HTTP Status Code: 400

## See Also
<a name="API_amazon-q-connect_ListMessageTemplateVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/qconnect-2020-10-19/ListMessageTemplateVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/qconnect-2020-10-19/ListMessageTemplateVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/qconnect-2020-10-19/ListMessageTemplateVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/qconnect-2020-10-19/ListMessageTemplateVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/qconnect-2020-10-19/ListMessageTemplateVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/qconnect-2020-10-19/ListMessageTemplateVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/qconnect-2020-10-19/ListMessageTemplateVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/qconnect-2020-10-19/ListMessageTemplateVersions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/qconnect-2020-10-19/ListMessageTemplateVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/qconnect-2020-10-19/ListMessageTemplateVersions)
