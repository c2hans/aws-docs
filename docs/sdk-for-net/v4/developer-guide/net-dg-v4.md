---
source_url: https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html
---

Version 4 (V4) of the AWS SDK for .NET has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html).

 [https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html)

# Migrating to version 4 of the AWS SDK for .NET
<a name="net-dg-v4"></a>

The AWS SDK for .NET version 4 (V4) has a significant number of breaking changes from version 3 (V3) of the SDK. This topic describes the breaking changes in version 4 and possible work that you might need to do to migrate your environment or code from V3. For additional information about other noteworthy changes in the SDK, see the following resources:
+ The development-tracker issue on GitHub: [https://github.com/aws/aws-sdk-net/issues/3362](https://github.com/aws/aws-sdk-net/issues/3362).
+ The blog post [Preview 1 of AWS SDK for .NET V4](https://aws.amazon.com/blogs/developer/preview-1-of-aws-sdk-for-net-v4/).
+ The blog post [Preview 4 of AWS SDK for .NET V4](https://aws.amazon.com/blogs/developer/preview-4-of-aws-sdk-for-net-v4/).
+ The blog post [General Availability of AWS SDK for .NET V4.0](https://aws.amazon.com/blogs/developer/general-availability-of-aws-sdk-for-net-v4-0/).

## .NET Framework
<a name="net-dg-v4-framework3.5"></a>

The .NET Framework 3.5 target has been removed from V4 of the AWS SDK for .NET. As a result, the SDK no longer supports .NET Framework 3.5. This version of the SDK is compiled against .NET Framework 4.7.2 and runs in the .NET 4.0 runtime. For more information, see [Supported platforms](net-dg-supported-platforms.md#net-dg-platform-diff-netfx45).

## Value types
<a name="net-dg-v4-value-types"></a>

Properties that use value types in classes that are used for making requests and responses have been changed to use nullable value types. Properties with the following types have been changed:
+ `bool` has been changed to `bool?`
+ `double` has been changed to `double?`
+ `int` has been changed to `int?`
+ `float` has been changed to `float?`
+ `long` has been changed to `long?`
+ `Datetime` has been changed to `Datetime?`

For additional information about this change, see the blog post [Preview 1 of AWS SDK for .NET V4](https://aws.amazon.com/blogs/developer/preview-1-of-aws-sdk-for-net-v4/).

## Collections
<a name="net-dg-v4-collections"></a>

Properties that use collections in classes that are used for making requests and responses now default to `null`. As a result, your code needs to verify that a collection isn't null before trying to use it. For example:

```
var sqsClient = new AmazonSQSClient();
var listResponse = await sqsClient.ListQueuesAsync(new ListQueuesRequest());
if (listResponse.QueueUrls != null)
{
    foreach (string qUrl in listResponse.QueueUrls)
    {
        // Perform operations on each queue such as displaying all the attributes.
    }
}
```

The V3 behavior of initializing collections can be restored by setting `Amazon.AWSConfigs.InitializeCollections` to `true`. This property also exists in V3 for users who want to try this behavior change before upgrading to V4.

For additional information about this change, see the blog post [Preview 1 of AWS SDK for .NET V4](https://aws.amazon.com/blogs/developer/preview-1-of-aws-sdk-for-net-v4/).

## AWS Security Token Service (STS)
<a name="net-dg-v4-sts"></a>
+ **The regional endpoint**

  When using credential providers that rely on AWS STS, the calls always use the regional endpoint. This differs from V3 of the SDK, which used the `us-east-1` Region by default when running in the public partition regardless of the configured Region.
+ **The `StsRegionalEndpointsValue` enum**

  The `StsRegionalEndpointsValue` enum was removed from the [Amazon.Runtime](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Runtime/NRuntime.html) namespace. Any code using that enum should be removed.
+ **The `STSAssumeRoleAWSCredentials` class**

  The deprecated STS assume role credential provider, `STSAssumeRoleAWSCredentials`, has been removed from the [Amazon.SecurityToken](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/SecurityToken/NSecurityToken.html) namespace. Use [AssumeRoleAWSCredentials](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Runtime/TAssumeRoleAWSCredentials.html) from [Amazon.Runtime](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Runtime/NRuntime.html) instead.

## Changes related to `ClientConfig`
<a name="net-dg-v4-clientconfig"></a>

The [Amazon.Runtime.ClientConfig](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Runtime/TClientConfig.html) class is the base class of service client configuration classes like [AmazonS3Config](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/S3/TS3Config.html). The following changes were made to this base class.
+  **Default retry mode**

  The `RetryMode` property defaults to `Standard` instead of `Legacy`. As a result, the `Legacy` value has been removed from the [Amazon.Runtime.RequestRetryMode](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Runtime/TRequestRetryMode.html) enum.
+  **Default configuration mode**

  The `DefaultConfigurationMode` property defaults to `Standard` instead of `Legacy`. As a result, the `Legacy` value has been removed from the [Amazon.Runtime.DefaultConfigurationMode](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Runtime/TDefaultConfigurationMode.html) enum.
+  **The `ReadWriteTimeout` property**

  The obsolete `ReadWriteTimeout` property was removed from all targets except .NET Framework 4.7.2.

## The AWSSDK.Extensions.NETCore.Setup NuGet package
<a name="net-dg-v4-netcore-setup"></a>

The [AWSSDK.Extensions.NETCore.Setup](https://www.nuget.org/packages/AWSSDK.Extensions.NETCore.Setup/) NuGet package has been updated to alleviate issues that were present in V3 of the SDK as well as to make the package safe for Native AOT. These changes are summarized below. For detailed information see [PR 3353](https://github.com/aws/aws-sdk-net/pull/3353) in the [aws-sdk-net](https://github.com/aws/aws-sdk-net) repository on GitHub.
+ **The `DefaultClientConfig` class**

  The `DefaultClientConfig` class is no longer inherited from the service client configuration base class [Amazon.Runtime.ClientConfig](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Runtime/TClientConfig.html). The relevant properties from `ClientConfig` have been replicated on `DefaultClientConfig` using nullable value types. This change allows us to detect when a value has been set on `DefaultClientConfig` when copying the values to the configuration being created for the service client.

  One particular result of this change is that `DefaultClientConfig.HttpClientFactory` is no longer available in V4. Use `AWSConfigs.HttpClientFactory` instead. For additional information, see [GitHub issue 3790](https://github.com/aws/aws-sdk-net/issues/3790).

  Another result of this change is that the generic overloads of the `IConfiguration.GetAWSOptions` extension method that accepted a service configuration object have been removed. The non-generic overload should be used instead, and the SDK will automatically handle populating service-specific settings. For additional information, see [GitHub issue 3866](https://github.com/aws/aws-sdk-net/issues/3866).
+ **Native AOT**

  A new mechanism for creating service clients that uses C\# 11 static interface methods has been added to the package. This change eliminates the need to do Assembly type loads to create instances of service clients, including string manipulation of the service interface name to compute the service client type, which is incompatible with Native AOT. This change is available only for .NET 8 and later; older versions still use the original mechanism.

For additional information in this guide about this package, see [AWSSDK.Extensions.NETCore.Setup and IConfiguration](net-dg-config-netcore.md). The source code for this package is on GitHub at [https://github.com/aws/aws-sdk-net/tree/main/extensions/src/AWSSDK.Extensions.NETCore.Setup](https://github.com/aws/aws-sdk-net/tree/main/extensions/src/AWSSDK.Extensions.NETCore.Setup).

## `CookieSigner` and `UrlSigner`
<a name="net-dg-v4-CookieSigner-UrlSigner"></a>

The `CookieSigner` and `UrlSigner` extensions for Amazon CloudFront have been moved to a separate extension package called [AWSSDK.Extensions.CloudFront.Signers](https://www.nuget.org/packages/AWSSDK.Extensions.CloudFront.Signers). This change is to support OpenSSL 3 and take a dependency on [BouncyCastle.Cryptography](https://www.nuget.org/packages/BouncyCastle.Cryptography).

The source code for this package is on GitHub at [https://github.com/aws/aws-sdk-net/tree/main/extensions/src/AWSSDK.Extensions.CloudFront.Signers](https://github.com/aws/aws-sdk-net/tree/main/extensions/src/AWSSDK.Extensions.CloudFront.Signers).

## DateTime versus UTC DateTime
<a name="net-dg-v4-utc-datetime"></a>

Some V3 classes have a DateTime property that's marked as "deprecated" or "obsolete", as well as an alternative UTC DateTime property. In these classes, the obsolete DateTime property has been removed, and the name of the UTC DateTime property has been changed to the original name of the DateTime property.

The following are some examples of classes for which this change has been implemented.
+ [DescribeSpotPriceHistoryRequest](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/EC2/TDescribeSpotPriceHistoryRequest.html):
  + The obsolete `StartTime` property has been removed, and the name of the `StartTimeUtc` property has been changed to "StartTime".
  + The obsolete `EndTime` property has been removed, and the name of the `EndTimeUtc` property has been changed to "EndTime".
+  [CreateFleetRequest](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/EC2/TCreateFleetRequest.html)
  + The obsolete `ValidFrom` property has been removed, and the name of the `ValidFromUtc` property has been changed to "ValidFrom".
  + The obsolete `ValidUntil` property has been removed, and the name of the `ValidUntilUtc` property has been changed to "ValidUntil".

This change might lead to offset times if an application is using the original, obsolete DateTime property. A compile time error will occur for code that uses the UTC DateTime property.

## DateTime parsing
<a name="net-dg-v4-datetime-parsing"></a>

The DateTimeUnmarshaller class has been updated. This class had been parsing and returning DateTime strings as local time. In some cases, these values were being converted back to UTC due to a prior update, but not always. Now, DateTime strings that are unmarshalled are assumed to be UTC and will be specified and unmarshalled as UTC. This update includes the following behavior changes.

Certain timestamp properties that are based on the DateTime class were being parsed into local times. These included response unmarshallers for timestamps and list timestamps for formats `TimestampFormat.ISO8601` and `TimestampFormat.RFC822`. DateTime parsing has been updated to return UTC times instead.

## `ConvertFromUnixEpochSeconds` and `ConvertFromUnixEpochMilliseconds`
<a name="net-dg-v4-ConvertFromUnixEpoch"></a>

The [ConvertFromUnixEpochSeconds](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Util/MAWSSDKUtilsConvertFromUnixEpochSecondsInt32.html) and [ConvertFromUnixEpochMilliseconds](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Util/MAWSSDKUtilsConvertFromUnixEpochMillisecondsInt64.html) methods, which convert Unix epoch seconds to a DateTime structure, were returning the Unix Epoch time as a local time instead of a UTC time. These methods now return UTC time.

## Logging
<a name="net-dg-v4-logging"></a>

The way in which you enable logging in the SDK has been updated for V4. Logging to the console and system diagnostics works the same as V3; that is, by setting the `LoggingConfig.LogTo` property of the [AWSConfigs](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Amazon/TAWSConfigs.html) class to either `LoggingOptions.Console` or `LoggingOptions.SystemDiagnostics`. The [LoggingOptions](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Amazon/TAWSConfigs.html) option for `log4net` has been removed along with the SDK's internal logic for using reflection to attach to an in-memory instance of `log4net`.

To include the SDK's logging into a logging framework, a separate adaptor package is used to connect the SDK with the logging framework. Use the [AWSSDK.Extensions.Logging.Log4NetAdaptor](https://www.nuget.org/packages/AWSSDK.Extensions.Logging.Log4NetAdaptor) package for `log4net` and the [AWSSDK.Extensions.Logging.ILoggerAdaptor](https://www.nuget.org/packages/AWSSDK.Extensions.Logging.ILoggerAdaptor/#readme-body-tab) package for `Microsoft.Extensions.Logging`. The following code examples show you how to configure logging in these two cases.

### Example configuration for log4net
<a name="w2aac25c11c27b7b1"></a>

Add the `AWSSDK.Extensions.Logging.Log4NetAdaptor` NuGet package and call the static `ConfigureAWSSDKLogging` method from `Log4NetAWSExtensions`.

```
using Amazon.DynamoDBv2;
using Amazon.Extensions.Logging.Log4NetAdaptor;
using log4net;

[assembly: log4net.Config.XmlConfigurator(ConfigFile = "log4net.config")]

Log4NetAWSExtensions.ConfigureAWSSDKLogging();
var logger = LogManager.GetLogger(typeof(Program));
```

### Example configuration for Microsoft.Extensions.Logging
<a name="w2aac25c11c27b7b3"></a>

Add the `AWSSDK.Extensions.Logging.ILoggerAdaptor` NuGet package and call the `ConfigureAWSSDKLogging` extension method from the `ILoggerFactory` interface.

```
var builder = WebApplication.CreateBuilder(args);

var app = builder.Build();

app.Services.GetRequiredService<ILoggerFactory>()
    .ConfigureAWSSDKLogging();
```

## Support for HTTP 2
<a name="net-dg-v4-http2"></a>

Support for HTTP 2 has been added to enable bi-directional streaming. For more information see [Support for HTTP 2](http2-support.md).

## Single sign-on
<a name="net-dg-v4-sso"></a>

The default value of the `SupportsGettingNewToken` property of the [SSOAWSCredentialsOptions](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Runtime/TSSOAWSCredentialsOptions.html) class has been changed from `true` to `false`. If you have applications that use the [SSOAWSCredentials](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Runtime/TSSOAWSCredentials.html) class to obtain SSO credentials, you might need to set the `Options.SupportsGettingNewToken` property to `true`. For examples of this configuration, see the [code examples](sso-tutorial-app-only.md#sso-tutorial-app-only-code) in [Tutorial for SSO using only .NET applications](sso-tutorial-app-only.md). For additional information, see [PR 3737](https://github.com/aws/aws-sdk-net/pull/3737) in the [aws-sdk-net](https://github.com/aws/aws-sdk-net) GitHub repository.

## Changes specific to DynamoDB
<a name="net-dg-v4-ddb-specific"></a>

The following changes are specific to Amazon DynamoDB. Many of them are breaking changes.

For additional information about changes to DynamoDB in V4 of the AWS SDK for .NET, see the blog post [Preview 4 of AWS SDK for .NET V4](https://aws.amazon.com/blogs/developer/preview-4-of-aws-sdk-for-net-v4/).

### Open to view items
<a name="w2aac25c11c35b7b1"></a>

V4 changes in the SDK for DynamoDB address some issues around testability, but primarily center around the high-level libraries:
+ The [.NET Document Model](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DotNetSDKMidLevel.html), named [DocumentModel](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/DynamoDBv2/NDynamoDBv2DocumentModel.html) in the code.
+ The [.NET Object Persistence Model](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/DotNetSDKHighLevel.html), named [DataModel](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/DynamoDBv2/NDynamoDBv2DataModel.html) in the code.

For detailed information about these programming modes, see [DynamoDB](dynamodb-intro.md) in this guide.

#### Document Model: Updated exception for mocked `IAmazonDynamoDB` interface
<a name="w2aac25c11c35b7b1b9"></a>

In the document model prior to V4 of the SDK, if a [Table](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/DynamoDBv2/TTable.html) was initialized with a mocked [IAmazonDynamoDB](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/DynamoDBv2/TIDynamoDB.html) interface, it would return `NullReferenceException`. V4 of the SDK returns `InvalidOperationException` instead. Async `Table` methods should work with a mocked client but you might still see exceptions when calling synchronous methods from `.NET/Core/Standard`.

For more information about this change, see [PR 3388](https://github.com/aws/aws-sdk-net/pull/3388) on GitHub.

#### Document Model: `FromJson` and `ToJson` methods
<a name="w2aac25c11c35b7b1c11"></a>

The `FromJson` and `ToJson` methods of the [Document](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/DynamoDBv2/TDocument.html) class now use `System.Text.Json` instead of LitJson for serialization, and LitJson has been removed from V4 of the SDK. A benefit of using `System.Text.Json` is that this parser supports using the .NET `Decimal` type, which supports higher precision for numeric floating point properties.

#### Object Persistence Model: The `DynamoDBOperationConfig` class
<a name="w2aac25c11c35b7b1c13"></a>

In the object persistence model, the following changes have been made to the shared [DynamoDBOperationConfig](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/DynamoDBv2/TDynamoDBOperationConfig.html) class:
+ The class has been separated into new operation-specific classes such as [SaveConfig](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/DynamoDBv2/TSaveConfig.html), [LoadConfig](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/DynamoDBv2/TLoadConfig.html), and [QueryConfig](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/DynamoDBv2/TQueryConfig.html). Methods that take `DynamoDBOperationConfig` have been marked as obsolete and are subject to removal in the future.

  For more information about this change, see [PR 3421](https://github.com/aws/aws-sdk-net/pull/3421) on GitHub.
+ The `MetadataCachingMode` and `DisableFetchingTableMetadata` properties have been removed from the class. These properties were not included in the new operation-specific classes mentioned earlier. The removed properties are table-level settings that should be specified on the global `Context` property of the [AWSConfigsDynamoDB](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Amazon/TAWSConfigsDynamoDB.html) class or on the [DynamoDBContextConfig](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/DynamoDBv2/TDynamoDBContextConfig.html) class.

  For more information about this change, see [PR 3422](https://github.com/aws/aws-sdk-net/pull/3422) on GitHub.
+ The class no longer inherits from the [DynamoDBContextConfig](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/DynamoDBv2/TDynamoDBContextConfig.html) class. This prevents you from passing a `DynamoDBOperationConfig` object in to the constructor for [DynamoDBContext](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/DynamoDBv2/TDynamoDBContext.html), where some properties on the operation-specific config (such as `OverrideTableName`) don't apply.

  For more information about this change, see [PR 3422](https://github.com/aws/aws-sdk-net/pull/3422) on GitHub.

#### Object Persistence Model: Polymorphism
<a name="w2aac25c11c35b7b1c15"></a>

The [DynamoDBPolymorphicTypeAttribute](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/DynamoDBv2/TDynamoDBPolymorphicTypeAttribute.html) class was added to the object persistence model. This class enables support for serialization and deserialization of polymorphic types. For more information, see [PR 3643](https://github.com/aws/aws-sdk-net/pull/3643) on GitHub.

#### Document Model and Object Persistence Model: Mockable operations
<a name="w2aac25c11c35b7b1c17"></a>

New operation-specific interfaces have been added that allow customers to mock DynamoDB operations. The factory methods on the [IDynamoDBContext](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/DynamoDBv2/TIDynamoDBContext.html) interface have been updated to return the new interfaces.

For more information about this change, see [PR 3450](https://github.com/aws/aws-sdk-net/pull/3450) on GitHub.
+ Object Persistence Model
  + Mock `BatchGet` operations via the `IBatchGet` and `IMultiTableBatchGet` interfaces.
  + Mock `BatchWrite` operations via the `IBatchWrite` and `IMultiTableBatchWrite` interfaces.
  + Mock `TransactGet` operations via the `ITransactGet` and `IMultiTableTransactGet` interfaces.
  + Mock `TransactWrite` operations via the `ITransactWrite` and `IMultiTableTransactWrite` interfaces.
  + Mock `Scan` and `Query` operations via the `IAsyncSearch` interface.
+ Document Model
  + Mock `Table` operations via the `ITable` interface.
  + Mock `Scan` and `Query` operations via the `ISearch` interface.
  + Mock `TransactWrite` operations via the `IDocumentTransactWrite` and `IMultiTableDocumentTransactWrite` interfaces.
  + Mock `TransactGet` operations via the `IDocumentTransactGet` and `IMultiTableDocumentTransactGet` interfaces.
  + Mock `BatchWrite` operations via the `IDocumentBatchWrite` and `IMultiTableDocumentBatchWrite` interfaces.
  + Mock `BatchGet` operations via the `IDocumentBatchGet` and `IMultiTableDocumentBatchGet` interfaces.

#### Document Model and Object Persistence Model: Support for Native AOT
<a name="w2aac25c11c35b7b1c19"></a>

A limitation of Native AOT is support for nested .NET types. In some cases, these nested types might go unnoticed by the trimming component of the .NET compiler. In this case, you might receive an exception such as: "`System.InvalidOperationException: Type <type> is unsupported, it cannot be instantiated.`"

You can work around this limitation by adding the `DynamicDependency` somewhere in the code path that informs the trimmer about the dependency on the sub-type. The constructor of the top-level .NET type being saved is a likely place. The following code example shows you how to use the `DynamicDependency` attribute:

```
[DynamoDBTable("TestTable")]
class TypeWithNestedTypeProperty
{
    [DynamicDependency(DynamicallyAccessedMemberTypes.All, typeof(SubType))]
    public TypeWithNestedTypeProperty()
    {

    }

    [DynamoDBHashKey]
    public string Id { get; set; }
    public string Name { get; set; }

    public SubType SubType { get; set; }
}

class SubType
{
    public string SubName { get; set; }
}
```

#### DynamoDBStreams
<a name="w2aac25c11c35b7b1c21"></a>

[DynamoDBStreams](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Streams.html) has been removed from the [AWSSDK.DynamoDB](https://www.nuget.org/packages/AWSSDK.DynamoDBv2) NuGet package and is available in its own package, [AWSSDK.DynamoDBStreams](https://www.nuget.org/packages/AWSSDK.DynamoDBStreams), and has its own namespace, `Amazon.DynamoDBStreams`.

#### Allow removal of the `TableNamePrefix` value
<a name="w2aac25c11c35b7b1c23"></a>

You can now remove the value of the `TableNamePrefix` property in the [DynamoDBContextConfig](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Util/TDynamoDBContextConfig.html) class on the individual operation level. For more information about this change, see [PR 3476](https://github.com/aws/aws-sdk-net/pull/3476) on GitHub.

#### `RetrieveDateTimeInUtc` property
<a name="w2aac25c11c35b7b1c25"></a>

For the [DynamoDBContextConfig](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Util/TDynamoDBContextConfig.html) class, the default value of the `RetrieveDateTimeInUtc` property has been changed to `true`.

#### `DynamoDBContextTableNamePrefix` property
<a name="w2aac25c11c35b7b1c27"></a>

Removed the `DynamoDBContextTableNamePrefix` property from [AWSConfigsDynamoDB](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Amazon/TAWSConfigsDynamoDB.html) class. Users should call `AWSConfigsDynamoDB.Context.TableNamePrefix` instead of

## Changes specific to EC2
<a name="net-dg-v4-ec2-specific"></a>

The following changes are specific to Amazon EC2. Most or all of them are breaking changes.

### Open to view items
<a name="w2aac25c11c39b5b1"></a>

#### `GetDecryptedPassword`
<a name="w2aac25c11c39b5b1b3"></a>

The `GetDecryptedPassword` extension for Amazon EC2 has been moved to a separate extension package called [AWSSDK.Extensions.EC2.DecryptPassword](https://www.nuget.org/packages/AWSSDK.Extensions.EC2.DecryptPassword). This change is to support OpenSSL 3 and take a dependency on [BouncyCastle.Cryptography](https://www.nuget.org/packages/BouncyCastle.Cryptography).

The source code for this package is on GitHub at [https://github.com/aws/aws-sdk-net/tree/main/extensions/src/AWSSDK.Extensions.EC2.DecryptPassword](https://github.com/aws/aws-sdk-net/tree/main/extensions/src/AWSSDK.Extensions.EC2.DecryptPassword).

#### Support for Amazon EC2 IMDSv1
<a name="w2aac25c11c39b5b1b5"></a>

Support for Instance Metadata Service Version 1 (IMDSv1) has been removed. V4 of the SDK always uses Instance Metadata Service Version 2 (IMDSv2) when fetching credentials and other metadata from the IMDS. For more information about the IMDS, see [Use the IMDS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-service.html) in the [Amazon EC2 User Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/).

#### Programming elements that were changed or removed
<a name="w2aac25c11c39b5b1b7"></a>
+ The entire `Amazon.EC2.Import` namespace and code have been removed.
+ The entire `Amazon.EC2.Util` namespace and code have been removed, which includes the AMI utilities that were used to look up EC2 AMIs for Windows.
+ The obsolete `IpRanges` property has been removed from the [IpPermission](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/EC2/TIpPermission.html) class. Use the `Ipv4Ranges` or `Ipv6Ranges` properties instead.
+ The following obsolete fields have been removed from the [EC2InstanceMetadata](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Util/TEC2InstanceMetadata.html) class: `EC2_METADATA_SVC`, `EC2_METADATA_ROOT`, `EC2_USERDATA_ROOT`, `EC2_DYNAMICDATA_ROOT`, and `EC2_APITOKEN_URL`.

## Changes specific to S3
<a name="net-dg-v4-s3-specific"></a>

The following changes are specific to Amazon S3. Most or all of them are breaking changes.

### Open to view items
<a name="w2aac25c11c43b5b1"></a>

#### AWS Region us-east-1
<a name="w2aac25c11c43b5b1b3"></a>

Amazon S3 service clients configured for the `us-east-1` Region can no longer access buckets in other Regions. Buckets must be accessed with S3 service clients configured for the Region the bucket is in.

For additional information about this change, see the blog post [Preview 4 of AWS SDK for .NET V4](https://aws.amazon.com/blogs/developer/preview-4-of-aws-sdk-for-net-v4/).

#### S3 encryption client
<a name="w2aac25c11c43b5b1b5"></a>

The Amazon S3 encryption client, which is defined in the `Amazon.S3.Encryption` namespace, has been removed from the [AWSSDK.S3](https://www.nuget.org/packages/AWSSDK.S3) package. This client has been moved to its own package called [Amazon.Extensions.S3.Encryption](https://www.nuget.org/packages/Amazon.Extensions.S3.Encryption), and the documentation for it is at [https://aws.github.io/amazon-s3-encryption-client-dotnet/api/Amazon.Extensions.S3.Encryption.html](https://aws.github.io/amazon-s3-encryption-client-dotnet/api/Amazon.Extensions.S3.Encryption.html). For information about migration, see [S3 Encryption Client Migration (V1 to V2)](s3-encryption-migration-v1-v2.md). For more information about S3 encryption, see [Supported encryption algorithms](https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide/encryption-algorithms.html) in the [Amazon S3 Encryption Client Developer Guide](https://docs.aws.amazon.com/amazon-s3-encryption-client/latest/developerguide).

#### S3 tagging directive for `CopyObject`
<a name="w2aac25c11c43b5b1b7"></a>

The `TaggingDirective` property has been exposed as a public property of the [CopyObjectRequest](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/S3/TCopyObjectRequest.html) class, which is used by `AmazonS3Client.CopyObject` methods. This property corresponds to the Amazon S3 `x-amz-tagging-directive` parameter, as defined in the [CopyObject](https://docs.aws.amazon.com/AmazonS3/latest/API/API_CopyObject.html) action.

The tagging directive is no longer automatically set to COPY. If a developer doesn't specify a tagging directive, the S3 backend automatically assumes it is COPY, but if a developer explicitly sets the property to null, then the value isn't set at all.

#### The `UseArnRegion` property for S3 configuration
<a name="w2aac25c11c43b5b1b9"></a>

The `UseArnRegion` property of the [Amazon.S3.AmazonS3Config](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/S3/TS3Config.html) class has been updated such that the `AWS_S3_USE_ARN_REGION` environment variable takes precedence over the `s3_use_arn_region` setting in the shared AWS `config` file. For more information about these variables and settings, see [Settings reference](https://docs.aws.amazon.com/sdkref/latest/guide/settings-reference.html) in the [AWS SDKs and Tools Reference Guide](https://docs.aws.amazon.com/sdkref/latest/guide/).

#### Leading slashes for the `CopyObject` and `CopyPart` methods
<a name="w2aac25c11c43b5b1c11"></a>

Leading slashes will no longer be trimmed for the Amazon S3 `CopyObject` and `CopyPart` methods. The `DisableTrimmingLeadingSlash` property has been removed from the [CopyObjectRequest](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/S3/TCopyObjectRequest.html) and [CopyPartRequest](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/S3/TCopyPartRequest.html) classes.

#### The `DoesS3BucketExist...` methods
<a name="w2aac25c11c43b5b1c13"></a>

The obsolete `DoesS3BucketExist` and `DoesS3BucketExistAsync` methods have been removed from the [AmazonS3Util](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/S3/TS3Util.html) class, which implements the [ICoreAmazonS3](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Runtime/TICoreS3.html) interface. These methods were removed because they always use HTTP. Use [DoesS3BucketExistV2](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/S3/MS3UtilDoesS3BucketExistV2IS3String.html) and [DoesS3BucketExistV2Async](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/S3/MS3UtilDoesS3BucketExistV2AsyncIS3String.html) instead.

#### SDK always uses SigV4
<a name="w2aac25c11c43b5b1c15"></a>

Version 4 of the AWS SDK for .NET always uses AWS Signature Version 4 (SigV4) for signing requests. This change results in the following related changes:
+ The `UseSignatureVersion4` property of the [AWSConfigsS3](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Amazon/TAWSConfigsS3.html) class has been removed.
+ The `SignatureVersion` property of the [Amazon.Runtime.ClientConfig](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Runtime/TClientConfig.html) class has been removed. This property was used only by Amazon S3 for backward compatibility.
+ The `RegionEndpoint.Endpoint` class has been removed. This includes the `SignatureVersionOverride` property, which was used to override signature versions for Amazon S3. Use the service-specific `client.DetermineServiceOperationEndPoint()` method instead.
+ Updated methods [AmazonS3Util.PostUpload](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/S3/MS3UtilPostUploadS3PostUploadRequest.html) and [S3PostUploadSignedPolicy.GetSignedPolicy](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/S3/MS3PostUploadSignedPolicyGetSignedPolicyStringAWSCredentialsString.html) to use SigV4. As a consequence, the `S3PostUploadSignedPolicy.GetSignedPolicyV4` method was removed because `GetSignedPolicy` now performs the same function. In addition, `GetSignedPolicy` has been given a third parameter for Region endpoint.

#### The `GetACL` and `PutACL` methods
<a name="w2aac25c11c43b5b1c17"></a>

The `GetACL` and `PutACL` methods of the [AmazonS3Client](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/S3/TS3Client.html) class have been marked as obsolete. To access the functionality of these methods, use the following new methods instead: `GetBucketACL`, `PutBucketACL`, `GetObjectACL`, and `PutObjectACL`.

#### Obsolete programming elements removed
<a name="w2aac25c11c43b5b1c19"></a>

A number of programming elements of the Amazon S3 implementation were removed from V4 of the SDK, including enumeration values, types, methods, namespaces, etc. These are listed below, if not already covered previously, along with potential steps that you can take to accommodate their removal.
+ The `DisableMD5Stream` property has been removed from the [TransferUtilityUploadRequest](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/S3/TTransferUtilityUploadRequest.html) class. Use the `DisableDefaultChecksumValidation` property instead.

  In addition, the `CalculateContentMD5Header` property has been removed from the `TransferUtilityUploadRequest` class. This property is no longer needed because the SDK computes a checksum by default.
+ The `ServerSideEncryptionMethod` and `ServerSideEncryptionKeyManagementServiceKeyId` properties have been removed from the [CopyPartRequest](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/S3/TCopyPartRequest.html) class. Use the properties with the same names in the [InitiateMultipartUploadRequest](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/S3/TInitiateMultipartUploadRequest.html) class instead, which is used in some of the `InitiateMultipartUpload...` methods of the [AmazonS3Client](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/S3/TS3Client.html) class.
+ The `Expires` property has been removed from the [GetObjectResponse](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/S3/TGetObjectResponse.html) class. Use the `ExpiresString` property instead. The string might not be in a valid timestamp format, so your code should use the `TryParse` method when converting to a `DateTime`.
+ Obsolete AWS Region identifiers have been removed from the [S3Region](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/S3/TS3Region.html) enumeration.
+ The `Prefix` property has been removed from the [LifecycleRule](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/S3/TLifecycleRule.html) class. Use the `Filter` property instead.

  In addition, the `NoncurrentVersionTransition` and `Transition` properties have been removed from the `LifecycleRule` class. Use the `NoncurrentVersionTransitions` and `Transitions` collections instead.
+ The `Event` property has been removed from the [TopicConfiguration](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/S3/TTopicConfiguration.html) class. Use the `Events` collection instead.
+ CalculateContentMD5Header property. This property no longer needed to be set because the SDK will compute a checksum by default.
+ The `Bucket` property has been removed from the [SelectObjectContentRequest](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/S3/TSelectObjectContentRequest.html) class. Use the `BucketName` property instead.
+ The `NumberOfUploadThreads` property has been removed from the [TransferUtilityConfig](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/S3/TTransferUtilityConfig.html) class. Use `ConcurrentServiceRequests` property instead.

## Programming elements that were removed
<a name="net-dg-v4-removed"></a>

A number of programming elements were removed from V4 of the SDK, including enumeration values, types, methods, namespaces, etc. These are listed below, if not already covered previously, along with potential steps that you can take to accommodate their removal.

### Open to view items
<a name="w2aac25c11c47b5b1"></a>

#### The `Amazon.Auth.AccessControlPolicy.ActionIdentifiers` namespace
<a name="w2aac25c11c47b5b1b3"></a>

The `Amazon.Auth.AccessControlPolicy.ActionIdentifiers` namespace has been removed. This includes IAM action identifiers, which were defined in the `IdentityandAccessManagementActionIdentifiers` class. Code that uses these action identifiers should be changed to use string values of the action name.

For additional information, see [Creating IAM managed policies from JSON](iam-policies-create-json.md) and [Overview of JSON policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policies-json) in the [IAM User Guide](https://docs.aws.amazon.com/IAM/latest/UserGuide/).

#### The `ClientConfig` class
<a name="w2aac25c11c47b5b1b7"></a>

The [Amazon.Runtime.ClientConfig](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Runtime/TClientConfig.html) class is the base class of service client configuration classes like [AmazonS3Config](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/S3/TS3Config.html). The following programming elements have been removed from this class.
+ The `DetermineServiceURL` and `DetermineDnsSuffix` methods have been removed. Use the `DetermineServiceOperationEndpoint` method of the service client instead; for example, [AmazonS3Client.DetermineServiceOperationEndpoint](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/S3/MS3DetermineServiceOperationEndpointWebServiceRequest.html).
+ The `ReadEntireResponse` property has been removed. Use one of the following instead:
  + The `LogResponses` property of the [AWSConfigs.LoggingConfig](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Util/TLoggingConfig.html) class.
  + The `LogResponse` property of the client configuration; for example, [AmazonS3Config](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/S3/TS3Config.html).

#### The `Amazon.Runtime` namespace
<a name="w2aac25c11c47b5b1c11"></a>

The [Amazon.Runtime](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Runtime/NRuntime.html) namespace was updated as follows:
+ The obsolete `ECSTaskCredentials` class has been removed from the namespace. Use the [GenericContainerCredentials](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Runtime/TGenericContainerCredentials.html) provider instead, which also supports [Amazon EKS Pod Identities](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html).
+ The obsolete `StoredProfileAWSCredentials` and `StoredProfileCredentials` classes have been removed from the namespace. Use the [NetSDKCredentialsFile](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Runtime/TNetSDKCredentialsFile.html) or the [SharedCredentialsFile](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Runtime/TSharedCredentialsFile.html) class of the [Amazon.Runtime.CredentialManagement](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Runtime/NRuntimeCredentialManagement.html) namespace instead.
+ The obsolete `HasCachedAccessTokenAvailable` method of the [SSOAWSCredentials](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Runtime/TSSOAWSCredentials.html) class has been removed from the namespace.
+ The obsolete `EnvironmentAWSCredentials` class has been removed from the namespace. Use the [AppConfigAWSCredentials](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Runtime/TAppConfigAWSCredentials.html) class instead.
+ The obsolete `StoredProfileFederatedCredentials` class has been removed from the namespace. Use the [FederatedAWSCredentials](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Runtime/TFederatedAWSCredentials.html) class instead.
+ The following obsolete classes have been removed from the namespace: `EnvironmentVariableAWSEndpointDiscoveryEnabled`, `ProfileAWSEndpointDiscoveryEnabled`, and `FallbackEndpointDiscoveryEnabledFactory`.
+ The obsolete `UseSigV4` property has been removed from the [AmazonWebServiceRequest](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Runtime/TWebServiceRequest.html) class. Use the `SignatureVersion` property instead.
+ The `ProfileIniFile` class in the `Amazon.Runtime.Internal.Util` namespace has an overloaded method called `TryGetSection`. The versions of the method that don't support the `out` parameter for `nestedProperties` have been removed from the class.
+ The obsolete `EventBridgeSigner` class in the `Amazon.Runtime.Internal.Auth` namespace has been removed.
+ The obsolete `Parameters` dictionary property has been removed from the [WebServiceRequestEventArgs](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Runtime/TWebServiceRequestEventArgs.html) class. Use the `ParameteCollection` property instead.

#### BouncyCastle
<a name="w2aac25c11c47b5b1c13"></a>

The source copy of BouncyCastle has been removed from V4 of the SDK.

#### The `StoredProfileSAMLCredentials` class
<a name="w2aac25c11c47b5b1c15"></a>

The obsolete `StoredProfileSAMLCredentials` class in the [Amazon.SecurityToken.SAML](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/SecurityToken/NSecurityTokenSAML.html) namespace has been removed. Use the [FederatedAWSCredentials](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Runtime/TFederatedAWSCredentials.html) class in the [Amazon.Runtime](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Runtime/NRuntime.html) namespace instead.

#### The `AWSSDKUtils` class
<a name="w2aac25c11c47b5b1c17"></a>

The following methods have been removed from the [AWSSDKUtils](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Util/TAWSSDKUtils.html) class: `ResolveResourcePath`, `ProtectEncodedSlashUrlEncode`, and `ConvertToUnixEpochMilliSeconds`.

#### The `ProfileManager` class
<a name="w2aac25c11c47b5b1c19"></a>

The obsolete `ProfileManager` class has been removed from the [Amazon.Util](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Util/NUtil.html) namespace. Use the [NetSDKCredentialsFile](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Runtime/TNetSDKCredentialsFile.html) or [SharedCredentialsFile](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Runtime/TSharedCredentialsFile.html) class from the [Amazon.Runtime.CredentialManagement](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Runtime/NRuntimeCredentialManagement.html) namespace instead.

#### The `AWSConfigs` class
<a name="w2aac25c11c47b5b1c21"></a>

The following obsolete properties have been removed from the [AWSConfigs](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Amazon/TAWSConfigs.html) class: `Logging`, `ResponseLogging`, and `LogMetrics`. Use the `LoggingConfig` property instead.

#### The `ConditionFactory` class
<a name="w2aac25c11c47b5b1c23"></a>

The method with the following signature has been removed from the [ConditionFactory](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Auth/TConditionFactory.html) class: `NewCondition(ConditionFactory.DateComparisonType, DateTime)`. Use the [NewConditionUtc](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Auth/MConditionFactoryNewConditionUtcConditionFactoryDateComparisonTypeDateTime.html) method instead.

#### Amazon CloudFront utilities
<a name="w2aac25c11c47b5b1c25"></a>

The obsolete `Amazon.CloudFront.Util` namespace and `AmazonCloudFrontUtil` class have been removed.

#### AWS IoT
<a name="w2aac25c11c47b5b1c27"></a>

In the [ListPrincipalThingsResponse](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/IoT/TListPrincipalThingsResponse.html) class, a legacy customization for a `NextToken` override has been removed in favor of pagination.

#### AWS Lambda
<a name="w2aac25c11c47b5b1c29"></a>

The following `Invoke...` methods of the [AmazonLambdaClient](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/Lambda/TLambdaClient.html) class have been removed because the names were confusing.
+ The V3 method with the following signature has been removed: `InvokeAsyncResponse InvokeAsync(InvokeAsyncRequest)`. This is a synchronous method in V3 of the SDK. Use `InvokeResponse Invoke(InvokeRequest)` (for synchronous processing) or `Task InvokeAsync(InvokeRequest, CancellationToken)` (for asynchronous processing) instead.
+ The V3 method with the following signature has been removed: `Task InvokeAsyncAsync(InvokeAsyncRequest, CancellationToken)`. This is an asynchronous method in V3 of the SDK. Use `Task InvokeAsync(InvokeRequest, CancellationToken)` instead.

#### Amazon SageMaker Runtime
<a name="w2aac25c11c47b5b1c31"></a>

Obsolete constructors for the [PayloadPart](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/SageMakerRuntime/TPayloadPart.html) class have been removed.
