---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_GetLaunchConfiguration.html
---

# GetLaunchConfiguration
<a name="API_GetLaunchConfiguration"></a>

Lists all LaunchConfigurations available, filtered by Source Server IDs.

## Request Syntax
<a name="API_GetLaunchConfiguration_RequestSyntax"></a>

```
POST /GetLaunchConfiguration HTTP/1.1
Content-type: application/json

{
   "accountID": "{{string}}",
   "sourceServerID": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetLaunchConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetLaunchConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [accountID](#API_GetLaunchConfiguration_RequestSyntax) **   <a name="mgn-GetLaunchConfiguration-request-accountID"></a>
Request to get Launch Configuration information by Account ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `.*[0-9]{12,}.*`
Required: No

 ** [sourceServerID](#API_GetLaunchConfiguration_RequestSyntax) **   <a name="mgn-GetLaunchConfiguration-request-sourceServerID"></a>
Request to get Launch Configuration information by Source Server ID.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`
Required: Yes

## Response Syntax
<a name="API_GetLaunchConfiguration_ResponseSyntax"></a>

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
<a name="API_GetLaunchConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [bootMode](#API_GetLaunchConfiguration_ResponseSyntax) **   <a name="mgn-GetLaunchConfiguration-response-bootMode"></a>
Launch configuration boot mode.
Type: String
Valid Values: `LEGACY_BIOS | UEFI | USE_SOURCE`

 ** [copyPrivateIp](#API_GetLaunchConfiguration_ResponseSyntax) **   <a name="mgn-GetLaunchConfiguration-response-copyPrivateIp"></a>
Copy Private IP during Launch Configuration.
Type: Boolean

 ** [copyTags](#API_GetLaunchConfiguration_ResponseSyntax) **   <a name="mgn-GetLaunchConfiguration-response-copyTags"></a>
Copy Tags during Launch Configuration.
Type: Boolean

 ** [ec2LaunchTemplateID](#API_GetLaunchConfiguration_ResponseSyntax) **   <a name="mgn-GetLaunchConfiguration-response-ec2LaunchTemplateID"></a>
Launch configuration EC2 Launch template ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [enableMapAutoTagging](#API_GetLaunchConfiguration_ResponseSyntax) **   <a name="mgn-GetLaunchConfiguration-response-enableMapAutoTagging"></a>
Enable map auto tagging.
Type: Boolean

 ** [launchDisposition](#API_GetLaunchConfiguration_ResponseSyntax) **   <a name="mgn-GetLaunchConfiguration-response-launchDisposition"></a>
Launch disposition for launch configuration.
Type: String
Valid Values: `STOPPED | STARTED`

 ** [licensing](#API_GetLaunchConfiguration_ResponseSyntax) **   <a name="mgn-GetLaunchConfiguration-response-licensing"></a>
Launch configuration OS licensing.
Type: [Licensing](API_Licensing.md) object

 ** [mapAutoTaggingMpeID](#API_GetLaunchConfiguration_ResponseSyntax) **   <a name="mgn-GetLaunchConfiguration-response-mapAutoTaggingMpeID"></a>
Map auto tagging MPE ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [name](#API_GetLaunchConfiguration_ResponseSyntax) **   <a name="mgn-GetLaunchConfiguration-response-name"></a>
Launch configuration name.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 128.

 ** [postLaunchActions](#API_GetLaunchConfiguration_ResponseSyntax) **   <a name="mgn-GetLaunchConfiguration-response-postLaunchActions"></a>
Post Launch Actions to executed on the Test or Cutover instance.
Type: [PostLaunchActions](API_PostLaunchActions.md) object

 ** [sourceServerID](#API_GetLaunchConfiguration_ResponseSyntax) **   <a name="mgn-GetLaunchConfiguration-response-sourceServerID"></a>
Launch configuration Source Server ID.
Type: String
Length Constraints: Fixed length of 19.
Pattern: `s-[0-9a-zA-Z]{17}`

 ** [targetInstanceTypeRightSizingMethod](#API_GetLaunchConfiguration_ResponseSyntax) **   <a name="mgn-GetLaunchConfiguration-response-targetInstanceTypeRightSizingMethod"></a>
Launch configuration Target instance type right sizing method.
Type: String
Valid Values: `NONE | BASIC`

## Errors
<a name="API_GetLaunchConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

## See Also
<a name="API_GetLaunchConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/GetLaunchConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/GetLaunchConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/GetLaunchConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/GetLaunchConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/GetLaunchConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/GetLaunchConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/GetLaunchConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/GetLaunchConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/GetLaunchConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/GetLaunchConfiguration)
