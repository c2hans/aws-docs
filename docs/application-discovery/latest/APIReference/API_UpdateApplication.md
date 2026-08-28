---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_UpdateApplication.html
---

# UpdateApplication
<a name="API_UpdateApplication"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

Updates metadata about an application.

## Request Syntax
<a name="API_UpdateApplication_RequestSyntax"></a>

```
{
   "configurationId": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}",
   "wave": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateApplication_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [configurationId](#API_UpdateApplication_RequestSyntax) **   <a name="DiscServ-UpdateApplication-request-configurationId"></a>
Configuration ID of the application to be updated.
Type: String
Length Constraints: Maximum length of 200.
Pattern: `\S+`
Required: Yes

 ** [description](#API_UpdateApplication_RequestSyntax) **   <a name="DiscServ-UpdateApplication-request-description"></a>
New description of the application to be updated.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `(^$|[\s\S]*\S[\s\S]*)`
Required: No

 ** [name](#API_UpdateApplication_RequestSyntax) **   <a name="DiscServ-UpdateApplication-request-name"></a>
New name of the application to be updated.
Type: String
Length Constraints: Maximum length of 127.
Pattern: `[\s\S]*\S[\s\S]*`
Required: No

 ** [wave](#API_UpdateApplication_RequestSyntax) **   <a name="DiscServ-UpdateApplication-request-wave"></a>
The new migration wave of the application that you want to update.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `^($|[^\s\x00]( *[^\s\x00])*$)`
Required: No

## Response Elements
<a name="API_UpdateApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateApplication_Errors"></a>

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
<a name="API_UpdateApplication_Examples"></a>

### Update application name and description
<a name="API_UpdateApplication_Example_1"></a>

In the following example, both the name and the description are changed (updated) of an existing application. The application is identified by passing the application id to the required parameter `configurationId`.

#### Sample Request
<a name="API_UpdateApplication_Example_1_Request"></a>

```
{
   "configurationId": "d-application-03767f7bddd6c0531",
   "description": "PSoft financials db migration",
   "name": "payroll_db_migration"
}
```

## See Also
<a name="API_UpdateApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/discovery-2015-11-01/UpdateApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/discovery-2015-11-01/UpdateApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/UpdateApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/discovery-2015-11-01/UpdateApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/UpdateApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/discovery-2015-11-01/UpdateApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/discovery-2015-11-01/UpdateApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/discovery-2015-11-01/UpdateApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/discovery-2015-11-01/UpdateApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/UpdateApplication)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Application Discovery Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query application-discovery` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
