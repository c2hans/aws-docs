---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_UpdateRelatedItem.html
---

# UpdateRelatedItem
<a name="API_connect-cases_UpdateRelatedItem"></a>

Updates the content of a related item associated with a case. The following related item types are supported:
+  **Comment** - Update the text content of an existing comment
+  **Custom** - Update the fields of a custom related item. You can add, modify, and remove fields from a custom related item. There's a quota for the number of fields allowed in a Custom type related item. See [Connect Customer Cases quotas](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#cases-quotas).

 **Important things to know**
+ When updating a Custom related item, all existing and new fields, and their associated values should be included in the request. Fields not included as part of this request will be removed.
+ If you provide a value for `performedBy.userArn` you must also have [DescribeUser](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html) permission on the ARN of the user that you provide.
+  [System case fields](https://docs.aws.amazon.com/connect/latest/adminguide/case-fields.html#system-case-fields) cannot be used in a custom related item.

 **Endpoints**: See [Connect Customer endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/connect_region.html).

## Request Syntax
<a name="API_connect-cases_UpdateRelatedItem_RequestSyntax"></a>

```
PUT /domains/{{domainId}}/cases/{{caseId}}/related-items/{{relatedItemId}} HTTP/1.1
Content-type: application/json

{
   "content": { ... },
   "performedBy": { ... }
}
```

## URI Request Parameters
<a name="API_connect-cases_UpdateRelatedItem_RequestParameters"></a>

The request uses the following URI parameters.

 ** [caseId](#API_connect-cases_UpdateRelatedItem_RequestSyntax) **   <a name="connect-connect-cases_UpdateRelatedItem-request-uri-caseId"></a>
A unique identifier of the case.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [domainId](#API_connect-cases_UpdateRelatedItem_RequestSyntax) **   <a name="connect-connect-cases_UpdateRelatedItem-request-uri-domainId"></a>
The unique identifier of the Cases domain.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [relatedItemId](#API_connect-cases_UpdateRelatedItem_RequestSyntax) **   <a name="connect-connect-cases_UpdateRelatedItem-request-uri-relatedItemId"></a>
Unique identifier of a related item.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Request Body
<a name="API_connect-cases_UpdateRelatedItem_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [content](#API_connect-cases_UpdateRelatedItem_RequestSyntax) **   <a name="connect-connect-cases_UpdateRelatedItem-request-content"></a>
The content of a related item to be updated.
Type: [RelatedItemUpdateContent](API_connect-cases_RelatedItemUpdateContent.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [performedBy](#API_connect-cases_UpdateRelatedItem_RequestSyntax) **   <a name="connect-connect-cases_UpdateRelatedItem-request-performedBy"></a>
Represents the user who performed the update of the related item.
Type: [UserUnion](API_connect-cases_UserUnion.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## Response Syntax
<a name="API_connect-cases_UpdateRelatedItem_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "associationTime": "string",
   "content": { ... },
   "createdBy": { ... },
   "lastUpdatedUser": { ... },
   "relatedItemArn": "string",
   "relatedItemId": "string",
   "tags": {
      "string" : "string"
   },
   "type": "string"
}
```

## Response Elements
<a name="API_connect-cases_UpdateRelatedItem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [associationTime](#API_connect-cases_UpdateRelatedItem_ResponseSyntax) **   <a name="connect-connect-cases_UpdateRelatedItem-response-associationTime"></a>
Time at which the related item was associated with the case.
Type: Timestamp

 ** [content](#API_connect-cases_UpdateRelatedItem_ResponseSyntax) **   <a name="connect-connect-cases_UpdateRelatedItem-response-content"></a>
Represents the content of the updated related item.
Type: [RelatedItemContent](API_connect-cases_RelatedItemContent.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [createdBy](#API_connect-cases_UpdateRelatedItem_ResponseSyntax) **   <a name="connect-connect-cases_UpdateRelatedItem-response-createdBy"></a>
Represents the creator of the related item.
Type: [UserUnion](API_connect-cases_UserUnion.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [lastUpdatedUser](#API_connect-cases_UpdateRelatedItem_ResponseSyntax) **   <a name="connect-connect-cases_UpdateRelatedItem-response-lastUpdatedUser"></a>
Represents the last user that updated the related item.
Type: [UserUnion](API_connect-cases_UserUnion.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [relatedItemArn](#API_connect-cases_UpdateRelatedItem_ResponseSyntax) **   <a name="connect-connect-cases_UpdateRelatedItem-response-relatedItemArn"></a>
The Amazon Resource Name (ARN) of the updated related item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

 ** [relatedItemId](#API_connect-cases_UpdateRelatedItem_ResponseSyntax) **   <a name="connect-connect-cases_UpdateRelatedItem-response-relatedItemId"></a>
The unique identifier of the updated related item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

 ** [tags](#API_connect-cases_UpdateRelatedItem_ResponseSyntax) **   <a name="connect-connect-cases_UpdateRelatedItem-response-tags"></a>
A map of of key-value pairs that represent tags on a resource. Tags are used to organize, track, or control access for this resource.
Type: String to string map

 ** [type](#API_connect-cases_UpdateRelatedItem_ResponseSyntax) **   <a name="connect-connect-cases_UpdateRelatedItem-response-type"></a>
Type of the updated related item.
Type: String
Valid Values: `Contact | Comment | File | Sla | ConnectCase | Custom`

## Errors
<a name="API_connect-cases_UpdateRelatedItem_Errors"></a>

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
<a name="API_connect-cases_UpdateRelatedItem_Examples"></a>

This section provides examples for updating supported related item types.

### Update Comment related item
<a name="API_connect-cases_UpdateRelatedItem_Example_1"></a>

Request to update a comment's text and content type:

```
{
  "domainId": "[domain_id]",
  "caseId": "[case_id]",
  "relatedItemId": "[related_item_id]",
  "content": {
    "comment": {
      "body": "Updated comment text with additional details",
      "contentType": "Text/Plain"
    }
  }
}
```

### Update Custom related item
<a name="API_connect-cases_UpdateRelatedItem_Example_2"></a>

Request to update field values in a custom related item:

**Note**
 [System case fields](https://docs.aws.amazon.com/connect/latest/adminguide/case-fields.html#system-case-fields) cannot be used in a custom related item.

```
{
  "domainId": "[domain_id]",
  "caseId": "[case_id]",
  "relatedItemId": "[related_item_id]",
  "content": {
    "custom": {
      "fields": [
        {
          "id": "[field_id_1]",
          "value": {
            "stringValue": "Updated value for first field"
          }
        },
        {
          "id": "[field_id_2]",
          "value": {
            "stringValue": "Updated value for second field"
          }
        },
        {
          "id": "[field_id_3]",
          "value": {
            "stringValue": "Existing value that remains unchanged"
          }
        }
      ]
    }
  }
}
```

### Update with performedBy parameter
<a name="API_connect-cases_UpdateRelatedItem_Example_3"></a>

Request to update a comment and specify who performed the update:

```
{
  "domainId": "[domain_id]",
  "caseId": "[case_id]",
  "relatedItemId": "[related_item_id]",
  "content": {
    "comment": {
      "body": "Updated comment text with additional details",
      "contentType": "Text/Plain"
    }
  },
  "performedBy": {
    "userArn": "arn:aws:connect:us-west-2:[account_id]:instance/[instance_id]/agent/[agent_id]"
  }
}
```

### UpdateRelatedItem Response example
<a name="API_connect-cases_UpdateRelatedItem_Example_4"></a>

All successful UpdateRelatedItem requests return the updated related item:

```
{
  "relatedItemArn": "arn:aws:cases:us-west-2:[account_id]:domain/[domain_id]/case/[case_id]/related-item/[related_item_id]",
  "relatedItemId": "[related_item_id]",
  "type": "Comment",
  "content": {
    "comment": {
      "body": "Updated comment text with additional details",
      "contentType": "Text/Plain"
    }
  },
  "associationTime": "2024-11-22T01:35:46.329Z",
  "lastUpdatedUser": {
    "userArn": "arn:aws:connect:us-west-2:[account_id]:instance/[instance_id]/agent/[agent_id]"
  },
  "createdBy": {
    "userArn": "arn:aws:connect:us-west-2:[account_id]:instance/[instance_id]/agent/[agent_id]"
  }
}
```

## See Also
<a name="API_connect-cases_UpdateRelatedItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcases-2022-10-03/UpdateRelatedItem)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcases-2022-10-03/UpdateRelatedItem)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/UpdateRelatedItem)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcases-2022-10-03/UpdateRelatedItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/UpdateRelatedItem)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcases-2022-10-03/UpdateRelatedItem)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcases-2022-10-03/UpdateRelatedItem)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcases-2022-10-03/UpdateRelatedItem)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcases-2022-10-03/UpdateRelatedItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/UpdateRelatedItem)
