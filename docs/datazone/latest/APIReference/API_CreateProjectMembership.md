---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_CreateProjectMembership.html
---

# CreateProjectMembership
<a name="API_CreateProjectMembership"></a>

Creates a project membership in Amazon DataZone.

## Request Syntax
<a name="API_CreateProjectMembership_RequestSyntax"></a>

```
POST /v2/domains/{{domainIdentifier}}/projects/{{projectIdentifier}}/createMembership HTTP/1.1
Content-type: application/json

{
   "designation": "{{string}}",
   "member": { ... }
}
```

## URI Request Parameters
<a name="API_CreateProjectMembership_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_CreateProjectMembership_RequestSyntax) **   <a name="datazone-CreateProjectMembership-request-uri-domainIdentifier"></a>
The ID of the Amazon DataZone domain in which project membership is created.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [projectIdentifier](#API_CreateProjectMembership_RequestSyntax) **   <a name="datazone-CreateProjectMembership-request-uri-projectIdentifier"></a>
The ID of the project for which this project membership was created.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

## Request Body
<a name="API_CreateProjectMembership_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [designation](#API_CreateProjectMembership_RequestSyntax) **   <a name="datazone-CreateProjectMembership-request-designation"></a>
The designation of the project membership.
Type: String
Valid Values: `PROJECT_OWNER | PROJECT_CONTRIBUTOR | PROJECT_CATALOG_VIEWER | PROJECT_CATALOG_CONSUMER | PROJECT_CATALOG_STEWARD`
Required: Yes

 ** [member](#API_CreateProjectMembership_RequestSyntax) **   <a name="datazone-CreateProjectMembership-request-member"></a>
The project member whose project membership was created.
Type: [Member](API_Member.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

## Response Syntax
<a name="API_CreateProjectMembership_ResponseSyntax"></a>

```
HTTP/1.1 201
```

## Response Elements
<a name="API_CreateProjectMembership_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response with an empty HTTP body.

## Errors
<a name="API_CreateProjectMembership_Errors"></a>

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
<a name="API_CreateProjectMembership_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/CreateProjectMembership)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/CreateProjectMembership)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/CreateProjectMembership)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/CreateProjectMembership)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/CreateProjectMembership)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/CreateProjectMembership)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/CreateProjectMembership)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/CreateProjectMembership)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/CreateProjectMembership)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/CreateProjectMembership)
