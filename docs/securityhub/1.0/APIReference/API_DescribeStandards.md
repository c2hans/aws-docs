---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeStandards.html
---

# DescribeStandards
<a name="API_DescribeStandards"></a>

Returns a list of the available standards in Security Hub CSPM.

For each standard, the results include the standard ARN, the name, and a description.

## Request Syntax
<a name="API_DescribeStandards_RequestSyntax"></a>

```
GET /standards?MaxResults={{MaxResults}}&NextToken={{NextToken}}&Providers={{Providers}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeStandards_RequestParameters"></a>

The request uses the following URI parameters.

 ** [MaxResults](#API_DescribeStandards_RequestSyntax) **   <a name="securityhub-DescribeStandards-request-uri-MaxResults"></a>
The maximum number of standards to return.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_DescribeStandards_RequestSyntax) **   <a name="securityhub-DescribeStandards-request-uri-NextToken"></a>
The token that is required for pagination. On your first call to the `DescribeStandards` operation, set the value of this parameter to `NULL`.
For subsequent calls to the operation, to continue listing data, set the value of this parameter to the value returned from the previous response.

 ** [Providers](#API_DescribeStandards_RequestSyntax) **   <a name="securityhub-DescribeStandards-request-uri-Providers"></a>
A list of cloud providers to filter the standards by. For example, specify `Azure` to return only standards that evaluate Azure resources.
Valid Values: `AWS | Azure`

## Request Body
<a name="API_DescribeStandards_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeStandards_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "NextToken": "string",
   "Standards": [
      {
         "Description": "string",
         "EnabledByDefault": boolean,
         "Name": "string",
         "Provider": "string",
         "StandardsArn": "string",
         "StandardsManagedBy": {
            "Company": "string",
            "Product": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_DescribeStandards_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeStandards_ResponseSyntax) **   <a name="securityhub-DescribeStandards-response-NextToken"></a>
The pagination token to use to request the next page of results.
Type: String

 ** [Standards](#API_DescribeStandards_ResponseSyntax) **   <a name="securityhub-DescribeStandards-response-Standards"></a>
A list of available standards.
Type: Array of [Standard](API_Standard.md) objects

## Errors
<a name="API_DescribeStandards_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

## See Also
<a name="API_DescribeStandards_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/DescribeStandards)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/DescribeStandards)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/DescribeStandards)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/DescribeStandards)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/DescribeStandards)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/DescribeStandards)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/DescribeStandards)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/DescribeStandards)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/DescribeStandards)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/DescribeStandards)
