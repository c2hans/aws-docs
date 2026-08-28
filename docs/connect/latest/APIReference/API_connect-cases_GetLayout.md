---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_GetLayout.html
---

# GetLayout
<a name="API_connect-cases_GetLayout"></a>

Returns the details for the requested layout.

## Request Syntax
<a name="API_connect-cases_GetLayout_RequestSyntax"></a>

```
POST /domains/{{domainId}}/layouts/{{layoutId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-cases_GetLayout_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainId](#API_connect-cases_GetLayout_RequestSyntax) **   <a name="connect-connect-cases_GetLayout-request-uri-domainId"></a>
The unique identifier of the Cases domain.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [layoutId](#API_connect-cases_GetLayout_RequestSyntax) **   <a name="connect-connect-cases_GetLayout-request-uri-layoutId"></a>
The unique identifier of the layout.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Request Body
<a name="API_connect-cases_GetLayout_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-cases_GetLayout_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "content": { ... },
   "createdTime": "string",
   "deleted": boolean,
   "lastModifiedTime": "string",
   "layoutArn": "string",
   "layoutId": "string",
   "name": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_connect-cases_GetLayout_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [content](#API_connect-cases_GetLayout_ResponseSyntax) **   <a name="connect-connect-cases_GetLayout-response-content"></a>
Information about which fields will be present in the layout, the order of the fields, and read-only attribute of the field.
Type: [LayoutContent](API_connect-cases_LayoutContent.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [createdTime](#API_connect-cases_GetLayout_ResponseSyntax) **   <a name="connect-connect-cases_GetLayout-response-createdTime"></a>
Timestamp at which the resource was created.
Type: Timestamp

 ** [deleted](#API_connect-cases_GetLayout_ResponseSyntax) **   <a name="connect-connect-cases_GetLayout-response-deleted"></a>
Denotes whether or not the resource has been deleted.
Type: Boolean

 ** [lastModifiedTime](#API_connect-cases_GetLayout_ResponseSyntax) **   <a name="connect-connect-cases_GetLayout-response-lastModifiedTime"></a>
Timestamp at which the resource was created or last modified.
Type: Timestamp

 ** [layoutArn](#API_connect-cases_GetLayout_ResponseSyntax) **   <a name="connect-connect-cases_GetLayout-response-layoutArn"></a>
The Amazon Resource Name (ARN) of the newly created layout.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

 ** [layoutId](#API_connect-cases_GetLayout_ResponseSyntax) **   <a name="connect-connect-cases_GetLayout-response-layoutId"></a>
The unique identifier of the layout.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

 ** [name](#API_connect-cases_GetLayout_ResponseSyntax) **   <a name="connect-connect-cases_GetLayout-response-name"></a>
The name of the layout. It must be unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*[\S]`

 ** [tags](#API_connect-cases_GetLayout_ResponseSyntax) **   <a name="connect-connect-cases_GetLayout-response-tags"></a>
A map of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.
Type: String to string map

## Errors
<a name="API_connect-cases_GetLayout_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
We couldn't process your request because of an issue with the server. Try again later.
 ** retryAfterSeconds **
Advice to clients on when the call can be safely retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **
We couldn't find the requested resource. Check that your resources exists and were created in the same AWS Region as your request, and try your request again.
 ** resourceId **
Unique identifier of the resource affected.
 ** resourceType **
Type of the resource affected.
HTTP Status Code: 404

 ** ThrottlingException **
The rate has been exceeded for this API. Please try again after a few minutes.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. Check the syntax and try again.
HTTP Status Code: 400

## Examples
<a name="API_connect-cases_GetLayout_Examples"></a>

### Request and Response example
<a name="API_connect-cases_GetLayout_Example_1"></a>

Following is an example of a content attribute.

```
{ }
```

```
{
  "name": "My layout",
  "content": {
  "basic": {
    "topPanel": {
      "sections": [
      {
        "fieldGroup": {
        "fields": [
          {
          "editable": false,
          "fieldId": "[field_id_1]"
          },
          {
          "editable": false,
          "fieldId": "[field_id_2]"
          }
         ]
       }
     }
    ]
  },
  "moreInfo": {
  "sections": [
      {
      "fieldGroup": {
        "name": "Address",
        "fields": [
          {
          "editable": false,
          "fieldId": "[field_id_3]"
          },
          {
          "editable": false,
          "fieldId": "[field_id_4]"
          }
         ]
        }
       }
      ]
     }
    }
  },
  "layoutArn": "arn:aws:cases:us-west-2:[account_id]:domain/[domain_id]/layout/[layout_id]",
  "layoutId": "[layout_id]",
  "tags": {}
}
```

## See Also
<a name="API_connect-cases_GetLayout_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcases-2022-10-03/GetLayout)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcases-2022-10-03/GetLayout)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/GetLayout)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcases-2022-10-03/GetLayout)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/GetLayout)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcases-2022-10-03/GetLayout)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcases-2022-10-03/GetLayout)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcases-2022-10-03/GetLayout)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcases-2022-10-03/GetLayout)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/GetLayout)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
