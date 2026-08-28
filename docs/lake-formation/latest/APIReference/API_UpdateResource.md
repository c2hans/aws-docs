---
source_url: https://docs.aws.amazon.com/lake-formation/latest/APIReference/API_UpdateResource.html
---

# UpdateResource
<a name="API_UpdateResource"></a>

Updates the data access role used for vending access to the given (registered) resource in AWS Lake Formation.

## Request Syntax
<a name="API_UpdateResource_RequestSyntax"></a>

```
POST /UpdateResource HTTP/1.1
Content-type: application/json

{
   "ExpectedResourceOwnerAccount": "{{string}}",
   "HybridAccessEnabled": {{boolean}},
   "ResourceArn": "{{string}}",
   "RoleArn": "{{string}}",
   "WithFederation": {{boolean}}
}
```

## URI Request Parameters
<a name="API_UpdateResource_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateResource_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ExpectedResourceOwnerAccount](#API_UpdateResource_RequestSyntax) **   <a name="lakeformation-UpdateResource-request-ExpectedResourceOwnerAccount"></a>
The AWS account that owns the AWS Glue tables associated with specific Amazon S3 locations.
Type: String
Pattern: `^\d{12}$`
Required: No

 ** [HybridAccessEnabled](#API_UpdateResource_RequestSyntax) **   <a name="lakeformation-UpdateResource-request-HybridAccessEnabled"></a>
 Specifies whether the data access of tables pointing to the location can be managed by both Lake Formation permissions as well as Amazon S3 bucket policies.
Type: Boolean
Required: No

 ** [ResourceArn](#API_UpdateResource_RequestSyntax) **   <a name="lakeformation-UpdateResource-request-ResourceArn"></a>
The resource ARN.
Type: String
Required: Yes

 ** [RoleArn](#API_UpdateResource_RequestSyntax) **   <a name="lakeformation-UpdateResource-request-RoleArn"></a>
The new role to use for the given resource registered in Lake Formation.
Type: String
Pattern: `arn:aws:iam::[0-9]*:role/.*`
Required: Yes

 ** [WithFederation](#API_UpdateResource_RequestSyntax) **   <a name="lakeformation-UpdateResource-request-WithFederation"></a>
Whether or not the resource is a federated resource.
Type: Boolean
Required: No

## Response Syntax
<a name="API_UpdateResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateResource_Errors"></a>

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
<a name="API_UpdateResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lakeformation-2017-03-31/UpdateResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lakeformation-2017-03-31/UpdateResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lakeformation-2017-03-31/UpdateResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lakeformation-2017-03-31/UpdateResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lakeformation-2017-03-31/UpdateResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lakeformation-2017-03-31/UpdateResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lakeformation-2017-03-31/UpdateResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lakeformation-2017-03-31/UpdateResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lakeformation-2017-03-31/UpdateResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lakeformation-2017-03-31/UpdateResource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Lake Formation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lake-formation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
