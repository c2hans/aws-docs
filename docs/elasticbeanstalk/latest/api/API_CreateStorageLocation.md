---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_CreateStorageLocation.html
---

# CreateStorageLocation
<a name="API_CreateStorageLocation"></a>

Creates a bucket in Amazon S3 to store application versions, logs, and other files used by Elastic Beanstalk environments. The Elastic Beanstalk console and EB CLI call this API the first time you create an environment in a region. If the storage location already exists, `CreateStorageLocation` still returns the bucket name but does not create a new bucket.

## Response Elements
<a name="API_CreateStorageLocation_ResponseElements"></a>

The following element is returned by the service.

 ** S3Bucket **
The name of the Amazon S3 bucket created.
Type: String
Length Constraints: Maximum length of 255.

## Errors
<a name="API_CreateStorageLocation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InsufficientPrivileges **
The specified account does not have sufficient privileges for one or more AWS services.
HTTP Status Code: 403

 ** S3SubscriptionRequired **
The specified account does not have a subscription to Amazon S3.
HTTP Status Code: 400

 ** TooManyBuckets **
The specified account has reached its limit of Amazon S3 buckets.
HTTP Status Code: 400

## Examples
<a name="API_CreateStorageLocation_Examples"></a>

### Example
<a name="API_CreateStorageLocation_Example_1"></a>

This example illustrates one usage of CreateStorageLocation.

#### Sample Request
<a name="API_CreateStorageLocation_Example_1_Request"></a>

```
https://elasticbeanstalk.us-west-2.amazonaws.com/?Operation=CreateStorageLocation
&AuthParams
```

#### Sample Response
<a name="API_CreateStorageLocation_Example_1_Response"></a>

```
          <CreateStorageLocationResponse xmlns="https://elasticbeanstalk.amazonaws.com/docs/2010-12-01/">
  <CreateStorageLocationResult>
    <S3Bucket>elasticbeanstalk-us-east-1-780612358023</S3Bucket>
  </CreateStorageLocationResult>
  <ResponseMetadata>
    <RequestId>ef51b94a-f1d6-11df-8a78-9f77047e0d0c</RequestId>
  </ResponseMetadata>
</CreateStorageLocationResponse>
```

## See Also
<a name="API_CreateStorageLocation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/elasticbeanstalk-2010-12-01/CreateStorageLocation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/elasticbeanstalk-2010-12-01/CreateStorageLocation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/CreateStorageLocation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/elasticbeanstalk-2010-12-01/CreateStorageLocation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/CreateStorageLocation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/elasticbeanstalk-2010-12-01/CreateStorageLocation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/elasticbeanstalk-2010-12-01/CreateStorageLocation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/elasticbeanstalk-2010-12-01/CreateStorageLocation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/elasticbeanstalk-2010-12-01/CreateStorageLocation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/CreateStorageLocation)
