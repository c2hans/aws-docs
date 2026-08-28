---
source_url: https://docs.aws.amazon.com/servicecatalog/latest/APIReference/API_UpdateProvisionedProductProperties.html
---

# UpdateProvisionedProductProperties
<a name="API_UpdateProvisionedProductProperties"></a>

Requests updates to the properties of the specified provisioned product.

## Request Syntax
<a name="API_UpdateProvisionedProductProperties_RequestSyntax"></a>

```
{
   "AcceptLanguage": "{{string}}",
   "IdempotencyToken": "{{string}}",
   "ProvisionedProductId": "{{string}}",
   "ProvisionedProductProperties": {
      "{{string}}" : "{{string}}"
   }
}
```

## Request Parameters
<a name="API_UpdateProvisionedProductProperties_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [AcceptLanguage](#API_UpdateProvisionedProductProperties_RequestSyntax) **   <a name="servicecatalog-UpdateProvisionedProductProperties-request-AcceptLanguage"></a>
The language code.
+  `jp` - Japanese
+  `zh` - Chinese
Type: String
Length Constraints: Maximum length of 100.
Required: No

 ** [IdempotencyToken](#API_UpdateProvisionedProductProperties_RequestSyntax) **   <a name="servicecatalog-UpdateProvisionedProductProperties-request-IdempotencyToken"></a>
The idempotency token that uniquely identifies the provisioning product update request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`
Required: Yes

 ** [ProvisionedProductId](#API_UpdateProvisionedProductProperties_RequestSyntax) **   <a name="servicecatalog-UpdateProvisionedProductProperties-request-ProvisionedProductId"></a>
The identifier of the provisioned product.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`
Required: Yes

 ** [ProvisionedProductProperties](#API_UpdateProvisionedProductProperties_RequestSyntax) **   <a name="servicecatalog-UpdateProvisionedProductProperties-request-ProvisionedProductProperties"></a>
A map that contains the provisioned product properties to be updated.
The `LAUNCH_ROLE` key accepts role ARNs. This key allows an administrator to call `UpdateProvisionedProductProperties` to update the launch role that is associated with a provisioned product. This role is used when an end user calls a provisioning operation such as `UpdateProvisionedProduct`, `TerminateProvisionedProduct`, or `ExecuteProvisionedProductServiceAction`. Only a role ARN is valid. A user ARN is invalid.
The `OWNER` key accepts user ARNs, IAM role ARNs, and STS assumed-role ARNs. The owner is the user that has permission to see, update, terminate, and execute service actions in the provisioned product.
The administrator can change the owner of a provisioned product to another IAM or STS entity within the same account. Both end user owners and administrators can see ownership history of the provisioned product using the `ListRecordHistory` API. The new owner can describe all past records for the provisioned product using the `DescribeRecord` API. The previous owner can no longer use `DescribeRecord`, but can still see the product's history from when he was an owner using `ListRecordHistory`.
If a provisioned product ownership is assigned to an end user, they can see and perform any action through the API or AWS Service Catalog console such as update, terminate, and execute service actions. If an end user provisions a product and the owner is updated to someone else, they will no longer be able to see or perform any actions through API or the AWS Service Catalog console on that provisioned product.
Type: String to string map
Map Entries: Maximum number of 100 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Valid Keys: `OWNER | LAUNCH_ROLE`
Value Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: Yes

## Response Syntax
<a name="API_UpdateProvisionedProductProperties_ResponseSyntax"></a>

```
{
   "ProvisionedProductId": "string",
   "ProvisionedProductProperties": {
      "string" : "string"
   },
   "RecordId": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_UpdateProvisionedProductProperties_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ProvisionedProductId](#API_UpdateProvisionedProductProperties_ResponseSyntax) **   <a name="servicecatalog-UpdateProvisionedProductProperties-response-ProvisionedProductId"></a>
The provisioned product identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`

 ** [ProvisionedProductProperties](#API_UpdateProvisionedProductProperties_ResponseSyntax) **   <a name="servicecatalog-UpdateProvisionedProductProperties-response-ProvisionedProductProperties"></a>
A map that contains the properties updated.
Type: String to string map
Map Entries: Maximum number of 100 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Valid Keys: `OWNER | LAUNCH_ROLE`
Value Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [RecordId](#API_UpdateProvisionedProductProperties_ResponseSyntax) **   <a name="servicecatalog-UpdateProvisionedProductProperties-response-RecordId"></a>
The identifier of the record.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^[a-zA-Z0-9_\-]*`

 ** [Status](#API_UpdateProvisionedProductProperties_ResponseSyntax) **   <a name="servicecatalog-UpdateProvisionedProductProperties-response-Status"></a>
The status of the request.
Type: String
Valid Values: `CREATED | IN_PROGRESS | IN_PROGRESS_IN_ERROR | SUCCEEDED | FAILED`

## Errors
<a name="API_UpdateProvisionedProductProperties_Errors"></a>

 ** InvalidParametersException **
One or more parameters provided to the operation are not valid.
HTTP Status Code: 400

 ** InvalidStateException **
An attempt was made to modify a resource that is in a state that is not valid. Check your resources to ensure that they are in valid states before retrying the operation.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 400

## See Also
<a name="API_UpdateProvisionedProductProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/servicecatalog-2015-12-10/UpdateProvisionedProductProperties)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/servicecatalog-2015-12-10/UpdateProvisionedProductProperties)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/servicecatalog-2015-12-10/UpdateProvisionedProductProperties)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/servicecatalog-2015-12-10/UpdateProvisionedProductProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/servicecatalog-2015-12-10/UpdateProvisionedProductProperties)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/UpdateProvisionedProductProperties)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/servicecatalog-2015-12-10/UpdateProvisionedProductProperties)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/servicecatalog-2015-12-10/UpdateProvisionedProductProperties)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/servicecatalog-2015-12-10/UpdateProvisionedProductProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/servicecatalog-2015-12-10/UpdateProvisionedProductProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Service Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query servicecatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
