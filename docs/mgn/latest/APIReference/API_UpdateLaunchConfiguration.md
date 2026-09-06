---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_UpdateLaunchConfiguration.html
---

# UpdateLaunchConfiguration
<a name="API_UpdateLaunchConfiguration"></a>

Updates multiple LaunchConfigurations by Source Server ID.

**Note**
bootMode valid values are `LEGACY_BIOS | UEFI | USE_SOURCE`

## Request Syntax
<a name="API_UpdateLaunchConfiguration_RequestSyntax"></a>

```
POST /UpdateLaunchConfiguration HTTP/1.1
Content-type: application/json

{
   "accountID": "{{string}}",
   "bootMode": "{{string}}",
   "copyPrivateIp": {{boolean}},
   "copyTags": {{boolean}},
   "enableMapAutoTagging": {{boolean}},
   "launchDisposition": "{{string}}",
   "licensing": {
      "osByol": {{boolean}}
   },
   "mapAutoTaggingMpeID": "{{string}}",
   "name": "{{string}}",
   "postLaunchActions": {
      "cloudWatchLogGroupName": "{{string}}",
      "deployment": "{{string}}",
      "s3LogBucket": "{{string}}",
      "s3OutputKeyPrefix": "{{string}}",
      "ssmDocuments": [
         {
            "actionName": "{{string}}",
            "externalParameters": {
               "{{string}}" : { ... }
            },
            "mustSucceedForCutover": {{boolean}},
            "parameters": {
               "{{string}}" : [
                  {
                     "parameterName": "{{string}}",
                     "parameterType": "{{string}}"
                  }
               ]
            },
            "ssmDocumentName": "{{string}}",
            "timeoutSeconds": {{number}}
         }
      ]
   },
   "sourceServerID": "{{string}}",
   "targetInstanceTypeRightSizingMethod": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateLaunchConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateLaunchConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountID](#API_UpdateLaunchConfiguration_RequestSyntax) **   <a name="mgn-UpdateLaunchConfiguration-request-accountID"></a>
Update Launch configuration Account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

 ** [bootMode](#API_UpdateLaunchConfiguration_RequestSyntax) **   <a name="mgn-UpdateLaunchConfiguration-request-bootMode"></a>
Update Launch configuration boot mode request.
Type: String
Valid Values: `LEGACY_BIOS | UEFI | USE_SOURCE`
Required: No

 ** [copyPrivateIp](#API_UpdateLaunchConfiguration_RequestSyntax) **   <a name="mgn-UpdateLaunchConfiguration-request-copyPrivateIp"></a>
Update Launch configuration copy Private IP request.
Type: Boolean
Required: No

 ** [copyTags](#API_UpdateLaunchConfiguration_RequestSyntax) **   <a name="mgn-UpdateLaunchConfiguration-request-copyTags"></a>
Update Launch configuration copy Tags request.
Type: Boolean
Required: No

 ** [enableMapAutoTagging](#API_UpdateLaunchConfiguration_RequestSyntax) **   <a name="mgn-UpdateLaunchConfiguration-request-enableMapAutoTagging"></a>
Enable map auto tagging.
Type: Boolean
Required: No

 ** [launchDisposition](#API_UpdateLaunchConfiguration_RequestSyntax) **   <a name="mgn-UpdateLaunchConfiguration-request-launchDisposition"></a>
Update Launch configuration launch disposition request.
Type: String
Valid Values: `STOPPED | STARTED`
Required: No

 ** [licensing](#API_UpdateLaunchConfiguration_RequestSyntax) **   <a name="mgn-UpdateLaunchConfiguration-request-licensing"></a>
Update Launch configuration licensing request.
Type: [Licensing](API_Licensing.md) object
Required: No

 ** [mapAutoTaggingMpeID](#API_UpdateLaunchConfiguration_RequestSyntax) **   <a name="mgn-UpdateLaunchConfiguration-request-mapAutoTaggingMpeID"></a>
Launch configuration map auto tagging MPE ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [name](#API_UpdateLaunchConfiguration_RequestSyntax) **   <a name="mgn-UpdateLaunchConfiguration-request-name"></a>
Update Launch configuration name request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.
Required: No

 ** [postLaunchActions](#API_UpdateLaunchConfiguration_RequestSyntax) **   <a name="mgn-UpdateLaunchConfiguration-request-postLaunchActions"></a>
Post Launch Actions to be executed on the Test or Cutover instance.
Type: [PostLaunchActions](API_PostLaunchActions.md) object
Required: No

 ** [sourceServerID](#API_UpdateLaunchConfiguration_RequestSyntax) **   <a name="mgn-UpdateLaunchConfiguration-request-sourceServerID"></a>
Update Launch configuration by Source Server ID request.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`
Required: Yes

 ** [targetInstanceTypeRightSizingMethod](#API_UpdateLaunchConfiguration_RequestSyntax) **   <a name="mgn-UpdateLaunchConfiguration-request-targetInstanceTypeRightSizingMethod"></a>
Update Launch configuration Target instance right sizing request.
Type: String
Valid Values: `NONE | BASIC`
Required: No

## Response Syntax
<a name="API_UpdateLaunchConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "bootMode": "string",
   "copyPrivateIp": boolean,
   "copyTags": boolean,
   "ec2LaunchTemplateID": "string",
   "enableMapAutoTagging": boolean,
   "launchDisposition": "string",
   "licensing": {
      "osByol": boolean
   },
   "mapAutoTaggingMpeID": "string",
   "name": "string",
   "postLaunchActions": {
      "cloudWatchLogGroupName": "string",
      "deployment": "string",
      "s3LogBucket": "string",
      "s3OutputKeyPrefix": "string",
      "ssmDocuments": [
         {
            "actionName": "string",
            "externalParameters": {
               "string" : { ... }
            },
            "mustSucceedForCutover": boolean,
            "parameters": {
               "string" : [
                  {
                     "parameterName": "string",
                     "parameterType": "string"
                  }
               ]
            },
            "ssmDocumentName": "string",
            "timeoutSeconds": number
         }
      ]
   },
   "sourceServerID": "string",
   "targetInstanceTypeRightSizingMethod": "string"
}
```

## Response Elements
<a name="API_UpdateLaunchConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [bootMode](#API_UpdateLaunchConfiguration_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfiguration-response-bootMode"></a>
Launch configuration boot mode.
Type: String
Valid Values: `LEGACY_BIOS | UEFI | USE_SOURCE`

 ** [copyPrivateIp](#API_UpdateLaunchConfiguration_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfiguration-response-copyPrivateIp"></a>
Copy Private IP during Launch Configuration.
Type: Boolean

 ** [copyTags](#API_UpdateLaunchConfiguration_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfiguration-response-copyTags"></a>
Copy Tags during Launch Configuration.
Type: Boolean

 ** [ec2LaunchTemplateID](#API_UpdateLaunchConfiguration_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfiguration-response-ec2LaunchTemplateID"></a>
Launch configuration EC2 Launch template ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [enableMapAutoTagging](#API_UpdateLaunchConfiguration_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfiguration-response-enableMapAutoTagging"></a>
Enable map auto tagging.
Type: Boolean

 ** [launchDisposition](#API_UpdateLaunchConfiguration_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfiguration-response-launchDisposition"></a>
Launch disposition for launch configuration.
Type: String
Valid Values: `STOPPED | STARTED`

 ** [licensing](#API_UpdateLaunchConfiguration_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfiguration-response-licensing"></a>
Launch configuration OS licensing.
Type: [Licensing](API_Licensing.md) object

 ** [mapAutoTaggingMpeID](#API_UpdateLaunchConfiguration_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfiguration-response-mapAutoTaggingMpeID"></a>
Map auto tagging MPE ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [name](#API_UpdateLaunchConfiguration_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfiguration-response-name"></a>
Launch configuration name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.

 ** [postLaunchActions](#API_UpdateLaunchConfiguration_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfiguration-response-postLaunchActions"></a>
Post Launch Actions to be executed on the Test or Cutover instance.
Type: [PostLaunchActions](API_PostLaunchActions.md) object

 ** [sourceServerID](#API_UpdateLaunchConfiguration_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfiguration-response-sourceServerID"></a>
Launch configuration Source Server ID.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`

 ** [targetInstanceTypeRightSizingMethod](#API_UpdateLaunchConfiguration_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfiguration-response-targetInstanceTypeRightSizingMethod"></a>
Launch configuration Target instance type right sizing method.
Type: String
Valid Values: `NONE | BASIC`

## Errors
<a name="API_UpdateLaunchConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the target resource.
 ** errors **
Conflict Exception specific errors.
 ** resourceId **
A conflict occurred when prompting for the Resource ID.
 ** resourceType **
A conflict occurred when prompting for resource type.
HTTP Status Code: 409

 ** ResourceNotFoundException **
Resource not found exception.
 ** resourceId **
Resource ID not found error.
 ** resourceType **
Resource type not found error.
HTTP Status Code: 404

 ** UninitializedAccountException **
Uninitialized account exception.
HTTP Status Code: 400

 ** ValidationException **
Validate exception.
 ** fieldList **
Validate exception field list.
 ** reason **
Validate exception reason.
HTTP Status Code: 400

## See Also
<a name="API_UpdateLaunchConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/UpdateLaunchConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/UpdateLaunchConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/UpdateLaunchConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/UpdateLaunchConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/UpdateLaunchConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/UpdateLaunchConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/UpdateLaunchConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/UpdateLaunchConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/UpdateLaunchConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/UpdateLaunchConfiguration)
