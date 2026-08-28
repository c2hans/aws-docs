---
source_url: https://docs.aws.amazon.com/data-exchange/latest/apireference/API_UpdateDataSet.html
---

# UpdateDataSet
<a name="API_UpdateDataSet"></a>

This operation updates a data set.

## Request Syntax
<a name="API_UpdateDataSet_RequestSyntax"></a>

```
PATCH /v1/data-sets/{{DataSetId}} HTTP/1.1
Content-type: application/json

{
   "Description": "{{string}}",
   "Name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateDataSet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DataSetId](#API_UpdateDataSet_RequestSyntax) **   <a name="dataexchange-UpdateDataSet-request-uri-DataSetId"></a>
The unique identifier for a data set.
Pattern: `[a-zA-Z0-9]{30,40}`
Required: Yes

## Request Body
<a name="API_UpdateDataSet_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Description](#API_UpdateDataSet_RequestSyntax) **   <a name="dataexchange-UpdateDataSet-request-Description"></a>
The description for the data set.
Type: String
Required: No

 ** [Name](#API_UpdateDataSet_RequestSyntax) **   <a name="dataexchange-UpdateDataSet-request-Name"></a>
The name of the data set.
Type: String
Required: No

## Response Syntax
<a name="API_UpdateDataSet_ResponseSyntax"></a>

```
HTTP/1.1 200
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
   "UpdatedAt": "string"
}
```

## Response Elements
<a name="API_UpdateDataSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Arn](#API_UpdateDataSet_ResponseSyntax) **   <a name="dataexchange-UpdateDataSet-response-Arn"></a>
The ARN for the data set.
Type: String

 ** [AssetType](#API_UpdateDataSet_ResponseSyntax) **   <a name="dataexchange-UpdateDataSet-response-AssetType"></a>
The type of asset that is added to a data set.
Type: String
Valid Values: `S3_SNAPSHOT | REDSHIFT_DATA_SHARE | API_GATEWAY_API | S3_DATA_ACCESS | LAKE_FORMATION_DATA_PERMISSION`

 ** [CreatedAt](#API_UpdateDataSet_ResponseSyntax) **   <a name="dataexchange-UpdateDataSet-response-CreatedAt"></a>
The date and time that the data set was created, in ISO 8601 format.
Type: Timestamp

 ** [Description](#API_UpdateDataSet_ResponseSyntax) **   <a name="dataexchange-UpdateDataSet-response-Description"></a>
The description for the data set.
Type: String

 ** [Id](#API_UpdateDataSet_ResponseSyntax) **   <a name="dataexchange-UpdateDataSet-response-Id"></a>
The unique identifier for the data set.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`

 ** [Name](#API_UpdateDataSet_ResponseSyntax) **   <a name="dataexchange-UpdateDataSet-response-Name"></a>
The name of the data set.
Type: String

 ** [Origin](#API_UpdateDataSet_ResponseSyntax) **   <a name="dataexchange-UpdateDataSet-response-Origin"></a>
A property that defines the data set as OWNED by the account (for providers) or ENTITLED to the account (for subscribers).
Type: String
Valid Values: `OWNED | ENTITLED`

 ** [OriginDetails](#API_UpdateDataSet_ResponseSyntax) **   <a name="dataexchange-UpdateDataSet-response-OriginDetails"></a>
If the origin of this data set is ENTITLED, includes the details for the product on AWS Marketplace.
Type: [OriginDetails](API_OriginDetails.md) object

 ** [SourceId](#API_UpdateDataSet_ResponseSyntax) **   <a name="dataexchange-UpdateDataSet-response-SourceId"></a>
The data set ID of the owned data set corresponding to the entitled data set being viewed. This parameter is returned when a data set owner is viewing the entitled copy of its owned data set.
Type: String
Pattern: `[a-zA-Z0-9]{30,40}`

 ** [UpdatedAt](#API_UpdateDataSet_ResponseSyntax) **   <a name="dataexchange-UpdateDataSet-response-UpdatedAt"></a>
The date and time that the data set was last updated, in ISO 8601 format.
Type: Timestamp

## Errors
<a name="API_UpdateDataSet_Errors"></a>

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

 ** ResourceNotFoundException **
The resource couldn't be found.
 ** Message **
The resource couldn't be found.
 ** ResourceId **
The unique identifier for the resource that couldn't be found.
 ** ResourceType **
The type of resource that couldn't be found.
HTTP Status Code: 404

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
<a name="API_UpdateDataSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/dataexchange-2017-07-25/UpdateDataSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/dataexchange-2017-07-25/UpdateDataSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dataexchange-2017-07-25/UpdateDataSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/dataexchange-2017-07-25/UpdateDataSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dataexchange-2017-07-25/UpdateDataSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/dataexchange-2017-07-25/UpdateDataSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/dataexchange-2017-07-25/UpdateDataSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/dataexchange-2017-07-25/UpdateDataSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/dataexchange-2017-07-25/UpdateDataSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dataexchange-2017-07-25/UpdateDataSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Data Exchange. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query data-exchange` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
