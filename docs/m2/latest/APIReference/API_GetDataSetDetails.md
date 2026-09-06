---
source_url: https://docs.aws.amazon.com/m2/latest/APIReference/API_GetDataSetDetails.html
---

# GetDataSetDetails
<a name="API_GetDataSetDetails"></a>

**Important**
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).

Gets the details of a specific data set.

## Request Syntax
<a name="API_GetDataSetDetails_RequestSyntax"></a>

```
GET /applications/{{applicationId}}/datasets/{{dataSetName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetDataSetDetails_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_GetDataSetDetails_RequestSyntax) **   <a name="m2-GetDataSetDetails-request-uri-applicationId"></a>
The unique identifier of the application that this data set is associated with.
Pattern: `\S{1,80}`
Required: Yes

 ** [dataSetName](#API_GetDataSetDetails_RequestSyntax) **   <a name="m2-GetDataSetDetails-request-uri-dataSetName"></a>
The name of the data set.
Pattern: `\S{1,200}`
Required: Yes

## Request Body
<a name="API_GetDataSetDetails_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetDataSetDetails_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "blocksize": number,
   "creationTime": number,
   "dataSetName": "string",
   "dataSetOrg": { ... },
   "fileSize": number,
   "lastReferencedTime": number,
   "lastUpdatedTime": number,
   "location": "string",
   "recordLength": number
}
```

## Response Elements
<a name="API_GetDataSetDetails_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [blocksize](#API_GetDataSetDetails_ResponseSyntax) **   <a name="m2-GetDataSetDetails-response-blocksize"></a>
The size of the block on disk.
Type: Integer

 ** [creationTime](#API_GetDataSetDetails_ResponseSyntax) **   <a name="m2-GetDataSetDetails-response-creationTime"></a>
The timestamp when the data set was created.
Type: Timestamp

 ** [dataSetName](#API_GetDataSetDetails_ResponseSyntax) **   <a name="m2-GetDataSetDetails-response-dataSetName"></a>
The name of the data set.
Type: String
Pattern: `\S{1,200}`

 ** [dataSetOrg](#API_GetDataSetDetails_ResponseSyntax) **   <a name="m2-GetDataSetDetails-response-dataSetOrg"></a>
The type of data set. The only supported value is VSAM.
Type: [DatasetDetailOrgAttributes](API_DatasetDetailOrgAttributes.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [fileSize](#API_GetDataSetDetails_ResponseSyntax) **   <a name="m2-GetDataSetDetails-response-fileSize"></a>
File size of the dataset.
Type: Long

 ** [lastReferencedTime](#API_GetDataSetDetails_ResponseSyntax) **   <a name="m2-GetDataSetDetails-response-lastReferencedTime"></a>
The last time the data set was referenced.
Type: Timestamp

 ** [lastUpdatedTime](#API_GetDataSetDetails_ResponseSyntax) **   <a name="m2-GetDataSetDetails-response-lastUpdatedTime"></a>
The last time the data set was updated.
Type: Timestamp

 ** [location](#API_GetDataSetDetails_ResponseSyntax) **   <a name="m2-GetDataSetDetails-response-location"></a>
The location where the data set is stored.
Type: String
Pattern: `\S{1,2000}`

 ** [recordLength](#API_GetDataSetDetails_ResponseSyntax) **   <a name="m2-GetDataSetDetails-response-recordLength"></a>
The length of records in the data set.
Type: Integer

## Errors
<a name="API_GetDataSetDetails_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The account or role doesn't have the right permissions to make the request.
HTTP Status Code: 403

 ** ConflictException **
The parameters provided in the request conflict with existing resources.
 ** resourceId **
The ID of the conflicting resource.
 ** resourceType **
The type of the conflicting resource.
HTTP Status Code: 409

 ** ExecutionTimeoutException **
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).
 Failed to connect to server, or didn’t receive response within expected time period.
HTTP Status Code: 504

 ** InternalServerException **
An unexpected error occurred during the processing of the request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
 ** resourceId **
The ID of the missing resource.
 ** resourceType **
The type of the missing resource.
HTTP Status Code: 404

 ** ServiceUnavailableException **
 AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html).
Server cannot process the request at the moment.
HTTP Status Code: 503

 ** ThrottlingException **
The number of requests made exceeds the limit.
 ** quotaCode **
The identifier of the throttled request.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
 ** serviceCode **
The identifier of the service that the throttled request was made to.
HTTP Status Code: 429

 ** ValidationException **
One or more parameters provided in the request is not valid.
 ** fieldList **
The list of fields that failed service validation.
 ** reason **
The reason why it failed service validation.
HTTP Status Code: 400

## See Also
<a name="API_GetDataSetDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/m2-2021-04-28/GetDataSetDetails)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/m2-2021-04-28/GetDataSetDetails)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/m2-2021-04-28/GetDataSetDetails)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/m2-2021-04-28/GetDataSetDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/m2-2021-04-28/GetDataSetDetails)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/m2-2021-04-28/GetDataSetDetails)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/m2-2021-04-28/GetDataSetDetails)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/m2-2021-04-28/GetDataSetDetails)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/m2-2021-04-28/GetDataSetDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/m2-2021-04-28/GetDataSetDetails)
