---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_CancelContact.html
---

# CancelContact
<a name="API_CancelContact"></a>

Cancels or stops a contact with a specified contact ID based on its position in the [contact lifecycle](https://docs.aws.amazon.com/ground-station/latest/ug/contacts.lifecycle.html).

For contacts that:
+ Have yet to start, the contact will be cancelled.
+ Have started but have yet to finish, the contact will be stopped.

## Request Syntax
<a name="API_CancelContact_RequestSyntax"></a>

```
DELETE /contact/{{contactId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_CancelContact_RequestParameters"></a>

The request uses the following URI parameters.

 ** [contactId](#API_CancelContact_RequestSyntax) **   <a name="groundstation-CancelContact-request-uri-contactId"></a>
UUID of a contact.
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`
Required: Yes

## Request Body
<a name="API_CancelContact_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_CancelContact_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "contactId": "string",
   "versionId": number
}
```

## Response Elements
<a name="API_CancelContact_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [contactId](#API_CancelContact_ResponseSyntax) **   <a name="groundstation-CancelContact-response-contactId"></a>
UUID of a contact.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [versionId](#API_CancelContact_ResponseSyntax) **   <a name="groundstation-CancelContact-response-versionId"></a>
Version ID of a contact.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 128.

## Errors
<a name="API_CancelContact_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DependencyException **
Dependency encountered an error.
 ** parameterName **
Name of the parameter that caused the exception.
HTTP Status Code: 531

 ** InvalidParameterException **
One or more parameters are not valid.
 ** parameterName **
Name of the invalid parameter.
HTTP Status Code: 431

 ** ResourceNotFoundException **
Resource was not found.
HTTP Status Code: 434

## See Also
<a name="API_CancelContact_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/groundstation-2019-05-23/CancelContact)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/groundstation-2019-05-23/CancelContact)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/CancelContact)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/groundstation-2019-05-23/CancelContact)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/CancelContact)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/groundstation-2019-05-23/CancelContact)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/groundstation-2019-05-23/CancelContact)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/groundstation-2019-05-23/CancelContact)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/groundstation-2019-05-23/CancelContact)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/CancelContact)
