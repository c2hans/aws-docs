---
source_url: https://docs.aws.amazon.com/textract/latest/APIReference/API_ListBlueprints.html
---

# ListBlueprints

Lists the blueprints that are available to the caller, with optional filtering by project and resource owner. The results are paginated. If the response includes a `NextToken` value, pass it in a subsequent call to retrieve the next page of results.

## Request Syntax
<a name="API_ListBlueprints_RequestSyntax"></a>

```
{
   "BlueprintArn": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "ProjectFilter": {
      "ProjectArn": "{{string}}"
   },
   "ResourceOwner": "{{string}}"
}
```

## Request Parameters
<a name="API_ListBlueprints_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [BlueprintArn](#API_ListBlueprints_RequestSyntax) **   <a name="Textract-ListBlueprints-request-BlueprintArn"></a>
The Amazon Resource Name (ARN) of a blueprint to filter the results by.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^arn:aws(|-cn|-iso|-iso-[a-z]|-us-gov):textract:[a-zA-Z0-9-]*:(aws|[0-9]{12}):blueprint/(public-[a-zA-Z0-9-_]{1,30}|[a-zA-Z0-9-]{12,36})$`
Required: No

 ** [MaxResults](#API_ListBlueprints_RequestSyntax) **   <a name="Textract-ListBlueprints-request-MaxResults"></a>
The maximum number of blueprints to return in each page of results. If you don't specify a value, the service selects a default page size. Use the `NextToken` value in the response to retrieve any remaining results.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** [NextToken](#API_ListBlueprints_RequestSyntax) **   <a name="Textract-ListBlueprints-request-NextToken"></a>
A pagination token returned from a previous call to `ListBlueprints`. Use it to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*\S.*`
Required: No

 ** [ProjectFilter](#API_ListBlueprints_RequestSyntax) **   <a name="Textract-ListBlueprints-request-ProjectFilter"></a>
A filter that limits the results to blueprints associated with the specified project.
Type: [ProjectFilter](API_ProjectFilter.md) object
Required: No

 ** [ResourceOwner](#API_ListBlueprints_RequestSyntax) **   <a name="Textract-ListBlueprints-request-ResourceOwner"></a>
A filter that limits the results to blueprints owned by your account or to blueprints provided by Amazon Textract.
Type: String
Valid Values: `ACCOUNT | SERVICE`
Required: No

## Response Syntax
<a name="API_ListBlueprints_ResponseSyntax"></a>

```
{
   "Blueprints": [
      {
         "BlueprintArn": "string",
         "BlueprintName": "string",
         "BlueprintVersion": "string",
         "CreationTime": number,
         "LastModifiedTime": number,
         "ResourceOwner": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListBlueprints_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Blueprints](#API_ListBlueprints_ResponseSyntax) **   <a name="Textract-ListBlueprints-response-Blueprints"></a>
A list of blueprint summaries that match the request.
Type: Array of [BlueprintSummary](API_BlueprintSummary.md) objects

 ** [NextToken](#API_ListBlueprints_ResponseSyntax) **   <a name="Textract-ListBlueprints-response-NextToken"></a>
A pagination token to use in a subsequent call to `ListBlueprints` to retrieve the next page of results. This value is `null` when there are no more results to return.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `.*\S.*`

## Errors
<a name="API_ListBlueprints_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You aren't authorized to perform the action. Use the Amazon Resource Name (ARN) of an authorized user or IAM role to perform the operation.
HTTP Status Code: 400

 ** InternalServerError **
Amazon Textract experienced a service issue. Try your call again.
HTTP Status Code: 500

 ** InvalidParameterException **
An input parameter violated a constraint. For example, in synchronous operations, an `InvalidParameterException` exception occurs when neither of the `S3Object` or `Bytes` values are supplied in the `Document` request parameter. Validate your parameter before calling the API operation again.
HTTP Status Code: 400

 ** ProvisionedThroughputExceededException **
The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Textract.
HTTP Status Code: 400

 ** ResourceNotFoundException **
 Returned when an operation tried to access a nonexistent resource.
HTTP Status Code: 400

 ** ValidationException **
 Indicates that a request was not valid. Check request for proper formatting.
HTTP Status Code: 400

## See Also
<a name="API_ListBlueprints_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/textract-2018-06-27/ListBlueprints)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/textract-2018-06-27/ListBlueprints)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/textract-2018-06-27/ListBlueprints)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/textract-2018-06-27/ListBlueprints)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/textract-2018-06-27/ListBlueprints)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/textract-2018-06-27/ListBlueprints)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/textract-2018-06-27/ListBlueprints)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/textract-2018-06-27/ListBlueprints)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/textract-2018-06-27/ListBlueprints)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/textract-2018-06-27/ListBlueprints)
