---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_CreateSourceNetwork.html
---

# CreateSourceNetwork
<a name="API_CreateSourceNetwork"></a>

Create a new Source Network resource for a provided VPC ID.

## Request Syntax
<a name="API_CreateSourceNetwork_RequestSyntax"></a>

```
POST /CreateSourceNetwork HTTP/1.1
Content-type: application/json

{
   "originAccountID": "{{string}}",
   "originRegion": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "vpcID": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateSourceNetwork_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateSourceNetwork_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [originAccountID](#API_CreateSourceNetwork_RequestSyntax) **   <a name="drs-CreateSourceNetwork-request-originAccountID"></a>
Account containing the VPC to protect.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: Yes

 ** [originRegion](#API_CreateSourceNetwork_RequestSyntax) **   <a name="drs-CreateSourceNetwork-request-originRegion"></a>
Region containing the VPC to protect.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `(us(-gov)?|ap|ca|cn|eu|eusc|sa|af|me|mx|il)-([a-z]{2}-)?(central|north|(north(?:east|west))|south|south(?:east|west)|east|west)-[0-9]`
Required: Yes

 ** [tags](#API_CreateSourceNetwork_RequestSyntax) **   <a name="drs-CreateSourceNetwork-request-tags"></a>
A set of tags to be associated with the Source Network resource.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [vpcID](#API_CreateSourceNetwork_RequestSyntax) **   <a name="drs-CreateSourceNetwork-request-vpcID"></a>
Which VPC ID to protect.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 21.
Pattern: `vpc-[0-9a-fA-F]{8,}`
Required: Yes

## Response Syntax
<a name="API_CreateSourceNetwork_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "sourceNetworkID": "string"
}
```

## Response Elements
<a name="API_CreateSourceNetwork_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [sourceNetworkID](#API_CreateSourceNetwork_ResponseSyntax) **   <a name="drs-CreateSourceNetwork-response-sourceNetworkID"></a>
ID of the created Source Network.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `sn-[0-9a-zA-Z]{17}`

## Errors
<a name="API_CreateSourceNetwork_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the target resource.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 409

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource for this operation was not found.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request could not be completed because its exceeded the service quota.
 ** quotaCode **
Quota code.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
 ** serviceCode **
Service code.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
Quota code.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
 ** serviceCode **
Service code.
HTTP Status Code: 429

 ** UninitializedAccountException **
The account performing the request has not been initialized.
HTTP Status Code: 400

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
Validation exception reason.
HTTP Status Code: 400

## See Also
<a name="API_CreateSourceNetwork_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/CreateSourceNetwork)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/CreateSourceNetwork)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/CreateSourceNetwork)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/CreateSourceNetwork)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/CreateSourceNetwork)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/CreateSourceNetwork)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/CreateSourceNetwork)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/CreateSourceNetwork)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/CreateSourceNetwork)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/CreateSourceNetwork)
