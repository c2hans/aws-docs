---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_UpdateApplication.html
---

# UpdateApplication
<a name="API_UpdateApplication"></a>

Updates the specified application to have the specified properties.

**Note**
If a property (for example, `description`) is not provided, the value remains unchanged. To clear these properties, specify an empty string.

## Request Parameters
<a name="API_UpdateApplication_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** ApplicationName **
The name of the application to update. If no such application is found, `UpdateApplication` returns an `InvalidParameterValue` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** Description **
A new description for the application.
Default: If not specified, AWS Elastic Beanstalk does not update the description.
Type: String
Length Constraints: Maximum length of 200.
Required: No

## Response Elements
<a name="API_UpdateApplication_ResponseElements"></a>

The following element is returned by the service.

 ** Application **
 The [ApplicationDescription](API_ApplicationDescription.md) of the application.
Type: [ApplicationDescription](API_ApplicationDescription.md) object

## Errors
<a name="API_UpdateApplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_UpdateApplication_Examples"></a>

### Example
<a name="API_UpdateApplication_Example_1"></a>

This example illustrates one usage of UpdateApplication.

#### Sample Request
<a name="API_UpdateApplication_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?ApplicationName=SampleApp
&Description=Another%20Description
&Operation=UpdateApplication
&AuthParams
```

#### Sample Response
<a name="API_UpdateApplication_Example_1_Response"></a>

```
<UpdateApplicationResponse xmlns="https://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <UpdateApplicationResult>
    <Application>
      <Versions>
        <member>New Version</member>
      </Versions>
      <Description>Another Description</Description>
      <ApplicationName>SampleApp</ApplicationName>
      <DateCreated>2010-11-17T19:26:20.410Z</DateCreated>
      <DateUpdated>2010-11-17T20:42:54.611Z</DateUpdated>
      <ConfigurationTemplates>
        <member>Default</member>
      </ConfigurationTemplates>
    </Application>
  </UpdateApplicationResult>
  <ResponseMetadata>
    <RequestId>40be666b-f28b-11df-8a78-9f77047e0d0c</RequestId>
  </ResponseMetadata>
</UpdateApplicationResponse>
```

## See Also
<a name="API_UpdateApplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/UpdateApplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/UpdateApplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/UpdateApplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/UpdateApplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/UpdateApplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/UpdateApplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/UpdateApplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/UpdateApplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/UpdateApplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/UpdateApplication)
