---
source_url: https://docs.aws.amazon.com/incident-manager/latest/APIReference/API_CreateReplicationSet.html
---

# CreateReplicationSet
<a name="API_CreateReplicationSet"></a>

**Important**
 AWS Systems Manager Incident Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Incident Manager availability change](https://docs.aws.amazon.com/incident-manager/latest/userguide/incident-manager-availability-change.html).

A replication set replicates and encrypts your data to the provided Regions with the provided AWS KMS key.

## Request Syntax
<a name="API_CreateReplicationSet_RequestSyntax"></a>

```
POST /createReplicationSet HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "regions": {
      "{{string}}" : {
         "sseKmsKeyId": "{{string}}"
      }
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateReplicationSet_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateReplicationSet_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateReplicationSet_RequestSyntax) **   <a name="IncidentManager-CreateReplicationSet-request-clientToken"></a>
A token that ensures that the operation is called only once with the specified details.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** [regions](#API_CreateReplicationSet_RequestSyntax) **   <a name="IncidentManager-CreateReplicationSet-request-regions"></a>
The Regions that Incident Manager replicates your data to. You can have up to three Regions in your replication set.
Type: String to [RegionMapInputValue](API_RegionMapInputValue.md) object map
Map Entries: Maximum number of 3 items.
Key Length Constraints: Minimum length of 0. Maximum length of 20.
Required: Yes

 ** [tags](#API_CreateReplicationSet_RequestSyntax) **   <a name="IncidentManager-CreateReplicationSet-request-tags"></a>
A list of tags to add to the replication set.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `(?!aws:)[A-Za-z0-9 _=@:.+-/]+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `[A-Za-z0-9 _=@:.+-/]*`
Required: No

## Response Syntax
<a name="API_CreateReplicationSet_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "arn": "string"
}
```

## Response Elements
<a name="API_CreateReplicationSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateReplicationSet_ResponseSyntax) **   <a name="IncidentManager-CreateReplicationSet-response-arn"></a>
The Amazon Resource Name (ARN) of the replication set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.
Pattern: `arn:aws(-cn|-us-gov)?:[a-z0-9-]*:[a-z0-9-]*:([0-9]{12})?:.+`

## Errors
<a name="API_CreateReplicationSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this operation.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource causes an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
Request would cause a service quota to be exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## Examples
<a name="API_CreateReplicationSet_Examples"></a>

### Example
<a name="API_CreateReplicationSet_Example_1"></a>

This example illustrates one usage of CreateReplicationSet.

#### Sample Request
<a name="API_CreateReplicationSet_Example_1_Request"></a>

```
POST /createReplicationSet HTTP/1.1
Host: ssm-incidents.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.129-72.229.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/ssm-incidents.create-replication-set
X-Amz-Date: 20210810T210320Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210810/us-east-1/ssm-incidents/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 286

{
	"regions": {"us-east-1": {"sseKmsKeyId": "arn:aws:kms:us-east-1:111122223333:key/de6a2f4e-5d40-4443-ad82-1db179510a32"}, "us-east-2": {"sseKmsKeyId": "arn:aws:kms:us-east-2:111122223333:key/6f1572c9-05ca-43cf-bf03-ee7bc93f59bd"}},
	"clientToken": "aa1b2cde-27e3-42ff-9cac-99380EXAMPLE"
}
```

#### Sample Response
<a name="API_CreateReplicationSet_Example_1_Response"></a>

```
{
	"arn":"arn:aws:ssm-incidents::111122223333:replication-set/40bd98f0-4110-2dee-b35e-b87006f9e172"
}
```

## See Also
<a name="API_CreateReplicationSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ssm-incidents-2018-05-10/CreateReplicationSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ssm-incidents-2018-05-10/CreateReplicationSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-incidents-2018-05-10/CreateReplicationSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ssm-incidents-2018-05-10/CreateReplicationSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-incidents-2018-05-10/CreateReplicationSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ssm-incidents-2018-05-10/CreateReplicationSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ssm-incidents-2018-05-10/CreateReplicationSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ssm-incidents-2018-05-10/CreateReplicationSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ssm-incidents-2018-05-10/CreateReplicationSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-incidents-2018-05-10/CreateReplicationSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Incident Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query incident-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
