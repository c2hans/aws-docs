---
source_url: https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_GetControl.html
---

# GetControl
<a name="API_GetControl"></a>

Returns details about a specific control, most notably a list of AWS Regions where this control is supported. Input a value for the *ControlArn* parameter, in ARN form. `GetControl` accepts *controltower* or *controlcatalog* control ARNs as input. Returns a *controlcatalog* ARN format.

In the API response, controls that have the value `GLOBAL` in the `Scope` field do not show the `DeployableRegions` field, because it does not apply. Controls that have the value `REGIONAL` in the `Scope` field return a value for the `DeployableRegions` field, as shown in the example.

## Request Syntax
<a name="API_GetControl_RequestSyntax"></a>

```
POST /get-control HTTP/1.1
Content-type: application/json

{
   "ControlArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetControl_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetControl_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ControlArn](#API_GetControl_RequestSyntax) **   <a name="controlcatalog-GetControl-request-ControlArn"></a>
The Amazon Resource Name (ARN) of the control. It has one of the following formats:
 *Global format*
 `arn:{PARTITION}:controlcatalog:::control/{CONTROL_CATALOG_OPAQUE_ID}`
 *Or Regional format*
 `arn:{PARTITION}:controltower:{REGION}::control/{CONTROL_TOWER_OPAQUE_ID}`
Here is a more general pattern that covers AWS Control Tower and Control Catalog ARNs:
 `^arn:(aws(?:[-a-z]*)?):(controlcatalog|controltower):[a-zA-Z0-9-]*::control/[0-9a-zA-Z_\\-]+$`
Type: String
Length Constraints: Minimum length of 34. Maximum length of 2048.
Pattern: `arn:(aws(?:[-a-z]*)?):(controlcatalog|controltower):[a-zA-Z0-9-]*::control/[0-9a-zA-Z_\-]+`
Required: Yes

## Response Syntax
<a name="API_GetControl_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Aliases": [ "string" ],
   "Arn": "string",
   "Behavior": "string",
   "CreateTime": number,
   "Description": "string",
   "GovernedProviders": [ "string" ],
   "GovernedResources": [ "string" ],
   "Implementation": {
      "Identifier": "string",
      "Type": "string"
   },
   "Name": "string",
   "ParameterRequirementSummary": "string",
   "Parameters": [
      {
         "Name": "string",
         "Requirement": "string"
      }
   ],
   "RegionConfiguration": {
      "DeployableRegions": [ "string" ],
      "Scope": "string"
   },
   "Severity": "string"
}
```

## Response Elements
<a name="API_GetControl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Aliases](#API_GetControl_ResponseSyntax) **   <a name="controlcatalog-GetControl-response-Aliases"></a>
A list of alternative identifiers for the control. These are human-readable designators, such as `SH.S3.1`. Several aliases can refer to the same control across different AWS services or compliance frameworks.
Type: Array of strings
Pattern: `[a-zA-Z0-9](?:[a-zA-Z0-9_.-]{0,254}[a-zA-Z0-9])`

 ** [Arn](#API_GetControl_ResponseSyntax) **   <a name="controlcatalog-GetControl-response-Arn"></a>
The Amazon Resource Name (ARN) of the control.
Type: String
Length Constraints: Minimum length of 34. Maximum length of 2048.
Pattern: `arn:(aws(?:[-a-z]*)?):(controlcatalog|controltower):[a-zA-Z0-9-]*::control/[0-9a-zA-Z_\-]+`

 ** [Behavior](#API_GetControl_ResponseSyntax) **   <a name="controlcatalog-GetControl-response-Behavior"></a>
A term that identifies the control's functional behavior. One of `Preventive`, `Detective`, `Proactive`
Type: String
Valid Values: `PREVENTIVE | PROACTIVE | DETECTIVE`

 ** [CreateTime](#API_GetControl_ResponseSyntax) **   <a name="controlcatalog-GetControl-response-CreateTime"></a>
A timestamp that notes the time when the control was released (start of its life) as a governance capability in AWS.
Type: Timestamp

 ** [Description](#API_GetControl_ResponseSyntax) **   <a name="controlcatalog-GetControl-response-Description"></a>
A description of what the control does.
Type: String

 ** [GovernedProviders](#API_GetControl_ResponseSyntax) **   <a name="controlcatalog-GetControl-response-GovernedProviders"></a>
A list of providers whose resources are governed by this control. For example, a value of `AWS` indicates that the control governs AWS resources.
Type: Array of strings
Length Constraints: Minimum length of 2. Maximum length of 64.
Pattern: `[A-Z]{2,64}`

 ** [GovernedResources](#API_GetControl_ResponseSyntax) **   <a name="controlcatalog-GetControl-response-GovernedResources"></a>
A list of resource types that are governed by this control. This information helps you understand which controls can govern certain types of resources, and conversely, which resources are affected when the control is implemented. For AWS controls, the resources are represented as CloudFormation resource types. For non-AWS controls, the resources are represented in a provider-specific format. If `GovernedResources` cannot be represented by available resource types, it’s returned as an empty list.
Type: Array of strings
Pattern: `[A-Za-z0-9][A-Za-z0-9.:/_-]{1,254}`

 ** [Implementation](#API_GetControl_ResponseSyntax) **   <a name="controlcatalog-GetControl-response-Implementation"></a>
Returns information about the control, as an `ImplementationDetails` object that shows the underlying implementation type for a control.
Type: [ImplementationDetails](API_ImplementationDetails.md) object

 ** [Name](#API_GetControl_ResponseSyntax) **   <a name="controlcatalog-GetControl-response-Name"></a>
The display name of the control.
Type: String

 ** [ParameterRequirementSummary](#API_GetControl_ResponseSyntax) **   <a name="controlcatalog-GetControl-response-ParameterRequirementSummary"></a>
A summary that indicates whether the control requires parameters, accepts optional parameters, or does not support parameters. Use this field to determine whether you need to supply parameter values when you enable the control.
Type: String
Valid Values: `REQUIRED | OPTIONAL | NONE`

 ** [Parameters](#API_GetControl_ResponseSyntax) **   <a name="controlcatalog-GetControl-response-Parameters"></a>
Returns an array of `ControlParameter` objects that specify the parameters a control supports. An empty list is returned for controls that don’t support parameters.
Type: Array of [ControlParameter](API_ControlParameter.md) objects

 ** [RegionConfiguration](#API_GetControl_ResponseSyntax) **   <a name="controlcatalog-GetControl-response-RegionConfiguration"></a>
Returns information about the control, including the scope of the control, if enabled, and the Regions in which the control is available for deployment. For more information about scope, see [Global services](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/global-services.html).
If you are applying controls through an AWS Control Tower landing zone environment, remember that the values returned in the `RegionConfiguration` API operation are not related to the governed Regions in your landing zone. For example, if you are governing Regions `A`,`B`,and `C` while the control is available in Regions `A`, `B`, C`,` and `D`, you'd see a response with `DeployableRegions` of `A`, `B`, `C`, and `D` for a control with `REGIONAL` scope, even though you may not intend to deploy the control in Region `D`, because you do not govern it through your landing zone.
Type: [RegionConfiguration](API_RegionConfiguration.md) object

 ** [Severity](#API_GetControl_ResponseSyntax) **   <a name="controlcatalog-GetControl-response-Severity"></a>
An enumerated type, with the following possible values:
Type: String
Valid Values: `LOW | MEDIUM | HIGH | CRITICAL`

## Errors
<a name="API_GetControl_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request has invalid or missing parameters.
HTTP Status Code: 400

## Examples
<a name="API_GetControl_Examples"></a>

### Retrieve information about a control
<a name="API_GetControl_Example_1"></a>

Use this operation to retrieve information about a control, including a list of Regions in which the control is available for deployment.

#### Sample Request
<a name="API_GetControl_Example_1_Request"></a>

```
aws controlcatalog get-control --control-arn arn:aws:controlcatalog:::control/4b0nsxnd47747up54ytdqesxi --region us-east-1
```

```
##Alternatively, a control with regional identifier
```

#### Sample Request
<a name="API_GetControl_Example_1_Request"></a>

```
aws controlcatalog get-control --control-arn arn:aws:controltower:us-east-1::control/YEHYWYAUIQHZ --region us-east-1
```

#### Sample Response
<a name="API_GetControl_Example_1_Response"></a>

```
{
    "Arn": "arn:aws:controlcatalog:::control/4b0nsxnd47747up54ytdqesxi",
    "Aliases": [
        "CT.CODEBUILD.PR.3"
    ],
    "Name": "Require any AWS CodeBuild project environment to have logging configured",
    "Description": "This control checks whether AWS CodeBuild projects environment has at least one logging option enabled.",
    "Behavior": "PROACTIVE",
    "Severity": "MEDIUM",
    "RegionConfiguration": {
        "Scope": "REGIONAL",
        "DeployableRegions": [
            "af-south-1",
            "ap-east-1",
            "ap-northeast-1",
            "ap-northeast-2",
            "ap-northeast-3",
            "ap-south-1",
            "ap-south-2",
            "ap-southeast-1",
            "ap-southeast-2",
            "ap-southeast-3",
            "ap-southeast-4",
            "ap-southeast-5",
            "ap-southeast-7",
            "ca-central-1",
            "ca-west-1",
            "eu-central-1",
            "eu-central-2",
            "eu-north-1",
            "eu-south-1",
            "eu-south-2",
            "eu-west-1",
            "eu-west-2",
            "eu-west-3",
            "il-central-1",
            "me-central-1",
            "me-south-1",
            "mx-central-1",
            "sa-east-1",
            "us-east-1",
            "us-east-2",
            "us-west-1",
            "us-west-2"
        ]
    },
    "Implementation": {
        "Type": "AWS::CloudFormation::Type::HOOK"
    },
    "Parameters": [],
    "CreateTime": "2022-11-27T16:00:00-08:00",
    "GovernedResources": [
        "AWS::CodeBuild::Project"
    ]
}
```

## See Also
<a name="API_GetControl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/controlcatalog-2018-05-10/GetControl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/controlcatalog-2018-05-10/GetControl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controlcatalog-2018-05-10/GetControl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/controlcatalog-2018-05-10/GetControl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controlcatalog-2018-05-10/GetControl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/controlcatalog-2018-05-10/GetControl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/controlcatalog-2018-05-10/GetControl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/controlcatalog-2018-05-10/GetControl)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/controlcatalog-2018-05-10/GetControl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controlcatalog-2018-05-10/GetControl)
