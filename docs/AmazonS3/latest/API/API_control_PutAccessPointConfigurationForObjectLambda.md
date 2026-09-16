---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutAccessPointConfigurationForObjectLambda.html
---

# PutAccessPointConfigurationForObjectLambda
<a name="API_control_PutAccessPointConfigurationForObjectLambda"></a>

**Note**
This operation is not supported by directory buckets.

Replaces configuration for an Object Lambda Access Point.

The following actions are related to `PutAccessPointConfigurationForObjectLambda`:
+  [GetAccessPointConfigurationForObjectLambda](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_GetAccessPointConfigurationForObjectLambda.html)

## Request Syntax
<a name="API_control_PutAccessPointConfigurationForObjectLambda_RequestSyntax"></a>

```
PUT /v20180820/accesspointforobjectlambda/{{name}}/configuration HTTP/1.1
Host: s3-control.amazonaws.com
x-amz-account-id: {{AccountId}}
<?xml version="1.0" encoding="UTF-8"?>
<PutAccessPointConfigurationForObjectLambdaRequest xmlns="http://awss3control.amazonaws.com/doc/2018-08-20/">
   <Configuration>
      <AllowedFeatures>
         <AllowedFeature>{{string}}</AllowedFeature>
      </AllowedFeatures>
      <CloudWatchMetricsEnabled>{{boolean}}</CloudWatchMetricsEnabled>
      <SupportingAccessPoint>{{string}}</SupportingAccessPoint>
      <TransformationConfigurations>
         <TransformationConfiguration>
            <Actions>
               <Action>{{string}}</Action>
            </Actions>
            <ContentTransformation>
               <AwsLambda>
                  <FunctionArn>{{string}}</FunctionArn>
                  <FunctionPayload>{{string}}</FunctionPayload>
               </AwsLambda>
            </ContentTransformation>
         </TransformationConfiguration>
      </TransformationConfigurations>
   </Configuration>
</PutAccessPointConfigurationForObjectLambdaRequest>
```

## URI Request Parameters
<a name="API_control_PutAccessPointConfigurationForObjectLambda_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_control_PutAccessPointConfigurationForObjectLambda_RequestSyntax) **   <a name="AmazonS3-control_PutAccessPointConfigurationForObjectLambda-request-uri-uri-Name"></a>
The name of the Object Lambda Access Point.
Length Constraints: Minimum length of 3. Maximum length of 45.
Pattern: `^[a-z0-9]([a-z0-9\-]*[a-z0-9])?$`
Required: Yes

 ** [x-amz-account-id](#API_control_PutAccessPointConfigurationForObjectLambda_RequestSyntax) **   <a name="AmazonS3-control_PutAccessPointConfigurationForObjectLambda-request-header-AccountId"></a>
The account ID for the account that owns the specified Object Lambda Access Point.
Length Constraints: Maximum length of 64.
Pattern: `^\d{12}$`
Required: Yes

## Request Body
<a name="API_control_PutAccessPointConfigurationForObjectLambda_RequestBody"></a>

The request accepts the following data in XML format.

 ** [PutAccessPointConfigurationForObjectLambdaRequest](#API_control_PutAccessPointConfigurationForObjectLambda_RequestSyntax) **   <a name="AmazonS3-control_PutAccessPointConfigurationForObjectLambda-request-PutAccessPointConfigurationForObjectLambdaRequest"></a>
Root level tag for the PutAccessPointConfigurationForObjectLambdaRequest parameters.
Required: Yes

 ** [Configuration](#API_control_PutAccessPointConfigurationForObjectLambda_RequestSyntax) **   <a name="AmazonS3-control_PutAccessPointConfigurationForObjectLambda-request-Configuration"></a>
Object Lambda Access Point configuration document.
Type: [ObjectLambdaConfiguration](API_control_ObjectLambdaConfiguration.md) data type
Required: Yes

## Response Syntax
<a name="API_control_PutAccessPointConfigurationForObjectLambda_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_control_PutAccessPointConfigurationForObjectLambda_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## See Also
<a name="API_control_PutAccessPointConfigurationForObjectLambda_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/s3control-2018-08-20/PutAccessPointConfigurationForObjectLambda)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/s3control-2018-08-20/PutAccessPointConfigurationForObjectLambda)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/PutAccessPointConfigurationForObjectLambda)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/s3control-2018-08-20/PutAccessPointConfigurationForObjectLambda)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutAccessPointConfigurationForObjectLambda)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/s3control-2018-08-20/PutAccessPointConfigurationForObjectLambda)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/s3control-2018-08-20/PutAccessPointConfigurationForObjectLambda)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/s3control-2018-08-20/PutAccessPointConfigurationForObjectLambda)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/s3control-2018-08-20/PutAccessPointConfigurationForObjectLambda)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/PutAccessPointConfigurationForObjectLambda)
