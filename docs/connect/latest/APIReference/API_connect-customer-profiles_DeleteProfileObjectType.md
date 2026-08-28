---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_DeleteProfileObjectType.html
---

# DeleteProfileObjectType
<a name="API_connect-customer-profiles_DeleteProfileObjectType"></a>

Removes a ProfileObjectType from a specific domain as well as removes all the ProfileObjects of that type. It also disables integrations from this specific ProfileObjectType. In addition, it scrubs all of the fields of the standard profile that were populated from this ProfileObjectType.

## Request Syntax
<a name="API_connect-customer-profiles_DeleteProfileObjectType_RequestSyntax"></a>

```
DELETE /domains/{{DomainName}}/object-types/{{ObjectTypeName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_DeleteProfileObjectType_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_DeleteProfileObjectType_RequestSyntax) **   <a name="connect-connect-customer-profiles_DeleteProfileObjectType-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [ObjectTypeName](#API_connect-customer-profiles_DeleteProfileObjectType_RequestSyntax) **   <a name="connect-connect-customer-profiles_DeleteProfileObjectType-request-uri-ObjectTypeName"></a>
The name of the profile object type.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z_][a-zA-Z_0-9-]*$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_DeleteProfileObjectType_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_DeleteProfileObjectType_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Message": "string"
}
```

## Response Elements
<a name="API_connect-customer-profiles_DeleteProfileObjectType_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Message](#API_connect-customer-profiles_DeleteProfileObjectType_ResponseSyntax) **   <a name="connect-connect-customer-profiles_DeleteProfileObjectType-response-Message"></a>
A message that indicates the delete request is done.
Type: String

## Errors
<a name="API_connect-customer-profiles_DeleteProfileObjectType_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** InternalServerException **
An internal service error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource does not exist, or access was denied.
HTTP Status Code: 404

 ** ThrottlingException **
You exceeded the maximum number of requests.
HTTP Status Code: 429

## Examples
<a name="API_connect-customer-profiles_DeleteProfileObjectType_Examples"></a>

### Example
<a name="API_connect-customer-profiles_DeleteProfileObjectType_Example_1"></a>

This example illustrates one usage of DeleteProfileObjectType.

#### Sample Request
<a name="API_connect-customer-profiles_DeleteProfileObjectType_Example_1_Request"></a>

```
DELETE /domains/ExampleDomainName/object-types/MyCustomObjectTypeName HTTP/1.1
```

#### Sample Response
<a name="API_connect-customer-profiles_DeleteProfileObjectType_Example_1_Response"></a>

```
Content-type: application/json
{
   "Message": "Deleted"
}
```

## See Also
<a name="API_connect-customer-profiles_DeleteProfileObjectType_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/DeleteProfileObjectType)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/DeleteProfileObjectType)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/DeleteProfileObjectType)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/DeleteProfileObjectType)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/DeleteProfileObjectType)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/DeleteProfileObjectType)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/DeleteProfileObjectType)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/DeleteProfileObjectType)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/DeleteProfileObjectType)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/DeleteProfileObjectType)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
