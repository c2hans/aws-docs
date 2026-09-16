---
source_url: https://docs.aws.amazon.com/awsconsolehelpdocs/latest/APIReference/API_ListServices.html
---

# ListServices
<a name="API_ListServices"></a>

Returns a paginated list of AWS service identifiers that you can use as values for the `visibleServices` setting in [UpdateAccountCustomizations](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/APIReference/API_UpdateAccountCustomizations.html). The available services vary by AWS partition. Use pagination to retrieve all results.

**Note**
The `visibleServices` setting controls only the appearance of services in the AWS Management Console. It does not restrict access through the AWS CLI, SDKs, or other APIs.

## Request Syntax
<a name="API_ListServices_RequestSyntax"></a>

```
GET /v1/services?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListServices_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListServices_RequestSyntax) **   <a name="uxc-ListServices-request-uri-maxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 1000.

 ** [nextToken](#API_ListServices_RequestSyntax) **   <a name="uxc-ListServices-request-uri-nextToken"></a>
The token for retrieving the next page of results. Use the `nextToken` value from a previous response.
Length Constraints: Minimum length of 32. Maximum length of 512.
Pattern: `[-A-Za-z0-9+/_]+=*`

## Request Body
<a name="API_ListServices_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListServices_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "nextToken": "string",
   "services": [ "string" ]
}
```

## Response Elements
<a name="API_ListServices_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListServices_ResponseSyntax) **   <a name="uxc-ListServices-response-nextToken"></a>
The token for retrieving the next page of results. This value is `null` when no more results are available.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 512.
Pattern: `[-A-Za-z0-9+/_]+=*`

 ** [services](#API_ListServices_ResponseSyntax) **   <a name="uxc-ListServices-response-services"></a>
The list of available AWS service identifiers.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 500 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-z0-9]+(-[a-z0-9]+)*`

## Errors
<a name="API_ListServices_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation. Verify that your IAM policy includes the required `uxc:` permissions for the operation that you are calling. For more information on IAM permissions, see [AWS managed policies for AWS Management Console](https://docs.aws.amazon.com/awsconsolehelpdocs/latest/gsg/security-iam-awsmanpol.html).
HTTP Status Code: 403

 ** InternalServerException **
The service encountered an internal error. Try your request again later.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied because of request throttling. Reduce the frequency of your requests.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The list of fields that are invalid.
HTTP Status Code: 400

## Examples
<a name="API_ListServices_Examples"></a>

### List available service identifiers
<a name="API_ListServices_Example_1"></a>

The following example retrieves the first page of available service identifiers with a maximum of three results per page. The `nextToken` value in the response indicates that additional results are available.

#### Sample Request
<a name="API_ListServices_Example_1_Request"></a>

```
GET /v1/services?maxResults=3 HTTP/1.1
Host: uxc.us-east-1.amazonaws.com
Content-type: application/json
```

#### Sample Response
<a name="API_ListServices_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-type: application/json

{
   "services": ["dynamodb", "ec2", "fargate"],
   "nextToken": "eyJpZCI6MTIzfQ=="
}
```

## See Also
<a name="API_ListServices_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/uxc-2024-07-01/ListServices)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/uxc-2024-07-01/ListServices)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/uxc-2024-07-01/ListServices)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/uxc-2024-07-01/ListServices)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/uxc-2024-07-01/ListServices)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/uxc-2024-07-01/ListServices)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/uxc-2024-07-01/ListServices)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/uxc-2024-07-01/ListServices)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/uxc-2024-07-01/ListServices)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/uxc-2024-07-01/ListServices)
