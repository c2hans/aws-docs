---
source_url: https://docs.aws.amazon.com/application-discovery/latest/APIReference/API_AssociateConfigurationItemsToApplication.html
---

# AssociateConfigurationItemsToApplication
<a name="API_AssociateConfigurationItemsToApplication"></a>

**Important**
 AWS Application Discovery Service is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS Application Discovery Service availability change](https://docs.aws.amazon.com/application-discovery/latest/userguide/application-discovery-service-availability-change.html).

Associates one or more configuration items with an application.

## Request Syntax
<a name="API_AssociateConfigurationItemsToApplication_RequestSyntax"></a>

```
{
   "applicationConfigurationId": "{{string}}",
   "configurationIds": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_AssociateConfigurationItemsToApplication_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [applicationConfigurationId](#API_AssociateConfigurationItemsToApplication_RequestSyntax) **   <a name="DiscServ-AssociateConfigurationItemsToApplication-request-applicationConfigurationId"></a>
The configuration ID of an application with which items are to be associated.
Type: String
Length Constraints: Maximum length of 200.
Pattern: `\S+`
Required: Yes

 ** [configurationIds](#API_AssociateConfigurationItemsToApplication_RequestSyntax) **   <a name="DiscServ-AssociateConfigurationItemsToApplication-request-configurationIds"></a>
The ID of each configuration item to be associated with an application.
Type: Array of strings
Length Constraints: Maximum length of 200.
Pattern: `\S*`
Required: Yes

## Response Elements
<a name="API_AssociateConfigurationItemsToApplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_AssociateConfigurationItemsToApplication_Errors"></a>

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
<a name="API_AssociateConfigurationItemsToApplication_Examples"></a>

### Associate configuration items to an application
<a name="API_AssociateConfigurationItemsToApplication_Example_1"></a>

The following example associates two Application Discovery Service discovered resources specified by their configuration ids to the application identified by the value passed to the parameter `applicationConfigurationId` in the request.

#### Sample Request
<a name="API_AssociateConfigurationItemsToApplication_Example_1_Request"></a>

```
{
    "applicationConfigurationId":"d-application-0039038d504694533",
    "configurationIds": [
	      "d-server-0025db43a885966c8",
	      "d-server-0f0a32a0db4217bd6"
    ]
}
```

## See Also
<a name="API_AssociateConfigurationItemsToApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/discovery-2015-11-01/AssociateConfigurationItemsToApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/discovery-2015-11-01/AssociateConfigurationItemsToApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/discovery-2015-11-01/AssociateConfigurationItemsToApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/discovery-2015-11-01/AssociateConfigurationItemsToApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/discovery-2015-11-01/AssociateConfigurationItemsToApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/discovery-2015-11-01/AssociateConfigurationItemsToApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/discovery-2015-11-01/AssociateConfigurationItemsToApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/discovery-2015-11-01/AssociateConfigurationItemsToApplication)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/discovery-2015-11-01/AssociateConfigurationItemsToApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/discovery-2015-11-01/AssociateConfigurationItemsToApplication)
