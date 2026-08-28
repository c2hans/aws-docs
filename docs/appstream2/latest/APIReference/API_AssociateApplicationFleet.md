---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_AssociateApplicationFleet.html
---

# AssociateApplicationFleet
<a name="API_AssociateApplicationFleet"></a>

Associates the specified application with the specified fleet. This is only supported for Elastic fleets.

## Request Syntax
<a name="API_AssociateApplicationFleet_RequestSyntax"></a>

```
{
   "ApplicationArn": "{{string}}",
   "FleetName": "{{string}}"
}
```

## Request Parameters
<a name="API_AssociateApplicationFleet_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ApplicationArn](#API_AssociateApplicationFleet_RequestSyntax) **   <a name="WorkSpacesApplications-AssociateApplicationFleet-request-ApplicationArn"></a>
The ARN of the application.
Type: String
Pattern: `^arn:aws(?:\-cn|\-iso\-b|\-iso|\-us\-gov)?:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.\\-]{0,1023}$`
Required: Yes

 ** [FleetName](#API_AssociateApplicationFleet_RequestSyntax) **   <a name="WorkSpacesApplications-AssociateApplicationFleet-request-FleetName"></a>
The name of the fleet.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

## Response Syntax
<a name="API_AssociateApplicationFleet_ResponseSyntax"></a>

```
{
   "ApplicationFleetAssociation": {
      "ApplicationArn": "string",
      "FleetName": "string"
   }
}
```

## Response Elements
<a name="API_AssociateApplicationFleet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationFleetAssociation](#API_AssociateApplicationFleet_ResponseSyntax) **   <a name="WorkSpacesApplications-AssociateApplicationFleet-response-ApplicationFleetAssociation"></a>
If fleet name is specified, this returns the list of applications that are associated to it. If application ARN is specified, this returns the list of fleets to which it is associated.
Type: [ApplicationFleetAssociation](API_ApplicationFleetAssociation.md) object

## Errors
<a name="API_AssociateApplicationFleet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConcurrentModificationException **
An API error occurred. Wait a few minutes and try again.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** InvalidParameterCombinationException **
Indicates an incorrect combination of parameters, or a missing parameter.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** LimitExceededException **
The requested limit exceeds the permitted limit for an account.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** OperationNotPermittedException **
The attempted operation is not permitted.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_AssociateApplicationFleet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/AssociateApplicationFleet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/AssociateApplicationFleet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/AssociateApplicationFleet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/AssociateApplicationFleet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/AssociateApplicationFleet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/AssociateApplicationFleet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/AssociateApplicationFleet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/AssociateApplicationFleet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/AssociateApplicationFleet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/AssociateApplicationFleet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
