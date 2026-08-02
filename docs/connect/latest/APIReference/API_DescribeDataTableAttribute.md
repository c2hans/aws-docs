---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeDataTableAttribute.html
---

# DescribeDataTableAttribute
<a name="API_DescribeDataTableAttribute"></a>

Returns detailed information for a specific data table attribute including its configuration, validation rules, and metadata. "Describe" is a deprecated term but is allowed to maintain consistency with existing operations.

## Request Syntax
<a name="API_DescribeDataTableAttribute_RequestSyntax"></a>

```
GET /data-tables/{{InstanceId}}/{{DataTableId}}/attributes/{{AttributeName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeDataTableAttribute_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AttributeName](#API_DescribeDataTableAttribute_RequestSyntax) **   <a name="connect-DescribeDataTableAttribute-request-uri-AttributeName"></a>
The name of the attribute to retrieve detailed information for.
Length Constraints: Minimum length of 1. Maximum length of 127.
Pattern: `^[\p{L}\p{Z}\p{N}\-_.:=@'|]+$`
Required: Yes

 ** [DataTableId](#API_DescribeDataTableAttribute_RequestSyntax) **   <a name="connect-DescribeDataTableAttribute-request-uri-DataTableId"></a>
The unique identifier for the data table. Must also accept the table ARN with or without a version alias.
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [InstanceId](#API_DescribeDataTableAttribute_RequestSyntax) **   <a name="connect-DescribeDataTableAttribute-request-uri-InstanceId"></a>
The unique identifier for the Amazon Connect instance.
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Request Body
<a name="API_DescribeDataTableAttribute_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeDataTableAttribute_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Attribute": {
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
}
```

## Response Elements
<a name="API_DescribeDataTableAttribute_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Attribute](#API_DescribeDataTableAttribute_ResponseSyntax) **   <a name="connect-DescribeDataTableAttribute-response-Attribute"></a>
The complete attribute information including configuration, validation rules, lock version, and metadata.
Type: [DataTableAttribute](API_DataTableAttribute.md) object

## Errors
<a name="API_DescribeDataTableAttribute_Errors"></a>

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
<a name="API_DescribeDataTableAttribute_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DescribeDataTableAttribute)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DescribeDataTableAttribute)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DescribeDataTableAttribute)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DescribeDataTableAttribute)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DescribeDataTableAttribute)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DescribeDataTableAttribute)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DescribeDataTableAttribute)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DescribeDataTableAttribute)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DescribeDataTableAttribute)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DescribeDataTableAttribute)
