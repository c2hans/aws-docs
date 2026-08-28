---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateApplicationVersion.html
---

# UpdateApplicationVersion
<a name="API_UpdateApplicationVersion"></a>

Updates the specified application version to have the specified properties.

**Note**
If a property (for example, `description`) is not provided, the value remains unchanged. To clear properties, specify an empty string.

## Request Parameters
<a name="API_UpdateApplicationVersion_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ApplicationName **
The name of the application associated with this version.
 If no application is found with this name, `UpdateApplication` returns an `InvalidParameterValue` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** Description **
A new description for this version.
Type: String
Length Constraints: Maximum length of 200.
Required: No

 ** VersionLabel **
The name of the version to update.
If no application version is found with this label, `UpdateApplication` returns an `InvalidParameterValue` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

## Response Elements
<a name="API_UpdateApplicationVersion_ResponseElements"></a>

The following element is returned by the service.

 ** ApplicationVersion **
 The [ApplicationVersionDescription](API_ApplicationVersionDescription.md) of the application version.
Type: [ApplicationVersionDescription](API_ApplicationVersionDescription.md) object

## Errors
<a name="API_UpdateApplicationVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_UpdateApplicationVersion_Examples"></a>

### Example
<a name="API_UpdateApplicationVersion_Example_1"></a>

This example illustrates one usage of UpdateApplicationVersion.

#### Sample Request
<a name="API_UpdateApplicationVersion_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?ApplicationName=SampleApp
&VersionLabel=New%20Version
&Description=New%20Release%20Description
&Operation=UpdateApplicationVersion
&AuthParams
```

#### Sample Response
<a name="API_UpdateApplicationVersion_Example_1_Response"></a>

```
<UpdateApplicationVersionResponse xmlns="https://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <UpdateApplicationVersionResult>
    <ApplicationVersion>
      <SourceBundle>
        <S3Bucket>awsemr</S3Bucket>
        <S3Key>sample.war</S3Key>
      </SourceBundle>
      <VersionLabel>New Version</VersionLabel>
      <Description>New Release Description</Description>
      <ApplicationName>SampleApp</ApplicationName>
      <DateCreated>2010-11-17T19:26:20.699Z</DateCreated>
      <DateUpdated>2010-11-17T20:48:16.632Z</DateUpdated>
    </ApplicationVersion>
  </UpdateApplicationVersionResult>
  <ResponseMetadata>
    <RequestId>00b10aa1-f28c-11df-8a78-9f77047e0d0c</RequestId>
  </ResponseMetadata>
</UpdateApplicationVersionResponse>
```

## See Also
<a name="API_UpdateApplicationVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/UpdateApplicationVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/UpdateApplicationVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/UpdateApplicationVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/UpdateApplicationVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/UpdateApplicationVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/UpdateApplicationVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/UpdateApplicationVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/UpdateApplicationVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/UpdateApplicationVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/UpdateApplicationVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Beanstalk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query elasticbeanstalk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
