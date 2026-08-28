---
source_url: https://docs.aws.amazon.com/healthlake/latest/APIReference/API_DeleteFHIRDatastore.html
---

# DeleteFHIRDatastore
<a name="API_DeleteFHIRDatastore"></a>

Delete a FHIR-enabled data store.

## Request Syntax
<a name="API_DeleteFHIRDatastore_RequestSyntax"></a>

```
{
   "DatastoreId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteFHIRDatastore_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DatastoreId](#API_DeleteFHIRDatastore_RequestSyntax) **   <a name="HealthLake-DeleteFHIRDatastore-request-DatastoreId"></a>
 The AWS-generated identifier for the data store to be deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)`
Required: Yes

## Response Syntax
<a name="API_DeleteFHIRDatastore_ResponseSyntax"></a>

```
{
   "DatastoreArn": "string",
   "DatastoreEndpoint": "string",
   "DatastoreId": "string",
   "DatastoreStatus": "string"
}
```

## Response Elements
<a name="API_DeleteFHIRDatastore_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DatastoreArn](#API_DeleteFHIRDatastore_ResponseSyntax) **   <a name="HealthLake-DeleteFHIRDatastore-response-DatastoreArn"></a>
The Amazon Resource Name (ARN) that grants access permission to AWS HealthLake.
Type: String
Pattern: `arn:aws((-us-gov)|(-iso)|(-iso-b)|(-cn))?:healthlake:[a-zA-Z0-9-]+:[0-9]{12}:datastore/.+?`

 ** [DatastoreEndpoint](#API_DeleteFHIRDatastore_ResponseSyntax) **   <a name="HealthLake-DeleteFHIRDatastore-response-DatastoreEndpoint"></a>
The AWS endpoint of the data store to be deleted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 5000.
Pattern: `[\P{M}\p{M}]{1,5000}`

 ** [DatastoreId](#API_DeleteFHIRDatastore_ResponseSyntax) **   <a name="HealthLake-DeleteFHIRDatastore-response-DatastoreId"></a>
The AWS-generated ID for the deleted data store.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `([\p{L}\p{Z}\p{N}_.:/=+\-%@]*)`

 ** [DatastoreStatus](#API_DeleteFHIRDatastore_ResponseSyntax) **   <a name="HealthLake-DeleteFHIRDatastore-response-DatastoreStatus"></a>
The data store status.
Type: String
Valid Values: `CREATING | ACTIVE | DELETING | DELETED | CREATE_FAILED | UPDATING | UPDATE_FAILED`

## Errors
<a name="API_DeleteFHIRDatastore_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access is denied. Your account is not authorized to perform this operation.
HTTP Status Code: 400

 ** ConflictException **
The data store is in a transition state and the user requested action cannot be performed.
HTTP Status Code: 400

 ** InternalServerException **
An unknown internal error occurred in the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested data store was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The user has exceeded their maximum number of allowed calls to the given API.
HTTP Status Code: 400

 ** ValidationException **
The user input parameter was invalid.
HTTP Status Code: 400

## See Also
<a name="API_DeleteFHIRDatastore_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/healthlake-2017-07-01/DeleteFHIRDatastore)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/healthlake-2017-07-01/DeleteFHIRDatastore)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/healthlake-2017-07-01/DeleteFHIRDatastore)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/healthlake-2017-07-01/DeleteFHIRDatastore)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/healthlake-2017-07-01/DeleteFHIRDatastore)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/healthlake-2017-07-01/DeleteFHIRDatastore)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/healthlake-2017-07-01/DeleteFHIRDatastore)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/healthlake-2017-07-01/DeleteFHIRDatastore)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/healthlake-2017-07-01/DeleteFHIRDatastore)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/healthlake-2017-07-01/DeleteFHIRDatastore)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthLake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthlake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
