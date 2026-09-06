---
source_url: https://docs.aws.amazon.com/cases/latest/APIReference/API_CreateRelatedItem.html
---

# CreateRelatedItem
<a name="API_connect-cases_CreateRelatedItem"></a>

Creates a related item (comments, tasks, and contacts) and associates it with a case.

There's a quota for the number of fields allowed in a Custom type related item. See [Connect Customer Cases quotas](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html#cases-quotas).

 **Use cases**

Following are examples of related items that you may want to associate with a case:
+ Related contacts, such as calls, chats, emails tasks
+ Comments, for agent notes
+ SLAs, to capture target resolution goals
+ Cases, to capture related Connect Customer Cases
+ Files, such as policy documentation or customer-provided attachments
+ Custom related items, which provide flexibility for you to define related items that such as bookings, orders, products, notices, and more

 **Important things to know**
+ If you are associating a contact to a case by passing in `Contact` for a `type`, you must have [DescribeContact](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeContact.html) permission on the ARN of the contact that you provide in `content.contact.contactArn`.
+ A Related Item is a resource that is associated with a case. It may or may not have an external identifier linking it to an external resource (for example, a `contactArn`). All Related Items have their own internal identifier, the `relatedItemArn`. Examples of related items include `comments` and `contacts`.
+ If you provide a value for `performedBy.userArn`, you must also have [DescribeUser](https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeUser.html) permission on the ARN of the user that you provide.

 **Endpoints**: See [Connect Customer endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/connect_region.html).

## Request Syntax
<a name="API_connect-cases_CreateRelatedItem_RequestSyntax"></a>

```
POST /domains/{{domainId}}/cases/{{caseId}}/related-items/ HTTP/1.1
Content-type: application/json

{
   "content": { ... },
   "performedBy": { ... },
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-cases_CreateRelatedItem_RequestParameters"></a>

The request uses the following URI parameters.

 ** [caseId](#API_connect-cases_CreateRelatedItem_RequestSyntax) **   <a name="connect-connect-cases_CreateRelatedItem-request-uri-caseId"></a>
A unique identifier of the case.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** [domainId](#API_connect-cases_CreateRelatedItem_RequestSyntax) **   <a name="connect-connect-cases_CreateRelatedItem-request-uri-domainId"></a>
The unique identifier of the Cases domain.
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

## Request Body
<a name="API_connect-cases_CreateRelatedItem_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [content](#API_connect-cases_CreateRelatedItem_RequestSyntax) **   <a name="connect-connect-cases_CreateRelatedItem-request-content"></a>
The content of a related item to be created.
Type: [RelatedItemInputContent](API_connect-cases_RelatedItemInputContent.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [performedBy](#API_connect-cases_CreateRelatedItem_RequestSyntax) **   <a name="connect-connect-cases_CreateRelatedItem-request-performedBy"></a>
Represents the creator of the related item.
Type: [UserUnion](API_connect-cases_UserUnion.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [type](#API_connect-cases_CreateRelatedItem_RequestSyntax) **   <a name="connect-connect-cases_CreateRelatedItem-request-type"></a>
The type of a related item.
Type: String
Valid Values: `Contact | Comment | File | Sla | ConnectCase | Custom`
Required: Yes

## Response Syntax
<a name="API_connect-cases_CreateRelatedItem_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "relatedItemArn": "string",
   "relatedItemId": "string"
}
```

## Response Elements
<a name="API_connect-cases_CreateRelatedItem_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [relatedItemArn](#API_connect-cases_CreateRelatedItem_ResponseSyntax) **   <a name="connect-connect-cases_CreateRelatedItem-response-relatedItemArn"></a>
The Amazon Resource Name (ARN) of the related item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

 ** [relatedItemId](#API_connect-cases_CreateRelatedItem_ResponseSyntax) **   <a name="connect-connect-cases_CreateRelatedItem-response-relatedItemId"></a>
The unique identifier of the related item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.

## Errors
<a name="API_connect-cases_CreateRelatedItem_Errors"></a>

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
<a name="API_connect-cases_CreateRelatedItem_Examples"></a>

This section provides examples for supported related item types.

### Type: Comment
<a name="API_connect-cases_CreateRelatedItem_Example_1"></a>

Request:

```
{
  "content": {
    "comment": {
      "body": "Hello World!",
      "contentType": "Text/Plain"
    }
  },
  "type": "Comment"
}
```

### Type: Sla
<a name="API_connect-cases_CreateRelatedItem_Example_2"></a>

Request:
+  `name` is the descriptive name for the SLA
+  `targetSlaMinutes` is the time in minutes within which the SLA must be met
+  `type` only supports "CaseField"
+  `fieldId` only supports "status" field
+  `targetFieldValues` is the value that the field must reach for the SLA to be met and only supports one value.

```
{
  "content": {
    "sla": {
      "slaInputConfiguration": {
        "name": "Resolution SLA",
        "targetSlaMinutes": 10,
        "type": "CaseField",
        "fieldId": "status",
        "targetFieldValues": [
          {
            "stringValue": "closed"
          }
        ]
      }
    }
  },
  "type": "Sla"
}
```

### Type: File
<a name="API_connect-cases_CreateRelatedItem_Example_3"></a>

Request:

```
{
  "content": {
    "file": {
      "fileArn": "[fileArn]"
    }
  },
  "type": "File"
}
```

### Type: Contact
<a name="API_connect-cases_CreateRelatedItem_Example_4"></a>

Request to associate a customer contact with a case:

```
{
  "content": {
    "contact": {
      "contactArn": "[contactArn]"
    }
  },
  "type": "Contact"
}
```

### Type: Custom
<a name="API_connect-cases_CreateRelatedItem_Example_5"></a>

Request to associate a custom defined related item with a case:

**Note**
 [System case fields](https://docs.aws.amazon.com/connect/latest/adminguide/case-fields.html#system-case-fields) cannot be used in a custom related item.

```
{
  "content": {
    "custom": {
        "fields": [
            {
              "id": "[field_id_1]",
              "value": {
                "stringValue": "Billing"
              }
            },
            {
              "id": "[field_id_2]",
              "value": {
                "stringValue": "Incorrect Shipping Address"
              }
            }
        ]
    }
  },
  "type": "Custom"
}
```

### Type: ConnectCase
<a name="API_connect-cases_CreateRelatedItem_Example_6"></a>

Request to associate another Connect Customer case with a case:

```
{
  "content": {
    "connectCase": {
      "caseId": "[caseId]"
    }
  },
  "type": "ConnectCase"
}
```

### CreateRelatedItem Response example
<a name="API_connect-cases_CreateRelatedItem_Example_7"></a>

All successful CreateRelatedItem requests return the same response structure:

```
{
  "relatedItemArn": "arn:aws:cases:us-west-2:[account_id]:domain/[domain_id]/case/[case_id]/related-item/[related_item_id]",
  "relatedItemId": "[related_item_id]"
}
```

## See Also
<a name="API_connect-cases_CreateRelatedItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connectcases-2022-10-03/CreateRelatedItem)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connectcases-2022-10-03/CreateRelatedItem)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/CreateRelatedItem)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connectcases-2022-10-03/CreateRelatedItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/CreateRelatedItem)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connectcases-2022-10-03/CreateRelatedItem)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connectcases-2022-10-03/CreateRelatedItem)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connectcases-2022-10-03/CreateRelatedItem)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connectcases-2022-10-03/CreateRelatedItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/CreateRelatedItem)
