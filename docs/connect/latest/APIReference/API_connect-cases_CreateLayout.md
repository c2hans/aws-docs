---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_CreateLayout.html
---

# CreateLayout
<a name="API_connect-cases_CreateLayout"></a>

Creates a layout in the Cases domain. Layouts define the following configuration in the top section and More Info tab of the Cases user interface:
+ Fields to display to the users
+ Field ordering

**Note**
Title and Status fields cannot be part of layouts since they are not configurable.

## Request Syntax
<a name="API_connect-cases_CreateLayout_RequestSyntax"></a>

```
POST /domains/{{domainId}}/layouts HTTP/1.1
Content-type: application/json

{
   "content": { ... },
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-cases_CreateLayout_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainId](#API_connect-cases_CreateLayout_RequestSyntax) **   <a name="connect-connect-cases_CreateLayout-request-uri-domainId"></a>
The unique identifier of the Cases domain.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Request Body
<a name="API_connect-cases_CreateLayout_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [content](#API_connect-cases_CreateLayout_RequestSyntax) **   <a name="connect-connect-cases_CreateLayout-request-content"></a>
Information about which fields will be present in the layout, and information about the order of the fields.
Type: [LayoutContent](API_connect-cases_LayoutContent.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [name](#API_connect-cases_CreateLayout_RequestSyntax) **   <a name="connect-connect-cases_CreateLayout-request-name"></a>
The name of the layout. It must be unique for the Cases domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*[\S]`
Required: Yes

## Response Syntax
<a name="API_connect-cases_CreateLayout_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "layoutArn": "string",
   "layoutId": "string"
}
```

## Response Elements
<a name="API_connect-cases_CreateLayout_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [layoutArn](#API_connect-cases_CreateLayout_ResponseSyntax) **   <a name="connect-connect-cases_CreateLayout-response-layoutArn"></a>
The Amazon Resource Name (ARN) of the newly created layout.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

 ** [layoutId](#API_connect-cases_CreateLayout_ResponseSyntax) **   <a name="connect-connect-cases_CreateLayout-response-layoutId"></a>
The unique identifier of the layout.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

## Errors
<a name="API_connect-cases_CreateLayout_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The requested operation would cause a conflict with the current state of a service resource associated with the request. Resolve the conflict before retrying this request. See the accompanying error message for details.
HTTP Status Code: 409

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

 ** ServiceQuotaExceededException **
The service quota has been exceeded. For a list of service quotas, see [Connect Customer Service Quotas](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html) in the *Connect Customer Administrator Guide*.
HTTP Status Code: 402

 ** ThrottlingException **
The rate has been exceeded for this API. Please try again after a few minutes.
HTTP Status Code: 429

 ** ValidationException **
The request isn't valid. Check the syntax and try again.
HTTP Status Code: 400

## Examples
<a name="API_connect-cases_CreateLayout_Examples"></a>

### Request and Response example
<a name="API_connect-cases_CreateLayout_Example_1"></a>

This example illustrates one usage of CreateLayout.

```
{
  "content": {
    "basic": {
      "moreInfo": {
        "sections": [
          {
            "fieldGroup": {
              "fields": [
                {
                "id": "created_datetime"
                },
                {
                "id": "case_id"
                }
            ]
          }
        }
      ]
    },
  "topPanel": {
        "sections": [
          {
          "fieldGroup": {
          "fields": [
           {
           "id": "status"
           },
          {
          "id": "case_id"
          }
         ]
        }
       }
      ]
     }
    }
   },
  "name": "testLayout"
}
```

```
{
  "layoutArn": "arn:aws:cases:us-west-2:[account_id]:domain/[domain_id]/layout/[layout_id]",
  "layoutId": "[layout_id]"
}
```

## See Also
<a name="API_connect-cases_CreateLayout_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcases-2022-10-03/CreateLayout)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcases-2022-10-03/CreateLayout)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/CreateLayout)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcases-2022-10-03/CreateLayout)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/CreateLayout)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcases-2022-10-03/CreateLayout)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcases-2022-10-03/CreateLayout)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcases-2022-10-03/CreateLayout)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcases-2022-10-03/CreateLayout)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/CreateLayout)
