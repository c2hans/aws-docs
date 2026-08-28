---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_UpdateLaunchConfigurationTemplate.html
---

# UpdateLaunchConfigurationTemplate
<a name="API_UpdateLaunchConfigurationTemplate"></a>

Updates an existing Launch Configuration Template by ID.

## Request Syntax
<a name="API_UpdateLaunchConfigurationTemplate_RequestSyntax"></a>

```
POST /UpdateLaunchConfigurationTemplate HTTP/1.1
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
   "launchConfigurationTemplateID": "{{string}}",
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
   "targetInstanceTypeRightSizingMethod": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateLaunchConfigurationTemplate_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateLaunchConfigurationTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [associatePublicIpAddress](#API_UpdateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-request-associatePublicIpAddress"></a>
Associate public Ip address.
Type: Boolean
Required: No

 ** [bootMode](#API_UpdateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-request-bootMode"></a>
Launch configuration template boot mode.
Type: String
Valid Values: `LEGACY_BIOS | UEFI | USE_SOURCE`
Required: No

 ** [copyPrivateIp](#API_UpdateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-request-copyPrivateIp"></a>
Copy private Ip.
Type: Boolean
Required: No

 ** [copyTags](#API_UpdateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-request-copyTags"></a>
Copy tags.
Type: Boolean
Required: No

 ** [enableMapAutoTagging](#API_UpdateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-request-enableMapAutoTagging"></a>
Enable map auto tagging.
Type: Boolean
Required: No

 ** [enableParametersEncryption](#API_UpdateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-request-enableParametersEncryption"></a>
Enable parameters encryption.
Type: Boolean
Required: No

 ** [largeVolumeConf](#API_UpdateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-request-largeVolumeConf"></a>
Large volume config.
Type: [LaunchTemplateDiskConf](API_LaunchTemplateDiskConf.md) object
Required: No

 ** [launchConfigurationTemplateID](#API_UpdateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-request-launchConfigurationTemplateID"></a>
Launch Configuration Template ID.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `lct-[0-9a-zA-Z]{17}`
Required: Yes

 ** [launchDisposition](#API_UpdateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-request-launchDisposition"></a>
Launch disposition.
Type: String
Valid Values: `STOPPED | STARTED`
Required: No

 ** [licensing](#API_UpdateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-request-licensing"></a>
Configure Licensing.
Type: [Licensing](API_Licensing.md) object
Required: No

 ** [mapAutoTaggingMpeID](#API_UpdateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-request-mapAutoTaggingMpeID"></a>
Launch configuration template map auto tagging MPE ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [parametersEncryptionKey](#API_UpdateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-request-parametersEncryptionKey"></a>
Parameters encryption key.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** [postLaunchActions](#API_UpdateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-request-postLaunchActions"></a>
Post Launch Action to execute on the Test or Cutover instance.
Type: [PostLaunchActions](API_PostLaunchActions.md) object
Required: No

 ** [smallVolumeConf](#API_UpdateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-request-smallVolumeConf"></a>
Small volume config.
Type: [LaunchTemplateDiskConf](API_LaunchTemplateDiskConf.md) object
Required: No

 ** [smallVolumeMaxSize](#API_UpdateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-request-smallVolumeMaxSize"></a>
Small volume maximum size.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** [targetInstanceTypeRightSizingMethod](#API_UpdateLaunchConfigurationTemplate_RequestSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-request-targetInstanceTypeRightSizingMethod"></a>
Target instance type right-sizing method.
Type: String
Valid Values: `NONE | BASIC`
Required: No

## Response Syntax
<a name="API_UpdateLaunchConfigurationTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_UpdateLaunchConfigurationTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [arn](#API_UpdateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-response-arn"></a>
ARN of the Launch Configuration Template.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [associatePublicIpAddress](#API_UpdateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-response-associatePublicIpAddress"></a>
Associate public Ip address.
Type: Boolean

 ** [bootMode](#API_UpdateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-response-bootMode"></a>
Launch configuration template boot mode.
Type: String
Valid Values: `LEGACY_BIOS | UEFI | USE_SOURCE`

 ** [copyPrivateIp](#API_UpdateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-response-copyPrivateIp"></a>
Copy private Ip.
Type: Boolean

 ** [copyTags](#API_UpdateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-response-copyTags"></a>
Copy tags.
Type: Boolean

 ** [ec2LaunchTemplateID](#API_UpdateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-response-ec2LaunchTemplateID"></a>
EC2 launch template ID.
Type: String
Length Constraints: Fixed length of 20.
Pattern: `lt-[0-9a-z]{17}`

 ** [enableMapAutoTagging](#API_UpdateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-response-enableMapAutoTagging"></a>
Enable map auto tagging.
Type: Boolean

 ** [enableParametersEncryption](#API_UpdateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-response-enableParametersEncryption"></a>
Enable parameters encryption.
Type: Boolean

 ** [largeVolumeConf](#API_UpdateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-response-largeVolumeConf"></a>
Large volume config.
Type: [LaunchTemplateDiskConf](API_LaunchTemplateDiskConf.md) object

 ** [launchConfigurationTemplateID](#API_UpdateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-response-launchConfigurationTemplateID"></a>
ID of the Launch Configuration Template.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `lct-[0-9a-zA-Z]{17}`

 ** [launchDisposition](#API_UpdateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-response-launchDisposition"></a>
Launch disposition.
Type: String
Valid Values: `STOPPED | STARTED`

 ** [licensing](#API_UpdateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-response-licensing"></a>
Configure Licensing.
Type: [Licensing](API_Licensing.md) object

 ** [mapAutoTaggingMpeID](#API_UpdateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-response-mapAutoTaggingMpeID"></a>
Launch configuration template map auto tagging MPE ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [parametersEncryptionKey](#API_UpdateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-response-parametersEncryptionKey"></a>
Parameters encryption key.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [postLaunchActions](#API_UpdateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-response-postLaunchActions"></a>
Post Launch Actions of the Launch Configuration Template.
Type: [PostLaunchActions](API_PostLaunchActions.md) object

 ** [smallVolumeConf](#API_UpdateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-response-smallVolumeConf"></a>
Small volume config.
Type: [LaunchTemplateDiskConf](API_LaunchTemplateDiskConf.md) object

 ** [smallVolumeMaxSize](#API_UpdateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-response-smallVolumeMaxSize"></a>
Small volume maximum size.
Type: Long
Valid Range: Minimum value of 0.

 ** [tags](#API_UpdateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-response-tags"></a>
Tags of the Launch Configuration Template.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [targetInstanceTypeRightSizingMethod](#API_UpdateLaunchConfigurationTemplate_ResponseSyntax) **   <a name="mgn-UpdateLaunchConfigurationTemplate-response-targetInstanceTypeRightSizingMethod"></a>
Target instance type right-sizing method.
Type: String
Valid Values: `NONE | BASIC`

## Errors
<a name="API_UpdateLaunchConfigurationTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Operation denied due to a file permission or access check error.
HTTP Status Code: 403

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
<a name="API_UpdateLaunchConfigurationTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/UpdateLaunchConfigurationTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/UpdateLaunchConfigurationTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/UpdateLaunchConfigurationTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/UpdateLaunchConfigurationTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/UpdateLaunchConfigurationTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/UpdateLaunchConfigurationTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/UpdateLaunchConfigurationTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/UpdateLaunchConfigurationTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/UpdateLaunchConfigurationTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/UpdateLaunchConfigurationTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
