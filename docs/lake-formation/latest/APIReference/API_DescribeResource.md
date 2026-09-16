---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_DescribeResource.html
---

# DescribeResource
<a name="API_DescribeResource"></a>

Retrieves the current data access role for the given resource registered in AWS Lake Formation.

## Request Syntax
<a name="API_DescribeResource_RequestSyntax"></a>

```
POST /DescribeResource HTTP/1.1
Content-type: application/json

{
   "ResourceArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DescribeResource_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_DescribeResource_RequestSyntax) **   <a name="lakeformation-DescribeResource-request-ResourceArn"></a>
The resource ARN.
Type: String
Required: Yes

## Response Syntax
<a name="API_DescribeResource_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ResourceInfo": {
      "ExpectedResourceOwnerAccount": "string",
      "HybridAccessEnabled": boolean,
      "LastModified": number,
      "ResourceArn": "string",
      "RoleArn": "string",
      "VerificationStatus": "string",
      "WithFederation": boolean,
      "WithPrivilegedAccess": boolean
   }
}
```

## Response Elements
<a name="API_DescribeResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ResourceInfo](#API_DescribeResource_ResponseSyntax) **   <a name="lakeformation-DescribeResource-response-ResourceInfo"></a>
A structure containing information about an Lake Formation resource.
Type: [ResourceInfo](API_ResourceInfo.md) object

## Errors
<a name="API_DescribeResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** EntityNotFoundException **
A specified entity does not exist.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** OperationTimeoutException **
The operation timed out.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## See Also
<a name="API_DescribeResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/DescribeResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/DescribeResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/DescribeResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/DescribeResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/DescribeResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/DescribeResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/DescribeResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/DescribeResource)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/DescribeResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/DescribeResource)
