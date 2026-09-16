---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateApplicationVersion.html
---

# CreateApplicationVersion
<a name="API_CreateApplicationVersion"></a>

Creates an application version for the specified application. You can create an application version from a source bundle in Amazon S3, a commit in AWS CodeCommit, or the output of an AWS CodeBuild build as follows:

Specify a commit in an AWS CodeCommit repository with `SourceBuildInformation`.

Specify a build in an AWS CodeBuild with `SourceBuildInformation` and `BuildConfiguration`.

Specify a source bundle in Amazon S3 with `SourceBundle`

Omit both `SourceBuildInformation` and `SourceBundle` to use the default sample application.

**Note**
After you create an application version with a specified Amazon S3 bucket and key location, you can't change that Amazon S3 location. If you change the Amazon S3 location, you receive an exception when you attempt to launch an environment from the application version.

## Request Parameters
<a name="API_CreateApplicationVersion_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ApplicationName **
 The name of the application. If no application is found with this name, and `AutoCreateApplication` is `false`, returns an `InvalidParameterValue` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** AutoCreateApplication **
Set to `true` to create an application with the specified name if it doesn't already exist.
Type: Boolean
Required: No

 ** BuildConfiguration **
Settings for an AWS CodeBuild build.
Type: [BuildConfiguration](API_BuildConfiguration.md) object
Required: No

 ** Description **
A description of this application version.
Type: String
Length Constraints: Maximum length of 200.
Required: No

 ** Process **
Pre-processes and validates the environment manifest (`env.yaml`) and configuration files (`*.config` files in the `.ebextensions` folder) in the source bundle. Validating configuration files can identify issues prior to deploying the application version to an environment.
You must turn processing on for application versions that you create using AWS CodeBuild or AWS CodeCommit. For application versions built from a source bundle in Amazon S3, processing is optional.
The `Process` option validates Elastic Beanstalk configuration files. It doesn't validate your application's configuration files, like proxy server or Docker configuration.
Type: Boolean
Required: No

 ** SourceBuildInformation **
Specify a commit in an AWS CodeCommit Git repository to use as the source code for the application version.
Type: [SourceBuildInformation](API_SourceBuildInformation.md) object
Required: No

 ** SourceBundle **
The Amazon S3 bucket and key that identify the location of the source bundle for this version.
The Amazon S3 bucket must be in the same region as the environment.
Unless you're specifying a source bundle in the bucket that Elastic Beanstalk manages in your account, you must assign a custom policy to your user, and grant `Allow` permission to the `s3:Get*` actions on your S3 object resource, for example, `arn:aws:s3:::your-bucket/your-source-bundle-object`.
Specify a source bundle in Amazon S3 or a commit in an AWS CodeCommit repository (with `SourceBuildInformation`), but not both. If neither `SourceBundle` nor `SourceBuildInformation` are provided, Elastic Beanstalk uses a sample application.
Type: [S3Location](API_S3Location.md) object
Required: No

 **Tags.member.N**
Specifies the tags applied to the application version.
Elastic Beanstalk applies these tags only to the application version. Environments that use the application version don't inherit the tags.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** VersionLabel **
A label identifying this version.
Constraint: Must be unique per application. If an application version already exists with this label for the specified application, AWS Elastic Beanstalk returns an `InvalidParameterValue` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Response Elements
<a name="API_CreateApplicationVersion_ResponseElements"></a>

The following element is returned by the service.

 ** ApplicationVersion **
 The [ApplicationVersionDescription](API_ApplicationVersionDescription.md) of the application version.
Type: [ApplicationVersionDescription](API_ApplicationVersionDescription.md) object

## Errors
<a name="API_CreateApplicationVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CodeBuildNotInServiceRegion **
 AWS CodeBuild is not available in the specified region.
HTTP Status Code: 400

 ** InsufficientPrivileges **
The specified account does not have sufficient privileges for one or more AWS services.
HTTP Status Code: 403

 ** S3LocationNotInServiceRegion **
The specified S3 bucket does not belong to the S3 region in which the service is running. The following regions are supported:
+ IAD/us-east-1
+ PDX/us-west-2
+ DUB/eu-west-1
HTTP Status Code: 400

 ** TooManyApplications **
The specified account has reached its limit of applications.
HTTP Status Code: 400

 ** TooManyApplicationVersions **
The specified account has reached its limit of application versions.
HTTP Status Code: 400

## Examples
<a name="API_CreateApplicationVersion_Examples"></a>

### Example
<a name="API_CreateApplicationVersion_Example_1"></a>

This example illustrates one usage of CreateApplicationVersion.

#### Sample Request
<a name="API_CreateApplicationVersion_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?ApplicationName=SampleApp
&VersionLabel=Version1
&Description=description
&SourceBundle.S3Bucket=amazonaws.com
&SourceBundle.S3Key=sample.war
&AutoCreateApplication=true
&Operation=CreateApplicationVersion
&AuthParams
```

#### Sample Response
<a name="API_CreateApplicationVersion_Example_1_Response"></a>

```
<CreateApplicationVersionResponse xmlns="https://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <CreateApplicationVersionResult>
    <ApplicationVersion>
      <SourceBundle>
        <S3Bucket>amazonaws.com</S3Bucket>
        <S3Key>sample.war</S3Key>
      </SourceBundle>
      <VersionLabel>Version1</VersionLabel>
      <Description>description</Description>
      <ApplicationName>SampleApp</ApplicationName>
      <DateCreated>2010-11-17T03:21:59.161Z</DateCreated>
      <DateUpdated>2010-11-17T03:21:59.161Z</DateUpdated>
    </ApplicationVersion>
  </CreateApplicationVersionResult>
  <ResponseMetadata>
    <RequestId>d653efef-f1f9-11df-8a78-9f77047e0d0c</RequestId>
  </ResponseMetadata>
</CreateApplicationVersionResponse>
```

## See Also
<a name="API_CreateApplicationVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/CreateApplicationVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/CreateApplicationVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/CreateApplicationVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/CreateApplicationVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/CreateApplicationVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/CreateApplicationVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/CreateApplicationVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/CreateApplicationVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/CreateApplicationVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/CreateApplicationVersion)
