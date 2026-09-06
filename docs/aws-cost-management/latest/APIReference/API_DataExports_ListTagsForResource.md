---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DataExports_ListTagsForResource.html
---

# ListTagsForResource
<a name="API_DataExports_ListTagsForResource"></a>

List tags associated with an existing data export.

## Request Syntax
<a name="API_DataExports_ListTagsForResource_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DataExports_ListTagsForResource_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_DataExports_ListTagsForResource_RequestSyntax) **   <a name="awscostmanagement-DataExports_ListTagsForResource-request-MaxResults"></a>
The maximum number of objects that are returned for the request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 300.
Required: No

 ** [NextToken](#API_DataExports_ListTagsForResource_RequestSyntax) **   <a name="awscostmanagement-DataExports_ListTagsForResource-request-NextToken"></a>
The token to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`
Required: No

 ** [ResourceArn](#API_DataExports_ListTagsForResource_RequestSyntax) **   <a name="awscostmanagement-DataExports_ListTagsForResource-request-ResourceArn"></a>
The unique identifier for the resource.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z0-9]*:(bcm-data-exports):[-a-z0-9]*:[0-9]{12}:[-a-zA-Z0-9/:_]+`
Required: Yes

## Response Syntax
<a name="API_DataExports_ListTagsForResource_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "ResourceTags": [
      {
         "Key": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DataExports_ListTagsForResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DataExports_ListTagsForResource_ResponseSyntax) **   <a name="awscostmanagement-DataExports_ListTagsForResource-response-NextToken"></a>
The token to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `[\S\s]*`

 ** [ResourceTags](#API_DataExports_ListTagsForResource_ResponseSyntax) **   <a name="awscostmanagement-DataExports_ListTagsForResource-response-ResourceTags"></a>
An optional list of tags to associate with the specified export. Each tag consists of a key and a value, and each key must be unique for the resource.
Type: Array of [ResourceTag](API_DataExports_ResourceTag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.

## Errors
<a name="API_DataExports_ListTagsForResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
An error on the server occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified Amazon Resource Name (ARN) in the request doesn't exist.
 ** ResourceId **
The identifier of the resource that was not found.
 ** ResourceType **
The type of the resource that was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
 ** QuotaCode **
The quota code that exceeded the throttling limit.
 ** ServiceCode **
The service code that exceeded the throttling limit. It will always be “AWSBillingAndCostManagementDataExports”.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** Fields **
The list of fields that are invalid.
 ** Reason **
The reason for the validation exception.
HTTP Status Code: 400

## Examples
<a name="API_DataExports_ListTagsForResource_Examples"></a>

### The following is a sample request of the ListTagsForResource operation.
<a name="API_DataExports_ListTagsForResource_Example_1"></a>

This example illustrates one usage of ListTagsForResource.

#### Sample Request
<a name="API_DataExports_ListTagsForResource_Example_1_Request"></a>

```
{
  "ResourceArn": "arn:aws:bcm-data-exports:::export:Example/837fcfce-f85b-4600-b333-b38a12c3a927"
}
```

### The following is a sample response of the ListTagsForResource operation.
<a name="API_DataExports_ListTagsForResource_Example_2"></a>

This example illustrates one usage of ListTagsForResource.

#### Sample Response
<a name="API_DataExports_ListTagsForResource_Example_2_Response"></a>

```
{
  "ResourceTags": [
    {
      "Key": "YourTagKey",
      "Value": "YourTagValue"
    }
  ]
}
```

## See Also
<a name="API_DataExports_ListTagsForResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/bcm-data-exports-2023-11-26/ListTagsForResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/bcm-data-exports-2023-11-26/ListTagsForResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/bcm-data-exports-2023-11-26/ListTagsForResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/bcm-data-exports-2023-11-26/ListTagsForResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/bcm-data-exports-2023-11-26/ListTagsForResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/bcm-data-exports-2023-11-26/ListTagsForResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/bcm-data-exports-2023-11-26/ListTagsForResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/bcm-data-exports-2023-11-26/ListTagsForResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/bcm-data-exports-2023-11-26/ListTagsForResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/bcm-data-exports-2023-11-26/ListTagsForResource)
