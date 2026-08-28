---
source_url: https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeTrialComponent.html
---

# DescribeTrialComponent
<a name="API_DescribeTrialComponent"></a>

Provides a list of a trials component's properties.

## Request Syntax
<a name="API_DescribeTrialComponent_RequestSyntax"></a>

```
{
   "TrialComponentName": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeTrialComponent_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [TrialComponentName](#API_DescribeTrialComponent_RequestSyntax) **   <a name="sagemaker-DescribeTrialComponent-request-TrialComponentName"></a>
The name of the trial component to describe.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `(arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:(experiment|experiment-trial|experiment-trial-component|artifact|action|context)\/)?([a-zA-Z0-9](-*[a-zA-Z0-9]){0,119})`
Required: Yes

## Response Syntax
<a name="API_DescribeTrialComponent_ResponseSyntax"></a>

```
{
   "CreatedBy": {
      "DomainId": "string",
      "IamIdentity": {
         "Arn": "string",
         "PrincipalId": "string",
         "SourceIdentity": "string"
      },
      "UserProfileArn": "string",
      "UserProfileName": "string"
   },
   "CreationTime": number,
   "DisplayName": "string",
   "EndTime": number,
   "InputArtifacts": {
      "string" : {
         "MediaType": "string",
         "Value": "string"
      }
   },
   "LastModifiedBy": {
      "DomainId": "string",
      "IamIdentity": {
         "Arn": "string",
         "PrincipalId": "string",
         "SourceIdentity": "string"
      },
      "UserProfileArn": "string",
      "UserProfileName": "string"
   },
   "LastModifiedTime": number,
   "LineageGroupArn": "string",
   "MetadataProperties": {
      "CommitId": "string",
      "GeneratedBy": "string",
      "ProjectId": "string",
      "Repository": "string"
   },
   "Metrics": [
      {
         "Avg": number,
         "Count": number,
         "Last": number,
         "Max": number,
         "MetricName": "string",
         "Min": number,
         "SourceArn": "string",
         "StdDev": number,
         "TimeStamp": number
      }
   ],
   "OutputArtifacts": {
      "string" : {
         "MediaType": "string",
         "Value": "string"
      }
   },
   "Parameters": {
      "string" : {
         "NumberValue": number,
         "StringValue": "string"
      }
   },
   "Source": {
      "SourceArn": "string",
      "SourceType": "string"
   },
   "Sources": [
      {
         "SourceArn": "string",
         "SourceType": "string"
      }
   ],
   "StartTime": number,
   "Status": {
      "Message": "string",
      "PrimaryStatus": "string"
   },
   "TrialComponentArn": "string",
   "TrialComponentName": "string"
}
```

## Response Elements
<a name="API_DescribeTrialComponent_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CreatedBy](#API_DescribeTrialComponent_ResponseSyntax) **   <a name="sagemaker-DescribeTrialComponent-response-CreatedBy"></a>
Who created the trial component.
Type: [UserContext](API_UserContext.md) object

 ** [CreationTime](#API_DescribeTrialComponent_ResponseSyntax) **   <a name="sagemaker-DescribeTrialComponent-response-CreationTime"></a>
When the component was created.
Type: Timestamp

 ** [DisplayName](#API_DescribeTrialComponent_ResponseSyntax) **   <a name="sagemaker-DescribeTrialComponent-response-DisplayName"></a>
The name of the component as displayed. If `DisplayName` isn't specified, `TrialComponentName` is displayed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`

 ** [EndTime](#API_DescribeTrialComponent_ResponseSyntax) **   <a name="sagemaker-DescribeTrialComponent-response-EndTime"></a>
When the component ended.
Type: Timestamp

 ** [InputArtifacts](#API_DescribeTrialComponent_ResponseSyntax) **   <a name="sagemaker-DescribeTrialComponent-response-InputArtifacts"></a>
The input artifacts of the component.
Type: String to [TrialComponentArtifact](API_TrialComponentArtifact.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 60 items.
Key Length Constraints: Minimum length of 0. Maximum length of 128.
Key Pattern: `.*`

 ** [LastModifiedBy](#API_DescribeTrialComponent_ResponseSyntax) **   <a name="sagemaker-DescribeTrialComponent-response-LastModifiedBy"></a>
Who last modified the component.
Type: [UserContext](API_UserContext.md) object

 ** [LastModifiedTime](#API_DescribeTrialComponent_ResponseSyntax) **   <a name="sagemaker-DescribeTrialComponent-response-LastModifiedTime"></a>
When the component was last modified.
Type: Timestamp

 ** [LineageGroupArn](#API_DescribeTrialComponent_ResponseSyntax) **   <a name="sagemaker-DescribeTrialComponent-response-LineageGroupArn"></a>
The Amazon Resource Name (ARN) of the lineage group.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:lineage-group/.*`

 ** [MetadataProperties](#API_DescribeTrialComponent_ResponseSyntax) **   <a name="sagemaker-DescribeTrialComponent-response-MetadataProperties"></a>
Metadata properties of the tracking entity, trial, or trial component.
Type: [MetadataProperties](API_MetadataProperties.md) object

 ** [Metrics](#API_DescribeTrialComponent_ResponseSyntax) **   <a name="sagemaker-DescribeTrialComponent-response-Metrics"></a>
The metrics for the component.
Type: Array of [TrialComponentMetricSummary](API_TrialComponentMetricSummary.md) objects

 ** [OutputArtifacts](#API_DescribeTrialComponent_ResponseSyntax) **   <a name="sagemaker-DescribeTrialComponent-response-OutputArtifacts"></a>
The output artifacts of the component.
Type: String to [TrialComponentArtifact](API_TrialComponentArtifact.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 60 items.
Key Length Constraints: Minimum length of 0. Maximum length of 128.
Key Pattern: `.*`

 ** [Parameters](#API_DescribeTrialComponent_ResponseSyntax) **   <a name="sagemaker-DescribeTrialComponent-response-Parameters"></a>
The hyperparameters of the component.
Type: String to [TrialComponentParameterValue](API_TrialComponentParameterValue.md) object map
Map Entries: Minimum number of 0 items. Maximum number of 300 items.
Key Length Constraints: Minimum length of 0. Maximum length of 320.
Key Pattern: `.*`

 ** [Source](#API_DescribeTrialComponent_ResponseSyntax) **   <a name="sagemaker-DescribeTrialComponent-response-Source"></a>
The Amazon Resource Name (ARN) of the source and, optionally, the job type.
Type: [TrialComponentSource](API_TrialComponentSource.md) object

 ** [Sources](#API_DescribeTrialComponent_ResponseSyntax) **   <a name="sagemaker-DescribeTrialComponent-response-Sources"></a>
A list of ARNs and, if applicable, job types for multiple sources of an experiment run.
Type: Array of [TrialComponentSource](API_TrialComponentSource.md) objects

 ** [StartTime](#API_DescribeTrialComponent_ResponseSyntax) **   <a name="sagemaker-DescribeTrialComponent-response-StartTime"></a>
When the component started.
Type: Timestamp

 ** [Status](#API_DescribeTrialComponent_ResponseSyntax) **   <a name="sagemaker-DescribeTrialComponent-response-Status"></a>
The status of the component. States include:
+ InProgress
+ Completed
+ Failed
Type: [TrialComponentStatus](API_TrialComponentStatus.md) object

 ** [TrialComponentArn](#API_DescribeTrialComponent_ResponseSyntax) **   <a name="sagemaker-DescribeTrialComponent-response-TrialComponentArn"></a>
The Amazon Resource Name (ARN) of the trial component.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `arn:aws[a-z\-]*:sagemaker:[a-z0-9\-]*:[0-9]{12}:experiment-trial-component/.*`

 ** [TrialComponentName](#API_DescribeTrialComponent_ResponseSyntax) **   <a name="sagemaker-DescribeTrialComponent-response-TrialComponentName"></a>
The name of the trial component.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 120.
Pattern: `[a-zA-Z0-9](-*[a-zA-Z0-9]){0,119}`

## Errors
<a name="API_DescribeTrialComponent_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ResourceNotFound **
Resource being access is not found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeTrialComponent_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sagemaker-2017-07-24/DescribeTrialComponent)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sagemaker-2017-07-24/DescribeTrialComponent)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sagemaker-2017-07-24/DescribeTrialComponent)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sagemaker-2017-07-24/DescribeTrialComponent)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sagemaker-2017-07-24/DescribeTrialComponent)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sagemaker-2017-07-24/DescribeTrialComponent)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sagemaker-2017-07-24/DescribeTrialComponent)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sagemaker-2017-07-24/DescribeTrialComponent)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sagemaker-2017-07-24/DescribeTrialComponent)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sagemaker-2017-07-24/DescribeTrialComponent)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
