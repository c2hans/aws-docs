---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_ListDataTableAttributes.html
---

# ListDataTableAttributes
<a name="API_ListDataTableAttributes"></a>

Returns all attributes for a specified data table. A maximum of 100 attributes per data table is allowed. Customers can request an increase by using AWS Service Quotas. The response can be filtered by specific attribute IDs for CloudFormation integration.

## Request Syntax
<a name="API_ListDataTableAttributes_RequestSyntax"></a>

```
POST /data-tables/{{InstanceId}}/{{DataTableId}}/attributes?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
Content-type: application/json

{
   "AttributeIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_ListDataTableAttributes_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DataTableId](#API_ListDataTableAttributes_RequestSyntax) **   <a name="connect-ListDataTableAttributes-request-uri-DataTableId"></a>
The unique identifier for the data table whose attributes should be listed.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_ListDataTableAttributes_RequestSyntax) **   <a name="connect-ListDataTableAttributes-request-uri-InstanceId"></a>
The unique identifier for the Amazon Connect instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_ListDataTableAttributes_RequestSyntax) **   <a name="connect-ListDataTableAttributes-request-uri-MaxResults"></a>
The maximum number of data table attributes to return in one page of results.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [NextToken](#API_ListDataTableAttributes_RequestSyntax) **   <a name="connect-ListDataTableAttributes-request-uri-NextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.

## Request Body
<a name="API_ListDataTableAttributes_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AttributeIds](#API_ListDataTableAttributes_RequestSyntax) **   <a name="connect-ListDataTableAttributes-request-AttributeIds"></a>
Optional list of specific attribute IDs to retrieve. Used for CloudFormation to effectively describe attributes by ID. If NextToken is provided, this parameter is ignored.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_ListDataTableAttributes_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Attributes": [
      {
         "AttributeId": "string",
         "DataTableArn": "string",
         "DataTableId": "string",
         "Description": "string",
         "LastModifiedRegion": "string",
         "LastModifiedTime": number,
         "LockVersion": {
            "Attribute": "string",
            "DataTable": "string",
            "PrimaryValues": "string",
            "Value": "string"
         },
         "Name": "string",
         "Primary": boolean,
         "Validation": {
            "Enum": {
               "Strict": boolean,
               "Values": [ "string" ]
            },
            "ExclusiveMaximum": number,
            "ExclusiveMinimum": number,
            "IgnoreCase": boolean,
            "Maximum": number,
            "MaxLength": number,
            "MaxValues": number,
            "Minimum": number,
            "MinLength": number,
            "MinValues": number,
            "MultipleOf": number
         },
         "ValueType": "string",
         "Version": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListDataTableAttributes_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Attributes](#API_ListDataTableAttributes_ResponseSyntax) **   <a name="connect-ListDataTableAttributes-response-Attributes"></a>
A list of data table attributes with their complete configuration and metadata.
Type: Array of [DataTableAttribute](API_DataTableAttribute.md) objects

 ** [NextToken](#API_ListDataTableAttributes_ResponseSyntax) **   <a name="connect-ListDataTableAttributes-response-NextToken"></a>
Specify the pagination token from a previous request to retrieve the next page of results.
Type: String

## Errors
<a name="API_ListDataTableAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_ListDataTableAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/ListDataTableAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/ListDataTableAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/ListDataTableAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/ListDataTableAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/ListDataTableAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/ListDataTableAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/ListDataTableAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/ListDataTableAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/ListDataTableAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/ListDataTableAttributes)
