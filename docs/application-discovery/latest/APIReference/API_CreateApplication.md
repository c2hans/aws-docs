---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_CreateApplication.html
---

# CreateApplication
<a name="API_CreateApplication"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

Creates an application with the given name and description.

## Request Syntax
<a name="API_CreateApplication_RequestSyntax"></a>

```
{
   "description": "{{string}}",
   "name": "{{string}}",
   "wave": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateApplication_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [description](#API_CreateApplication_RequestSyntax) **   <a name="DiscServ-CreateApplication-request-description"></a>
The description of the application to be created.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `(^$|[\s\S]*\S[\s\S]*)`
Required: No

 ** [name](#API_CreateApplication_RequestSyntax) **   <a name="DiscServ-CreateApplication-request-name"></a>
The name of the application to be created.
Type: String
Length Constraints: Maximum length of 127.
Pattern: `[\s\S]*\S[\s\S]*`
Required: Yes

 ** [wave](#API_CreateApplication_RequestSyntax) **   <a name="DiscServ-CreateApplication-request-wave"></a>
The name of the migration wave of the application to be created.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^($|[^\s\x00]( *[^\s\x00])*$)`
Required: No

## Response Syntax
<a name="API_CreateApplication_ResponseSyntax"></a>

```
{
   "configurationId": "string"
}
```

## Response Elements
<a name="API_CreateApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configurationId](#API_CreateApplication_ResponseSyntax) **   <a name="DiscServ-CreateApplication-response-configurationId"></a>
The configuration ID of an application to be created.
Type: String
Length Constraints: Maximum length of 10000.
Pattern: `[\s\S]*`

## Errors
<a name="API_CreateApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationErrorException **
The user does not have permission to perform the action. Check the IAM policy associated with this user.
HTTP Status Code: 400

 ** HomeRegionNotSetException **
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).
The home Region is not set. Set the home Region to continue.
HTTP Status Code: 400

 ** InvalidParameterException **
One or more parameters are not valid. Verify the parameters and try again.
HTTP Status Code: 400

 ** InvalidParameterValueException **
The value of one or more parameters are either invalid or out of range. Verify the parameter values and try again.
HTTP Status Code: 400

 ** ServerInternalErrorException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

## Examples
<a name="API_CreateApplication_Examples"></a>

### Create an application
<a name="API_CreateApplication_Example_1"></a>

The following example creates an application specified by value passed the required parameter of `name` as well as a description passed to the optional parameter `description` in the request.

#### Sample Request
<a name="API_CreateApplication_Example_1_Request"></a>

```
{
    "name":"PeopleSoft_phase1",
	  "description":"components related to payroll app to be migrated"
}
```

#### Sample Response
<a name="API_CreateApplication_Example_1_Response"></a>

```
{
    "configurationId": "d-application-0282ccd1ba7c211ca"
}
```

## See Also
<a name="API_CreateApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/discovery-2015-11-01/CreateApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/discovery-2015-11-01/CreateApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/CreateApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/discovery-2015-11-01/CreateApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/CreateApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/discovery-2015-11-01/CreateApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/discovery-2015-11-01/CreateApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/discovery-2015-11-01/CreateApplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/discovery-2015-11-01/CreateApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/CreateApplication)
