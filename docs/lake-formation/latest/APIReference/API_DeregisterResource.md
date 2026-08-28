---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_DeregisterResource.html
---

# DeregisterResource
<a name="API_DeregisterResource"></a>

Deregisters the resource as managed by the Data Catalog.

When you deregister a path, Lake Formation removes the path from the inline policy attached to your service-linked role.

## Request Syntax
<a name="API_DeregisterResource_RequestSyntax"></a>

```
POST /DeregisterResource HTTP/1.1
Content-type: application/json

{
   "ResourceArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeregisterResource_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeregisterResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_DeregisterResource_RequestSyntax) **   <a name="lakeformation-DeregisterResource-request-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource that you want to deregister.
Type: String
Required: Yes

## Response Syntax
<a name="API_DeregisterResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeregisterResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeregisterResource_Errors"></a>

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
<a name="API_DeregisterResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/DeregisterResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/DeregisterResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/DeregisterResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/DeregisterResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/DeregisterResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/DeregisterResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/DeregisterResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/DeregisterResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/DeregisterResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/DeregisterResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
