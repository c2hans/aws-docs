---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_UpdateAnalysisPermissions.html
---

# UpdateAnalysisPermissions
<a name="API_UpdateAnalysisPermissions"></a>

Updates the read and write permissions for an analysis.

## Request Syntax
<a name="API_UpdateAnalysisPermissions_RequestSyntax"></a>

```
PUT /accounts/{{AwsAccountId}}/analyses/{{AnalysisId}}/permissions HTTP/1.1
Content-type: application/json

{
   "GrantPermissions": [
      {
         "Actions": [ "{{string}}" ],
         "Principal": "{{string}}"
      }
   ],
   "RevokePermissions": [
      {
         "Actions": [ "{{string}}" ],
         "Principal": "{{string}}"
      }
   ]
}
```

## URI Request Parameters
<a name="API_UpdateAnalysisPermissions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AnalysisId](#API_UpdateAnalysisPermissions_RequestSyntax) **   <a name="QS-UpdateAnalysisPermissions-request-uri-AnalysisId"></a>
The ID of the analysis whose permissions you're updating. The ID is part of the analysis URL.
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`
Required: Yes

 ** [AwsAccountId](#API_UpdateAnalysisPermissions_RequestSyntax) **   <a name="QS-UpdateAnalysisPermissions-request-uri-AwsAccountId"></a>
The ID of the AWS account that contains the analysis whose permissions you're updating. You must be using the AWS account that the analysis is in.
Length Constraints: Fixed length of 12.
Pattern: `^[0-9]{12}$`
Required: Yes

## Request Body
<a name="API_UpdateAnalysisPermissions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [GrantPermissions](#API_UpdateAnalysisPermissions_RequestSyntax) **   <a name="QS-UpdateAnalysisPermissions-request-GrantPermissions"></a>
A structure that describes the permissions to add and the principal to add them to.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Maximum number of 100 items.
Required: No

 ** [RevokePermissions](#API_UpdateAnalysisPermissions_RequestSyntax) **   <a name="QS-UpdateAnalysisPermissions-request-RevokePermissions"></a>
A structure that describes the permissions to remove and the principal to remove them from.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Maximum number of 100 items.
Required: No

## Response Syntax
<a name="API_UpdateAnalysisPermissions_ResponseSyntax"></a>

```
HTTP/1.1 {{Status}}
Content-type: application/json

{
   "AnalysisArn": "string",
   "AnalysisId": "string",
   "Permissions": [
      {
         "Actions": [ "string" ],
         "Principal": "string"
      }
   ],
   "RequestId": "string"
}
```

## Response Elements
<a name="API_UpdateAnalysisPermissions_ResponseElements"></a>

If the action is successful, the service sends back the following HTTP response.

 ** [Status](#API_UpdateAnalysisPermissions_ResponseSyntax) **   <a name="QS-UpdateAnalysisPermissions-response-Status"></a>
The HTTP status of the request.

The following data is returned in JSON format by the service.

 ** [AnalysisArn](#API_UpdateAnalysisPermissions_ResponseSyntax) **   <a name="QS-UpdateAnalysisPermissions-response-AnalysisArn"></a>
The Amazon Resource Name (ARN) of the analysis that you updated.
Type: String

 ** [AnalysisId](#API_UpdateAnalysisPermissions_ResponseSyntax) **   <a name="QS-UpdateAnalysisPermissions-response-AnalysisId"></a>
The ID of the analysis that you updated permissions for.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\w\-]+`

 ** [Permissions](#API_UpdateAnalysisPermissions_ResponseSyntax) **   <a name="QS-UpdateAnalysisPermissions-response-Permissions"></a>
A structure that describes the principals and the resource-level permissions on an analysis.
Type: Array of [ResourcePermission](API_ResourcePermission.md) objects
Array Members: Maximum number of 100 items.

 ** [RequestId](#API_UpdateAnalysisPermissions_ResponseSyntax) **   <a name="QS-UpdateAnalysisPermissions-response-RequestId"></a>
The AWS request ID for this operation.
Type: String

## Errors
<a name="API_UpdateAnalysisPermissions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 409

 ** InternalFailureException **
An internal failure occurred.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 500

 ** InvalidParameterValueException **
One or more parameters has a value that isn't valid.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 400

 ** LimitExceededException **
A limit is exceeded.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
Limit exceeded.
HTTP Status Code: 409

 ** ResourceNotFoundException **
One or more resources can't be found.
 ** RequestId **
The AWS request ID for this request.
 ** ResourceType **
The resource type for this request.
HTTP Status Code: 404

 ** ThrottlingException **
Access is throttled.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 429

 ** UnsupportedUserEditionException **
This error indicates that you are calling an operation on an Amazon Quick Suite subscription where the edition doesn't include support for that operation. Amazon Quick Suite currently has Standard Edition and Enterprise Edition. Not every operation and capability is available in every edition.
 ** RequestId **
The AWS request ID for this request.
HTTP Status Code: 403

## See Also
<a name="API_UpdateAnalysisPermissions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/quicksight-2018-04-01/UpdateAnalysisPermissions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/quicksight-2018-04-01/UpdateAnalysisPermissions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/UpdateAnalysisPermissions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/quicksight-2018-04-01/UpdateAnalysisPermissions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/UpdateAnalysisPermissions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/quicksight-2018-04-01/UpdateAnalysisPermissions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/quicksight-2018-04-01/UpdateAnalysisPermissions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/quicksight-2018-04-01/UpdateAnalysisPermissions)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/quicksight-2018-04-01/UpdateAnalysisPermissions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/UpdateAnalysisPermissions)
