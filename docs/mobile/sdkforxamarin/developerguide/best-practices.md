---
source_url: https://docs.aws.amazon.com/mobile/sdkforxamarin/developerguide/best-practices.html
---

The AWS Mobile SDK for Xamarin is now included in the AWS SDK for .NET. This guide references the archived version of the Mobile SDK for Xamarin.

# Best Practices for Using the AWS Mobile SDK for .NET and Xamarin
<a name="best-practices"></a>

There are only a few fundamentals and best practices that are helpful to know when using the AWS Mobile SDK for .NET and Xamarin.
+ Use Amazon Cognito to obtain AWS credentials instead of hardcoding your credentials in your application. If you hard code your credentials in your application, you may end up exposing them to the public, allowing others to make calls to AWS using your credentials. For instructions on how to use Amazon Cognito to obtain AWS credentials, see [Setting Up the AWS Mobile SDK for .NET and Xamarin](setup.md).
+ For best practices on using S3, see [this article on the AWS Blog](https://aws.amazon.com/articles/1904).
+ For best practices on using DynamoDB, see [DynamoDB Best Practices](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/BestPractices.html) in the DynamoDB Developer Guide.

We are always looking to help our customers be successful and welcome feedback, so please feel free to [post on the AWS forums](https://forums.aws.amazon.com/forum.jspa?forumID=88) or [open an issue on GitHub](https://github.com/awslabs/aws-sdk-xamarin/issues).

## Library of AWS Service Documentation
<a name="library-of-aws-service-documentation"></a>

Every service in the AWS Mobile SDK for .NET and Xamarin has a separate developer guide and service API reference which provides additional information that you might find helpful.

### Amazon Cognito Identity
<a name="amazon-cognito-identity"></a>
+  [Cognito Developer Guide](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html)
+  [Cognito Identity Service API Reference](https://docs.aws.amazon.com/cognitoidentity/latest/APIReference/Welcome.html)

### Amazon Cognito Sync
<a name="amazon-cognito-sync"></a>
+  [Cognito Developer Guide](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html)
+  [Cognito Sync Service API Reference](https://docs.aws.amazon.com/cognitosync/latest/APIReference/Welcome.html)

### Amazon Mobile Analytics
<a name="amazon-mobile-analytics"></a>
+  [Mobile Analytics Developer Guide](https://docs.aws.amazon.com/mobileanalytics/latest/ug/set-up.html)
+  [Mobile Analytics Service API Reference](https://docs.aws.amazon.com/mobileanalytics/latest/ug/server-reference.html)

### Amazon S3
<a name="amazon-s3"></a>
+  [S3 Developer Guide](https://docs.aws.amazon.com/AmazonS3/latest/dev/Welcome.html)
+  [S3 Getting Started Guide](https://docs.aws.amazon.com/AmazonS3/latest/gsg/GetStartedWithS3.html)
+  [S3 Service API Reference](https://docs.aws.amazon.com/AmazonS3/latest/API/Welcome.html)

### Amazon DynamoDB
<a name="amazon-dynamodb"></a>
+  [DynamoDB Developer Guide](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Introduction.html)
+  [DynamoDB Getting Started Guide](https://docs.aws.amazon.com/amazondynamodb/latest/gettingstartedguide/Welcome.html)
+  [DynamoDB Service API Reference](https://docs.aws.amazon.com/amazondynamodb/latest/APIReference/Welcome.html)

### Amazon Simply Notification Service (SNS)
<a name="amazon-simply-notification-service-sns"></a>
+  [SNS Developer Guide](https://docs.aws.amazon.com/sns/latest/dg/welcome.html)
+  [SNS Service API Reference](https://docs.aws.amazon.com/sns/latest/api/Welcome.html)

## Other Helpful Links
<a name="other-helpful-links"></a>
+  [AWS Glossary of Terms](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html)
+  [About AWS Credentials](https://docs.aws.amazon.com/general/latest/gr/aws-security-credentials.html)
