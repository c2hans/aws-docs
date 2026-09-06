---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_DeleteProjectMembership.html
---

# DeleteProjectMembership
<a name="API_DeleteProjectMembership"></a>

Deletes project membership in Amazon DataZone.

## Request Syntax
<a name="API_DeleteProjectMembership_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/projects/{{projectIdentifier}}/deleteMembership HTTP/1.1
Content-type: application/json

{
   "member": { ... }
}
```

## URI Request Parameters
<a name="API_DeleteProjectMembership_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_DeleteProjectMembership_RequestSyntax) **   <a name="datazone-DeleteProjectMembership-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain where project membership is deleted.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [projectIdentifier](#API_DeleteProjectMembership_RequestSyntax) **   <a name="datazone-DeleteProjectMembership-request-uri-projectIdentifier"></a>
The ID of the Amazon DataZone project the membership to which is deleted.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_DeleteProjectMembership_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [member](#API_DeleteProjectMembership_RequestSyntax) **   <a name="datazone-DeleteProjectMembership-request-member"></a>
The project member whose project membership is deleted.
Type: [Member](API_Member.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_DeleteProjectMembership_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteProjectMembership_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteProjectMembership_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request has exceeded the specified service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## See Also
<a name="API_DeleteProjectMembership_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/DeleteProjectMembership)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/DeleteProjectMembership)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/DeleteProjectMembership)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/DeleteProjectMembership)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/DeleteProjectMembership)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/DeleteProjectMembership)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/DeleteProjectMembership)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/DeleteProjectMembership)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/DeleteProjectMembership)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/DeleteProjectMembership)
