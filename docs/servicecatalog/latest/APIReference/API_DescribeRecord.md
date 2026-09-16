---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_DescribeRecord.html
---

# DescribeRecord
<a name="API_DescribeRecord"></a>

Gets information about the specified request operation.

Use this operation after calling a request operation (for example, [ProvisionProduct](API_ProvisionProduct.md), [TerminateProvisionedProduct](API_TerminateProvisionedProduct.md), or [UpdateProvisionedProduct](API_UpdateProvisionedProduct.md)).

**Note**
If a provisioned product was transferred to a new owner using [UpdateProvisionedProductProperties](API_UpdateProvisionedProductProperties.md), the new owner will be able to describe all past records for that product. The previous owner will no longer be able to describe the records, but will be able to use [ListRecordHistory](API_ListRecordHistory.md) to see the product's history from when he was the owner.

## Request Syntax
<a name="API_DescribeRecord_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "Id": "{{string}}",
   "PageSize": {{number}},
   "PageToken": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeRecord_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_DescribeRecord_RequestSyntax) **   <a name="servicecatalog-DescribeRecord-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [Id](#API_DescribeRecord_RequestSyntax) **   <a name="servicecatalog-DescribeRecord-request-Id"></a>
The record identifier of the provisioned product. This identifier is returned by the request operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

 ** [PageSize](#API_DescribeRecord_RequestSyntax) **   <a name="servicecatalog-DescribeRecord-request-PageSize"></a>
The maximum number of items to return with this call.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 20.
Required: No

 ** [PageToken](#API_DescribeRecord_RequestSyntax) **   <a name="servicecatalog-DescribeRecord-request-PageToken"></a>
The page token for the next set of results. To retrieve the first set of results, use null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`
Required: No

## Response Syntax
<a name="API_DescribeRecord_ResponseSyntax"></a>

```
{
   "NextPageToken": "string",
   "RecordDetail": {
      "CreatedTime": number,
      "LaunchRoleArn": "string",
      "PathId": "string",
      "ProductId": "string",
      "ProvisionedProductId": "string",
      "ProvisionedProductName": "string",
      "ProvisionedProductType": "string",
      "ProvisioningArtifactId": "string",
      "RecordErrors": [
         {
            "Code": "string",
            "Description": "string"
         }
      ],
      "RecordId": "string",
      "RecordTags": [
         {
            "Key": "string",
            "Value": "string"
         }
      ],
      "RecordType": "string",
      "Status": "string",
      "UpdatedTime": number
   },
   "RecordOutputs": [
      {
         "Description": "string",
         "OutputKey": "string",
         "OutputValue": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeRecord_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextPageToken](#API_DescribeRecord_ResponseSyntax) **   <a name="servicecatalog-DescribeRecord-response-NextPageToken"></a>
The page token to use to retrieve the next set of results. If there are no additional results, this value is null.
Type: String
Length Constraints: Maximum length of 2024.
Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

 ** [RecordDetail](#API_DescribeRecord_ResponseSyntax) **   <a name="servicecatalog-DescribeRecord-response-RecordDetail"></a>
Information about the product.
Type: [RecordDetail](API_RecordDetail.md) object

 ** [RecordOutputs](#API_DescribeRecord_ResponseSyntax) **   <a name="servicecatalog-DescribeRecord-response-RecordOutputs"></a>
Information about the product created as the result of a request. For example, the output for a CloudFormation-backed product that creates an S3 bucket would include the S3 bucket URL.
Type: Array of [RecordOutput](API_RecordOutput.md) objects

## Errors
<a name="API_DescribeRecord_Errors"></a>

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeRecord_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/DescribeRecord)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/DescribeRecord)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/DescribeRecord)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/DescribeRecord)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/DescribeRecord)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DescribeRecord)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/DescribeRecord)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/DescribeRecord)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/DescribeRecord)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/DescribeRecord)
