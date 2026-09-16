---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_DeleteJob.html
---

# DeleteJob
<a name="API_DeleteJob"></a>

Deletes a single Job by ID.

## Request Syntax
<a name="API_DeleteJob_RequestSyntax"></a>

```
POST /DeleteJob HTTP/1.1
Content-type: application/json

{
   "accountID": "{{string}}",
   "jobID": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteJob_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteJob_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountID](#API_DeleteJob_RequestSyntax) **   <a name="mgn-DeleteJob-request-accountID"></a>
Request to delete Job from service by Account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

 ** [jobID](#API_DeleteJob_RequestSyntax) **   <a name="mgn-DeleteJob-request-jobID"></a>
Request to delete Job from service by Job ID.
Type: String
Length Constraints: Fixed length of 24.
Pattern: `mgnjob-[0-9a-zA-Z]{17}`
Required: Yes

## Response Syntax
<a name="API_DeleteJob_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteJob_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteJob_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the target resource.
 ** errors **
Conflict Exception specific errors.
 ** resourceId **
A conflict occurred when prompting for the Resource ID.
 ** resourceType **
A conflict occurred when prompting for resource type.
HTTP Status Code: 409

 ** ResourceNotFoundException **
Resource not found exception.
 ** resourceId **
Resource ID not found error.
 ** resourceType **
Resource type not found error.
HTTP Status Code: 404

 ** UninitializedAccountException **
Uninitialized account exception.
HTTP Status Code: 400

## See Also
<a name="API_DeleteJob_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/DeleteJob)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/DeleteJob)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/DeleteJob)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/DeleteJob)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/DeleteJob)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/DeleteJob)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/DeleteJob)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/DeleteJob)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/DeleteJob)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/DeleteJob)
