---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_CreateDataSet.html
---

# CreateDataSet
<a name="API_CreateDataSet"></a>

This operation creates a data set.

## Request Syntax
<a name="API_CreateDataSet_RequestSyntax"></a>

```
POST /v1/data-sets HTTP/1.1
Content-type: application/json

{
   "AssetType": "{{string}}",
   "Description": "{{string}}",
   "Name": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateDataSet_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateDataSet_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AssetType](#API_CreateDataSet_RequestSyntax) **   <a name="dataexchange-CreateDataSet-request-AssetType"></a>
The type of asset that is added to a data set.
Type: String
Valid Values: `S3_SNAPSHOT | REDSHIFT_DATA_SHARE | API_GATEWAY_API | S3_DATA_ACCESS | LAKE_FORMATION_DATA_PERMISSION`
Required: Yes

 ** [Description](#API_CreateDataSet_RequestSyntax) **   <a name="dataexchange-CreateDataSet-request-Description"></a>
A description for the data set. This value can be up to 16,348 characters long.
Type: String
Required: Yes

 ** [Name](#API_CreateDataSet_RequestSyntax) **   <a name="dataexchange-CreateDataSet-request-Name"></a>
The name of the data set.
Type: String
Required: Yes

 ** [Tags](#API_CreateDataSet_RequestSyntax) **   <a name="dataexchange-CreateDataSet-request-Tags"></a>
A data set tag is an optional label that you can assign to a data set when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to these data sets and revisions.
Type: String to string map
Required: No

## Response Syntax
<a name="API_CreateDataSet_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "Arn": "string",
   "AssetType": "string",
   "CreatedAt": "string",
   "Description": "string",
   "Id": "string",
   "Name": "string",
   "Origin": "string",
   "OriginDetails": {
      "DataGrantId": "string",
      "ProductId": "string"
   },
   "SourceId": "string",
   "Tags": {
      "string" : "string"
   },
   "UpdatedAt": "string"
}
```

## Response Elements
<a name="API_CreateDataSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_CreateDataSet_ResponseSyntax) **   <a name="dataexchange-CreateDataSet-response-Arn"></a>
The ARN for the data set.
Type: String

 ** [AssetType](#API_CreateDataSet_ResponseSyntax) **   <a name="dataexchange-CreateDataSet-response-AssetType"></a>
The type of asset that is added to a data set.
Type: String
Valid Values: `S3_SNAPSHOT | REDSHIFT_DATA_SHARE | API_GATEWAY_API | S3_DATA_ACCESS | LAKE_FORMATION_DATA_PERMISSION`

 ** [CreatedAt](#API_CreateDataSet_ResponseSyntax) **   <a name="dataexchange-CreateDataSet-response-CreatedAt"></a>
The date and time that the data set was created, in ISO 8601 format.
Type: Timestamp

 ** [Description](#API_CreateDataSet_ResponseSyntax) **   <a name="dataexchange-CreateDataSet-response-Description"></a>
The description for the data set.
Type: String

 ** [Id](#API_CreateDataSet_ResponseSyntax) **   <a name="dataexchange-CreateDataSet-response-Id"></a>
The unique identifier for the data set.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`

 ** [Name](#API_CreateDataSet_ResponseSyntax) **   <a name="dataexchange-CreateDataSet-response-Name"></a>
The name of the data set.
Type: String

 ** [Origin](#API_CreateDataSet_ResponseSyntax) **   <a name="dataexchange-CreateDataSet-response-Origin"></a>
A property that defines the data set as OWNED by the account (for providers) or ENTITLED to the account (for subscribers).
Type: String
Valid Values: `OWNED | ENTITLED`

 ** [OriginDetails](#API_CreateDataSet_ResponseSyntax) **   <a name="dataexchange-CreateDataSet-response-OriginDetails"></a>
If the origin of this data set is ENTITLED, includes the details for the product on AWS Marketplace.
Type: [OriginDetails](API_OriginDetails.md) object

 ** [SourceId](#API_CreateDataSet_ResponseSyntax) **   <a name="dataexchange-CreateDataSet-response-SourceId"></a>
The data set ID of the owned data set corresponding to the entitled data set being viewed. This parameter is returned when a data set owner is viewing the entitled copy of its owned data set.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`

 ** [Tags](#API_CreateDataSet_ResponseSyntax) **   <a name="dataexchange-CreateDataSet-response-Tags"></a>
The tags for the data set.
Type: String to string map

 ** [UpdatedAt](#API_CreateDataSet_ResponseSyntax) **   <a name="dataexchange-CreateDataSet-response-UpdatedAt"></a>
The date and time that the data set was last updated, in ISO 8601 format.
Type: Timestamp

## Errors
<a name="API_CreateDataSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to the resource is denied.
 ** Message **
Access to the resource is denied.
HTTP Status Code: 403

 ** InternalServerException **
An exception occurred with the service.
 ** Message **
The message identifying the service exception that occurred.
HTTP Status Code: 500

 ** ServiceLimitExceededException **
The request has exceeded the quotas imposed by the service.
 ** LimitName **
The name of the limit that was reached.
 ** LimitValue **
The value of the exceeded limit.
 ** Message **
The request has exceeded the quotas imposed by the service.
HTTP Status Code: 402

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** Message **
The limit on the number of requests per second was exceeded.
HTTP Status Code: 429

 ** ValidationException **
The request was invalid.
 ** ExceptionCause **
The unique identifier for the resource that couldn't be found.
 ** Message **
The message that informs you about what was invalid about the request.
HTTP Status Code: 400

## See Also
<a name="API_CreateDataSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dataexchange-2017-07-25/CreateDataSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dataexchange-2017-07-25/CreateDataSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/CreateDataSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dataexchange-2017-07-25/CreateDataSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/CreateDataSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dataexchange-2017-07-25/CreateDataSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dataexchange-2017-07-25/CreateDataSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dataexchange-2017-07-25/CreateDataSet)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/dataexchange-2017-07-25/CreateDataSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/CreateDataSet)
