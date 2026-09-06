---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_CreateLaunchConfigurationTemplate.html
---

# CreateLaunchConfigurationTemplate
<a name="API_CreateLaunchConfigurationTemplate"></a>

Creates a new Launch Configuration Template.

## Request Syntax
<a name="API_CreateLaunchConfigurationTemplate_RequestSyntax"></a>

```
POST /CreateLaunchConfigurationTemplate HTTP/1.1
Content-type: application/json

{
   "associatePublicIpAddress": {{boolean}},
   "bootMode": "{{string}}",
   "copyPrivateIp": {{boolean}},
   "copyTags": {{boolean}},
   "enableMapAutoTagging": {{boolean}},
   "enableParametersEncryption": {{boolean}},
   "largeVolumeConf": {
      "iops": {{number}},
      "throughput": {{number}},
      "volumeType": "{{string}}"
   },
   "launchDisposition": "{{string}}",
   "licensing": {
      "osByol": {{boolean}}
   },
   "mapAutoTaggingMpeID": "{{string}}",
   "parametersEncryptionKey": "{{string}}",
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
   "smallVolumeConf": {
      "iops": {{number}},
      "throughput": {{number}},
      "volumeType": "{{string}}"
   },
   "smallVolumeMaxSize": {{number}},
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "targetInstanceTypeRightSizingMethod": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateLaunchConfigurationTemplate_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateLaunchConfigurationTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [associatePublicIpAddress](#API_CreateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-request-associatePublicIpAddress"></a>
Associate public Ip address.
Type: Boolean
Required: No

 ** [bootMode](#API_CreateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-request-bootMode"></a>
Launch configuration template boot mode.
Type: String
Valid Values: `LEGACY_BIOS | UEFI | USE_SOURCE`
Required: No

 ** [copyPrivateIp](#API_CreateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-request-copyPrivateIp"></a>
Copy private Ip.
Type: Boolean
Required: No

 ** [copyTags](#API_CreateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-request-copyTags"></a>
Copy tags.
Type: Boolean
Required: No

 ** [enableMapAutoTagging](#API_CreateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-request-enableMapAutoTagging"></a>
Enable map auto tagging.
Type: Boolean
Required: No

 ** [enableParametersEncryption](#API_CreateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-request-enableParametersEncryption"></a>
Enable parameters encryption.
Type: Boolean
Required: No

 ** [largeVolumeConf](#API_CreateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-request-largeVolumeConf"></a>
Large volume config.
Type: [LaunchTemplateDiskConf](API_LaunchTemplateDiskConf.md) object
Required: No

 ** [launchDisposition](#API_CreateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-request-launchDisposition"></a>
Launch disposition.
Type: String
Valid Values: `STOPPED | STARTED`
Required: No

 ** [licensing](#API_CreateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-request-licensing"></a>
Configure Licensing.
Type: [Licensing](API_Licensing.md) object
Required: No

 ** [mapAutoTaggingMpeID](#API_CreateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-request-mapAutoTaggingMpeID"></a>
Launch configuration template map auto tagging MPE ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [parametersEncryptionKey](#API_CreateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-request-parametersEncryptionKey"></a>
Parameters encryption key.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 276.
Pattern: `((arn:[\w-]+:kms:([a-z]{2}-(gov-)?[a-z]+-\d{1})?:(\d{12})?:((alias|key)/[a-zA-Z0-9:/_-]{1,256}))|())`
Required: No

 ** [postLaunchActions](#API_CreateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-request-postLaunchActions"></a>
Launch configuration template post launch actions.
Type: [PostLaunchActions](API_PostLaunchActions.md) object
Required: No

 ** [smallVolumeConf](#API_CreateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-request-smallVolumeConf"></a>
Small volume config.
Type: [LaunchTemplateDiskConf](API_LaunchTemplateDiskConf.md) object
Required: No

 ** [smallVolumeMaxSize](#API_CreateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-request-smallVolumeMaxSize"></a>
Small volume maximum size.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** [tags](#API_CreateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-request-tags"></a>
Request to associate tags during creation of a Launch Configuration Template.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [targetInstanceTypeRightSizingMethod](#API_CreateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-request-targetInstanceTypeRightSizingMethod"></a>
Target instance type right-sizing method.
Type: String
Valid Values: `NONE | BASIC`
Required: No

## Response Syntax
<a name="API_CreateLaunchConfigurationTemplate_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "arn": "string",
   "associatePublicIpAddress": boolean,
   "bootMode": "string",
   "copyPrivateIp": boolean,
   "copyTags": boolean,
   "ec2LaunchTemplateID": "string",
   "enableMapAutoTagging": boolean,
   "enableParametersEncryption": boolean,
   "largeVolumeConf": {
      "iops": number,
      "throughput": number,
      "volumeType": "string"
   },
   "launchConfigurationTemplateID": "string",
   "launchDisposition": "string",
   "licensing": {
      "osByol": boolean
   },
   "mapAutoTaggingMpeID": "string",
   "parametersEncryptionKey": "string",
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
   "smallVolumeConf": {
      "iops": number,
      "throughput": number,
      "volumeType": "string"
   },
   "smallVolumeMaxSize": number,
   "tags": {
      "string" : "string"
   },
   "targetInstanceTypeRightSizingMethod": "string"
}
```

## Response Elements
<a name="API_CreateLaunchConfigurationTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_CreateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-response-arn"></a>
ARN of the Launch Configuration Template.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [associatePublicIpAddress](#API_CreateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-response-associatePublicIpAddress"></a>
Associate public Ip address.
Type: Boolean

 ** [bootMode](#API_CreateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-response-bootMode"></a>
Launch configuration template boot mode.
Type: String
Valid Values: `LEGACY_BIOS | UEFI | USE_SOURCE`

 ** [copyPrivateIp](#API_CreateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-response-copyPrivateIp"></a>
Copy private Ip.
Type: Boolean

 ** [copyTags](#API_CreateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-response-copyTags"></a>
Copy tags.
Type: Boolean

 ** [ec2LaunchTemplateID](#API_CreateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-response-ec2LaunchTemplateID"></a>
EC2 launch template ID.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `lt-[0-9a-z]{17}`

 ** [enableMapAutoTagging](#API_CreateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-response-enableMapAutoTagging"></a>
Enable map auto tagging.
Type: Boolean

 ** [enableParametersEncryption](#API_CreateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-response-enableParametersEncryption"></a>
Enable parameters encryption.
Type: Boolean

 ** [largeVolumeConf](#API_CreateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-response-largeVolumeConf"></a>
Large volume config.
Type: [LaunchTemplateDiskConf](API_LaunchTemplateDiskConf.md) object

 ** [launchConfigurationTemplateID](#API_CreateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-response-launchConfigurationTemplateID"></a>
ID of the Launch Configuration Template.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `lct-[0-9a-zA-Z]{17}`

 ** [launchDisposition](#API_CreateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-response-launchDisposition"></a>
Launch disposition.
Type: String
Valid Values: `STOPPED | STARTED`

 ** [licensing](#API_CreateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-response-licensing"></a>
Configure Licensing.
Type: [Licensing](API_Licensing.md) object

 ** [mapAutoTaggingMpeID](#API_CreateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-response-mapAutoTaggingMpeID"></a>
Launch configuration template map auto tagging MPE ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [parametersEncryptionKey](#API_CreateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-response-parametersEncryptionKey"></a>
Parameters encryption key.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [postLaunchActions](#API_CreateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-response-postLaunchActions"></a>
Post Launch Actions of the Launch Configuration Template.
Type: [PostLaunchActions](API_PostLaunchActions.md) object

 ** [smallVolumeConf](#API_CreateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-response-smallVolumeConf"></a>
Small volume config.
Type: [LaunchTemplateDiskConf](API_LaunchTemplateDiskConf.md) object

 ** [smallVolumeMaxSize](#API_CreateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-response-smallVolumeMaxSize"></a>
Small volume maximum size.
Type: Long
Valid Range: Minimum value of 0.

 ** [tags](#API_CreateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-response-tags"></a>
Tags of the Launch Configuration Template.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [targetInstanceTypeRightSizingMethod](#API_CreateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-CreateLaunchConfigurationTemplate-response-targetInstanceTypeRightSizingMethod"></a>
Target instance type right-sizing method.
Type: String
Valid Values: `NONE | BASIC`

## Errors
<a name="API_CreateLaunchConfigurationTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Operation denied due to a file permission or access check error.
HTTP Status Code: 403

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
<a name="API_CreateLaunchConfigurationTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/CreateLaunchConfigurationTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/CreateLaunchConfigurationTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/CreateLaunchConfigurationTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/CreateLaunchConfigurationTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/CreateLaunchConfigurationTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/CreateLaunchConfigurationTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/CreateLaunchConfigurationTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/CreateLaunchConfigurationTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/CreateLaunchConfigurationTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/CreateLaunchConfigurationTemplate)
